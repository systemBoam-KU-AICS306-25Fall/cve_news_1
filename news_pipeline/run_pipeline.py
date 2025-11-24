from fetch_news import fetch_rss_news
from clean_text import clean_text
from extract_keywords import extract_keywords
from extract_cve import extract_cves
from RSS_FEEDS import RSS_FEEDS


def build_news_pipeline(max_articles_per_feed=5):
    # STEP 1: 뉴스 가져오기
    raw_news = fetch_rss_news(RSS_FEEDS, max_articles_per_feed=max_articles_per_feed)

    # STEP 2: 전처리된 텍스트 리스트 생성
    cleaned_texts = [clean_text(article["description"]) for article in raw_news]

    # STEP 3: 키워드 추출
    keywords_list = extract_keywords(cleaned_texts, top_n=5)

    # STEP 4: 뉴스마다 CVE 추출
    cve_list = [extract_cves(article["description"]) for article in raw_news]

    # STEP 5: 전체 구조 합치기
    final_results = []
    for idx, article in enumerate(raw_news):
        result = {
            "title": article["title"],
            "link": article["link"],
            "published": article["published"],
            "clean_text": cleaned_texts[idx],
            "keywords": keywords_list[idx],
            "cves": cve_list[idx],
        }
        final_results.append(result)

    return final_results


# 테스트 실행
if __name__ == "__main__":
    news_data = build_news_pipeline()
    for i, item in enumerate(news_data[:5]):
        print(f"\n==== 뉴스 {i+1} ====")
        print("제목:", item["title"])
        print("키워드:", item["keywords"])
        print("CVE:", item["cves"])
        print("정제 텍스트:", item["clean_text"][:100], "...")
