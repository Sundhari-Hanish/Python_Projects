import concurrent.futures
import threading
import requests
urls = [
    "https://www.yahoo.com",
    "https://google.com",
    "https://github.com",
    "https://wikipedia.org",
    "https://stackoverflow.com",
    "https://python.org",
    "https://openai.com",
    "https://reddit.com",
    "https://microsoft.com",
    "https://apple.com"
]
def fetch_url(url):
    thread_name = threading.current_thread().name
    print(f"{thread_name} fetching {url}")
    try:
        response = requests.get(url, timeout=5)
        status_code = response.status_code
        page_size = len(response.content)
        print(f"{thread_name} completed {url} | Status: {status_code} | Size: {page_size} bytes")
    except requests.exceptions.RequestException as e:
        print(f"{thread_name} error fetching {url} -> {e}")
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(fetch_url, urls)



# OUTPUT:
# ThreadPoolExecutor-0_0 fetching https://www.yahoo.com
# ThreadPoolExecutor-0_1 fetching https://google.com
# ThreadPoolExecutor-0_2 fetching https://github.com
# ThreadPoolExecutor-0_3 fetching https://wikipedia.org
# ThreadPoolExecutor-0_4 fetching https://stackoverflow.com
# ThreadPoolExecutor-0_3 completed https://wikipedia.org | Status: 403 | Size: 126 bytes
# ThreadPoolExecutor-0_3 fetching https://python.org
# ThreadPoolExecutor-0_0 completed https://www.yahoo.com | Status: 429 | Size: 23 bytes
# ThreadPoolExecutor-0_0 fetching https://openai.com
# ThreadPoolExecutor-0_2 completed https://github.com | Status: 200 | Size: 566064 bytes
# ThreadPoolExecutor-0_2 fetching https://reddit.com
# ThreadPoolExecutor-0_4 completed https://stackoverflow.com | Status: 200 | Size: 426864 bytes
# ThreadPoolExecutor-0_4 fetching https://microsoft.com
# ThreadPoolExecutor-0_0 completed https://openai.com | Status: 403 | Size: 11859 bytes
# ThreadPoolExecutor-0_0 fetching https://apple.com
# ThreadPoolExecutor-0_1 completed https://google.com | Status: 200 | Size: 22870 bytes
# ThreadPoolExecutor-0_3 completed https://python.org | Status: 200 | Size: 49418 bytes
# ThreadPoolExecutor-0_4 completed https://microsoft.com | Status: 200 | Size: 181192 bytes
# ThreadPoolExecutor-0_2 completed https://reddit.com | Status: 200 | Size: 476400 bytes
# ThreadPoolExecutor-0_0 completed https://apple.com | Status: 200 | Size: 267840 bytes
