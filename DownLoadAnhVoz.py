import requests
from bs4 import BeautifulSoup
import os


value={}
value['login']=input('nhap user:')
value['password']=input('password:')

s = requests.Session()
s.post('https://voz.vn/login/login',data=value)
filetxt=open('link.txt','r')
tam=filetxt.read()
tam=tam.split()
for i in tam:
	linktai=i
	dem=0
	folder="";
	for j in linktai:
		if (j=="/"):
			dem=dem+1
		elif (dem==4):
			folder=folder+j;
	tam=True
	for i in os.listdir(os.getcwd()):
		if (i==folder):
			tam=False
	if (tam):
		os.mkdir(folder)
	link=os.path.join(os.getcwd(),folder)
	lastpage=''
	k=0
	dem=0
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
			if ('https://voz.vn/' in temp):
				dem=dem+1
				response=s.get(temp)
				flags=1;
				temp1=str(dem)+'.jpg'
				for kt in os.listdir(link):
					if (temp1==kt):
						flags=0
						print(dem)
				if (flags==1):
					temp1=os.path.join(link,temp1)
					file=open(temp1,'wb')
					file.write(response.content)
					file.close()
print('Done')
