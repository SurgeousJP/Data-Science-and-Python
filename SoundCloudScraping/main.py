# this project using:  (pip) beautifulsoup4, csv, requests, and webdriver-manager, selenium
from bs4 import BeautifulSoup
import requests
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# get file, create soup instance and collect tracks
browser = webdriver.Chrome(ChromeDriverManager().install())  # start browser
browser.get("https://soundcloud.com/search?q=alan%20walker&query_urn=soundcloud%3Asearch-autocomplete%3Aecc45ccdd5d44a52b99c554f9872f8ef")  # get source_code
html_text = browser.page_source  # get html_text source code

soup = BeautifulSoup(html_text, "html.parser")
soundtracks = soup.find_all({"div"}, class_='sound__content')  # sometime, leave {} instead of "" works

# Create file csv and decide cols_name, writer
file = open("Tracklist.csv", "w", newline="")
cols_name = ("Name", "Time_posted", "Like", "Repost", "Link", "Plays", "Comments")
writer = csv.writer(file)
writer.writerow(cols_name)

# read data from tag and from buttons
for soundtrack in soundtracks:
    name = soundtrack.find({"a"}, class_="sc-link-primary soundTitle__title sc-link-dark sc-text-h4").text.strip()
    temp_link = soundtrack.find({"a"}, class_="sc-link-primary soundTitle__title sc-link-dark sc-text-h4")["href"]
    link = "soundcloud.com" + temp_link
    time_posted = soundtrack.find({"span"}, attrs={"aria-hidden": "true"}).text
    like = soundtrack.find({"button"}, attrs={"aria-label": "Like"}).text
    repost = soundtrack.find({"button"}, attrs={"aria-label": "Repost"}).text
    plays = soundtrack.find({"li"}, class_="sc-ministats-item")["title"]
    comments = (soundtrack.find({"li"}, class_="sc-ministats-item")).find_next_sibling({"li"})["title"]
    """
    print(name)
    print(link)
    print(time_posted)
    print(like)
    print(repost)
    print(plays)
    print(comments)
    print(tup)
    """
    tup = (name, time_posted, like, repost, link, plays, comments)
    writer.writerow(tup)
browser.close()  # close browser
file.close()








