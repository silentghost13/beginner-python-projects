import requests
from bs4 import BeautifulSoup as bs

#https://www.youtube.com/watch?v=SqvVm3QiQVk&t=40s

github_user = input('Input Github Username: ')
url = 'https://github.com/'+github_user
r = requests.get(url)
soup = bs(r.content, 'lxml')
profile_image = soup.find('img', class_ = 'avatar avatar-user width-full border color-bg-primary')['src']
print(profile_image) 
