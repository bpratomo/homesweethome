import scrapy
import time
import djangomodels  as dm


class ParariusSpider(scrapy.Spider):
    name = "pararius"

    start_urls = [
        'https://www.pararius.com/apartments/amsterdam',
    ]


    def parse(self, response):
        #Follow links to each specific house
        for href in response.xpath("//div[@class='details']/h2/a/@href"):
            time.sleep(3)
            print('traversing to house {}'.format(href))
            yield response.follow(href, self.parse_property)

        # Follow links to next page (maximum 5 pages)
        for href in response.xpath("//li[@class='next']/a/@href"):
            time.sleep(3)
            print('traversing to next page {}'.format(href))
            yield response.follow(href, self.parse_property)


    def parse_property(self,response):
        print("parse_property function triggered")