from bs4 import BeautifulSoup
from selenium import webdriver


def get_href_links(product_link_soup):
    return product_link_soup.find_all("a", href=True)


def get_list_content_in_html_tag(soup, htmlTag, classTag):
    if classTag is None:
        soup.find_all({htmlTag})
    return soup.find_all({htmlTag}, class_=classTag)


def get_content_in_html_tag(soup, htmlTag, classTag):
    if classTag is None:
        soup.find_all({htmlTag})
    return soup.find({htmlTag}, class_=classTag)


def get_soup_from_html_text(html_text):
    return BeautifulSoup(html_text, "html.parser")


def get_html_Text_From_Website(website):
    browser = webdriver.Chrome()
    browser.get(website)

    html_text = browser.page_source
    browser.close()

    return html_text
