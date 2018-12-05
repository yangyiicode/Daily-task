import scrapy
class mingyan(scrapy.Spider):

    name = 'mingyan2'   #定义蜘蛛名字
    def start_requests(self):  #通过调用该方法来爬取下面链接的页面


         #下面就是我要爬取的链接
        urls=[
            'http://lab.scrapyd.cn/page/1/',
            'http://lab.scrapyd.cn/page/2/',
        ]
        # url_start='https://bj.lianjia.com/ershoufang/pg'
        # depth = 10
        # for i in range(depth):
        #
        #     url = url_start+str(i)
        #     yield  scrapy.Request(url=url,meta={'index':i},callback=self.parse)

        for url in urls:
           yield  scrapy.Request(url=url,callback=self.parse)  #爬取页面并利用parse方法解析

    def parse(self, response):
        page = response.url.split("/")[-2]
        i =response.meta.get("index")

        filename ='mingyan-%s.html' %page
        with open(filename,'wb') as f:
            f.write(response.body)              #爬取的html文件自动存取在项目文件夹中
        self.log('保存文件： %s' % filename)

