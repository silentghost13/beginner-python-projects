from bs4 import BeautifulSoup
import requests
import time
#https://www.youtube.com/watch?v=XVv6mJpFOb0
print('Input skills you are not familiar with to be filtered (For multiple skill : a,b,c)')
unfamiliar_skills = input('Input here :')
unfamiliar_skills = unfamiliar_skills.split(',')
print(f'Filtering out {unfamiliar_skills}')

def find_job():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_ = 'sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
            skills_split = skills.split(',')
            more_info = job.header.h2.a['href']
            check = any(item in unfamiliar_skills for item in skills_split)
            if check is False:
                with open(f'posts/{index}.txt', 'w') as file:
                    file.write(f'Company Name : {company_name.strip()}\n')
                    file.write(f'Required Skills : {skills.strip()}\n')
                    file.write(f'More Info : {more_info}')
                print(f'File saved: {index}')

if __name__ == '__main__':
    while True:
        find_job()
        time_wait = 10
        print(f'Waiting {time_wait} minutes ...')
        time.sleep(time_wait * 60)
