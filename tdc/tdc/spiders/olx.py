import scrapy

class OlxSpider(scrapy.Spider):

    name = 'olx'
    start_urls = ['https://pe.olx.com.br/imoveis/aluguel']

    def parse(self, response):
        items = response.xpath('//*[@id="ad-list"]/li')
        for item in items:
            url = item.xpath(".//a/@href").extract_first()
            if url:
                yield scrapy.Request(
                    url=url, callback=self.parse_detail
                )
    
    def parse_detail(self, response):
        preco = response.xpath("//h2[@font-weight='400']/text()").extract_first()
        yield {
            'url': response.url,
            'titulo': response.xpath("//title/text()").extract_first(),
            'preco': preco,
        }

