from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse as parser


class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()

        f = open("index.html", 'r')
        data = f.read()
        # print(data)
        f.close()
        self.wfile.write(data.encode())

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        print('POST로 값이 들어왔습니다.')
        print(self.path.encode())
        data = self.rfile.read(int(self.headers['Content-Length']))
        if data is not None:
            data_decode = dict(parser.parse_qs(data.decode()))
        print(f'post params = {data_decode}')
        if data_decode['id'] == ['hojun'] and data_decode['pw'] == ['1234']:
            self.wfile.write('login success'.encode())
        else:
            f = open("index_fail.html", 'r')
            data = f.read()
            f.close()
            self.wfile.write(data.encode())


PORT = 8080
server = HTTPServer(('', PORT), ServerHandler)
print(f'서버가 {PORT}로 서비스 되고 있습니다.')
server.serve_forever()
