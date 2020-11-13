#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pytesseract
import re
import xlsxwriter


from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r#"executable path"

img = #Image.open(Your Image)

text = pytesseract.image_to_string(img)

lines = text.splitlines( )

for line in lines:
    if line == ' ':
        lines.remove(line)
lines






