import spacy
import re

nlp = spacy.load("en_core_web_sm")
url_pattern = re.compile(r'https?://\S+|www\.\S+')
ip_address_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
pan_number_pattern = re.compile(r'[A-Z]{5}[0-9]{4}[A-Z]')

def extract_entities(text):
    doc = nlp(text)
    urls = re.findall(url_pattern, text)
    ip_addresses = re.findall(ip_address_pattern, text)
    dates = re.findall(date_pattern, text)
    pan_numbers = re.findall(pan_number_pattern, text)

    # Extract named entities recognized by spaCy
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    return {
        'urls': urls,
        'ip_addresses': ip_addresses,
        'dates': dates,
        'pan_numbers': pan_numbers,
        'spaCy_entities': entities
    }
text_data = """
Visit our website at https://www.example.org. 
Server IP address is 192.168.45.22. 
Date of creation: 2024-10-07. 
Sample PAN card number: AEFGT4567P.
"""
results = extract_entities(text_data)
print("URLs:", results['urls'])
print("IP Addresses:", results['ip_addresses'])
print("Dates:", results['dates'])
print("PAN Numbers:", results['pan_numbers'])
print("Entities:", results['spaCy_entities'])
