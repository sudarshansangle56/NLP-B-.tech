import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

sentence = """MUMBAI -- During the annual tech summit in 2023, Sundar Pichai,
the CEO of Google, highlighted India’s growing role in artificial intelligence
research and announced a $1 billion investment to support digital education
initiatives across rural areas."""

for sent in nltk.sent_tokenize(sentence):
    words = nltk.word_tokenize(sent)
    tagged = nltk.pos_tag(words)
    entities = nltk.ne_chunk(tagged)
    print(entities)
