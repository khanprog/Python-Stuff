# ###############################################
#       Enter the Keywords in command line      #
#       and open the top 5 searches for the     #
#       keywords entered in new tabs using the  #
#       WEBBROWSER library.                     #
#                                               #
#################################################


import requests, bs4, webbrowser, sys


sys.argv

print("Googling for you.....")

response = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))

response.raise_for_status()

soup = bs4.BeautifulSoup(response.content, "html.parser")

links = soup.select('.r a')

noTimes = min(5, len(links))

for index in range(noTimes):
	webbrowser.open("http://www.google.com" + links[index].get("href"))

