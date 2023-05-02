# this project using:  (pip) beautifulsoup4, csv, requests, and webdriver-manager, selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def getProductInfoFromCellphoneSWebsites(website, file_name, index):
    browser = webdriver.Chrome(ChromeDriverManager().install())
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
    product_price = soup.find({"p"}, class_="product__price--through").text.strip()
    product_price = product_price.replace(".", "")
    product_price = product_price.replace("₫", "")

    with open(file_name, "a", encoding="utf-8") as f:
        f.write("INSERT INTO product VALUES")
        f.write("(" + str(index) + ",")
        f.write("'" + product_name + "'" + ",\n")
        f.write("'" + product_picture_url + "'" + ",\n")
        f.write("'")
        description_lines = product_description.text.split("\n")
        f.write("|\n".join(description_lines))
        f.write("'")
        f.write(",\n")
        f.write("'")
        for mini_spec in mini_specs:
            category = mini_spec.find({"p"}).text.strip()
            specific_spec = mini_spec.find({"div"}).text.strip()
            f.write(category + "    " + specific_spec + "|\n")
        browser.close()  # close browser
        f.write("'")
        f.write(",\n")
        f.write(str(product_price) + ",")


def writeAvailableStateAndCategory(file_name, available, category):
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(str(available) + "," + str(category) + ")" + "\n\n")
        f.close()


if __name__ == "__main__":
    available = 1
    category = 8
    index = 65
    website_list = [
        'https://cellphones.com.vn/mac-mini-m2-2023.html',
        'https://cellphones.com.vn/macbook-pro-16-inch-m2-max-2023.html',
        'https://cellphones.com.vn/macbook-air-2020-m1.html',
        'https://cellphones.com.vn/macbook-pro-14-inch-m2-pro-32gb-2023.html',
        'https://cellphones.com.vn/macbook-pro-m2-2022-512gb.html',
        'https://cellphones.com.vn/macbook-air-m2-2022-24gb.html',
        'https://cellphones.com.vn/macbook-pro-m2-2022.html'
    ]
    print(len(website_list))
    for website in website_list:
        getProductInfoFromCellphoneSWebsites(website, 'macs.txt', index)
        writeAvailableStateAndCategory('macs.txt', available, category)
        index += 1
