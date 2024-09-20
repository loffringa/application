import pandas as pd
import spacy

nlp = spacy.load("en_core_web_sm")

df = pd.read_csv('booksummaries.csv', nrows=5)  # Pas het aantal rijen aan naar behoefte

books_with_voldemort = df[df['title'].str.contains('Voldemort', case=False, na=False)]

print("Books mentioning 'Voldemort':")
print(books_with_voldemort[['title', 'genres']])
print("\n")

books_with_god = df[df['title'].str.contains('God', case=False, na=False)]

print("Books mentioning 'God':")
print(books_with_god[['title', 'genres']])
print("\n")

books_with_numbers_in_title = df[df['title'].str.contains(r'\d', na=False)]

print("Books with numbers in the title:")
print(books_with_numbers_in_title[['title', 'genres']])
print("\n")

lotr_books = df[df['title'].str.contains('Lord of the Rings', case=False, na=False)]

persons = set()
for index, row in lotr_books.iterrows():
    title = row['title']
    doc = nlp(title)
    persons.update([ent.text for ent in doc.ents if ent.label_ == "PERSON"])

print("Names of persons in 'Lord of the Rings' books:")
print(persons)
