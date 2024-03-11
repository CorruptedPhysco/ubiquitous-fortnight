
from bs4 import BeautifulSoup
import requests
import time
from flask import Flask
def getlink():
  url="https://bingotingo.com/best-social-media-platforms/"
  page=requests.get(url)
  html=page.content
  soup = BeautifulSoup(html,"html.parser") 
  job_desc = soup.find(
    'a', 
    class_='su-button su-button-style-soft su-button-wide')
  l = str(job_desc)
  list = l.split()
  for i in list:
    if "href" in i:
      j = (i.lstrip('href='))
      job_desc=j.replace('"', '')
      
  
    
  
  url2=job_desc
  print(url2)
  page2=requests.get(url2)
  html2=page2.content
  soup2 = BeautifulSoup(html2,"html.parser")
  div = soup2.find(
    'div',class_="public-container noselect")
  div2=div.find('div',class_='pb-links justify-content-center pb-links-noimg row m-0 effect-standard dl-LAYOUT_LIST_SMALL_RND ml-LAYOUT_LIST_SMALL_RND group-container-u')
  a=div2.find('a',class_="d-block pb-linkbox pb-desktop-list-small-rnd pb-mobile-list-small-rnd bt-2 mb-2 col-md-12 col-12")
  hi = str(a)
  li = hi.split()
  b=''
  for i in li:
    if "href" in i:
      b = (i.lstrip('href='))
  g=b.replace('"', '')
  finallink=f'https://ln.ki{g}'
  def remove(string):
    return string.replace(" ", "") 
  if "canva" in finallink:
    print('link returned')
    return remove(finallink)
  else:
    print('link not returned')
    return 'No'




app = Flask(__name__)

@app.route('/')
def show_getlink():
    return f'<h1>{getlink()}</h1>'

