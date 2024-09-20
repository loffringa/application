import pandas as pd
import spacy

nlp = spacy.load("en_core_web_sm")

df = pd.read_csv('booksummaries.csv', nrows=5)

for index, row in df.iterrows():
    summary = row['title']
    doc = nlp(summary)

    print(f"title {index + 1}: {summary}")

    nouns = [token.text for token in doc if token.pos_ == "NOUN"]
    verbs = [token.text for token in doc if token.pos_ == "VERB"]
    verb_related_words = [token.text for token in doc if token.dep_ in ("amod", "advmod", "dobj", "pobj", "attr")]
    compound_words = [token.text for token in doc if token.dep_ == "compound"]

    print(f"Nouns: {nouns}")
    print(f"Verbs: {verbs}")
    print(f"Words related to verbs: {verb_related_words}")
    print(f"Compound words: {compound_words}")
    print("\n")
