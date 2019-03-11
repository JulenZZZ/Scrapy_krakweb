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
             for response in response.xpath("//div[@class='item_wrap']"):
                yield {
                   'Title': response.xpath("//p[@class='title notranslate']").get(),
                    #'author': quote.css('small.author::text').get(),
                    #'tags': quote.css('div.tags a.tag::text').getall(),
                    
                }
    except:
        print('An error has occurred')
