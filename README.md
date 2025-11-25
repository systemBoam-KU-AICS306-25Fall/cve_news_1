# 🔍 CVE-Based Cybersecurity News Pipeline & Dashboard

A real-time cybersecurity news analysis system that collects security-related articles from Google News RSS, extracts CVE identifiers using NLP and regex, ranks the news based on importance, and displays the Top 5 CVE-related news on a dashboard.

This project was built as part of the **System Security (시스템보안)** team assignment.

---

## 🚀 Features

### ✔ 1. Automated News Collection
- Fetches global cybersecurity news through **Google News RSS**  
- Filters only articles that contain **CVE identifiers**

### ✔ 2. Text Cleaning & NLP Processing
- Removes HTML, stopwords, symbols  
- Extracts keywords using **TF-IDF**

### ✔ 3. CVE Extraction
- Identifies CVE patterns using regex:  
  `CVE-YYYY-NNNNN`

### ✔ 4. Importance Scoring (Ranking)
Each news article is ranked by a mixed score:
- **CVE Frequency Score** → 최근 7일 동안 해당 CVE가 얼마나 기사에서 많이 언급되었는지  
- **Recency Score** → 최신 뉴스일수록 높은 점수  
→ 두 점수를 합산해 Top 5 선정

### ✔ 5. REST API
Flask 서버를 통해 다음 API를 제공:

