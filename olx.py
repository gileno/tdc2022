import scrapy

class OlxSpider(scrapy.Spider):

    name = 'olx'
    start_urls = ['https://pe.olx.com.br/imoveis/aluguel']
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
    }

    def parse(self, response):
        items = response.xpath('//*[@id="ad-list"]/li')
        for item in items:
            yield {
                'url': item.xpath(".//a/@href").extract_first(),
                'titulo': item.xpath(".//h2/text()").extract_first(),
            }
