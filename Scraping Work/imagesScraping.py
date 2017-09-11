import requests, bs4, os, logging

# setup for logging for debugging 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

#function for saving the image from the website
def saveImage(linkOfImage):
	imageUrl = "http:" + linkOfImage
	image_name = os.path.split(imageUrl)[1]
	logging.debug("********** Got Image Name {} **********".format(image_name))

	response = requests.get(imageUrl)
	response.raise_for_status()

	if not os.path.exists("imgs"):
		os.mkdir("imgs")
	with open("imgs/" + image_name, "wb") as image:
		image.write(response.content)
	logging.debug("********** Image Saved **********")


# Link from which the data should be scraped
link = "https://xkcd.com"

while True:

	res = requests.get(link)
	logging.debug("********** Link reached **********")
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.content, "html.parser")
	imageElement = soup.select('#comic > img')
	if imageElement == []:
		imageElement = soup.select('#comic > a > img')
		if imageElement == []:
			# you can add more selectors if the image is inside some other tags
			# I am skipping this for now
			nextUrl = soup.select('.comicNav li > a')
			nextUrl = nextUrl[1].get("href")
			
			link = "https://xkcd.com"
			link += nextUrl

			continue

	#get the src of the image only
	imageLink = imageElement[0].get("src")
	logging.debug("**********Got Image Link:  {} **********". format(imageLink))
	saveImage(imageLink)

	#get the URL of the previous link
	nextUrl = soup.select('.comicNav li > a')
	nextUrl = nextUrl[1].get("href")

	link = "https://xkcd.com"
	link += nextUrl
