import requests


res = requests.get("http://automatetheboringstuff.com/files/rj.txt")

# checking the return code 
print(res.status_code)

# for checking if some error occured and close the program then

res.raise_for_status()

# writing the content fo the page to txt file 
# it should be written in binaru format to preserve the unicode characters


romeoFile = open("romeo&juliet.txt", "wb")

for linesChunk in res.iter_content(100000):
	romeoFile.write(linesChunk)

romeoFile.close()