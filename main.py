# if you want to scrape a website :
# 1. using api
# 2. html web scraping using some tool like bs4

# step 0 :
# install these:
# pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

# step 1 : get the html
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)


# step 2 : parse the html
soup = BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify)


# step 3 : html tree traversal
# commonly used type of objects
title = soup.title

# print(type(title))#1 tag
# print(type(title.string))#2 navigablestring
# print(type(soup))  #3 beautifulSoup


# get all the paragraphs from the page
    # paras = soup.find_all('p')
    # print(paras)

# # get all anchor tags from the page
# anchors = soup.find_all('a')
# print(anchors)

# get first element in the html page
# print(soup.find('p'))

# # get classes of any element in html page
# print(soup.find('p')['class'])

# find all  the elements with class lead
# print(soup.find_all('p',class_='lead'))

# get the text from the tags/soup
# print(soup.find('p').get_text())


# get all the links in the page
# all_links = set()
# for link in anchors:
#     if(link.get('href')!="#"):
#         linkText = "https://codewithharry.com" + link.get('href')
#         all_links.add(link)
        # print(linkText)


#4 comment
# markup = '<p><!--this is a comment--></p>'
# soup2 = BeautifulSoup(markup)
# print(type(soup2.p.string))

navbarSupportedContent = soup.find(id = 'navbarSupportedContent')
# .contents  =   a tags children are available as a list
# .children = a tags children are available as a
# for elem in navbarSupportedContent.contents:
#     print(elem)
# for item in navbarSupportedContent.strings:
#     print(item)
# for item in navbarSupportedContent.stripped_strings:
#     print(item)
# for item in navbarSupportedContent.parents:
    # print(item)
    # print(item.name)


# print(navbarSupportedContent.next_sibling.next_sibling)
# print(navbarSupportedContent.previous_sibling.previous_sibling)

elem = soup.select('.modal-footer')
print(elem)

# print(navbarSupportedContent.previous_sibling.previous_sibling)

# print(title)
