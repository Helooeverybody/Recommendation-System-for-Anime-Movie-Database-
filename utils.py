import numpy as np 

def ndcg_at_k(y_true, y_pred, k):
    """
    y_true: list hoặc set item relevant
    y_pred: list item được rank (giảm dần theo score)
    """
    if len(y_true) == 0:
        return 0.0

    y_true = set(y_true)
    y_pred_k = y_pred[:k]

    # DCG
    dcg = 0.0
    for i, item in enumerate(y_pred_k):
        if item in y_true:
            dcg += 1.0 / np.log2(i + 2)

    # IDCG
    ideal_hits = min(len(y_true), k)
    idcg = sum(1.0 / np.log2(i + 2) for i in range(ideal_hits))

    return dcg / idcg if idcg > 0 else 0.0

def precision_at_k(y_true, y_pred, k):
    top_k = y_pred[:k]
    hit = len(set(top_k) & set(y_true))

    return hit / k if k > 0 else 0.0


def average_precision_at_k(y_true, y_pred, k):
    if len(y_true) == 0:
        return 0.0

    score = 0.0
    hits = 0
    y_true = set(y_true)

    for i, item in enumerate(y_pred[:k], start=1):
        if item in y_true:
            hits += 1
            score += hits / i

    return score / min(len(y_true), k)