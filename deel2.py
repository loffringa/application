import pandas as pd
import spacy
from spacy import displacy

df = pd.read_csv("booksummaries.csv", nrows=1)

nlp = spacy.load("en_core_web_sm")
doc = nlp(df.to_string())
displacy.serve(doc, style="dep")