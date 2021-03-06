import gevent.monkey

from urllib.request import urlopen


gevent.monkey.patch_all()
urls = ["http://www.google.com",
        "http://www.yandex.ru",
        "http://www.python.org"]


def print_head(url):
    print(f"Старт {url}")
    data = urlopen(url).read()[:100]
    print(f"{url}: {len(data)} данные: {data} ...")


jobs = [gevent.spawn(print_head, _url) for _url in urls]
gevent.wait(jobs)