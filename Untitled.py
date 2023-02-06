#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install pytesseract')


# In[3]:


import pytesseract


# In[4]:


get_ipython().system('pip install opencv-python')


# In[5]:


import cv2 #using pip install opencv-python


# In[6]:


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# In[7]:


get_ipython().system('pip install matplotlib')


# In[8]:


import matplotlib.pyplot as plt


# In[9]:


img = cv2.imread(r'C:\Users\omkar\Downloads\Data\Data\Task1\1.jpg')


# In[10]:


plt.imshow(img)


# In[11]:


print(pytesseract.image_to_string(img))


# In[12]:


img_to_box = pytesseract.image_to_boxes(img)


# In[13]:


print(img_to_box)


# In[14]:


img.shape


# In[15]:


imgHeight, imgWidth,_=img.shape


# In[16]:


for boxes in img_to_box.splitlines():
    boxes = boxes.split(' ')
    x,y,w,h = int(boxes[1]),int(boxes[2]),int(boxes[3]),int(boxes[4])
    cv2.rectangle(img, (x,imgHeight-y), (w, imgHeight-h), (0,0,255),3)


# In[17]:


plt.imshow(img)


# In[18]:


plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))


# In[ ]:




