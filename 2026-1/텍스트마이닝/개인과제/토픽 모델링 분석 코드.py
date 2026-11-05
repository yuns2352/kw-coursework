# Topic Modeling Analysis Code - Revised report version
# Input: csv/savedrecs.csv exported from Web of Science
# Output: preprocessing statistics, NMF topics, document-topic assignments

import re
import pandas as pd
import numpy as np
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS
from sklearn.decomposition import NMF

df = pd.read_csv("savedrecs.csv")
data = df[df["Abstract"].notna()].copy()
data["text"] = data["Article Title"].fillna("") + " " + data["Abstract"].fillna("")

extra_stops = {"vehicle","vehicles","autonomous","automated","driving","drive","driver","car","cars",
               "paper","study","studies","proposed","method","methods","model","models","based","using","used",
               "approach","result","results","show","shows","data","av","avs","ego","framework","algorithm","algorithms","system","systems","road","roads"}
stop_words = sorted(set(ENGLISH_STOP_WORDS) | extra_stops)

vectorizer = TfidfVectorizer(lowercase=True, stop_words=stop_words, max_df=0.85, min_df=2,
                             ngram_range=(1, 2), token_pattern=r"(?u)\b[a-zA-Z][a-zA-Z\-]{2,}\b")
X = vectorizer.fit_transform(data["text"])
terms = np.array(vectorizer.get_feature_names_out())

nmf = NMF(n_components=5, random_state=42, init="nndsvda", max_iter=1000)
W = nmf.fit_transform(X)
H = nmf.components_

rows = []
for i, comp in enumerate(H, start=1):
    top_idx = comp.argsort()[::-1][:8]
    rows.append({"Topic": i, "Top Keywords": ", ".join(terms[top_idx]),
                 "Document Count": int((W.argmax(axis=1) + 1 == i).sum())})

topics = pd.DataFrame(rows)
data["topic_id"] = W.argmax(axis=1) + 1
data["topic_score"] = W.max(axis=1)

print("Total records:", len(df))
print("Records with abstracts:", len(data))
print("TF-IDF matrix:", X.shape)
print(topics)
topics.to_csv("nmf_topics.csv", index=False, encoding="utf-8-sig")
data[["Article Title", "Publication Year", "Source Title", "Document Type", "topic_id", "topic_score", "UT (Unique ID)"]].to_csv("document_topic_assignments.csv", index=False, encoding="utf-8-sig")
