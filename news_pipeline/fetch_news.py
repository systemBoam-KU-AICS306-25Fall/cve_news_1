import feedparser

def fetch_rss_news(feed_urls, max_articles_per_feed=10):
    articles = []

    for url in feed_urls:
        feed = feedparser.parse(url)

        for entry in feed.entries[:max_articles_per_feed]:
            articles.append({
                "title": entry.title if "title" in entry else "",
                "link": entry.link if "link" in entry else "",
                "description": entry.summary if "summary" in entry else "",
                "published": entry.published if "published" in entry else ""
            })

    return articles