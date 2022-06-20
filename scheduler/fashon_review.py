from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

args = {
    "owner" : "airflow",
}

with DAG(
    dag_id="nika-etl",
    default_args = args,
    # schedule_interval="0 9 * * 1",
    schedule_interval="@once",
    catchup=False,
    # dagrun_timeout=timedelta(minutes=5),
    start_date = days_ago(2),
) as dag:


    # zzang9daddy 데이터 수집
    t1 = BashOperator(
        task_id='zzang9daddy_crawler',
        bash_command='python3 /home/cho/airflow/dags/nika-etl/crawler/zzang9daddy_crawler.py',
        dag=dag)

    # gocd 데이터 수집
    t2 = BashOperator(
        task_id='gocd_crawler',
        bash_command='python3 /home/cho/airflow/dags/nika-etl/crawler/gocd_crawler.py',
        dag=dag)

    # s3 데이터 적재
    # t3 = PythonOperator(
    #     task_id='load_to_s3',
    #     python_callable=s3_upload_file,
    #     dag=dag
    # )

    # mongodb 데이터 적재
    t3 = BashOperator(
        task_id='load_to_mongo',
        bash_command='python3 /home/cho/airflow/dags/nika-etl/load/load_to_mongo.py',
        dag=dag)

    # mongodb 데이터 조회 및 전처리
    t4 = BashOperator(
        task_id='producer',
        bash_command='python3 /home/cho/airflow/dags/nika-etl/processing/producer.py',
        dag=dag)

    # elasticsearch 데이터 적재
    t5 = BashOperator(
        task_id='load_to_elasticsearch',
        bash_command='python3 /home/cho/airflow/dags/nika-etl/load/load_to_elasticsearch.py',
        dag=dag)


    t1 >> t2 >> t3 >> t4 >> t5
 