from elasticsearch import Elasticsearch
import json


def represents_int(year):
    try:
        int(year)
        return True
    except ValueError:
        return False


def search_custom(host="localhost", port=9200, index_name="paper_index", title_weight=10,
                  abstract_weight=2, date_weight=1.1, use_page_rank=True):
    es = Elasticsearch([{'host': host, 'port': port}])
    query_string = input("Enter query string:\n")
    while query_string == "" or query_string is None:
        query_string = input("Enter a legit query string, else I won't search\n")
    date_query = input("Enter the year after which the retrieved docs should have been published:\n")
    if not represents_int(date_query):
        print("Invalid year. Default year is 1940")
        date_query = "1940"
        # date_query = input("Enter a legit year, e.g. 2001, else I won't search\n")
    date_query = int(date_query)
    size = 100
    page_rank_coefficient = 1 if use_page_rank else 0
    ch = {
        "query": {
            "function_score": {
                "query": {
                    "multi_match": {
                        "query": query_string,
                        "type": "most_fields",
                        "fields": ["abstract^" + str(abstract_weight), "title^" + str(title_weight)]
                    }
                },
                "script_score": {
                    "script": {
                        "params": {
                            "date_weight": date_weight,
                            "date_query": date_query,
                            "pg_rank": page_rank_coefficient
                        },
                        "source": "_score * (params.pg_rank > 0 ? Math.log(params.pg_rank * (doc['page_rank'].value + 10)) : 1)"
                                  "* ((doc['date'].value >= params.date_query) && params.date_weight > 1 ? params.date_weight : 1)"
                    }
                }
            },

        },
        "collapse": {
            "field": "id.keyword"
        }
    }
    e = es.search(index=index_name, body=ch, size=size)
    # print(json.dumps(e, indent=4))
    results = [r['_source'] for r in e['hits']['hits']]
    print("Found", e['hits']['total']['value'], "results. Top",
          str(len([r['id'] for r in results])), "results are returned.")
    return results


res = search_custom()
# print(res)
for r in res:
    # print(r)
    print(r['id'], r['title'], "\t", r['date'], "page rank:", r['page_rank'], "authors:", r['authors'], "\tAbstract:", r['abstract'], r['id'],  "\tReferences:", r['references'])
    #       r['references'])
