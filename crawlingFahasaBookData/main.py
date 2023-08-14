# this project using:  (pip) beautifulsoup4, selenium (webdriver)
import json
from decimal import Decimal

from get_attributes_function import *
from json_utilities import *


def get_book_website_link_list(website):
    html_text = get_html_Text_From_Website(website)
    soup = get_soup_from_html_text(html_text)

    product_grids = get_list_content_in_html_tag(
        soup,
        "ul",
        "products-grid fhs-top"
    )
    product_link_soup = BeautifulSoup(str(product_grids[0]), "html.parser")
    linkHrefs = get_href_links(product_link_soup)

    links = set()
    # Adding fahasa.com to the prefix to make it a link, since I'm crawling from fahasa.com ^-^
    for linkHref in linkHrefs:
        links.add("https://www.fahasa.com" + linkHref['href'])

    return links


def get_book_info_from_website(website):
    html_text = get_html_Text_From_Website(website)
    soup = get_soup_from_html_text(html_text)

    product_essential = get_list_content_in_html_tag(
        soup,
        "div",
        "product-essential"
    )

    product_essential_soup = get_soup_from_html_text(str(product_essential))

    try:
        product_image_link = get_product_image_link(product_essential_soup)
    except Exception as e:
        product_image_link = ""

    try:
        product_name = get_product_name(product_essential_soup)
    except Exception as e:
        product_name = ""

    try:
        product_supplier = get_product_supplier(product_essential_soup)
    except Exception as e:
        product_supplier = ""

    try:
        product_author = get_product_author(product_essential_soup)
    except Exception as e:
        product_author = ""

    try:
        product_publisher = get_product_publisher(product_essential_soup)
    except Exception as e:
        product_publisher = ""

    try:
        product_layout = get_product_layout(product_essential_soup)
    except Exception as e:
        product_layout = ""

    try:
        product_series = get_product_series(product_essential_soup)
    except Exception as e:
        product_series = ""

    try:
        product_price = get_product_price(product_essential_soup).replace("đ", "").replace(".", "")
    except Exception as e:
        product_price = 0.0

    attributes = [
        ("name", product_name),
        ("book_img_url", product_image_link),
        ("supplier", product_supplier),
        ("author", product_author),
        ("publisher", product_publisher),
        ("book_layout", product_layout),
        ("series", product_series),
        ("price", float(product_price))
    ]

    return attributes

    # print(str(product_image_link) + "\n" + str(product_name) + "\n")
    # print("Supplier: " + product_supplier)
    # print("Author: " + product_author)
    # print("Publisher: " + product_publisher)
    # print("Book Layout: " + product_layout)
    # print("Series: " + product_series)
    # print("Product price: " + product_price)


if __name__ == "__main__":
    links = get_book_website_link_list("https://www.fahasa.com/searchengine?q=manga&size=n_48_n&filters%5B0%5D%5Bfield%5D=stock_status&filters%5B0%5D%5Bvalues%5D%5B0%5D=n_1_n&filters%5B0%5D%5Btype%5D=all")
    data = []
    num_of_data_expected = 5
    count = 0
    for link in links:
        if count >= num_of_data_expected:
            break
        dict_data = get_dict_data_from_attributes(get_book_info_from_website(link))
        if len(dict_data) == 0:
            continue
        data.append(dict_data)
        count += 1
        print("\n========================================================================\n")

    append_many_to_json_collection(
        data,
        "data_for_testing.json",
        "books"
    )
