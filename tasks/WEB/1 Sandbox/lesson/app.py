from flask import Flask
from flask import render_template, request
from files_db import Session, User_files

import os
import magic
import uuid
from werkzeug.utils import secure_filename

app = Flask(__name__)

FILES_PATH = 'static/users_files'

@app.route('/', methods = ['GET','POST'])
def f_page_1():
    if request.method == 'GET':
        return render_template('first_page.html')

    user_file = request.files.get('user_file')
    file_desc = request.form.get('file_desc')

    if not user_file or not file_desc:
        return "Недостатньо даних"

    mime = magic.Magic(mime=True)
    file_type = mime.from_buffer(user_file.read(1024))
    user_file.seek(0)

    if file_type not in ['image/png', 'image/jpeg', 'image/jpg'] :
        return "Обрано файл неправильного типу"

    if user_file.content_length > 10 * 1024 * 1024:
        return "Обрано файл великого розміру, допустимий розмір: менше 10 Мб"

    filename = secure_filename(user_file.filename)
    if not filename:
        return "Обрано файл неприйнятної назви"

    unique_filename = f"{uuid.uuid4()}_{filename}"

    file_path = os.path.join(FILES_PATH, unique_filename)
    user_file.save(file_path)
    
    with Session() as session:
        new_db_object = User_files(filename=unique_filename, description=file_desc)
        session.add(new_db_object)
        session.commit()
    
    return render_template('first_page.html',message='Файл успішно заванетажено!')

@app.route('/all_files')
def f_page_2():
    with Session() as session:
        all_data = session.query(User_files).all()
    return render_template('all_files.html',data = all_data)

if __name__ == '__main__':
    app.run(debug=True, port = 8000)