import scrapy
from book_scraper.items import BookScraperItem

class BookSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        item = BookScraperItem()
        
        #product loop to get information of each product
        products = response.css('.product_pod')
        for product in products:

            item['title'] = product.css('a > img').attrib['alt']
            item['price'] = float(product.css('.price_color::text').get().replace('£',''))
            item['image_url'] = response.urljoin(product.css('a > img').attrib['src'])
            detail_aux = response.urljoin(product.css('a').attrib['href'])
            #check if the url is correct
            if detail_aux.find('catalogue') == -1:
                detail_aux = self.start_urls[0] +'catalogue/'+ product.css('a').attrib['href']
            item['detail_url'] = detail_aux
            
            yield item
        #try to get the next page element
        try:
            next_page = response.css('li.next > a').attrib['href'] 
            if next_page is not None:
                yield response.follow(next_page, callback = self.parse)
        except Exception as e:
            print(e)
        
