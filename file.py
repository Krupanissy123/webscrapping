import requests
import bs4
import time
from tkinter import messagebox

pixel =requests.get("https://www.flipkart.com/google-pixel-4a-just-black-128-gb/p/itm023b9677aa45d")
soup = bs4.BeautifulSoup(pixel.text,'lxml')
price=soup.find("",{"class":'_30jeq3 _16Jk6d'})
print(price)
print(type(price))