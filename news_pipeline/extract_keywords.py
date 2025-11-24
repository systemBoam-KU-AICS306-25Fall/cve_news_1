from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(cleaned_text_list, top_n=5):
    """
    cleaned_text_list: 전처리된 문서들의 리스트 (문자열 리스트)
    top_n: 각 문서에서 뽑을 키워드 개수
    """

    # 1) TF-IDF 벡터라이저 생성
    vectorizer = TfidfVectorizer(max_df=0.8, min_df=2)
    
    # 2) TF-IDF 행렬 생성
    tfidf_matrix = vectorizer.fit_transform(cleaned_text_list)

    # 3) 모든 단어(특징) 리스트
    feature_names = vectorizer.get_feature_names_out()

    # 4) 문서별로 상위 N개의 키워드 추출
    keywords_per_doc = []

    for doc_idx in range(tfidf_matrix.shape[0]):
        row = tfidf_matrix[doc_idx].toarray().flatten()

        # 키워드 인덱스 상위 N개
        top_indices = row.argsort()[::-1][:top_n]

        keywords = [feature_names[i] for i in top_indices]
        keywords_per_doc.append(keywords)

    return keywords_per_doc
