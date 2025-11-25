from fetch_news import fetch_rss_news
from clean_text import clean_text
from extract_keywords import extract_keywords
from extract_cve import extract_cves
from RSS_FEEDS import RSS_FEEDS

def build_news_pipeline(max_articles_per_feed=5):
    # ----- 1) 수집 -----
    raw_news = fetch_rss_news(RSS_FEEDS, max_articles_per_feed)

    # ----- 2) 전처리 -----
    cleaned_texts = [clean_text(article["description"]) for article in raw_news]

    # ----- 3) 키워드 추출 -----
    keywords_list = extract_keywords(cleaned_texts, top_n=5)

    # ----- 4) CVE 추출 -----
    cve_list = [extract_cves(article["description"]) for article in raw_news]

    # ----- 5) 데이터 구조 합치기 -----
    final_results = []
    for idx, article in enumerate(raw_news):
        item = {
            "title": article["title"],
            "link": article["link"],
            "published": article["published"],
            "clean_text": cleaned_texts[idx],
            "keywords": keywords_list[idx],
            "cves": cve_list[idx],
        }
        final_results.append(item)

    # 6) 최근 트렌드 점수 계산

    seven_days_ago = datetime.datetime.utcnow() - datetime.timedelta(days=7)

    def parse_date(pub):
        try:
            return datetime.datetime.strptime(pub, "%a, %d %b %Y %H:%M:%S %Z")
        except:
            return datetime.datetime(2000, 1, 1)

    recent_cves = []
    for news in final_results:
        pub_date = parse_date(news["published"])
        if pub_date >= seven_days_ago:
            recent_cves.extend(news["cves"])

    cve_week_freq = Counter(recent_cves)

    for news in final_results:
        trend_score = sum(cve_week_freq[cve] for cve in news["cves"])
        news["trend_score"] = trend_score


    return final_results
