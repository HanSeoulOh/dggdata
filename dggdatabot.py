import scrapy


class dggDataBot(scrapy.Spider):
    name = "chatlogs"
    start_urls = [
        'https://overrustlelogs.xyz/Destinygg%20chatlog'
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)