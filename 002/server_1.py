from http.server import HTTPServer, BaseHTTPRequestHandler


class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # self.send_error()
        # self.send_header()
        # self.send_response()
        self.send_response(200)  # http 응답값
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('hello world<br>'.encode())
        self.wfile.write(self.path.encode())
        # http://www.jejuiucc.or.kr/default/Bd/list.php?btable=notice&mode=search&ischkdel=&ischkmove=&lcate=&chkdelvar=&l_search=sc&keyword=제주+코딩
        # 127.0.0.1:8080?btable=notice&mode=search&ischkdel=&ischkmove=&lcate=&chkdelvar=&l_search=sc&keyword=제주+코딩
        # localhost:8080?btable=notice&mode=search&ischkdel=&ischkmove=&lcate=&chkdelvar=&l_search=sc&keyword=제주+코딩
        # 이렇게 했을 때 어떻게 보여지는지 한 번 보세요.
        # url 구조
        # URL(URI)의 구조
        # http://www.paullab.co.kr/about/?uid=Redplus&pwd=1234#bottom
        # 1. 도메인 : www.paullab.co.kr
        # 2. 프로토콜 or PORT : http://주소:80, https://주소:443...
        # 3. 하위 디렉토리 또는 자원경로 : /about/
        # 4. 기본문서(페이지) : 가장 먼저 실행되는 페이지는 보통 index.html
        # 5. 쿼리스트링(QueryString) : list.php에 물음표 뒤의 값(키와 값) 정보를 전달 '?키1=값1&키2=값2&키3=값3...'


PORT = 8080
server = HTTPServer(('', PORT), ServerHandler)
print(f'서버가 {PORT}로 서비스 되고 있습니다.')
server.serve_forever()
