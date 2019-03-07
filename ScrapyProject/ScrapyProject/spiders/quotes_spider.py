import scrapy

class QuotesSpider(scrapy.Spider):
    try: 
        name = "quotes"
        start_urls = [
        'https://www.mieszkaniowi.pl/deweloperzy/',
        
        ]
        value = 2
        for i in range(121):
            start_urls.append('https://www.mieszkaniowi.pl/deweloperzy/strona_%s' % value)
            value +=1
            
        
        def parse(self, response):
            for quote in response.css('div.item_wrap'):
                yield {
                   'Title': quote.css('div.item_wrap2 a.item div.bd div.info p.title notranslate::text').get(),
                    #'author': quote.css('small.author::text').get(),
                    #'tags': quote.css('div.tags a.tag::text').getall(),
                    
                }
    except:
        print('An error has occurred')