from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_candidates(job_description, resumes):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([job_description] + resumes)
    scores = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
    return scores
