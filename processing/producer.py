from difflib import get_close_matches
from konlpy.tag import Mecab
import pymongo
import re
import sys
sys.path.append("/home/cho/airflow/dags/nika-etl/load")
import load_to_mongo as m
import date_format as dt


# Mecab 객체 선언
mecab = Mecab()

dates = dt.date_range(dt.before_one_week.strftime('%Y-%m-%d'), dt.now.strftime('%Y-%m-%d'))

# 데이터 형태소 분석
def producer():
    collection = m.connect_mongo()
    list_st = []
    for i in collection.find({'date':{'$in':dates}},{'_id':0,'title':1}):        
        st = str(i)
        st = st.strip("{\'title\'\:")
        new_st = re.sub(r"[^a-zA-Z0-9ㄱ-ㅎ가-힣 ]","",st)
        list_st.extend(mecab.morphs(new_st))
    return list_st


if __name__ == '__main__':
    producer()
    