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
            response = """
            <html>
            <head>
                <title>TODOs</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                    }
                    .card {
                        border: 1px solid #ccc;
                        padding: 10px;
                        margin-bottom: 10px;
                        background-color: #f9f9f9;
                    }
                    .form-container {
                        max-width: 400px;
                        margin: 0 auto;
                    }
                    .form-container input[type="text"] {
                        width: calc(100% - 22px);
                        padding: 10px;
                        margin-bottom: 10px;
                    }
                    .form-container select {
                        width: calc(100% - 22px);
                        padding: 10px;
                        margin-bottom: 10px;
                    }
                    .form-container button {
                        width: 100%;
                        padding: 10px;
                        background-color: #007BFF;
                        color: white;
                        border: none;
                        cursor: pointer;
                    }
                    .form-container button:hover {
                        background-color: #0056b3;
                    }
                </style>
            </head>
            <body>
                <div class="form-container">
                    <h1>Add New Todo</h1>
                    <form action="/add" method="post">
                        <input type="text" name="title" placeholder="Title" required>
                        <select name="priority">
                            <option value="Low">Low</option>
                            <option value="Medium">Medium</option>
                            <option value="High">High</option>
                        </select>
                        <button type="submit">Add</button>
                    </form>
                </div>
                <div>
                    <h1>Existing Todos</h1>
                    <div id="todos">
            """
            for todo in TODOS:
                response += f"""
                <div class="card">
                    <p>{todo['title']} - {todo['priority']}</p>
                </div>
                """
            response += """
                    </div>
                </div>
            </body>
            </html>
            """
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
