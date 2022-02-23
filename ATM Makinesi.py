hosgeldniz = ' ATM Makinesine Hoşgeldiniz'
print(hosgeldniz.center(50, '*'))
islemler =  """
1-) Para Çekme
2-) Para Yatırma
3-) Bakiye Sorgulama
4-) Çıkış
            """
print(islemler)
bakiye = int(input('Bakiyenizi Giriniz: '))
while True:
    secim = input('İşlem seçiniz: ')
    if(secim == '3'):
        print(f'Bakiyeniz: {bakiye} TL')
    elif(secim == '1'):
        para_Cekme = int(input('Çekmek istediğiniz tutar: '))
        if(para_Cekme > bakiye):
            print('Yetersiz Bakiye')
            continue
        bakiye -= para_Cekme
    elif(secim == '2'):
        para_Yatirma = int(input('Yatırmak istediğiniz tutar: '))
        if(para_Yatirma > 4000):
            print('Üzgünüz en fazla 4000 TL yatırabilirsiniz')
            continue
        bakiye += para_Yatirma
    elif(secim == '4'):
        break
    else:
        print('Geçersiz İşlem')