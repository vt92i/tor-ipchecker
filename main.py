from datetime import datetime
import requests as req
import time as t
import sys


def get_current_ip():
    session = req.Session()
    session.proxies = {}
    session.proxies['http'] = 'socks5://127.0.0.1:9050'
    session.proxies['https'] = 'socks5://127.0.0.1:9050'
    try:
        res = session.get("https://icanhazip.com")
        return res.text.strip()
    except req.RequestException:
        t.sleep(3)
        get_current_ip()


if __name__ == "__main__":
    num = 0
    while True:
        try:
            num += 1
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f'|{num}|', f'|{get_current_ip()}|', f'|{current_time}|')
        except KeyboardInterrupt:
            sys.exit()
