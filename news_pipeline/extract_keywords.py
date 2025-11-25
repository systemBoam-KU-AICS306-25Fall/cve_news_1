from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(cleaned_text_list, top_n=5):

    vectorizer = TfidfVectorizer(max_df=0.8, min_df=2)
    tfidf_matrix = vectorizer.fit_transform(cleaned_text_list)
    feature_names = vectorizer.get_feature_names_out()

    keywords_per_doc = []

    for doc_idx in range(tfidf_matrix.shape[0]):
        row = tfidf_matrix[doc_idx].toarray().flatten()
        top_indices = row.argsort()[::-1][:top_n]

        keywords = [feature_names[i] for i in top_indices]
        keywords_per_doc.append(keywords)

    return keywords_per_doc
