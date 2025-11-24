import requests
from datetime import datetime

def fetch_tradingview_news():
    url = "https://news-mediator.tradingview.com/news-flow/v1/news"
    params = {
        "filter": [
            "lang:en",
            "symbol:CAPITALCOM:GOLD,MCX:GOLD1!,NCDEX:GOLD,OANDA:XAUUSD,SP:SPX,TVC:GOLD,VELOCITY:GOLD"
        ],
        "streaming": "false"  # Set to "true" for streaming, "false" for a single snapshot
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    news_items = response.json().get("items", [])

    for item in news_items:
        published_dt = datetime.utcfromtimestamp(item["published"])
        related = ", ".join([s["symbol"] for s in item.get("relatedSymbols", [])])
        link = item.get("link") or f"https://www.tradingview.com{item.get('storyPath','')}"
        print(f"📰 {item['title']}")
        print(f"    Source: {item['source']} | Published: {published_dt.strftime('%Y-%m-%d %H:%M:%S UTC')}")
        print(f"    Related Symbols: {related}")
        print(f"    Read more: {link}\n")

if __name__ == "__main__":
    fetch_tradingview_news()
