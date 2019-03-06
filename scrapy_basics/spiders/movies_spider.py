

import scrapy
from scrapy_basics.items import MovieItem
from scrapy.loader import ItemLoader

class MoviesSpider(scrapy.Spider):
    name = "movies_spider"
    allowed_domains = ['www.blu-ray.com']
    start_urls = ['https://www.blu-ray.com/community/collection.php?u=317478&']

    #relevant xpaths
    #_categories = '//center[2]//td[2]/h2'
    #_movies = "/html/body/center[2]/table/tbody/tr/td[2]//a[@class='hoverlink']"

    def start_requests(self):
        url = 'https://www.blu-ray.com/community/collection.php?u=317478&'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #item = MovieItem()

        tile_overview = response.xpath('//td[2]')[7]
        categories = tile_overview.xpath('//h2')
        hoverlink_elements = tile_overview.css('a.hoverlink')

        page_hoverlinks = []
        page_categories = []
        page = 0

        page += 1

        for category in categories.extract():
            page_categories.append(category)

        for title_item in hoverlink_elements.extract():
                page_hoverlinks.append(title_item)

        yield {f'page_{page}_hoverlinks': page_hoverlinks,
               f'page_{page}_categories': page_categories}

        next_page = response.xpath("//div[@class='button']/a/@href").extract()[-1]
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield response.follow(url=next_page_link, callback=self.parse)

"""
   categories = body > center:nth-child(3) > table > tbody > tr > td:nth-child(2) > h2
   titles = body > center:nth-child(3) > table > tbody > tr > td:nth-child(2) > table:nth-child(61) > tbody > tr > td > center > a
"""
