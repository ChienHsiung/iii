
# coding: utf-8

# In[9]:


# Go to  https://chromedriver.storage.googleapis.com/index.html?path=2.30/
# Download linux_64
# Extract, 
# sudo cp chromedriver /usr/local/bin/


# In[10]:


get_ipython().system('pip install splinter')


# In[11]:


import splinter


# In[12]:


browser = splinter.Browser(driver_name='chrome')


# In[13]:


browser.visit('https://ianchenhq.com')


# In[14]:


elem = browser.find_by_xpath("/html/body/div/div/div[2]/section/article[1]/h2/a")


# In[15]:


elem.click()


# In[16]:


browser.back()


# In[21]:


browser.cookies.all()


# In[22]:


browser.visit("https://thingiverse.com")


# In[28]:


browser.click_link_by_partial_text("Sign in / Join")


# In[34]:


browser.windows[1].is_current = True


# In[37]:


browser.fill('username', 'ytn63241@tqosi.com')


# In[38]:


browser.fill('password', 'pythonetl')


# In[39]:


browser.click_link_by_id("sso_sign_in")


# In[41]:


browser.cookies.all()


# In[58]:


elem = browser.find_by_css("a.dropdown-toggle")


# In[59]:


elem.click()


# In[60]:


elem = browser.find_by_xpath('//*[@id="push-main"]/div[2]/div/ul/li[2]/ul/li[1]/a')


# In[61]:


elem.click()


# In[66]:


browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')


# In[67]:


browser.html


# In[68]:


browser.screenshot('./myscreenshot.png')


# In[ ]:




