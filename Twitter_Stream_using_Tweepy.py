
# coding: utf-8

# In[11]:

import tweepy  #another popular twitter API wrapper
import json
import config   #twitter OAuth configuration
import datetime
import pylib
import utils
import python_utils
from datetime import datetime
from dateutil import tz
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import urllib2
import csv
import time


# In[14]:


# the authentication process for tweepy
auth = tweepy.OAuthHandler("Oaiu1JguieNrSkoCyNh6jGvIg","ceaCiux8njHGe5x07WikXARUNCh9PVGzeL3EpMGBgohnVSVJbY")
auth.set_access_token("2295578748-WwyxCL32c0TOdHan9cjlMWkcEIjI2IxmSpsYYyh","Rv1kE1hQqVqmBmLSemVCLlwhxWKs1DMzNw6EDK4WrdlsI")
api = tweepy.API(auth)


# In[107]:

tweets = api.user_timeline(id="cnnbrk",count=100)


# In[108]:

df = pd.DataFrame()

df['Tweet'] = [t.text for t in tweets]
df['Retweet_Count'] = [t.retweet_count for t in tweets]
df['Source'] = [t.source for t in tweets]
df['Favorite_Count'] = [t.favorite_count for t in tweets]

# from_zone = tz.tzutc()
# to_zone = tz.tzlocal()
df['Created_At'] = [t.created_at.replace(tzinfo=tz.tzutc()).astimezone(tz.tzlocal()) for t in tweets]


# In[114]:

count = 0

for t in tweets:
    urls = [url['url'] for url in t.entities['urls']]
    hashtags = [hashtag['text'] for hashtag in t.entities['hashtags']]
    
    df['Url_Count'][count] = len(urls)
    df['Hashtag_Count'][count] = len(hashtags)  
        
    df['Urls'][count] = ','.join(urls)
    df['Hashtags'][count] = ','.join(hashtags)
    
    count+=1


# In[115]:

df.head()


# In[111]:

from wordcloud import WordCloud,STOPWORDS
text = (' '.join(list(df['Tweet'])))


# In[92]:

text


# In[112]:


cleaned_word = " ".join([word for word in text.split()
                            if 'http' not in word
                                and not word.startswith('@')
                                and word != 'RT'
                            ])

wordcloud = WordCloud(stopwords=STOPWORDS,
                      background_color='black',
                      width=3000,
                      height=2500
                     ).generate(cleaned_word)

plt.figure(1,figsize=(12, 12))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()


# In[91]:

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

d = path.dirname("C:\\Users\\saura\\Desktop\\alice.jpg")

alice_mask = np.array(Image.open(path.join(d, "alice.jpg")))

wordcloud = WordCloud(background_color="white",max_words=2000, mask=alice_mask,
               stopwords=STOPWORDS)

wordcloud.generate(cleaned_word)

# store to file
wordcloud.to_file(path.join(d, "alice.png"))

# show
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.figure()
#plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()


# In[ ]:




# In[ ]:



