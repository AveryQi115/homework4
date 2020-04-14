
with open('./flask/static/book.txt', 'r', encoding='UTF-8') as f:
    book_dict = dict()
    strLine = f.readline()
    line = strLine.split()
    length = len(line)
    book_dict = book_dict.fromkeys(line, [])
    print(book_dict)

    num=[]
    name=[]
    type=[]
    for i in range(5):
        f.readline()
        line = f.readline().split()
        assert(len(line) == length)
        num.append(line[0])
        name.append(line[1])
        type.append(line[2])

    book_dict['\ufeff序号'] = num
    book_dict['书名'] = name
    book_dict['分类'] = type
    print(book_dict)





