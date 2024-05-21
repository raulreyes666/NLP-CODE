import nltk
from nltk.corpus import movie_reviews
corpus_words = movie_reviews.words()
print(("Cantidad de Palabras:"))
print((len(corpus_words)))
print(corpus_words)

print("Palabras mas frecuentes sin simbolos:")
words_no_punct= []
for word in corpus_words:
    if word.isalnum():
        words_no_punct.append(word)

freq = nltk.FreqDist(words_no_punct)

print("Common words:", freq.most_common(50))
freq.plot(50, cumulative= False)