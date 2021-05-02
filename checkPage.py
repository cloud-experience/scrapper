import requests
from bs4 import BeautifulSoup


def unshortenURL(URL):
    print(f"원본 URL : {URL}")
    session = requests.Session()  # so connections are recycled
    r = session.head(URL, allow_redirects=True)
    return r.url


def conn(URL):
    print(f"실제 URL : {URL}")
    r = requests.get(URL)
    if r.status_code == 200:
        print(f"{URL} CONNECTED")
    else:
        print(f"ERROR CODE : {r.status_code}")
    return r.text


def extractString(data):
    soup = BeautifulSoup(data, "html.parser")
    words = soup.find_all("a")
    return words


def checkString(words, TARGET_WORDS):
    count = 0
    for word in words:
        if word.string in TARGET_WORDS:
            count += 1
        # print(f"{word.string} : {count}")
    return count


def checkPage(URL, TARGET_WORDS):
    URL = unshortenURL(URL)
    data = conn(URL)
    words = extractString(data)
    count = checkString(words, TARGET_WORDS)
    return count