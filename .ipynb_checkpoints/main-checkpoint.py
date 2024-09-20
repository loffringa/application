import pandas as pd
import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

df = pd.read_csv('booksummaries.csv', nrows=5)

for index, row in df.iterrows():
    summary = row['title']
    doc = nlp(summary)

    displacy.render(doc, style="ent", jupyter=True)
    print(f"Summary {index + 1}:")
    print(summary)
    print("\n")
