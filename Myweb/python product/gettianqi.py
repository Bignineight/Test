from bs4 import BeautifulSoup
import requests
import pymysql
 
conn=pymysql.connect(host='localhost',user='root',passwd='123',db='my_web',port=3306,charset='utf8')
cursor=conn.cursor()
def get_temperature(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'} # 设置头文件信息
    response = requests.get(url, headers=headers).content    # 提交requests get 请求
    soup = BeautifulSoup(response, "lxml")       # 用Beautifulsoup 进行解析
 
    conmid = soup.find('div', class_='conMidtab')
    conmid2 = conmid.findAll('div', class_='conMidtab2')
 
    for info in conmid2:
        tr_list = info.find_all('tr')[2:]       # 使用切片取到第三个tr标签
        for index, tr in enumerate(tr_list):     # enumerate可以返回元素的位置及内容
            td_list = tr.find_all('td')
            if index == 0:
                province_name = td_list[0].text.replace('\n', '')   # 取每个标签的text信息，并使用replace()函数将换行符删除
                city_name = td_list[1].text.replace('\n', '')
                weather = td_list[5].text.replace('\n', '')
                wind = td_list[6].text.replace('\n', '')
                max = td_list[4].text.replace('\n', '')
                min = td_list[7].text.replace('\n', '')
                print(province_name)
            else:
                city_name = td_list[0].text.replace('\n', '')
                weather = td_list[4].text.replace('\n', '')
                wind = td_list[5].text.replace('\n', '')
                max = td_list[3].text.replace('\n', '')
                min = td_list[6].text.replace('\n', '')
 
            print(city_name, weather, wind, max, min)
            cursor.execute('insert into web_tianqi_sun(city,weather,wind,max,min) values(%s,%s,%s,%s,%s)',(city_name,weather,wind,max,min))
 
 
 
 
if __name__=='__main__':
    urls = 'http://www.weather.com.cn/textFC/hb.shtml'
    get_temperature(urls)
    conn.commit()
