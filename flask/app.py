from flask import Flask
import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

app = Flask(__name__)


@app.route('/')
def table():
    with open('./static/book.txt', 'r', encoding='UTF-8') as f:
        book_dict = dict()
        strLine = f.readline()
        line = strLine.split()
        length = len(line)
        book_dict = book_dict.fromkeys(line, [])

        num = []
        name = []
        type = []
        for i in range(5):
            f.readline()
            line = f.readline().split()
            assert (len(line) == length)
            num.append(line[0])
            name.append(line[1])
            type.append(line[2])

        book_dict['\ufeff序号'] = num
        book_dict['书名'] = name
        book_dict['分类'] = type
    return render_template('table.html', table=book_dict)


if __name__ == '__main__':
    app.run(debug=True)
