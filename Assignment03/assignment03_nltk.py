import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')  
nltk.download('maxent_ne_chunker')
nltk.download('maxent_ne_chunker_tab')           
nltk.download('words')


sentence = """MUMBAI -- During the annual tech summit in 2023, Sundar Pichai, 
the CEO of Google, highlighted India’s growing role in artificial intelligence 
research and announced a $1 billion investment to support digital education 
initiatives across rural areas."""


for sent in nltk.sent_tokenize(sentence):
    words = nltk.word_tokenize(sent)
    pos_tags = nltk.pos_tag(words)
    chunks = nltk.ne_chunk(pos_tags)
    for chunk in chunks:
        if hasattr(chunk, 'label'):
            print(chunk.label(), ' '.join(c[0] for c in chunk))