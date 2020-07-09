import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class YFScreener(CrawlSpider):
    name = 'YFScreener'
    allowed_domains = ['finance.yahoo.com']
    start_urls = ['https://finance.yahoo.com/screener/unsaved/c97bc7b4-0e94-43dc-9df1-b46f936742e6?count=25&offset=0']

    # rules = (
    #     # Extract links matching 'item.php' and parse them with the spider's method parse_item
    #     Rule(LinkExtractor(allow=('https://finance.yahoo.com/screener/.*count=\d+\&offset=\d+')), callback='parse_item'),
    # )

    def parse_item(self, response):
        return {"tick": response.css('tr.simpTblRow:nth-child(1) > td:nth-child(1) > a:nth-child(2)::text').get()}