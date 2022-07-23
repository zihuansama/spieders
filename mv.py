import scrapy


from scrapy_movie_099.items import ScrapyMovie099Item

class MvSpider(scrapy.Spider):
    name = 'mv'
    allowed_domains = ['www.dytt8.net']
    start_urls = ['https://www.dytt8.net/html/gndy/china/index.html']

    def parse(self, response):
        a_list=response.xpath('//div[@class="[co_content8]"//td[2]//a[2]')

        for a in  a_list:
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./hefr()').extract_first()

            #第二页地址
            url = 'https://www.dytt8.net'+href

            #访问第二页

            yield scrapy.Request(url=url,callback=self.parse_second,meta={'name':name})




    def parse_second(self,response):
        src = response.xpath('//div[@id="zoom"]//img/@src').extract_first()

        name = response.meta['name']

        movuie = ScrapyMovie099Item(src=src,name=name)

        yield movie
