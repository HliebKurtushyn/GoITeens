from flask import Flask, Response
import json

app = Flask(__name__)

books = [
    {"id": 1, "title": "1984", "author": "George Orwell", "genre": "Dystopian"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Classic"}
]

@app.route('/')
def index():
    return 'Home Page'

# @app.route('/about/')
# def about():
#     return 'About page'

# @app.route('/book/')
# def book_list():
#     books_list = "<br>".join([f"{book['id']}. {book['title']} — {book['author']}" for book in books])
#     return f"Список книг:<br>{books_list}"

# @app.route('/book/<int:id>/')
# def book(id):
#     book = next((book for book in books if book["id"] == id), None)
#     if book:
#         return f'Назва: {book['title']}<br>Автор: {book["author"]}<br>Жанр: {book['genre']}'
#     else:
#         return 'Книгу не знайдено', 404
    
# @app.route('/genres/')
# def genres():
#     genres = '<br>'.join(set(book['genre'] for book in books))
#     return genres

# @app.route('/user/<username>/')
# def user(username):
#     return f'Hello, {username}'

# @app.route('/contacts/')
# def contact():
#     return 'Contacts page'

# @app.route('/multiply/<int:num1>/<int:num2>/')
# def multiply(num1, num2):
#     return f'Result: {num1 * num2}'

# @app.route('/json-example/')
# def return_json():
#     dict_example = {
#         'message': 'Урок Flask завершено успішно'
#     }
#     dict_json = json.dumps(dict_example, ensure_ascii=False)
    
#     return Response(dict_json, content_type="application/json")

if __name__ == "__main__":
    app.run(debug=True)