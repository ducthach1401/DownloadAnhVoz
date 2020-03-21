import requests
from bs4 import BeautifulSoup
import os


value={'login':'nameuser','password':'pass'}
s = requests.Session()
s.post('https://next.voz.vn/login/login',data=value)
br=s.get("https://next.voz.vn/t/no-sex-test-dang-anh-nextvoz.613/")
tam=True
for i in os.listdir(os.getcwd()):
	if (i=='Image'):
		tam=False
if (tam):
	os.mkdir('Image')
soup=BeautifulSoup(br.text,'lxml')
link=os.path.join(os.getcwd(),"Image")
lastpage=''
k=0
while True: 
	k+=1
	linkpage='https://next.voz.vn/t/no-sex-test-dang-anh-nextvoz.613/page-'+str(k)
	br=s.get(linkpage)
	lastpage=linkpage
	if (br.url!=lastpage) and (k!=1):
		break
	soup=BeautifulSoup(br.text,'lxml')
	print(br.url)
	for i in soup.find_all('img'):
		temp=i.get('src')
		if ('https' in temp):
			response=s.get(temp)
			soluong=len(os.listdir(link))+1
			temp1=str(soluong)+'.jpg'
			temp1=os.path.join(link,temp1)

			file=open(temp1,'wb')
			file.write(response.content)
			file.close()
print('Done')
