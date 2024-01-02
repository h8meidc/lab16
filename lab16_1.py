import nltk
from nltk.corpus import gutenberg
import matplotlib.pyplot as plt
import string
from collections import Counter
import re
from nltk.corpus import stopwords
File = nltk.corpus.gutenberg.raw('shakespeare-macbeth.txt')
    

def count_words(File):

    sentences = nltk.sent_tokenize(File) #токенізація по реченням

    k_words = 0

    for sentence in sentences:

        words = nltk.word_tokenize(sentence)

        #words - список зі словами

        k_words += len(words)

    return k_words

def most_used_words(File):
    words = File.split()  # список зі словами
   
    word_count = Counter(words)  # підрахунок кількості кожного слова
    top_words = word_count.most_common(10)  # 10 найбільш вживаних слів

    x = [word[0] for word in top_words]  # слова
    y = [word[1] for word in top_words]  # кількість повторень у тексті

    plt.bar(x, y)
    plt.title("10 найбільш вживаних слів у тексті")
    plt.xlabel("Слова")
    plt.ylabel("Зустрічаються разів у тексті")
    plt.show()

def most_used_words_without_stop(File):
    stop_words = set(stopwords.words("english"))
    words = nltk.word_tokenize(File)  # список зі словами
    
    words = [word for word in words if not word.lower() in stop_words]
    words = [x for x in words if not re.fullmatch('[' + string.punctuation + ']+', x)]
    word_count = Counter(words)  # підрахунок кількості кожного слова
    top_words = word_count.most_common(10)  # 10 найбільш вживаних слів

    x = [word[0] for word in top_words]  # слова
    y = [word[1] for word in top_words]  # кількість повторень у тексті

    plt.bar(x, y)
    plt.title("10 найбільш вживаних слів у тексті після видалення пунктуації та стоп слів")
    plt.xlabel("Слова")
    plt.ylabel("Зустрічаються разів у тексті")
    plt.show()


print("Кількість слів у тексті - ", count_words(File))
most_used_words(File)
most_used_words_without_stop(File)