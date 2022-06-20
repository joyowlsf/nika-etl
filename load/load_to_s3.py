import boto3
import glob

def s3_connection():
    try:
        # s3 클라이언트 생성
        s3 = boto3.client(
            service_name="s3",
            region_name="ap-northeast-2",
            aws_access_key_id="AKIAS27VBE5WIXWFJRFO",
            aws_secret_access_key="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",
        )
    except Exception as e:
        print(e)
    else:
        print("s3 bucket connected!") 
        return s3
        

#S3로 파일 업로드 함수
def s3_upload_file():
    s3 = s3_connection()
    for f in glob.glob("/home/cho/airflow/dags/data/*{}*.csv".format("_")):
        key = 'nika/'+f.split('/')[-1]
        try:
            s3.upload_file(f,
                        "nika-bucket",
                        key)
        except Exception as e:
            print(e)


