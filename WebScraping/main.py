"""Import necessary library"""
from bs4 import BeautifulSoup
"""Open file"""
with open('HTML h1 to h6 tag.html', 'r') as html_file:
    # Create an instance of text containing html code read from the file
    content = html_file.read()

    # Create an instance of beautifulsoup -> arguments: content, parser
    soup = BeautifulSoup(content, "html.parser")

    """turn a Beautiful Soup parse tree into a nicely formatted Unicode string
    print(soup.prettify())
    
    # function find -> find the first appearance of str
    # note that for ('div', class_=?)
    tags = soup.find('h1')

    # function find_all -> all occurences
    courses_html_tags = soup.find_all('h1')

    # iterate through the list and print text only
    for course in courses_html_tags:
        print(course.text)
     """

    # Basic scraping
    headers = soup.find_all('div', class_="w3-example")
    for header in headers:
        try:
            print(header.h3.text)
            print(header.p.text)
        except AttributeError:
            pass
