import pygame as pg
import random
# paket birleştirme ve pencere ayarlama
pg.init()
genislik = 750
yukseklik = 600
pencere = pg.display.set_mode((genislik, yukseklik))

#Hile Cheat
Gecmis=[]
hile_kod=[pg.K_w, pg.K_w, pg.K_s, pg.K_s, pg.K_a, pg.K_d, pg.K_a, pg.K_d]

# degiskenler
can=3
_ = 0
l = 0
v = 0
ieksi=0
Kombo=0
Efekt=0
music=0
ceat=True
oyun_durumu="Menu"
duraklatildi = False  # Pause durumu için bayrak
muzik=True
efekt=True

#ucan efektler
ucan_yazilar=[]

# ayar çekme
taban_hiz=3
Hiz = 3
FPS = 75
saat = pg.time.Clock()

# ses
eks = pg.Sound("eksi.mp3")
par = pg.Sound("para.mp3")
heal = pg.Sound("Heal.mp3")
game = pg.Sound("gameover.mp3")
game_over = pg.Sound("gameoverrr.mp3")
pg.mixer.music.load("arka_ses.mp3")
pg.mixer.music.play(-1)

# para
para = pg.image.load("para.png")
para_kordinat = para.get_rect()
para_kordinat.topleft = (350, 250)

buyuk_para=pg.image.load("iyipara.png")
buyuk_para_kordinat = buyuk_para.get_rect()
buyuk_para_aktif=False
# eksi para
eksi_para = pg.image.load("para engel.png")
eksi_para_kordinat = eksi_para.get_rect()
eksi_para_kordinat.center = (300, 400)

ieksi_para=pg.image.load("para engel.png")
ieksi_para_kordinat = ieksi_para.get_rect()
ieksi_para_kordinat.center=(100,100)

# font ve skor
para_Sayisi = 0
font = pg.font.SysFont("arial", 23)
buyuk_font = pg.font.SysFont("arial", 36)

# slime
slime_kucuk = pg.image.load("kucukslime.png")
slime_kucuk_kordinat = slime_kucuk.get_rect()

slime_orta = pg.image.load("degisik.png")
slime_orta_kordi = slime_orta.get_rect()

slime_buyuk = pg.image.load("degisikadam.png")
slime_buyuk_kordi = slime_buyuk.get_rect()

slime = slime_kucuk
slime_kordinat = slime.get_rect()
slime_kordinat.topleft = (200, 200)
#Kalpler

kalp = pg.image.load("kalp.png")
#etki edenler büyü vb.
#ekstra kalp
donkalp=pg.image.load("don.png")
donkalp_kordinat = donkalp.get_rect()
don_aktif=False
#İksir
iksir=pg.image.load("iksir.png")
iksir_kordinat = iksir.get_rect()
iskir=False
hizlanma=False
iksir_bitis_zamani=0
Suresi=20000
# eksi parayı ayarlama
eksi_hiz_x = 5
eksi_hiz_y = 5

ieksi_hiz_y=5
ieksi_hiz_x=5
durum = True
while durum:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            durum = False
        elif event.type == pg.KEYDOWN:
            # P veya ESC tuşuna basınca duraklatma durumunu değiştirir
            if event.key ==event.key == pg.K_ESCAPE:
                duraklatildi = not duraklatildi
                if duraklatildi:
                    pg.mixer.music.pause()
                else:
                    pg.mixer.music.unpause()
            if event.key == pg.K_m:
                muzik=not muzik
                if not muzik :
                    pg.mixer.music.stop()
                elif muzik:
                    pg.mixer.music.play(-1)
            if event.key==pg.K_n:
                efekt=not efekt
            Gecmis.append(event.key)
            if len(Gecmis)>8:
                Gecmis.pop(0)
            if Gecmis==hile_kod:
                ceat=not ceat
                can=9
                Gecmis=[]


    while oyun_durumu=="Menu" and durum:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                durum = False
        pencere.fill((0,0,0))
        ilk_yazi=font.render("To'PARA", True, (255, 255, 255))
        musici=font.render("Sesi kapatmak için M ye basabilirsiniz",True, (0, 255, 0))
        ogretici=font.render("Hareket için 'W,A,S,D' \nDurdurmak için esc yada P\nBaşlamak için 'SPACE' e basın",True,(255,0,0))
        tus=pg.key.get_pressed()
        if tus[pg.K_SPACE]:
            oyun_durumu="oyun"
        pencere.blit(musici,(260,400))
        pencere.blit(ogretici,(260,200))
        pencere.blit(ilk_yazi,(340,50))
        pg.display.flip()
        saat.tick(FPS)

    if ieksi==0 and para_Sayisi>19:
        ieksi=1

    # Oyun duraklatıldıysa karesel döngüyü dondurup pause yazısını basar
    if duraklatildi:
        pencere.fill((0, 0, 0))
        duraklat_yazisi = buyuk_font.render("OYUN DURDURULDU", True, (255, 255, 255))
        devam_yazisi = font.render("Devam etmek için 'P' veya 'ESC' tuşuna bas", True, (200, 200, 200))

        pencere.blit(duraklat_yazisi, (genislik // 2 - 160, yukseklik // 2 - 40))
        pencere.blit(devam_yazisi, (genislik // 2 - 180, yukseklik // 2 + 10))
        pg.display.flip()
        saat.tick(FPS)
        continue  # Oyun mekaniklerini çalıştırmayıp başa döner

    pencere.fill((0, 0, 0))
    if hizlanma:
        su_anki_zaman = pg.time.get_ticks()
        if su_anki_zaman >= iksir_bitis_zamani:
            hizlanma = False
    # hangi tuşla oynanması gerektiği
    tus = pg.key.get_pressed()
    if tus[pg.K_w] and slime_kordinat.y > 0:
        slime_kordinat.y -= Hiz

    if tus[pg.K_s] and slime_kordinat.y < yukseklik - slime.get_height():
        slime_kordinat.y += Hiz

    if tus[pg.K_a] and slime_kordinat.x > 0:
        slime_kordinat.x -= Hiz

    if tus[pg.K_d] and slime_kordinat.x < genislik - slime.get_width():
        slime_kordinat.x += Hiz
    # eksi para hareket
    eksi_para_kordinat.x += eksi_hiz_x
    eksi_para_kordinat.y += eksi_hiz_y

    if eksi_para_kordinat.left <= 0 :
        eksi_para_kordinat.left=0
        eksi_hiz_x *= -1
    if eksi_para_kordinat.right >= genislik:
        eksi_para_kordinat.right=genislik
        eksi_hiz_x *= -1
    if eksi_para_kordinat.top <= 0:
       eksi_para_kordinat.top=0
       eksi_hiz_y*= -1
    if eksi_para_kordinat.bottom >= yukseklik:
       eksi_para_kordinat.bottom=yukseklik
       eksi_hiz_y *= -1

    #Dondurma kalp
    if not don_aktif and can<=4 and random.randint(1,1000)==1 and ceat:
        donkalp_kordinat.x=random.randint(30,genislik-30)
        donkalp_kordinat.y=random.randint(30,yukseklik-30)
        don_aktif=True
    #5li paranın çıkışı
    if buyuk_para_aktif==False and random.randint(1,1000)==19:
        buyuk_para_aktif=True
        buyuk_para_kordinat.x=random.randint(30,genislik-30)
        buyuk_para_kordinat.y=random.randint(30,yukseklik-30)
    #iksir
    if iskir==False and hizlanma==False and random.randint(1,1000)==1:
        iskir=True
        iksir_kordinat.x=random.randint(30,genislik-30)
        iksir_kordinat.y=random.randint(30,yukseklik-30)

    # ikinci eksi para hareket
    ieksi_para_kordinat.x += ieksi_hiz_x
    ieksi_para_kordinat.y += ieksi_hiz_y

    if ieksi_para_kordinat.left<=0:
        ieksi_para_kordinat.left=0
        ieksi_hiz_x *= -1
    if ieksi_para_kordinat.right >= genislik:
        ieksi_para_kordinat.right=genislik
        ieksi_hiz_x *= -1
    if ieksi_para_kordinat.top <= 0:
        ieksi_para_kordinat.top = 0
        ieksi_hiz_y *= -1
    if ieksi_para_kordinat.bottom>=yukseklik:
        ieksi_para_kordinat.bottom=yukseklik
        ieksi_hiz_y *= -1

    # slime ve paraların etkileşimleri
    if don_aktif:
        pencere.blit(donkalp,donkalp_kordinat)
        if slime_kordinat.colliderect(donkalp_kordinat):
          can+=1
          if efekt:
             heal.play()
          don_aktif=False

    if buyuk_para_aktif:
        pencere.blit(buyuk_para,buyuk_para_kordinat)
        if slime_kordinat.colliderect(buyuk_para_kordinat):
            para_Sayisi +=5
            Kombo+=1
            if efekt:
                par.play()
            buyuk_para_aktif=False
    if iskir:
        pencere.blit(iksir,iksir_kordinat)
        if slime_kordinat.colliderect(iksir_kordinat):
            hizlanma=True
            iskir=False
            iksir_bitis_zamani=pg.time.get_ticks()+Suresi

    if slime_kordinat.colliderect(para_kordinat):
        para_kordinat.x = random.randint(0, genislik - para.get_width())
        para_kordinat.y = random.randint(3, yukseklik - para.get_height())
        Kombo+=1
        if 6>=Kombo>=1:
          para_Sayisi +=1
        if 13>=Kombo>6:
          para_Sayisi +=2
        if 15>=Kombo>13:
          para_Sayisi +=3
        if 20>=Kombo>15:
          para_Sayisi +=4
        if Kombo>20:
          para_Sayisi +=5

        if efekt:
          par.play()

    if slime_kordinat.colliderect(eksi_para_kordinat) and ceat:
        eksi_para_kordinat.x = random.randint(0, genislik - eksi_para.get_width())
        eksi_para_kordinat.y = random.randint(3, yukseklik - eksi_para.get_height())
        para_Sayisi = para_Sayisi - 1
        Kombo=0
        if efekt:
         eks.play()
        can-=1

    if ieksi==1 and slime_kordinat.colliderect(ieksi_para_kordinat) and ceat:
        ieksi_para_kordinat.x=random.randint(0, genislik - ieksi_para.get_width())
        ieksi_para_kordinat.y=random.randint(3, yukseklik - ieksi_para.get_height())
        para_Sayisi = para_Sayisi - 1
        Kombo=0
        if efekt:
         eks.play()
        can-=1

    # yazı
    skor_yazisi = font.render(str(f"Skor: {para_Sayisi}"), True, (0, 255, 0))
    kombo_yazisi=font.render(str(f"Kombo: {Kombo}"), True, (0, 255, 0))
    # slimein büyüyüp küçülmesi
    if 40 > para_Sayisi >= 30:
        if v == 0:
            taban_hiz=4
            eksi_hiz_y = 8
            eksi_hiz_x = 8
            ieksi_hiz_y = 8
            ieksi_hiz_x = 8
            v = 1
    if 30 > para_Sayisi >= 20:
        slime = slime_buyuk
        taban_hiz = 5
        if v == 1:

            eksi_hiz_y = 6.5
            eksi_hiz_x = 6.5
            ieksi_hiz_y = 6.5
            ieksi_hiz_x = 6.5
            v = 0
        if _ == 0:
            slime_buyuk_kordi.x = slime_orta_kordi.x
            slime_buyuk_kordi.y = slime_orta_kordi.y
            slime_kordinat = slime_buyuk_kordi
            _ = +1

            eksi_hiz_y = 6.5
            eksi_hiz_x = 6.5
            ieksi_hiz_y = 6.5
            ieksi_hiz_x = 6.5
    if 20 > para_Sayisi >= 10:
        slime = slime_orta
        slime_kordinat = slime_orta_kordi
        taban_hiz = 4
        if para_Sayisi >= 18 and _ >= 1:
            slime_orta_kordi.x = slime_buyuk_kordi.x
            slime_orta_kordi.y = slime_buyuk_kordi.y
            _ = 0
            slime_kordinat = slime_orta_kordi

            eksi_hiz_y = 5
            eksi_hiz_x = 5
            ieksi_hiz_y = 5
            ieksi_hiz_x = 5
        if l >= 1 and para_Sayisi >= 10:
            slime_orta_kordi.x = slime_kucuk_kordinat.x
            slime_orta_kordi.y = slime_kucuk_kordinat.y
            l = 0
            slime_kordinat = slime_orta_kordi

            eksi_hiz_y = 5
            eksi_hiz_x = 5
            ieksi_hiz_y = 5
            ieksi_hiz_x = 5
    if para_Sayisi < 10:
        slime = slime_kucuk
        slime_kordinat = slime_kucuk_kordinat
        if l == 0 and para_Sayisi < 10:
            slime_kucuk_kordinat.x = slime_orta_kordi.x
            slime_kucuk_kordinat.y = slime_orta_kordi.y
            l = +1
            slime_kordinat = slime_kucuk_kordinat
            Hiz = 3
            eksi_hiz_y = 3
            eksi_hiz_x = 3

    if hizlanma:
        Hiz=taban_hiz+6
    if not hizlanma:
        Hiz=taban_hiz

    # bitiş ekranı
    if para_Sayisi < 0 or can==0:
        if muzik:
            game_over.play(-1)
        if efekt:
          game.play()

        with open ("skor.txt","r") as file:
            for line in file:
              high = int(line)
            high=int(high)
            birinci=high
            if para_Sayisi>high:
                with open("skor.txt","w") as f:
                 f.write(str(para_Sayisi))



        while durum:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    durum = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_m:
                        muzik = not muzik
                        if muzik and music==0:
                            game_over.play(-1)
                            music=1
                        elif muzik and music==1:
                            game_over.stop()
                            music=0
                    if event.key == pg.K_n:
                        efekt = not efekt
                        if efekt and Efekt==0:
                            game.play()
                            Efekt=1
            pg.mixer.music.stop()
            pencere.fill((0, 0, 0))
            skor = font.render(f"Oyun bitti! Skorun:{para_Sayisi}", True, (0, 255, 0))
            yeniden = font.render("yeniden denemek için 'R' tuşuna basman gerekicek", True, (0, 255, 0))
            if para_Sayisi<=birinci:
              highscore = font.render(f"Skoru geçemedin en yüksek skor: {high}", True, (255, 255, 255))
              pencere.blit(highscore, (60, 60))
            elif para_Sayisi>birinci:
              breakscore=font.render(f"**Skoru geçtin:{para_Sayisi}**", True, (255, 255, 255))
              pencere.blit(breakscore, (60, 60))
              high=para_Sayisi
            pencere.blit(skor, (300, 225))
            pencere.blit(yeniden, (175, 250))
            pg.display.flip()
            saat.tick(FPS)
            tus=pg.key.get_pressed()
            if tus[pg.K_r]:
                para_Sayisi = 0
                game_over.stop()
                pg.mixer.music.play(-1)
                _ = 0
                l = 0
                can=3
                v = 0
                ceat=True
                ieksi=0
                Efekt=0
                music=0
                efekt=True
                don_aktif=False
                slime_kordinat.center=(300,270)
                slime_kucuk_kordinat.center=(300,270)
                slime_orta_kordi.center=(300,270)
                slime_buyuk_kordi.center=(300,270)
                break

    # yenilemeler ekran
    for i in range(can):
        pencere.blit(kalp, (10+i*20,10))
    pencere.blit(skor_yazisi, (345, 10))
    pencere.blit(kombo_yazisi, (600, 10))
    pencere.blit(slime, slime_kordinat)
    pencere.blit(para, para_kordinat)
    pencere.blit(eksi_para, eksi_para_kordinat)
    if ieksi==1:
     pencere.blit(ieksi_para, ieksi_para_kordinat)
    pg.display.flip()
    saat.tick(FPS)

pg.quit()