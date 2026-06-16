import requests
from bs4 import BeautifulSoup
URL = "https://bdixtv24.com/live-tv/football-world-cup-2026/"
def get_stream_url():
    try:
        resp = requests.get(URL, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')
        for iframe in soup.find_all('iframe'):
            src = iframe.get('src')
            if src and ('server' in src.lower() or 'embed' in src.lower()):
                return src
        first = soup.find('iframe')
        if first and first.get('src'):
            return first.get('src')
    except Exception as e:
        print(f"Scraping error: {e}")
    return None
if __name__ == "__main__":
    url = get_stream_url()
    if url:
        with open("stream_url.txt", "w") as f:
            f.write(url)
        print(f"✅ Stream URL: {url}")
    else:
        print("❌ No stream found")
        exit(1)