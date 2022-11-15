from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

url = "https://www.flipkart.com/adidas-stormex-hiking-trekking-shoes-men/p/itm856f14954174c?pid=SHOGEH424THTGSUV&lid=LSTSHOGEH424THTGSUVIFXVQS&marketplace=FLIPKART&sattr[]=color&st=color&otracker=search"

response = requests.get(url)

htmlcontent = response.content

soup = BeautifulSoup(htmlcontent, "html.parser")

print(soup.prettify)

product=[]
reviews=[]
ratings=[]
product = soup.find('div', attrs={'class':'B_NuCI'})
print(product.text)
for a in soup.findAll('a',href=True,attrs={'class':'B_NuCI'}):
    reviews=a.find('div',attrs={'class':'_2QKOHZ _33R3aa'})
    reviews.append(reviews.text)
    print(reviews.text)
    df=pd.DataFrame({"Product Name":product,'Reviews':reviews})
    df.head()
    df.to_csv('product.csv')