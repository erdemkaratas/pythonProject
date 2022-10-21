'''
kendisine gönderile sayılardan sadece palindrom olanları toplayan diğerlerini de bu toplamdan çıkaran ve geri döndüren python programını yazınız
'''



def palindrom(*dram):
    toplam=fark=0
    for sayi in dram:
        if str(sayi)==str(sayi)[::-1]:
            toplam+=sayi
        else:
            fark+=sayi
    return toplam-fark

print(palindrom(10,101,55,40,9009))

