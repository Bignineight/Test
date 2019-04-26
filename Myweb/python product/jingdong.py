from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time
import MySQLdb


# 声明一个谷歌驱动器，并设置不加载图片，间接加快访问速度
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {'profile.managed_default_content_settings.images': 2})
browser = webdriver.Chrome(options=options)
 # 请求url
 # url
url = 'https://www.jd.com/'
browser.get(url)
# 获取输入框的id，并输入关键字python爬虫
browser.find_element_by_id('key').send_keys('python爬虫')
# 输入回车进行搜索
browser.find_element_by_id('key').send_keys(Keys.ENTER)

# 声明一个list，存储dict
price_list=[]
name_list=[]
shop_list=[]
comment_list=[]
type_list=[]




def start_spider():  
    try:
        WebDriverWait(browser, 1000).until( 
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'gl-item')  )   )
        # 将滚动条拉到最下面的位置，因为往下拉才能将这一页的商品信息全部加载出来
        browser.execute_script('document.documentElement.scrollTop=10000')
        # 随机延迟,等下元素全部刷新
        time.sleep(random.randint(1, 3))
        browser.execute_script('document.documentElement.scrollTop=0')

        # 开始提取信息,找到ul标签下的全部li标签
        lis = browser.find_elements_by_class_name('gl-item')
        # 遍历
        for li in lis:
            # 名字
            dong_name = li.find_element_by_xpath('.//div[@class="p-name p-name-type-2"]//em').text
            # 价格
            price = li.find_element_by_xpath('.//div[@class="p-price"]//i').text
            # 评论数
            comment = li.find_elements_by_xpath('.//div[@class="p-commit"]//a')
            if comment:
                comment = comment[0].text
            else:
                comment = None
            # 商铺名字
            shop = li.find_elements_by_class_name('J_im_icon')
            if shop:
                shop = shop[0].text
            else:
                shop = None
            # 商家类型
            shop_type = li.find_elements_by_class_name('goods-icons')
            if shop_type:
                shop_type = shop_type[0].text
            else:
                shop_type = None

            #在上面定义了数组
            name_list.append(dong_name)      
            price_list.append(price)
            shop_list.append(shop)
            type_list.append(shop_type)  
            comment_list.append(comment)

            #print(name_list)
   
               # data_dict = {}
               # data_dict['dong_name'] = dong_name
               # data_dict['price'] = price
               # data_dict['comment'] = comment
               # data_dict['shop'] = shop
               #  data_dict['shop_type'] = shop_type
               # data_list.append(data_dict)
                                                                                     
    except Exception as e:
        start_spider()
    return name_list,shop_list,type_list,comment_list,price_list
def Mysql_save():
    print("下面进行数据库写入：")
    try:
        conn=MySQLdb.connect(host="localhost",user="root",passwd="123",db="my_web",charset="gbk")
        cursor=conn.cursor()
        print("数据库链接成功！")
        for i in range(1000):
            sql=("insert into web_jingdong_test(shop,comment,shop_type,price,dong_name) VALUES(%s,%s,%s,%s,%s)")
            #print(name_list[i])
            val=(shop_list[i],comment_list[i],type_list[i],price_list[i],name_list[i])
            cursor.execute(sql,val)
            conn.commit()
        cursor.close()
        conn.close()    
    except Exception as e:
        print(e)
    print("over")    

def turn():
    WebDriverWait(browser, 1000).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="J_bottomPage"]/span[1]/a[9]/em'))).click()
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")



if __name__ == '__main__':
    num=0      
    for i in range(1000):
        num =num+1
        print("当前为第{}页".format(num))
        start_spider()
        Mysql_save()
        turn()
    
    
