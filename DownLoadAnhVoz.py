import requests
from bs4 import BeautifulSoup
import os


value={'login':'ducthach1401','password':'mk14012000'}
s = requests.Session()
s.post('https://next.voz.vn/login/login',data=value)
filetxt=open('link.txt','r')
tam=filetxt.read()
tam=tam.split()
for i in tam:
	linktai=i
	tam=True
	for i in os.listdir(os.getcwd()):
		if (i=='Image'):
			tam=False
	if (tam):
		os.mkdir('Image')
	link=os.path.join(os.getcwd(),"Image")
	lastpage=''
	k=0

	while True: 
		k+=1
		linkpage=linktai+'page-'+str(k)
		br=s.get(linkpage)
		lastpage=linkpage
		if (br.url!=lastpage) and (k!=1):
			break
		soup=BeautifulSoup(br.text,'lxml')
		print(br.url)
		for i in soup.find_all('img'):
			temp=i.get('src')
			if ('https://next.voz.vn/' in temp):
				response=s.get(temp)
				soluong=len(os.listdir(link))+1
				temp1=str(soluong)+'.jpg'
				temp1=os.path.join(link,temp1)

				file=open(temp1,'wb')
				file.write(response.content)
				file.close()
print('Done')
