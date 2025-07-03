# 1
import requests

# URL = "https://jsonplaceholder.typicode.com/posts"

# result = requests.get('https://jsonplaceholder.typicode.com/posts')

# for post in result.json()[:6]:
#     print(f"ID: {post['id']}, Title: {post['title']}")

# 2
# from flask import Flask
# from bs4 import BeautifulSoup
# import requests

# app = Flask(__name__)

# @app.route('/')
# def first_page():
#     response = requests.get('https://quotes.toscrape.com/')
#     soup = BeautifulSoup(response.text, 'html.parser')
#     quote = soup.find('span', class_='text')
#     return quote.text
    
    
# if __name__ == '__main__':
#     app.run(debug=True, port = 8000)

# 3
