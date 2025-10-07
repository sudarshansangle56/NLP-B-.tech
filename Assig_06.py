import spacy
from spacy import displacy

# Load the small English model from spaCy
nlp = spacy.load("en_core_web_sm")

# Input paragraph for dependency parsing
multiline_text = """
Artificial Intelligence is transforming the way humans interact with technology. 
It enables machines to perform tasks that traditionally required human intelligence. 
Through deep learning and data analysis, AI systems can now recognize speech, translate languages, and even make decisions.
"""

# Process the text with the NLP model
multiline_doc = nlp(multiline_text)

# Display each token’s tag, head, and dependency relation
for token in multiline_doc:
    print(
        f"""
TOKEN: {token.text}
=====
{token.tag_ = }
{token.head.text = }
{token.dep_ = }"""
    )

# Visualize the dependency structure in the browser
displacy.serve(multiline_doc, style="dep")
