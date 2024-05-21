import nltk 
from nltk.corpus import stopwords

stop_words = list(set(stopwords.words('spanish')))
print(len(stop_words))
print(stop_words[0:50])

languages = stopwords.fileids()
print('\n Stopwords for this n of  languages: ', len(languages))
print(languages)