def rank_candidates(scores):
    ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
    return ranked
