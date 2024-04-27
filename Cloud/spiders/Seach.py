import scrapy


class Search(scrapy.Spider):
    name = 'Search'

    start_urls = ['https://www.amazon.com/']

    def parse(self, response, **kwargs):
        print(response.body)
