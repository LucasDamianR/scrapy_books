# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from itemadapter import ItemAdapter
import pymongo

class BookScraperPipeline:

    def __init__(self):
        #set local connection
        self.cnxn = pymongo.MongoClient(
                                'localhost',
                                27017
                            )
        db = self.cnxn['my_books']
        self.collection = db['book']


    def process_item(self, item, spider):
        #insert documents
        self.collection.insert_one(dict(item))
        return item
