from crawler_yhd import crawler as yhd
import os
from pyhdfs import HdfsClient

def main(word):
    """ 比价工具整合 """
    products_list = []
    # 1号店数据
    print('1号店数据爬取完成')
    yhd(word, products_list)

    print('-------------------------开始排序---------------------------------')

    # 排序书的数据
    products_list = sorted(products_list, key=lambda item: float(item['price']), reverse=False)

    return products_list


if __name__ == '__main__':
    word = input('请输入商品名称：')
    main(word)
