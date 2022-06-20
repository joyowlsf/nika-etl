import csv
import datetime as dt
import os


# 수집 날짜
collection_date = dt.datetime.now().strftime('%y%m%d')

# 파일 저장
def create_csv(filename):

    # 디렉토리 생성
    # create_directory("/home/cho/airflow/dags/data/{}/".format(filename))
    create_directory("/home/cho/airflow/dags/data/")

    # 저장 경로
    # path = "/home/cho/airflow/dags/data/{}/".format(filename) + "{}_{}.csv".format(filename,collection_date)
    path = "/home/cho/airflow/dags/data/{}_{}.csv".format(filename,collection_date)

    # 파일 열기
    f = open(path, "w", encoding="utf-8-sig", newline="")
    writer = csv.writer(f)

    # 타이틀 제목
    # title ="title date".split()
    # writer.writerow(title)

    return writer



# 디렉토리 생성
def create_directory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)