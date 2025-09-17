from flask import Flask, render_template_string, request, send_file
import os
import requests

app = Flask(__name__)

temp_qr = "temp_qrcode.jpg"

@app.after_request
def delete_images(response):
    if os.path.exists(temp_qr):
        try:
            os.remove(temp_qr)
        except Exception as e:
            return 'deletion error'
    return response

@app.route('/set_up')
def get_qr_code():
    return render_template_string(''' 
        <form action="{{ url_for('response') }}" method="get">
            <input placeholder="Enter a text to convert it into qr code" name="text" required>
            <input type="submit" value="Generate qr">
        </form>            
    ''')

@app.route('/')
def response():
    text = request.args.get('text')

    r = requests.get(f'https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={text}')
    if r.status_code == 200:
        with open(f'homeworks/{temp_qr}', 'wb') as f:
            f.write(r.content)
        return send_file(temp_qr, mimetype='image/jpeg')
    else:
        return 'error generating'

if __name__ == "__main__":
    app.run(debug=True)
