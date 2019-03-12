
# coding: utf-8

# In[1]:

from pdf2image import convert_from_path
pages = convert_from_path('pdf1.pdf', 500)


# In[2]:

for page in pages:
    page.save('out.jpg', 'JPEG')


# In[3]:

from PIL import Image
import pytesseract
#import tesseract


# In[4]:

text = pytesseract.image_to_string(Image.open('out.jpg'))


# In[5]:

text


# In[ ]:



