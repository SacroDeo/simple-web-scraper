# scraper.py
import time
import requests
from urllib.parse import urlparse
import urllib.robotparser
from bs4 import BeautifulSoup, Comment

USER_AGENT = "SimpleScraperUI/1.0 (+https://example.com/contact)"
REQUEST_TIMEOUT = 10
SLEEP_BETWEEN_REQUESTS = 1.0

def can_fetch(url, user_agent=USER_AGENT):
    parsed = urlparse(url)
    robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
    rp = urllib.robotparser.RobotFileParser()
    try:
        rp.set_url(robots_url)
        rp.read()
    except Exception:
        return True
    return rp.can_fetch(user_agent, url)

def fetch_html(url):
    headers = {"User-Agent": USER_AGENT, "Accept-Language": "en-US,en;q=0.9"}
    resp = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    return resp.text

def extract_visible_text(html):
    """Extract all visible text from the page, ignoring scripts, styles, etc."""
    soup = BeautifulSoup(html, "lxml")

    # Remove unwanted elements
    for tag in soup(["script", "style", "noscript", "iframe"]):
        tag.decompose()

    # Remove comments
    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()

    # Get all visible text and clean it
    text = soup.get_text(separator="\n", strip=True)
    lines = [line for line in text.split("\n") if line.strip()]
    return lines

def scrape_entire_page(url):
    if not can_fetch(url):
        return {"error": f"robots.txt disallows scraping {url}"}

    html = fetch_html(url)
    time.sleep(SLEEP_BETWEEN_REQUESTS)
    lines = extract_visible_text(html)

    if not lines:
        return {"error": "No visible text found on the page."}
    return {"results": lines}
