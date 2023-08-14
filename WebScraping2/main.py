from bs4 import BeautifulSoup
# using requests library to see a Website's HTML
import requests
import csv

# enter unfamiliar skill and filtering it out
print("Enter your unfamiliar skill:")
unfamiliar_skill = input('>')
print(f"Filtering out {unfamiliar_skill}....")

def function():
    # using function get to get html code from website, if successul, it will print Response 200
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
    soup = BeautifulSoup(html_text, "html.parser")
    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

    # write into csv file
    file = open("job.csv", "w", newline="")
    # inorder to input new row, data must be stored in tuple, first row needs to be the label
    col_names = ("Company Name", "Skills Required", "More Info")
    # create a writer to write into csv file, insert the column names
    writer = csv.writer(file)
    writer.writerow(col_names)

    # find all job that was posted just a few days ago
    # strip function remove empty spaces from begin and end of string
    for job in jobs:
        job_published_date = job.find('span', class_="sim-posted").span.text
        # condition to check whether the job is just a few days ago
        if 'few' in job_published_date:
            skills = job.find('span', class_="srp-skills").text.replace(' ', '')
            # condition to check whether unfamiliar skill in skills required (lower case both to avoid wrong comparison)
            if unfamiliar_skill.lower() not in skills.lower():
                company_name = job.find('h3', class_="joblist-comp-name").text
                link = job.header.h2.a['href']
                tup = (company_name.strip(), skills.strip(), link)
                print(tup)
                writer.writerow(tup)
    file.close()


if __name__ == "__main__":
    function()
