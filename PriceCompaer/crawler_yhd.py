from pyhdfs import HdfsClient
import requests
from lxml import html
import urllib.parse

def crawler(word, products_list=[]):
    """ 爬取一号店的商品数据 """
    word = urllib.parse.quote(word)

    url = 'https://search.yhd.com/c0-0/k{0}'.format(word)

    # 获取html源码
    html_doc = requests.get(url).text

    # xpath对象
    selector = html.fromstring(html_doc)

    # 商品列表
    ul_list = selector.xpath('//div[@id="itemSearchList"]/div')

    # 解析数据
    for li in ul_list:

        # 标题
        title = li.xpath('div//p[@class="proName clearfix"]/a/@title')
        #print(title)

        # 链接
        link = li.xpath('div//p[@class="proName clearfix"]/a/@href')
        #print(link)

        # 价格
        price = li.xpath('div//p[@class="proPrice"]/em/@yhdprice')

        with open("p_price", "a", encoding="gbk") as f:
            for j in range(len(price)):
                f.write(price[j]+"\n")

        f.close()
        #print(price)


        if len(title) > 0 and len(link) > 0 and len(price) > 0:
            # print(title)
            # print(link)
            # print(price)
            # print('--------------------')

            products_list.append({
                'title': title[0],
                'price': price[0],
                'link': 'https:' + link[0],
                'referer': '1号店'
            })
    client = HdfsClient(hosts='222.27.166.209:50070', user_name='hadoop')
    client.copy_from_local('/home/hadoop/Downloads/PriceCompaer/p_price', '/p_price.txt')


if __name__ == '__main__':
    a = []
    crawler('玫瑰花', a)
