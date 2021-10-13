from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse as parser


class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('hello world'.encode())
        self.wfile.write('<br>'.encode())
        self.wfile.write(self.path.encode())
        self.wfile.write('<br>'.encode())
        # localhost:8080?btable=notice&mode=search&keyword=제주+코딩
        if '?' in self.path:
            self.wfile.write(str(self.path.split('?')[1].split('&')).encode())
            print(parser.parse_qsl(self.path.split('?')[1]))
            print(dict(parser.parse_qsl(self.path.split('?')[1])))


PORT = 8080
server = HTTPServer(('', PORT), ServerHandler)
print(f'서버가 {PORT}로 서비스 되고 있습니다.')
server.serve_forever()
