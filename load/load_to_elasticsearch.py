from elasticsearch import Elasticsearch
from elasticsearch import helpers
from datetime import datetime
import sys
sys.path.append("/home/cho/airflow/dags/nika-etl/processing")
import producer as pr

es = Elasticsearch('http://localhost:9200')

docs = []

# elasticsearch 데이터 적재
def save_to_elasticsearch():
    for data in pr.producer():
        docs.append({
            '_index': "brand_data",
            '_source': {
                "title": data,
            }
        })

helpers.bulk(es,docs)

if __name__ == '__main__':
   save_to_elasticsearch()
   print("success")