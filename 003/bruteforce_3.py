import requests

로그인패킷 = {
    'id': 'hojun',
    'pw': '1234',
}

address = requests.post('http://127.0.0.1:8080/', data=로그인패킷)
