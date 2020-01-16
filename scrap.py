""" my mini project to scrap the content inna specific website """
from bs4 import BeautifulSoup as b
import requests as r
import webbrowser as web

def houseofbots():
 
  p=r.get("https://www.houseofbots.com").text
  soup=b(p,features="html.parser")
  k=1
  head=[]
  link=[]
  print("The contents  in house of bots are \n")
  for i in soup.find_all("li"):
      if( i.find("h4")!=None):
        print(str(k)+"."+i.find("h4").text)
        print()
        head.append(i.find("h4").text)
        link.append(i.find("a").get("href"))
        k+=1
  browsing=int(input("Enter a number to open the content in webbrowser "))
  print(link[browsing-1])
  web.open_new_tab(link[browsing-1])

  
def fossbytes():
  p=r.get("https://fossbytes.com").text
  soup=b(p,features="html.parser")
  k=1
  head=[]
  link=[]
  print("The contents  in fossbytes are \n")
  for i in soup.find_all("h3"):
      head.append(i.text)
      print(str(k)+"."+i.text+"\n") 
      k+=1
      print()
      link.append(i.find("a").get("href"))
      
  browsing=int(input("Enter a number to open the content in webbrowser "))
  print(link[browsing-1])
  web.open_new_tab(link[browsing-1])



def hackernews():
  p=r.get("https://thehackernews.com").text
  soup=b(p,features="html.parser")
  k=1
  head=[]
  link=[]
  print("The contents  in fossbytes are \n")
  for i in soup.find_all("h2"):
      head.append(i.text)
      print(str(k)+"."+i.text+"\n") 
      k+=1
      print()
  for i in soup.find_all("a",class_='story-link'):
    link.append(i.get("href"))
  browsing=int(input("Enter a number to open the content in nwebbrowser "))
  print(link[browsing-1])
  web.open_new_tab(link[browsing-1])


print("welocome to my web site scrapping \n".upper())
print("1.house of bots \n".upper())
print("2.fossbytes\n".upper())
print("3.hackernews\n".upper())
c=int(input("choose the website to scrap the content"))
if(c==1):
    houseofbots()
elif(c==2):
    fossbytes()
elif(c==3):
  hackernews()

