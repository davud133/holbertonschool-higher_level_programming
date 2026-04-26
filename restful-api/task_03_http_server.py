#!/usr/bin/python3


from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')
        elif self.path =="/data":
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"ame": "John", "age": 30, "city": "New York"}')
        elif self.path == "/status":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'OK.')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Page Not Found')

server = HTTPServer(("localhost",8000), MyHandler)
server.serve_forever()

