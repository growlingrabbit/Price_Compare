from flask import Flask, render_template, request
from crawler_product import main

app = Flask(__name__)


@app.route('/')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to PriceCompare!')


@app.route('/compare', methods=['POST'])
def search_products() -> str:
    word = request.form['word']
    title = '比价结果'
    titles = ('商品', '价格', '链接', '来源')
    results = main(word)
    return render_template('results.html',
                           the_word=word,
                           the_title=title,
                           the_row_titles=titles,
                           the_data=results,)


app.run()
