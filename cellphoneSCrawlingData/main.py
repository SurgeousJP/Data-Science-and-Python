# this project using:  (pip) beautifulsoup4, csv, requests, and webdriver-manager, selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def getProductInfoFromCellphoneSWebsites(website, file_name, index):
    browser = webdriver.Chrome()
    browser.get(website)
    html_text = browser.page_source

    soup = BeautifulSoup(html_text, "html.parser")
    product_name = soup.find({"div"}, class_="box-product-name").find({"h1"}).text.strip()
    # in normal, use class_ box-ksp
    # with components use gallery-product-detail my-2
    product_picture_url = soup.find({"div"}, class_="box-ksp").find({"img"})['src'].strip()
    product_description = soup.find({"div"}, class_="desktop")
    spec = soup.find_all({"ul"}, class_='technical-content')  # sometime, leave {} instead of "" works
    mini_soup = BeautifulSoup(str(spec[0]), "html.parser")
    mini_specs = mini_soup.find_all({"li"},
                                    class_='technical-content-item is-flex is-align-items-center is-justify-content-space-between p-2')
    # product_price = soup.find({"p"}, class_="product__price--through").text.strip()
    product_price = soup.find({"p"}, class_="tpt---sale-price").text.strip()
    product_price = product_price.replace(".", "")
    product_price = product_price.replace("₫", "")

    with open(file_name, "a", encoding="utf-8") as f:
        # f.write("INSERT INTO product VALUES")
        # f.write("(" + str(index) + ",")
        # f.write("'" + product_name + "'" + ",\n")
        # f.write("'" + product_picture_url + "'" + ",\n")
        # f.write("'")
        # description_lines = product_description.text.split("\n")
        # f.write("|\n".join(description_lines))
        # f.write("'")
        # f.write(",\n")
        # f.write("'")
        # for mini_spec in mini_specs:
        #     category = mini_spec.find({"p"}).text.strip()
        #     specific_spec = mini_spec.find({"div"}).text.strip()
        #     f.write(category + "    " + specific_spec + "|\n")
        # browser.close()  # close browser
        # f.write("'")
        # f.write(",\n")
        # f.write(str(product_price) + ",")
        f.write(str(index) + "," + product_name + "," + product_picture_url + ",")
        description_lines = product_description.text.split("\n")
        f.write("|\n".join(description_lines))


def writeAvailableStateAndCategory(file_name, available, category):
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(str(available) + "," + str(category) + ")" + "\n\n")
        f.close()


if __name__ == "__main__":
    available = 1
    category = 1
    index = 73
    website_list = [
        'https://cellphones.com.vn/laptop-asus-vivobook-15-oled-a1505va-l1114w.html',
        'https://cellphones.com.vn/laptop-lenovo-ideapad-gaming-3-15iah7-82s9006yvn.html',
        'https://cellphones.com.vn/laptop-asus-gaming-rog-zephyrus-g14-ga401qc-k2199w.html',
        'https://cellphones.com.vn/laptop-asus-gaming-rog-zephyrus-g16-gu603vu-n3898w.html',
        'https://cellphones.com.vn/laptop-lenovo-gaming-legion-5-15ach6h-82ju00dgvn.html'
    ]
    print(len(website_list))
    for website in website_list:
        getProductInfoFromCellphoneSWebsites(website, 'new_laptop.txt', index)
        writeAvailableStateAndCategory('new_laptop.txt', available, category)
        index += 1