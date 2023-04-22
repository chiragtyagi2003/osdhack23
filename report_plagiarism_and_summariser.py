#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import string
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter

def preprocess_text(text):
    # Tokenize the text into sentences and words
    sentences = sent_tokenize(text)
    words = [word_tokenize(sentence) for sentence in sentences]
    
    # Remove stop words and punctuation
    stop_words = set(stopwords.words('english') + list(string.punctuation))
    words = [[word.lower() for word in sentence if word.lower() not in stop_words] for sentence in words]
    
    # Stem the words
    stemmer = SnowballStemmer('english')
    words = [[stemmer.stem(word) for word in sentence] for sentence in words]
    
    # Flatten the list of words into a single list
    words = [word for sentence in words for word in sentence]
    
    return words

def calculate_similarity(text1, text2):
    # Preprocess the texts
    words1 = preprocess_text(text1)
    words2 = preprocess_text(text2)
    
    # Count the frequency of each word in the texts
    freq1 = Counter(words1)
    freq2 = Counter(words2)
    
    # Get the list of unique words in both texts
    unique_words = list(set(words1 + words2))
    
    # Create the frequency vectors for both texts
    vector1 = [freq1[word] for word in unique_words]
    vector2 = [freq2[word] for word in unique_words]
    
    # Calculate the cosine similarity between the two vectors
    similarity = cosine_similarity([vector1], [vector2])[0][0]
    
    return similarity

text1 = "This is the first text."
text2 = "This is the second text."

similarity = calculate_similarity(text1, text2)

print("Similarity between the two texts:", similarity)


# In[ ]:


import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import SnowballStemmer

def generate_summary(text, num_sentences):
    # Tokenize the text into sentences and words
    sentences = sent_tokenize(text)
    words = [word_tokenize(sentence) for sentence in sentences]
    
    # Remove stop words and punctuation
    stop_words = set(stopwords.words('english'))
    words = [[word.lower() for word in sentence if word.lower() not in stop_words and word.isalnum()] for sentence in words]
    
    # Stem the words
    stemmer = SnowballStemmer('english')
    words = [[stemmer.stem(word) for word in sentence] for sentence in words]
    
    # Calculate the word frequencies
    all_words = [word for sentence in words for word in sentence]
    freq_dist = FreqDist(all_words)
    
    # Score the sentences based on their word frequencies
    scores = {}
    for i, sentence in enumerate(sentences):
        words_in_sentence = words[i]
        sentence_score = sum([freq_dist[word] for word in words_in_sentence])
        scores[sentence] = sentence_score
    
    # Get the top n sentences with the highest scores
    top_sentences = sorted(scores, key=scores.get, reverse=True)[:num_sentences]
    
    # Join the top sentences into a summary
    summary = ' '.join(top_sentences)
    
    return summary

text = "Natural language processing (NLP) is a field of computer science, artificial intelligence, and computational linguistics concerned with the interactions between computers and human (natural) languages. In particular, it focuses on programming computers to process and analyze large amounts of natural language data. NLP is used in a wide range of applications, including machine translation, speech recognition, sentiment analysis, and chatbots. Some of the techniques used in NLP include tokenization, part-of-speech tagging, and named entity recognition."

summary = generate_summary(text, 2)

print("Summary:\n", summary)


# In[ ]:


import PyPDF2 as pdf
string=" "
file=open(r"C:\Users\shash\Downloads\prp_pbl_21103026_b1.pdf",'rb')
reader=pdf.PdfReader(file)
for i in range(len(reader.pages)):
    page=reader.pages[i].extract_text()
    string=string+str(page)
        


# In[ ]:


def pdf_reader(location):
    string=" "
    file=open(location,'rb')
    reader=pdf.PdfReader(file)
    for i in range(len(reader.pages)):
        page=reader.pages[i].extract_text()
        string=string+str(page)
    return string

