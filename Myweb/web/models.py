from django.db import models
class Douban_top(models.Model):
    # 电影唯一ID
    rankey=models.AutoField(primary_key=True)
    # 电影名称
    name=models.TextField()
    # 电影别名
    alias=models.TextField()
    # 电影导演
    director=models.TextField()
    # 上映年份
    showYear=models.TextField()
    # 制作国家/地区
    makeCountry=models.TextField()
    # 电影类别
    movieType=models.TextField()
    # 评分
    movieScore=models.TextField()
    #参评人数
    scoreNum=models.TextField()
    #简短影评
    shortFilm=models.TextField()

    def __str__(self):
        return self.rankey

class tianqi_sun(models.Model):
    id=models.AutoField(primary_key=True)
    # 城市
    city=models.TextField()
    # 天气
    weather=models.TextField()
    # 风
    wind=models.TextField()
    # 最高温
    max=models.TextField()
    # 最低温
    min=models.TextField()
    
    def __str__(self):
        return self.id

class jingdong_test(models.Model):
    dong_id=models.AutoField(primary_key=True)
    # 出版社
    shop=models.TextField()
    # 评论数
    comment=models.TextField()
    # 营业类型
    shop_type=models.TextField()
    # 价格
    price=models.TextField()
    # 书名
    dong_name=models.TextField()
    
    def __str__(self):
        return self.dong_id