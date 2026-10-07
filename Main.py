import pygame as pg
import random

# paket birleştirme ve pencere ayarlama
pg.init()
genislik = 750
yukseklik = 600
pencere = pg.display.set_mode((genislik, yukseklik))

# degiskenler
_ = 0
l = 0
z = 0
v = 0
ieksi=0
oyun_durumu="Menu"
duraklatildi = False  # Pause durumu için bayrak
muzik=True
efekt=True
# ayar çekme
Hiz = 10
FPS = 60
saat = pg.time.Clock()

# ses
eks = pg.Sound("eksi.mp3")
par = pg.Sound("para.mp3")
game = pg.Sound("gameover.mp3")
game_over = pg.Sound("gameoverrr.mp3")
pg.mixer.music.load("arka_ses.mp3")
pg.mixer.music.play(-1)

# para
para = pg.image.load("para.png")
para_kordinat = para.get_rect()
para_kordinat.topleft = (350, 250)

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
            if event.key == pg.K_p or event.key == pg.K_ESCAPE:
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

    if ieksi==0 and para_Sayisi>20:
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
    if slime_kordinat.colliderect(para_kordinat):
        para_kordinat.x = random.randint(0, genislik - para.get_width())
        para_kordinat.y = random.randint(3, yukseklik - para.get_height())
        para_Sayisi = para_Sayisi + 1
        if efekt:
         par.play()

    if slime_kordinat.colliderect(eksi_para_kordinat):
        eksi_para_kordinat.x = random.randint(0, genislik - eksi_para.get_width())
        eksi_para_kordinat.y = random.randint(3, yukseklik - eksi_para.get_height())
        para_Sayisi = para_Sayisi - 1
        if efekt:
         eks.play()
        z += 1

    if ieksi==1 and slime_kordinat.colliderect(ieksi_para_kordinat):
        ieksi_para_kordinat.x=random.randint(0, genislik - ieksi_para.get_width())
        ieksi_para_kordinat.y=random.randint(3, yukseklik - ieksi_para.get_height())
        para_Sayisi = para_Sayisi - 1
        pg.mixer.Sound.play(eks)
        z +=1

    # yazı
    skor_yazisi = font.render(str(f"Skor: {para_Sayisi}"), True, (0, 255, 0))
    hata_yazisi = font.render(str(f"Hata: {z}"), True, (26, 255, 0))

    # slimein büyüyüp küçülmesi
    if 40 > para_Sayisi >= 30:
        if v == 0:
            eksi_hiz_y = 17
            eksi_hiz_x = 17
            ieksi_hiz_y = 17
            ieksi_hiz_x = 17
            v = 1
    if 30 > para_Sayisi >= 20:
        slime = slime_buyuk
        if v == 1:
            eksi_hiz_y = 13
            eksi_hiz_x = 13
            ieksi_hiz_y = 13
            ieksi_hiz_x = 13
            v = 0
        if _ == 0:
            slime_buyuk_kordi.x = slime_orta_kordi.x
            slime_buyuk_kordi.y = slime_orta_kordi.y
            slime_kordinat = slime_buyuk_kordi
            _ = +1
            Hiz = 9
            eksi_hiz_y = 13
            eksi_hiz_x = 13
            ieksi_hiz_y = 13
            ieksi_hiz_x = 13
    if 20 > para_Sayisi >= 10:
        slime = slime_orta
        slime_kordinat = slime_orta_kordi

        if para_Sayisi >= 18 and _ >= 1:
            slime_orta_kordi.x = slime_buyuk_kordi.x
            slime_orta_kordi.y = slime_buyuk_kordi.y
            _ = 0
            slime_kordinat = slime_orta_kordi
            Hiz=13
            eksi_hiz_y = 10
            eksi_hiz_x = 10
            ieksi_hiz_y = 10
            ieksi_hiz_x = 10
        if l >= 1 and para_Sayisi >= 10:
            slime_orta_kordi.x = slime_kucuk_kordinat.x
            slime_orta_kordi.y = slime_kucuk_kordinat.y
            l = 0
            slime_kordinat = slime_orta_kordi
            Hiz=13
            eksi_hiz_y = 10
            eksi_hiz_x = 10
            ieksi_hiz_y = 10
            ieksi_hiz_x = 10
    if para_Sayisi < 10:
        slime = slime_kucuk
        slime_kordinat = slime_kucuk_kordinat
        if l == 0 and para_Sayisi < 10:
            slime_kucuk_kordinat.x = slime_orta_kordi.x
            slime_kucuk_kordinat.y = slime_orta_kordi.y
            l = +1
            slime_kordinat = slime_kucuk_kordinat
            Hiz = 15
            eksi_hiz_y = 10
            eksi_hiz_x = 10

    # bitiş ekranı
    if para_Sayisi < 0 or z >= 10:
        if muzik:
            game_over.play(-1)
        if efekt:
          game.play()

        with open ("skor.txt","r") as file:
            for line in file:
                high = int(line)
            if para_Sayisi>high:
              with open("skor.txt","w") as f:
               f.write(str(para_Sayisi))



        while durum:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    durum = False
            pg.mixer.music.stop()
            pencere.fill((0, 0, 0))
            skor = font.render(f"Oyun bitti! Skorun:{para_Sayisi}", True, (0, 255, 0))
            yeniden = font.render("yeniden denemek için 'R' tuşuna basman gerekicek", True, (0, 255, 0))
            if para_Sayisi<=high:
              highscore = font.render(f"Skoru geçemedin en yüksek skor: {high}", True, (255, 255, 255))
              pencere.blit(highscore, (60, 60))
            elif para_Sayisi>high:
              breakscore=font.render(f"**Skoru geçtin:{para_Sayisi}**", True, (255, 255, 255))
              pencere.blit(breakscore, (60, 60))
              high=para_Sayisi
            pencere.blit(skor, (300, 225))
            pencere.blit(yeniden, (175, 250))
            pg.display.flip()
            saat.tick(FPS)

            tus = pg.key.get_pressed()
            if tus[pg.K_r]:
                para_Sayisi = 0
                game_over.stop()
                pg.mixer.music.play(-1)
                _ = 0
                l = 0
                z = 0
                v = 0
                ieksi=0
                slime_kordinat.center=(300,270)
                slime_kucuk_kordinat.center=(300,270)
                slime_orta_kordi.center=(300,270)
                slime_buyuk_kordi.center=(300,270)
                break

    # yenilemeler ekran

    pencere.blit(hata_yazisi, (10, 10))
    pencere.blit(skor_yazisi, (345, 10))
    pencere.blit(slime, slime_kordinat)
    pencere.blit(para, para_kordinat)
    pencere.blit(eksi_para, eksi_para_kordinat)
    if ieksi==1:
     pencere.blit(ieksi_para, ieksi_para_kordinat)
    pg.display.flip()
    saat.tick(FPS)

pg.quit()