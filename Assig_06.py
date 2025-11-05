import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")

multiline_text = """
Artificial Intelligence is transforming the way humans interact with technology. 
It enables machines to perform tasks that traditionally required human intelligence. 
Through deep learning and data analysis, AI systems can now recognize speech, translate languages, and even make decisions.
"""

multiline_doc = nlp(multiline_text)

for token in multiline_doc:
    print(
        f"""
TOKEN: {token.text}
=====
{token.tag_ = }
{token.head.text = }
{token.dep_ = }"""
    )

displacy.serve(multiline_doc, style="dep")
