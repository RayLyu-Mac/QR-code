#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import numpy as np
import pyzbar.pyzbar as pb
import requests
import qrcode
from PIL import Image
import matplotlib.pyplot as plt


# In[4]:


#point: create an QR code, it's characteristic, 
dt=plt.imread('me.jpg')
qr = qrcode.QRCode(version=1,box_size=15, border=10)
data=str(dt)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='yellow',back_color='red')
plt.imshow(img)


# In[11]:


#create an QR code that has an logo in the center: problem, the time needed increase 
logo =Image.open('me.jpg')
bw=75
wp=(bw/float(logo.size[0]))
hsize=int((float(logo.size[1])*float(wp)))
logo=logo.resize((bw,hsize),Image.ANTIALIAS)
qr=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data('Hi there, Nice to meet you! My name is Ray, Second year biomed and material Engineering student.')
qr.make(fit=True)
img = qr.make_image(fill='#0b4e39',back_color='white').convert("RGB")
pos=((img.size[0]-logo.size[0])//2,(img.size[1]-logo.size[1])//2)
img.paste(logo,pos)
plt.imshow(img)


# In[2]:


cap = cv2.VideoCapture(0)
#scan the QR code and get the information of the website 

while(1):
    _, frame = cap.read()
    decode=pb.decode(frame)
    cv2.imshow('rect',frame)
    if len(decode)>0:
        for obj in decode:
            a=str(obj.data)
            b=a.index('https')
            c=len(a)-1
            d=a[b:c]
            print(d)
            res=requests.get(d)
            print(res.text)
        break
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
    


# In[3]:


a='bahttps://u.wechat.com/EBqQRfNx_RSe0oOa7UrfjZ8'
a.index('https')


# In[ ]:




