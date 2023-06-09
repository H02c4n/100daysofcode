from bs4 import BeautifulSoup
import requests
import lxml

with open("index.html") as file:
    content = file.read()

#soup = BeautifulSoup(content, "html.parser")

#print(soup.prettify())
#print(soup.h1)
#all_li = soup.find_all(name="li")
#print(all_li)

#for tag in all_li:
#   print(tag.getText())


#res = requests.get("https://www.essentialenglish.review/apps/illustrated-everyday-expressions-with-stories-1/lesson-1-the-sun-the-moon-and-the-bat/#0")
#esen = res.text
soup = BeautifulSoup(content, "html.parser")

item_lists = soup.find_all(name="div", class_="wordlist-cover")
print(item_lists[0].find(name="div", class_="en-word").getText())
splited = item_lists[0].find(name="div", class_="en-exam").getText().split(".")
for item in splited:
    print(item+"\n")
