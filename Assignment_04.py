from nltk import ngrams
from nltk.util import ngrams

n = 1
sentence = "Machine learning allows computers to learn from data and make predictions or decisions without being explicitly programmed."


unigrams = ngrams(sentence.split(), n)
print(f"\n***********   UNIGRAMS   ************************")
for item in unigrams:
    print(item)

n = 2
sentence = "Machine learning allows computers to learn from data and make predictions or decisions without being explicitly programmed."
bigrams = ngrams(sentence.split(), n)
print(f"\n***********   BIGRAMS   ************************")
for item in bigrams:
    print(item)

n = 3
sentence = "Machine learning allows computers to learn from data and make predictions or decisions without being explicitly programmed."
trigrams = ngrams(sentence.split(), n)
print(f"\n***********   TRIGRAMS   ************************")
for item in trigrams:
    print(item)
