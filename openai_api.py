#!/usr/bin/env python
# coding: utf-8

# In[14]:


# import openai
# openai.api_key = "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"

# def generate_text(prompt):
#     response = openai.Completion.create(
#         engine="davinci",
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.7,
#     )

#     text = response.choices[0].text.strip()
#     return text



# text = generate_text('Once there was a boy')
# print(text)


# In[104]:


from gpt_index import SimpleDirectoryReader, GPTListIndex, GPTSimpleVectorIndex, LLMPredictor, PromptHelper, Document
from langchain import OpenAI
import sys
import os
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer


# In[99]:


# api key
os.environ["OPENAI_API_KEY"] = "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"


# In[61]:


# # knowledge base on which our system can run
# # fun to create a vector index
# # param1 => path of file
# def createVectorIndex(path):
#     max_input = 4096
#     tokens = 256
#     chunk_size = 600
#     max_chunk_overlap = 20
    
    
#     # defining our prompt
#     prompt_helper = PromptHelper(max_input, tokens, max_chunk_overlap, chunk_size_limit = chunk_size)
    
#     # define LLM
#     llmPredictor = LLMPredictor(llm =OpenAI(temperature =0, name = "text-davinci-003", max_tokens = tokens))
    
#     # load data, read your files
#     reader = SimpleDirectoryReader(path)
#     documents = [Document(doc.text) for doc in reader.load_data()]
    
#     #documents = [Document(name=name, content=content) for name, content in docs.load_data()]
    
    
#     #create vector index
# #     vectorIndex = GPTSimpleVectorIndex.from_documents(documents)
# #     vectorIndex.build_vectors(documents,llm_predictor = llmPredictor, prompt_helper = prompt_helper)

#     vectorIndex = GPTSimpleVectorIndex()

#     vectorIndex.build(documents)
    
#     # param => file name in which data will be stored
#     vectorIndex.save_to_disk('vectorIndex.json')
    
#     # return vector index
#     return vectorIndex


# In[126]:


# knowledge base on which our system can run
# fun to create a vector index
# param1 => path of file
def createVectorIndex(path):
    max_input = 4096
    tokens = 256
    chunk_size = 600
    max_chunk_overlap = 20
    

    # defining our prompt
    prompt_helper = PromptHelper(max_input, tokens, max_chunk_overlap, chunk_size_limit = chunk_size)
    
    # define LLM
    llmpredictor = LLMPredictor(llm =OpenAI(temperature =0, name = "text-davinci-003", max_tokens = tokens))
    
    # load data, read your files
    docs = SimpleDirectoryReader(path).load_data()
    
    
    #create vector index
    vectorIndex = GPTSimpleVectorIndex.from_documents(docs)
    vectorIndex.build(llpredictor,prompt_helper)
   

    # param => file name in which data will be stored
    vectorIndex.save_to_disk('vectorIndex.json')
    
    # return vector index
    return vectorIndex


# In[127]:


vectorIndex = createVectorIndex(r'C:\Users\HP\Desktop\knowledge')


# In[ ]:


def answerMe(vectorIndex):
    VIndex = GPTSimpleVectorIndex.load_from_disk(vectorIndex)
    while True:
        prompt = input('Please Ask: ')
        response = vIndex.query(prompt, response_mode = "compact")
        print(f'Response: {response} \n')
        
        


# In[ ]:


answerMe('vectorIndexwlwl.json')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




