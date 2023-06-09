from bs4 import BeautifulSoup

with open("index.html") as file:
    content = file.read()

soup = BeautifulSoup(content)

print(soup.prettify())