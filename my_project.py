#importing the modules 
from urllib.request import urlopen as uReq
#importing urls from the web, through urllib.request pakage and opening through the urlopen and calling as the uReq

from bs4 import BeautifulSoup as soup
#import Beautifulsoup function from the bs4(beautifulsoup4) as soup

my_urls = "https://www.hotcoursesabroad.com/india/training-degrees/uk/masters/artificial-intelligence-ai-courses/loc/210/slevel/57-3-3/cgory/cb.31-4/sin/ct/programs.html"
#importing url from the web

#grabbing page from the web
uClient = uReq(my_urls) #urlopen fuction will grab page
page_html = uClient.read() #it will read every line
uClient.close() #we are closing the uClient or file

#html parsing, try print every rhing from here only because html is very scrap
page_soup = soup(page_html, "html.parser")

filename = "TopAIColleges.csv"
f = open(filename, "w")

hearder = "headings, Ranks, views, favorites \n"

f.write(hearder)

starts = page_soup.findAll("div",{"class":"pr_hd"})
for start in starts:
    sta = start
    s = (sta.findAll("div",{"class":"sr_nam"}))
    s1 = s[0]
    headings = s1.h2.a.text
    ranks = sta.p.text
    pw = (sta.findAll("div",{"class":"vtxt bd"}))
    p1 = pw[0]
    Ai = p1.text
    vw = sta.findAll("span", {"class":"vw grey"})
    v = vw[0]
    views = v.span.text
    rw = sta.findAll("div", {"class":"sfv"})
    v = rw[0]
    favorites = v.span.text
    print("headings:" + headings + "," + "ranks:" + ranks + "," + "artif:"  + "," + "views:" + views +","+ "favorites:"+ favorites + "\n")
    f.write(headings + "," + ranks.replace(",", "|") + "," + views.replace(",", "|") + "," + favorites + "\n")
print(len(starts))
f.close()
