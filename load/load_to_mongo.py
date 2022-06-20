import sys
from pymongo import MongoClient
import csv
import glob

MONGO_HOST = 'localhost'
MONGO_PORT = 27017

DOCUMENT_NAME = 'mydatabase'
COLLECTION_NAME = 'test8'

COLUMNS = ('cafe','title', 'date')

# mongodb 접속
def connect_mongo():
    try:
        client = MongoClient(MONGO_HOST, MONGO_PORT)
        db = client[DOCUMENT_NAME]
        return  db[COLLECTION_NAME]
    except Exception as e:
        print('Got an error!')
        print(e)
        sys.exit(1)


# mongodb 데이터 저장
def save_to_mongo(datas):
    collection = connect_mongo()
    data = datas 
    try:
        result = collection.insert_many(data)
        print('%d rows are saved to "%s" collection in "%s" document successfully!' % (len(result.inserted_ids), COLLECTION_NAME, DOCUMENT_NAME))
        # sys.exit(1)
    except Exception as e:
        print('Got an error!')
        print(e)
        sys.exit(1)

# csv파일 읽기
def read_csv():
    for filename in glob.glob("/home/cho/airflow/dags/data/*{}*.csv".format("_")):
        try:
            reader = open(filename, 'r') 
            save_to_mongo(csv.DictReader(reader, COLUMNS))
        except Exception as e:
            print(e)        

if __name__ == '__main__':
    read_csv()

