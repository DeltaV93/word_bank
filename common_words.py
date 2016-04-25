import requests
import re
from bs4 import BeautifulSoup

#Website you want to scrap info from  
res = requests.get("https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-usa.txt")
# Getting just the content using bs4
soup = BeautifulSoup(res.content, "lxml")

# Creating the CSV file
commonFile = open('common_words.csv', 'wb')

# Grabbing the lines you want
for node in soup.findAll("tr"):
	# Getting just the text and removing the html
    words = ''.join(node.findAll(text=True))
    # Removing the extra lines
    ID = re.sub(r'[\t\r\n]', '', words)
    # Needed to add a break in the line to make the rows
    update = ''.join(ID)+'\n'
    # Now we add this to the file 
    commonFile.write(update)
commonFile.close()