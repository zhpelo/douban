import scrapy
import re
import json
import time
from douban.items import DoubanBookItem


class AllBookSpider(scrapy.Spider):
    name = 'allbook'
    allowed_domains = ['book.douban.com']
    
    def start_requests(self):
        # 36175320 10000000 -1
        # 4000000,10000000
        for i in range(36175320,10000000, -1):
            url='https://book.douban.com/subject/%s/'%i
            yield scrapy.Request(url)

    def parse(self, response):
        item = DoubanBookItem()
        item['grab_url'] = response.url
        schema = response.xpath("//script[@type='application/ld+json']/text()").extract_first()
        if schema is not None:
            d = eval(schema)
            item['title'] = d.get('name')
            item['isbn'] = d.get('isbn')
            try:
                author = d['author'][0].get('name')
            except IndexError:
                pass
            else:
                item['author'] = author
        info = response.xpath("//div[@id='info']").extract_first()
        info_map = {
            '副标题': 'subtitle',
            '原作名': 'origin_title',
            '出版年': 'pubdate',
            '出版社': 'publisher',
            '页数': 'pages',
            '定价': 'price',
            '装帧': 'binding',
            '丛书': 'series',
        }
        for name, item_name in info_map.items():
            try:
                temp = re.search(rf'{name}:</span>([\s\S]*?)<br>', info)
            except:
                continue
            if temp is not None:
                item[item_name] = temp.group(1).strip()

        rating = response.xpath("//strong[@class='ll rating_num ']/text()").extract_first()
        if rating is not None:
            item['rating'] = rating.strip()
        #书籍封面
        item['image'] = response.xpath("//*[@id='mainpic']/a/@href").extract_first()
        #译者
        translator = response.xpath("//span[contains(text(),' 译者')]/../a/text()").extract()
        item["translator"] = ','.join(translator)

        #内容简介
        item['summary'] = response.xpath("//*[@id='link-report']/span[@class='all hidden']/div/div[@class='intro']").extract_first()
        if not item['summary']:
            item['summary'] = response.xpath("//*[@id='link-report']/div/div").extract_first('NULL')

        #作者简介
        item['author_intro'] = response.xpath(
            "//span[text()='作者简介']/../following-sibling::div[1]//div[@class='intro']").extract_first('NULL')
        
        if response.url is not None:
            book_id = re.search(r'(\d+)/$', response.url).group(1)
            # #豆瓣id
            # item['douban_id'] = book_id
            directory_list = response.xpath(f"//div[@id='dir_{book_id}_full']/text()").extract()
            
            item['catalog'] = ';'.join(directory_list)

        #采集时间
        item["updatetime"] = int(time.time())

        #更多格式处理
        item['image'] = item['image'][25: ]

        pattern = re.compile(r'<[^>]+>',re.S)

        if item.get('series'):
            item['series'] = pattern.sub('', item['series'])

        if item.get('publisher'):
            item['publisher'] = pattern.sub('', item['publisher'])

        item['catalog'] = item['catalog'][: -25]

        yield item

       

    def parse_review_page(self, response):
        review_item = DoubanBookReview()
        data = response.meta["data"]
        review_item['url'] = data['url']
        review_item['title'] = data['title']
        review = re.sub(r'<.*?>', ' ', json.loads(response.text)['html'])
        review_item['review'] = re.sub(r"--&gt;|\u3000|\n|\t|&nbsp;|&amp;|&quot;", " ", review).strip()
        yield review_item


if __name__ == '__main__':
    from scrapy.cmdline import execute
    # cmd: scrapy crawl book
    execute(['scrapy', 'crawl', 'book'])