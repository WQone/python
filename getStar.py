# 爬取星座
import requests
import json
from bs4 import BeautifulSoup
import datetime
from mysqlpy import my_db

sql = my_db()
cur = sql.cursor()


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except requests.HTTPError:
        return "产生异常"


def getContent(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "lxml")
    top = soup.select_one("div.c_main  div.top")
    # 星座数据
    star_name = top.select_one("strong").text,  # 星座名称
    day_type = top.select_one("a.on").text,  # 今日运势
    for p in soup.select("div.c_cont p"):
        fortune_type = p.select_one("strong").text,
        des_text = p.select_one("span").text,
        print(fortune_type, des_text, datetime.datetime.now())
        cur.execute(
            'insert into star(star_name, day_type, fortune_type, des_text, date, creat_time) VALUE (%s, %s, %s, %s, %s, %s)',
            (star_name, day_type, fortune_type, des_text,
             datetime.datetime.now().strftime('%Y-%m-%d'),
             datetime.datetime.now()))
        sql.commit()


def main():
    url = "https://www.xzw.com/fortune/"
    star_arr = [
        'aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra',
        'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces'
    ]
    for star in star_arr:
        for i in range(5):
            print(url + star + '/' + str(i) + '.html')
            getContent(url + star + '/' + str(i) + '.html')


main()
