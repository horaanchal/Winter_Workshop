from scrapy import Spider
from scrapy.selector import Selector
from stack.items import StackItem

class StackSpider(Spider):
	name = "news"
	allowed_domains = ["news.ycombinator.com"]
	start_urls = [
		"https://news.ycombinator.com/"
	]
	def parse(self, response):
		titles = Selector(response).xpath('//td[@class="title"]')
		for title in titles:
			item = StackItem()
			item['title'] = title.xpath('a[@class="storylink"]/text()').extract()[0]
            		item['url'] = title.xpath('a[@class="storylink"]/@href').extract()[0]
            		yield item
