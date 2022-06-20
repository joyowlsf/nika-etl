from bs4 import BeautifulSoup
from selenium import webdriver

# import create_csv as csv
import sys
sys.path.append("/home/cho/airflow/dags/nika-etl/processing")
import create_csv as csv


options = webdriver.ChromeOptions()
options.add_argument('--headless')
# options.add_argument('window-size=1200x600')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(chrome_options=options)
#chrome드라이버가 PATH 환경변수 설정이 되어있지 않다면 executable_path 옵션으로 chromedriver 위치 지정
driver = webdriver.Chrome(chrome_options=options, executable_path="/usr/local/bin/chromedriver")

filename = "branded"

writer = csv.create_csv(filename)


def main():
    
    for i in range(3):
        
        url = "https://cafe.naver.com/coredenim?iframe_url=/ArticleList.nhn%3Fsearch.clubid=27877258%26search.menuid=2%26search.boardtype=I%26search.totalCount=201%26search.cafeId=27877258%26search.page={}".format(i+1)
        
        driver.get(url)
        driver.switch_to.frame("cafe_main")
        search_url = driver.page_source
        soup = BeautifulSoup(search_url, 'lxml')
        posts = soup.select(".article-album-sub > li")


        for post in posts:
            data_list = []
            data_list.append("branded")
            title = post.select_one(".inner > span").text
            data_list.append(title)
            date = post.select_one(".date").text
            data_list.append(date)

            writer.writerow(data_list)


if __name__ == "__main__":
    print("브랜디드 시작")
    main()
    print("브랜디드 성공")