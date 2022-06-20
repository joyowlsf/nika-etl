from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime, timedelta
import re
import sys
sys.path.append("/home/cho/airflow/dags/nika-etl/processing")
import create_csv as csv
import date_format as dt



options = webdriver.ChromeOptions()
options.add_argument('--headless')
# options.add_argument('window-size=1200x600')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(chrome_options=options)
#chrome드라이버가 PATH 환경변수 설정이 되어있지 않다면 executable_path 옵션으로 chromedriver 위치 지정
driver = webdriver.Chrome(chrome_options=options, executable_path="/usr/local/bin/chromedriver")

filename = "news"

writer = csv.create_csv(filename)



def main():
    for i in range(10):
        url = "https://cafe.naver.com/zzang9daddy?iframe_url=/ArticleList.nhn%3Fsearch.clubid=29328371%26search.menuid=21%26search.boardtype=I%26search.totalCount=201%26search.cafeId=29328371%26search.page={}".format(i+1)
        
        driver.get(url)
        driver.switch_to.frame("cafe_main")
        search_url = driver.page_source
        soup = BeautifulSoup(search_url, 'lxml')
        posts = soup.select(".article-album-sub > li")

        for post in posts:
            data_list = []
            data_list.append("zzang9daddy")

            title = post.select_one(".inner > span").text
            data_list.append(title)

            date = post.select_one(".date").text
            
            # 정규식 처리
            re_date = re.sub(r"[^0-9]","",date)
            
            if len(re_date) == 8:
                # 문자열을 datetiem으로 변환
                date_obj = datetime.strptime(re_date,'%Y%m%d').date().strftime('%Y-%m-%d')
            
                # 현재 날짜 기준으로 일주인전
                dates = dt.date_range(dt.before_one_week.strftime('%Y-%m-%d'), dt.now.strftime('%Y-%m-%d'))
            
                for j in dates:
                    if j == date_obj:
                        data_list.append(date_obj)
                        writer.writerow(data_list)




if __name__ == "__main__":
    print("짱구대디 시작")
    main()
    print("짱구대디 성공")
