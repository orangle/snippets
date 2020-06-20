# coding:utf-8
import requests
import asyncio
from concurrent import futures

MAX_WORKERS = 100
url_list = ["http://baidu.com"]*500


def fetch_one(url):
    try:
        resp = requests.get(url, timeout=2)
    except requests.exceptions.ConnectionError:
        return False
    except Exception as e:
        return False
    return resp.status_code == 200


def download_thread():
    workers = min(MAX_WORKERS, len(url_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(fetch_one, sorted(url_list))
    print(list(res))
    return len(list(res))


def download_sync():
    res = []
    for url in url_list:
        res = fetch_one(url)
    return res


def download_async():
    pass


def test_down_many():
    print(download_thread())


def test_down_sync():
    print(download_sync())


