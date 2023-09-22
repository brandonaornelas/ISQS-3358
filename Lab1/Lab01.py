import requests as r


URLS = {
    "Samsung Galaxy s20 5G": "http://drd.ba.ttu.edu/isqs3358/labs/lab1/phone.php?id=1",
    "Apple IPhone 11": "http://drd.ba.ttu.edu/isqs3358/labs/lab1/phone.php?id=1341",
    "Google Pixel 4a": "http://drd.ba.ttu.edu/isqs3358/labs/lab1/phone.php?id=4228"
}

def get_information(res, url=None, key=None):
    res = r.get(url)
    print(f"Length of characters found in page: {len(res.text)}")
    print(f"HTML response code: {res.status_code}")
    print(f"Time to connect: {res.elapsed.microseconds}")
    print(f"Encoding Type: {res.encoding}")
    print(f"Content Type: {res.content[:50]}...")
    if url.startswith("https"):
        print("Website is SSL protected")
    else:
        print("Website is not SSL protected")
    print()
    

def main():
    for key, url in URLS.items():
        res = r.get(url)
        get_information(res, url, key)

main()