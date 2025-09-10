import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

texts = [
    "Barack Obama was the 44th President of the United States.",
    "Google was founded in 1998 in California by Larry Page and Sergey Brin.",
    "The Taj Mahal is located in Agra, India and was built by Shah Jahan.",
    "Apple is planning to release the new iPhone in September 2025.",
    "Cristiano Ronaldo plays for Al Nassr in Saudi Arabia.",
    "Amazon headquarters is in Seattle and Jeff Bezos was its founder."
]

for text in texts:
    print("\nInput Text:", text)
    doc = nlp(text)
    for ent in doc.ents:
        print(f"{ent.text} --> {ent.label_} ({spacy.explain(ent.label_)})")
    
    displacy.serve(doc, style="ent")
