import requests
from bs4 import BeautifulSoup
import re


class TwitterAuth:
    __BASE_URL = "https://twitter.com/"
    __AUTH_URL = "https://abs.twimg.com:443/responsive-web/client-web/main.6c1aeb65.js"

    __auth_headers = {
        "Connection": "close",
        "x-twitter-client-language": "en",
        "x-twitter-active-user": "yes",
        "content-type": "application/json",
        "Accept": "*/*",
        "Origin": "https://twitter.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://twitter.com/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9"
    }

    __token_req_headers = {
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9"
    }

    @classmethod
    def refresh_token(cls):
        r = requests.get(cls.__BASE_URL, headers=cls.__token_req_headers)
        if r.ok:
            soup = BeautifulSoup(r.content, 'lxml')
            token_tag = soup.find_all("script")[-1]
            return re.findall(r"gt=([\d]+)|$", str(token_tag))[0]

    @classmethod
    def auth_header(cls):
        r = requests.get(cls.__AUTH_URL)
        if r.ok:
            response_js = r.text
            bearer_start_index = response_js.find('AAAAAAAAAA')
            bearer_end_index = response_js[bearer_start_index:].find('"') + bearer_start_index
            return f"Bearer {response_js[bearer_start_index: bearer_end_index]}"

    @classmethod
    def get_base_cookies(cls):
        r = requests.get(cls.__BASE_URL)
        if r.ok:
            return r.cookies
