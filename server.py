# server.py
from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000

class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

server = HTTPServer(("", PORT), Handler)
print(f"🎉 Server running at http://localhost:{PORT}")
server.serve_forever()
