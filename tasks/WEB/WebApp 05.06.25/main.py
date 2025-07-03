from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import mimetypes
import pathlib


class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        pr_url = urllib.parse.urlparse(self.path)

        if pr_url.path == '/':  # Головна сторінка
            self.send_html_file('index.html')
        elif pr_url.path == '/search': # Сторінка пошуку пісні
            self.send_html_file('search.html')
        elif pathlib.Path().joinpath(pr_url.path[1:]).exists():  # Статичні ресурси
            self.send_static()
        else:  # Сторінка помилки
            self.send_html_file('error.html', 404)
    
    def send_html_file(self, filename, status=200):
        """Відправка HTML-файлу у відповідь браузеру."""
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        try:
            with open(filename, 'rb') as file:
                self.wfile.write(file.read())
        except FileNotFoundError:
            self.send_html_file('error.html', 404)

    def send_static(self):
        """Відправка статичних файлів (CSS, зображення) у відповідь клієнту."""
        self.send_response(200)
        mt = mimetypes.guess_type(self.path)  # Визначення типу файлу
        if mt[0]:
            self.send_header("Content-type", mt[0])  # Додаємо тип MIME
        else:
            self.send_header("Content-type", 'application/octet-stream')
        self.end_headers()


        try:
            with open(f'.{self.path}', 'rb') as file:
                self.wfile.write(file.read())
        except FileNotFoundError:
            self.send_html_file('error.html', 404)

    


def run(server_class=HTTPServer, handler_class=HttpHandler):
    """Запуск локального сервера."""
    server_address = ('', 8000)  # Сервер працює на порту 8000
    http = server_class(server_address, handler_class)
    try:
        print("Сервер запущено на <http://localhost:8000>")
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()

if __name__ == '__main__':
    run()