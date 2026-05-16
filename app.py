import http.server
import socketserver
from urllib.parse import urlparse, parse_qs

TODOS = []

def add_todo(title, priority="Medium"):
    todo = {"title": title, "priority": priority}
    TODOS.append(todo)
    return title

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            response = "<html><head><title>TODOs</title></head><body>"
            for todo in TODOS:
                response += f"<p>{todo['title']} - {todo['priority']}</p>"
            response += "</body></html>"
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(response.encode())
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == '/add':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = parse_qs(post_data.decode('utf-8'))
            title = data.get('title', [''])[0]
            priority = data.get('priority', ['Medium'])[0]
            add_todo(title, priority)
            self.send_response(302)
            self.send_header('Location', '/')
            self.end_headers()
        else:
            self.send_error(404)

if __name__ == "__main__":
    PORT = 8000
    with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
