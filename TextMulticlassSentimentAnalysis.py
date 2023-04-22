#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pickle
with open('_multiclass_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('_multiclass_model_tfidf.pkl','rb') as f:
    tfidf=pickle.load(f)
    


# In[55]:


x=["angry"]
xt=tfidf.transform(x)
t=model.predict(xt)
if(t[0][0]==1):
    print("anger")
elif


# In[73]:


def GiveSentiment(text):
    xt=tfidf.transform([text])
    t=model.predict(xt)
    res=" "
    if(t[0][0]==1):
        return "professional"
    if(t[0][1]==1):
        return "poor"
    if(t[0][2]==1):
        return "confident"
    if(t[0][3]==1):
        return "neutral"
    if(t[0][4]==1):
        return "average"


# In[74]:


GiveSentiment("sad")


# In[ ]:




