import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")


text = """
Barack Obama was the 44th President of the United States. 
Apple Inc. is planning to open a new office in London by next year. 
Elon Musk held a meeting in Berlin to discuss Tesla’s expansion in Europe. 
The United Nations will host a climate summit in Paris this December.
"""

doc = nlp(text)

print("----- Named Entities -----")
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

displacy.serve(doc, style="ent", host="127.0.0.1", port=5000)