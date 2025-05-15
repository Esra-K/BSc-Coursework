import json
from elasticsearch import Elasticsearch, helpers
import time


def make_index(host='localhost', port=9200, index_name='paper_index', file_address = 'ranked_results.json'):
    es = Elasticsearch([{'host': host, 'port': port}])
    with open(file_address) as json_data:
        a = json.load(json_data)
    helpers.bulk(es, a, index=index_name, doc_type='_doc', request_timeout=200)


def delete_index(host='localhost', port=9200, name='paper_index'):
    es1 = Elasticsearch([{'host': host, 'port': port}])
    es1.indices.delete(index=name, ignore=[400, 404])


host1 = input("Enter host\n")
port1 = int(input("Enter port\n"))

make_index('localhost', 9200, "paper_index", 'ranked_results.json')
# time.sleep(7)
# delete_index(host='localhost', port=9200, name='paper_index')
