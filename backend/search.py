from flask import Flask
from flask import request
from flask import jsonify



app = Flask(__name__)

app.route('/api/search.py', methods=['POST'])
def search_book(book_name):
    with open('E:/books/bookprice/sampledata.json', 'r', encoding = "utf8") as f:
        data = json.load(f)
        for book in data['books']:
            if book['title'] == book_name:
                return book
        return 'Book not found'


if __name__ == '__main__':
    app.run(debug=True)