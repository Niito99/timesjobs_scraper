from bs4 import BeautifulSoup
import requests


def scrape():
    search_skill = input("What is the query for your search \n You may input: python or front end or backend or "
                         "database or linux \n")
    search_loc = input("What location are basing your search on? \n If you want it to be worldwide input a space \n")
    search_exp = input("What is the minimum work experience that favors you \n If you want an entry level job, "
                       "input 0 \n")
    search_unfamiliar_skill = input("What skill are you unfamiliar with\n")
    print("filtering out " + search_unfamiliar_skill + " ...")

    skill = f"{search_skill}"
    loc = f"{search_loc}"
    work_exp = f"{search_exp}"
    html_file = requests.get(f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from"
                             f"=submit&txtKeywords={skill}&txtLocation={loc}&cboWorkExp1={work_exp}").text
    soup = BeautifulSoup(html_file, "lxml")
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

    for job in jobs:
        job_name = job.h2.text.strip()
        company_name = job.h3.text.strip()
        more_details = job.h2.a["href"]
        time_stamp = job.find("span", class_="sim-posted").text.strip()
        skills = job.find("span", class_ = "srp-skills").text.strip()
        if "few" in time_stamp:
            continue
        if search_unfamiliar_skill in skills:
            continue

        print(f"Company Name: {company_name} \nJob Name: {job_name}\nRequired Skills: {skills}\nMore Details: {more_details}")
        print("(" + time_stamp + ")")
        print("\n")


scrape()
