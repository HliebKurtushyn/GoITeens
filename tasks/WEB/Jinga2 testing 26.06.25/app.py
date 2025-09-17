from flask import Flask, render_template

app = Flask(__name__)

# 1
# @app.route('/')
# def student():
#     is_student = False
    
#     return render_template("student.html", is_student = is_student)

# 2
# @app.route('/')
# def store():
#     suplies = []
    
#     return render_template("shop.html", suplies=suplies)

# 4
# @app.route('/todos/')
# def todos():
#     tasks = [
#         {"name": "Вивчити Flask", "completed": True},
#         {"name": "Зрозуміти Jinja2", "completed": False},
#         {"name": "Зробити домашнє завдання", "completed": False}
#     ]
    
#     return render_template("todos.html", tasks=tasks)
    
# 5
# works = [
#     {"working": "Telegram-bot", "year": 2023},
#     {"working": "Game", "year": 2022},
#     {"working": "Website", "year": 2023}
# ]

# @app.route('/')
# def portfolio():
#     context = {
#         'title': 'Portfolio',
#         'portfolio': works
#     }
    
#     return render_template('portfolio.html', **context)




if __name__ == '__main__':
  app.run(debug=True)
