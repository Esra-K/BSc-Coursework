import xml.etree.ElementTree as et
from hazm import *
import pickle
from collections import defaultdict
import numpy as np
from numpy.linalg import norm
import re
from collections import Counter
import string
import math
from math import *


def dict_level_two():
    return defaultdict(list)


def dict_level_one():
    return defaultdict(dict_level_two)


normalizer = Normalizer()
stemmer = Stemmer()
pids = []
index_dict = defaultdict(dict_level_one)
title_idf = defaultdict(float)
text_idf = defaultdict(float)


def prepare_text(raw_text):
    raw_text = raw_text.translate({ord(c): None for c in string.punctuation.replace("-", "")})
    raw_text = normalizer.normalize(raw_text)
    prepared_text = word_tokenize(raw_text)
    punctuation = "!@#$%^&?<>*()[}{]-=/|~`+_'.,:;؛،\؟«»ٰ'\"\\\t\n"
    result = []
    for i in range(len(prepared_text)):
        if not (prepared_text[i] in punctuation or len(prepared_text[i]) < 2):
            result.append(stemmer.stem(prepared_text[i]))
    return result


def update_idf():
    global title_idf, text_idf, index_dict
    for term in index_dict:
        num_of_titles = 0
        num_of_texts = 0
        for doc_id in index_dict[term]:
            if 'title' in index_dict[term][doc_id]:
                num_of_titles += 1
            if 'text' in index_dict[term][doc_id]:
                num_of_texts += 1
            title_idf[term] = log(float(len(pids) / num_of_titles)) if num_of_titles != 0 else 0
            text_idf[term] = log(float(len(pids) / num_of_texts)) if num_of_texts != 0 else 0


def construct_positional_indexes(docs_path):
    global pids, index_dict, title_idf, text_idf
    tree = et.parse(docs_path)
    root = tree.getroot()
    all_content = root.findall('{http://www.mediawiki.org/xml/export-0.10/}page')
    for page_index, pg in enumerate(all_content):
        title = pg.find('{http://www.mediawiki.org/xml/export-0.10/}title').text
        txt = pg.find('{http://www.mediawiki.org/xml/export-0.10/}revision') \
            .find('{http://www.mediawiki.org/xml/export-0.10/}text').text
        pid = int(pg.find('{http://www.mediawiki.org/xml/export-0.10/}id').text)
        pids += [pid]

        title_arr = prepare_text(title)
        txt_arr = prepare_text(txt)

        for term_index, term in enumerate(title_arr):
            index_dict[term][pid]["title"].append(term_index)

        for term_index, term in enumerate(txt_arr):
            index_dict[term][pid]["text"].append(term_index)
    update_idf()


construct_positional_indexes("Persian.xml")


def get_posting_list(word):
    posting_list = index_dict[word]
    return posting_list


def add_document_to_indexes(docs_path, doc_num):
    global pids, index_dict, title_idf, text_idf
    tree = et.parse(docs_path + "/" + doc_num)
    root = tree.getroot()
    all_content = root.findall('{http://www.mediawiki.org/xml/export-0.10/}page')
    for page_index, pg in enumerate(all_content):
        title = pg.find('{http://www.mediawiki.org/xml/export-0.10/}title').text
        txt = pg.find('{http://www.mediawiki.org/xml/export-0.10/}revision') \
            .find('{http://www.mediawiki.org/xml/export-0.10/}text').text
        pid = int(pg.find('{http://www.mediawiki.org/xml/export-0.10/}id').text)
        pids += [pid]

        title_arr = prepare_text(title)
        txt_arr = prepare_text(txt)

        for term_index, term in enumerate(title_arr):
            index_dict[term][pid]["title"].append(term_index)

        for term_index, term in enumerate(txt_arr):
            index_dict[term][pid]["text"].append(term_index)
    update_idf()


def delete_document_from_indexes(docs_path, doc_num):
    global pids, index_dict
    tree = et.parse(docs_path + "/" + doc_num)
    root = tree.getroot()
    all_content = root.findall('{http://www.mediawiki.org/xml/export-0.10/}page')
    for page_index, pg in enumerate(all_content):
        title = pg.find('{http://www.mediawiki.org/xml/export-0.10/}title').text
        txt = pg.find('{http://www.mediawiki.org/xml/export-0.10/}revision') \
            .find('{http://www.mediawiki.org/xml/export-0.10/}text').text
        pid = int(pg.find('{http://www.mediawiki.org/xml/export-0.10/}id').text)
        pids.remove(pid)

        title_arr = prepare_text(title)
        txt_arr = prepare_text(txt)

        for term_index, term in enumerate(title_arr):
            index_dict[term][pid] = defaultdict(list)

        for term_index, term in enumerate(txt_arr):
            index_dict[term][pid] = defaultdict(list)
    update_idf()


def save_index(destination):
    global index_dict, pids, title_idf, text_idf
    with open(destination, 'wb') as f:
        pickle.dump(index_dict, f)
    with open("pids.txt", 'wb') as f:
        pickle.dump(pids, f)
    with open("title_idf.txt", 'wb') as f:
        pickle.dump(title_idf, f)
    with open("text_idf.txt", 'wb') as f:
        pickle.dump(text_idf, f)


save_index("index.txt")


def load_index(source):
    global index_dict, pids, title_idf, text_idf
    with open(source, 'rb') as file:
        index_dict = pickle.load(file)
    with open("pids.txt", 'rb') as f:
        pids = pickle.load(f)
    with open("title_idf.txt", 'rb') as f:
        title_idf = pickle.load(f)
    with open("text_idf.txt", 'rb') as f:
        text_idf = pickle.load(f)


load_index("index.txt")


def int_dict():
    return defaultdict(float)


def search_util(query, method="ltn-lnn", weight=5):
    global pids, title_idf, text_idf, index_dict
    rest_of_query = query
    pages = []
    if "\"" in query:
        p = re.findall(r'"([^"]*)"', query)
        to_be_merged = []
        for i in range(len(p)):
            merge_element_i = []
            phrase_query = p[i]
            rest_of_query = rest_of_query.replace(phrase_query, "")
            phrase_query_arr = prepare_text(phrase_query)
            for term in phrase_query_arr:
                if term not in index_dict.keys():
                    phrase_query_arr.remove(term)
            length_of_phrase = len(phrase_query_arr)
            exact_phrase = "".join(phrase_query_arr)
            for page_index in pids:
                sequence_in_title = []
                sequence_in_text = []
                for word_index, term in enumerate(phrase_query_arr):
                    for place in index_dict[term][page_index]["title"]:
                        sequence_in_title.append((term, place))
                    for place in index_dict[term][page_index]["text"]:
                        sequence_in_text.append((term, place))

                sequence_in_title = sorted(sequence_in_title, key=lambda x: x[1])
                sequence_in_text = sorted(sequence_in_text, key=lambda x: x[1])
                candidate_indices_title = [ind for ind, val in enumerate(sequence_in_title) if
                                           (val[0] == phrase_query_arr[0] and ind <= len(
                                               sequence_in_title) - length_of_phrase)]
                candidate_indices_text = [ind for ind, val in enumerate(sequence_in_text) if
                                          (val[0] == phrase_query_arr[0] and ind <= len(
                                              sequence_in_text) - length_of_phrase)]
                flag = False
                for ind in candidate_indices_title:
                    if "".join([x[0] for x in sequence_in_title[ind:ind + length_of_phrase]]) == exact_phrase:
                        flag = True
                        break
                if flag:
                    merge_element_i.append(page_index)
                    continue
                for ind in candidate_indices_text:
                    if "".join([x[0] for x in sequence_in_text[ind:ind + length_of_phrase]]) == exact_phrase:
                        flag = True
                        break
                if flag:
                    merge_element_i.append(page_index)
            to_be_merged.append(merge_element_i)
        pages = list(set().union(*to_be_merged))

    else:
        rest_of_query = query
        pages = [j for j in pids]

    query_arr = prepare_text(rest_of_query)
    query_dict = defaultdict(float, Counter(query_arr))
    search_terms = list(query_dict.keys())

    title_indices = defaultdict(int_dict)
    text_indices = defaultdict(int_dict)
    page_list = []
    for term in query_arr:
        title_tf = defaultdict(float)
        text_tf = defaultdict(float)
        for pid in index_dict[term]:
            if pid in pages:
                title_tf[pid] = len(index_dict[term][pid]['title'])
                text_tf[pid] = len(index_dict[term][pid]['text'])
                page_list.append(pid)
        title_indices[term] = title_tf
        text_indices[term] = text_tf

    score_title = defaultdict(float)
    score_text = defaultdict(float)
    norm1 = 0
    norm2 = 0
    for term in query_arr:
        for pid in title_indices[term]:
            score_title[pid] += float(log(max(1, weight * title_indices[term][pid])) + 1) * float(
                title_idf[term]) * float(log(query_dict[term]) + 1)
            if method == "ltc-lnc":
                norm1 += float(log(max(1, weight * title_indices[term][pid])) + 1) * float(title_idf[term]) * float(
                    log(query_dict[term]) + 1)

        for pid in text_indices[term]:
            score_text[pid] += float(log(max(1, text_indices[term][pid])) + 1) * float(text_idf[term]) * float(
                log(query_dict[term]) + 1)
            if method == "ltc-lnc":
                norm2 += float(log(max(1, text_indices[term][pid])) + 1) * float(text_idf[term]) * float(
                    log(query_dict[term]) + 1)

    total_score = defaultdict(float)
    for pid in page_list:
        score = score_title[pid] + score_text[pid]
        if method == "ltc-lnc":
            norm_of_query = 0
            for term in query_dict:
                norm_of_query += (query_dict[term]) ** 2
            score /= ((norm2 + norm1) * norm_of_query) ** 0.5
        total_score[pid] = score
    return total_score


def search(query, method="ltn-lnn", weight=5):
    total_score = search_util(query, method, weight)
    return [x[0] for x in Counter(total_score).most_common(min(20, len(list(total_score.keys()))))]


def detailed_search(title_query, text_query, method="ltn-lnn"):
    title_score = search_util(title_query, method, weight=2**16)
    text_score = search_util(text_query, method, weight=0)
    geometric_mean = {k: title_score.get(k, 0) * text_score.get(k, 0) for k in set(title_score) | set(text_score)}
    print("detailed:", [x[0] for x in Counter(geometric_mean).most_common(min(20, len(list(geometric_mean.keys()))))])
    return [x[0] for x in Counter(geometric_mean).most_common(min(20, len(list(geometric_mean.keys()))))]


detailed_search('عجایب هفت‌گانه', 'چشمگیرترین بناهای تاریخی جهان', "ltc-lnc")


def R_Precision(query_id='all'):
    if query_id == 'all':
        r_precision = []
        for i in range(1, 21):
            with open("relevance/" + str(i) + ".txt", 'r') as relevance_file:
                list_of_relevants = list(map(int, relevance_file.read().split(",")))
            with open("queries/" + str(i) + ".txt", 'r') as query_file:
                query = query_file.read()
                my_relevants = search(query)

            if len(my_relevants) < len(list_of_relevants):
                list_of_relevants = list_of_relevants[:len(my_relevants)]
            else:
                my_relevants = my_relevants[:len(list_of_relevants)]

            # evaluation
            true_positive = [x for x in my_relevants if x in list_of_relevants]
            precision = len(true_positive) / len(my_relevants)
            rprecision = precision
            r_precision.append(rprecision)
        print("r_precision:", np.mean(r_precision))
        return np.mean(r_precision)

    else:
        with open("relevance/" + str(query_id) + ".txt") as relevance_file:
            list_of_relevants = list(map(int, relevance_file.read().split(",")))

        with open('queries/' + str(query_id) + '.txt') as query_file:
            query = query_file.read()
            my_relevants = search(query)

        if len(my_relevants) < len(list_of_relevants):
            list_of_relevants = list_of_relevants[:len(my_relevants)]
        else:
            my_relevants = my_relevants[:len(list_of_relevants)]

        # evaluation
        true_positive = [x for x in my_relevants if x in list_of_relevants]
        precision = len(true_positive) / len(my_relevants) if len(my_relevants) > 0 else -1
        rprecision = precision

        return rprecision


R_Precision()


def F_measure(query_id='all'):
    beta = 2
    if query_id == 'all':
        f_measure = []
        for i in range(1, 21):
            with open("relevance/" + str(i) + ".txt", 'r') as relevance_file:
                list_of_relevants = list(map(int, relevance_file.read().split(",")))
            with open("queries/" + str(i) + ".txt", 'r') as query_file:
                query = query_file.read()
                my_relevants = search(query)

            if len(my_relevants) < len(list_of_relevants):
                list_of_relevants = list_of_relevants[:len(my_relevants)]
            else:
                my_relevants = my_relevants[:len(list_of_relevants)]

            # evaluation
            true_positive = [x for x in my_relevants if x in list_of_relevants]
            precision = len(true_positive) / len(my_relevants)
            recall = len(true_positive) / len(list_of_relevants)
            f = (1 + beta ** 2) * precision * recall / (beta ** 2 * precision + recall)
            f_measure.append(f)
        print("f_measure", f_measure)
        return np.mean(f_measure)

    else:
        with open("relevance/" + str(query_id) + ".txt") as relevance_file:
            list_of_relevants = list(map(int, relevance_file.read().split(",")))

        with open('queries/' + str(query_id) + '.txt') as query_file:
            query = query_file.read()
            my_relevants = search(query)

        if len(my_relevants) < len(list_of_relevants):
            list_of_relevants = list_of_relevants[:len(my_relevants)]
        else:
            my_relevants = my_relevants[:len(list_of_relevants)]

        # evaluation
        true_positive = [x for x in my_relevants if x in list_of_relevants]
        precision = len(true_positive) / len(my_relevants)
        recall = len(true_positive) / len(list_of_relevants)
        f = (1 + beta ** 2) * precision * recall / (beta ** 2 * precision + recall)
        return f


F_measure()


def MAP(query_id='all'):
    if query_id == 'all':
        mapp = []
        for i in range(1, 21):
            with open("relevance/" + str(i) + ".txt", 'r') as relevance_file:
                list_of_relevants = list(map(int, relevance_file.read().split(",")))
            with open("queries/" + str(i) + ".txt", 'r') as query_file:
                query = query_file.read()
                my_relevants = search(query)
            if len(my_relevants) < len(list_of_relevants):
                list_of_relevants = list_of_relevants[:len(my_relevants)]
            else:
                my_relevants = my_relevants[:len(list_of_relevants)]
            num_of_relevant = 0
            total_precision = 0
            for index, pid in enumerate(my_relevants):
                if pid in list_of_relevants:
                    num_of_relevant += 1
                    total_precision += num_of_relevant / (index + 1)
            mapp.append(total_precision / num_of_relevant)
        print("map:", mapp)
        return np.mean(mapp)

    else:
        with open("relevance/" + str(query_id) + ".txt") as relevance_file:
            list_of_relevants = list(map(int, relevance_file.read().split(",")))

        with open('queries/' + str(query_id) + '.txt') as query_file:
            query = query_file.read()
            my_relevants = search(query)

        if len(my_relevants) < len(list_of_relevants):
            list_of_relevants = list_of_relevants[:len(my_relevants)]
        else:
            my_relevants = my_relevants[:len(list_of_relevants)]
        num_of_relevant = 0
        total_precision = 0
        for index, pid in enumerate(my_relevants):
            if pid in list_of_relevants:
                num_of_relevant += 1
                total_precision += num_of_relevant / (index + 1)
        m = total_precision / num_of_relevant
        return m


MAP()


def NDCG(query_id='all'):
    if query_id == 'all':
        ndcg = []
        for i in range(1, 21):
            with open("relevance/" + str(i) + ".txt", 'r') as relevance_file:
                list_of_relevants = list(map(int, relevance_file.read().split(",")))
            with open("queries/" + str(i) + ".txt", 'r') as query_file:
                query = query_file.read()
                my_relevants = search(query)

            if len(my_relevants) < len(list_of_relevants):
                list_of_relevants = list_of_relevants[:len(my_relevants)]
            else:
                my_relevants = my_relevants[:len(list_of_relevants)]
            iDCG = sum([1 / np.log10(n + 2) for n in range(len(list_of_relevants))])
            DCG = sum([1 / np.log10(n + 2) for n in range(len(my_relevants)) if my_relevants[n] in list_of_relevants])
            ndcg.append(DCG / iDCG)
            print("ndcg:", ndcg)
        return np.mean(ndcg)

    else:
        with open("relevance/" + str(query_id) + ".txt") as relevance_file:
            list_of_relevants = list(map(int, relevance_file.read().split(",")))

        with open('queries/' + str(query_id) + '.txt') as query_file:
            query = query_file.read()
            my_relevants = search(query)

        if len(my_relevants) < len(list_of_relevants):
            list_of_relevants = list_of_relevants[:len(my_relevants)]
        else:
            my_relevants = my_relevants[:len(list_of_relevants)]
        iDCG = sum([1 / np.log10(n + 2) for n in range(len(list_of_relevants))])
        DCG = sum([1 / np.log10(n + 2) for n in range(len(my_relevants)) if my_relevants[n] in list_of_relevants])
        m = DCG / iDCG
        return m


NDCG()
