from instabot import Bot
import random,os,time

bot = Bot()
bot.login(username=input("Kullanıcı Adı: "), password=input("Şifre: "))
baslik = input("başlık giriniz: ")
yol = input("postların bulunduğu klasör yolunu giriniz: ")
kacdakika = int(input("kaç dakika arayla post atılsın: "))
while True:
    postx = random.choice(os.listdir(yol))
    bot.upload_photo(yol+"/"+postx,  caption = baslik) 
    print(f"{kacdakika} dakika bekleniyor..")
    time.sleep(kacdakika*60)