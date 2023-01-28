# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from douban_book.items import DoubanBookItem
from uuid import uuid1
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from pymysql.err import DataError


class MysqlPipeline:
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.db = pymysql.connect(self.host, self.user, self.password, self.database, charset='utf8',
                                  port=self.port)
        self.cursor = self.db.cursor()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            port=crawler.settings.get('MYSQL_PORT'),
        )

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.db.ping(reconnect=True)
        self.db.close()

    def process_item(self, item, spider):
        # book_id = uuid1().hex
        if isinstance(item, DoubanBookItem):
            print('book: ', item.get('title'), item.get('grab_url'))
            data = dict(item)
            self._store_dict_to_table(data, 'book')

        return item

    def _store_dict_to_table(self, data: dict, table):
        """
        存入字典数据进入mysql.db中给定table
        :param data: 字典数据
        :param table: 表名称
        """
        # url = data['grab_url']
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql =f'insert into {table} ({keys}) values ({values})'
        # 防止断开
        self.db.ping(reconnect=True)
        try:
            self.cursor.execute(sql, tuple(data.values()))
        except DataError as e:
            error = str(e)
            if 'catalog' in error:
                del data['catalog']
            elif 'summary' in error:
                del data['summary']
            self._store_dict_to_table(data, table)
        else:
            self.db.commit()


# class ImagePipeline(ImagesPipeline):
#     def file_path(self, request, response=None, info=None, *, item=None):
#         url = request.url
#         file_name = url.split('/')[-1]
#         return file_name

#     def item_completed(self, results, item, info):
#         if isinstance(item, DoubanBookItem):
#             image_paths = [x['path'] for ok, x in results if ok]
#             # if not image_paths:
#             #     raise DropItem('Image Downloaded Failed')
#             return item

#     def get_media_requests(self, item, info):
#         if isinstance(item, DoubanBookItem):
#             yield Request(item['image'])
