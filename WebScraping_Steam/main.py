from bs4 import BeautifulSoup
import requests
import csv
import re


def function():
    html_text = requests.get("https://store.steampowered.com/search/?filter=topsellers").text
    soup = BeautifulSoup(html_text, "html.parser")
    games = soup.find_all({"div"}, class_="responsive_search_name_combined")

    file = open("steam_topseller.csv", 'w', newline='')
    cols_name = ("Name", "Platforms", "Release date", "Review", "Discount", "Original price")
    writer = csv.writer(file)
    writer.writerow(cols_name)

    for game in games:
        name = game.find({"span"}, class_="title").text  # checked !

        platforms = game.find_all({"span"}, class_=["platform_img win", "platform_img mac", "platform_img linux"])
        lst_platform = []
        for platform in platforms:
            if "win" in platform["class"]:
                lst_platform.append("Windows")
            if "mac" in platform["class"]:
                lst_platform.append("Mac")
            if "linux" in platform["class"]:
                lst_platform.append("Linux")
        platform = ", ".join(lst_platform)

        release_date = game.find({"div"}, class_="col search_released responsive_secondrow").text

        find_review_pos = game.find({"span"}, class_="search_review_summary positive")
        find_review_mixed = game.find({"span"}, class_="search_review_summary mixed")
        if find_review_pos:
            review = "Positive"
        elif find_review_mixed:
            review = "Mixed"
        else:
            review = "None"

        find_discount = game.find({"div"}, class_="col search_discount responsive_secondrow").find({"span"})
        if find_discount is None:
            discount = "No discount"
            original_price = game.find({"div"}, class_="col search_price responsive_secondrow").text.strip()
        else:
            discount = find_discount.text
            original_price = game.find({"strike"}).text

        tup = (name, platform, release_date, review, discount, original_price)
        writer.writerow(tup)
        # comment code block for suitable use
        # print line code for easy-test
        # print(name)
        # print(platform)
        # print("Windows", end=' ')
        # print("Mac", end=' ')
        # print("Linux", end=' ')
        # print()
        # print(release_date)
        # print(review)
        # print(discount)
        # print(original_price)
        # print()
    file.close()


if __name__ == "__main__":
    function()





