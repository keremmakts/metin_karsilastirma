# İlk metni dosyadan oku ve temizle
str1 = open('ar.txt', 'r').read()
str2 = open('edain.txt', 'r').read()

# Karşılaştırma için kullanılan durma kelimeleri
durma_kelimeleri = ["ve", "veya", "ile", "çünkü", "birkaç", "böyle", "falan", "herkes", "hiçbiri",
                    "gibi", "hangi", "kim", "şu", "şey", "yada", "zira", "zaten", "yine", "neyse",
                    "ama", "ancak", "asla", "az", "bazı", "bazısı", "belki", "birçok", "çok", "çoğu",
                    "daha", "değil", "diğer", "elbette", "hiç", "ise", "kendi", "kime", "niye", "önce",
                    "ötürü", "rağmen", "şunu", "şunlar", "tümü", "veya", "yoksa", "zaten", "zira"]

# Metinlerden durma kelimelerini kaldır
for kelime in durma_kelimeleri:
    str1 = str1.replace(kelime, "")
    str2 = str2.replace(kelime, "")

# Temizlenmiş metinleri listeye çevir
liste1 = str1.split()
liste2 = str2.split()

# Listeleri kümelere çevir
kume1 = set(liste1)
kume2 = set(liste2)

# İki metnin birleşim kümesini oluştur
birlesim_kumesi = kume1.union(kume2)

# Tekil sözcük sayılarını hesapla
tekil_sozcuk_sayisi_metin1 = len(kume1)
tekil_sozcuk_sayisi_metin2 = len(kume2)
tekil_sozcuk_sayisi_birlesim = len(birlesim_kumesi)

# Sonuçları ekrana yazdır
print("İki metin için tekil sözcük sayısı =", tekil_sozcuk_sayisi_metin1 + tekil_sozcuk_sayisi_metin2)
print("Birleşim sonrası tekil sözcük sayısı =", tekil_sozcuk_sayisi_birlesim)

# Farkı hesapla
fark = (tekil_sozcuk_sayisi_metin1 + tekil_sozcuk_sayisi_metin2) - tekil_sozcuk_sayisi_birlesim

# Benzeme oranını hesapla
benzeme_orani = (fark * 100) / tekil_sozcuk_sayisi_birlesim

# Sonuçları ekrana yazdır
print("Fark =", fark)
print("Benzeme oranı = %", benzeme_orani)
