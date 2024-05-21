import nltk
from nltk import FreqDist
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Supongamos que 'texto' es tu libro de primero de primaria
texto = "Paco el Chato vivía en un rancho. Al cumplir seis años Paco debía entrar a la escuela. Para eso su papá lo llevó a la ciudad, donde vivía su abuelita. Al llegar a la escuela, el primer día de clases, la abuelita le dijo: — A la salida me esperas en la puerta, Paco esperó un rato, después empezó a caminar y se perdió, Paco se asustó y empezó a llorar. Un policía le preguntó su nombre, su apellido y su dirección."  # Tu texto aquí

# Tokenización con NLTK
palabras = word_tokenize(texto)

# Análisis de frecuencia de palabras con NLTK
frecuencia = FreqDist(palabras)
print("Palabras más comunes:", frecuencia.most_common(10))

# Análisis de frecuencia de palabras con CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform([" ".join(palabras)])  # Necesitas pasar una lista de documentos
frecuencia_vectorizada = dict(zip(vectorizer.get_feature_names_out(), X.toarray()[0]))
print("Palabras más comunes:", sorted(frecuencia_vectorizada.items(), key=lambda x: x[1], reverse=True)[:10])

# Visualización de WordCloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(frecuencia)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show(block=True)