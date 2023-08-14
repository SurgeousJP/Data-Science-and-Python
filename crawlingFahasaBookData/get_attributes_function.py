from support_fuction import *


def get_product_price(product_essential_soup):
    product_price = product_essential_soup.find_all(
        "span", class_="price")[0].getText().strip()
    return product_price


def get_product_series(product_essential_soup):
    product_series = get_list_content_in_html_tag(
        get_soup_from_html_text(
            str(get_href_links(
                get_soup_from_html_text(str(
                    get_content_in_html_tag(
                        product_essential_soup,
                        "div",
                        "product-view-sa-series"
                    )
                ))
            )[0]
                )),
        "span",
        None
    )[0].text.strip()
    return product_series


def get_product_layout(product_essential_soup):
    product_layout = get_list_content_in_html_tag(
        get_soup_from_html_text(
            str(
                get_list_content_in_html_tag(
                    product_essential_soup,
                    "div",
                    "product-view-sa-author"
                )[1]
            )
        ),
        "span",
        None
    )[1].text.strip()
    return product_layout


def get_product_publisher(product_essential_soup):
    product_publisher = get_list_content_in_html_tag(
        get_soup_from_html_text(
            str(
                get_list_content_in_html_tag(
                    product_essential_soup,
                    "div",
                    "product-view-sa-supplier"
                )[1]
            )
        ),
        "span",
        None
    )[1].text.strip()
    return product_publisher


def get_product_author(product_essential_soup):
    product_author = get_list_content_in_html_tag(
        get_soup_from_html_text(
            str(
                get_list_content_in_html_tag(
                    product_essential_soup,
                    "div",
                    "product-view-sa-author"
                )[0]
            )
        ),
        "span",
        None
    )[1].text.strip()
    return product_author


def get_product_supplier(product_essential_soup):
    product_supplier = get_href_links(
        get_soup_from_html_text(
            str(
                get_list_content_in_html_tag(
                    product_essential_soup,
                    "div",
                    "product-view-sa-supplier"
                )[0]
            )
        )
    )[0].text.strip()
    return product_supplier


def get_product_name(product_essential_soup):
    product_name = get_content_in_html_tag(
        product_essential_soup,
        "div",
        "product-essential-detail"
    ).h1.text.strip()
    return product_name


def get_product_image_link(product_essential_soup):
    product_image_link = get_content_in_html_tag(
        product_essential_soup,
        "img",
        "fhs-p-img lazyloaded"
    )['src']
    return product_image_link
