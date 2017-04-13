import scrapy


class dggDataBot(scrapy.Spider):
    name = "chatlogs"
    start_urls = [
        'https://overrustlelogs.xyz/Destinygg%20chatlog'
    ]

    def parse(self, response):
        for month in response.css('a::attr(href)').extract():
        	if month[:21] == "/Destinygg%20chatlog/":
        		next_url = response.urljoin(month)
        		yield scrapy.Request(next_url, callback = self.parseUsers)

    def parseUsers(self, response):
    	for user in response.css('a::attr(href)').extract():
    		if user.split('/')[2] == 'userlogs':
    			next_url = reponse.urljoin(user)
    			yield scrapy.Request(next_url, callback = self.parseUser)

   	def parseUser(self, reponse):
   		