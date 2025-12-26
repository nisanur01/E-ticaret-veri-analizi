E-Ticaret Yorum Analizi ve Puan Tahminleme
​Bu proje, Apache Spark (PySpark) kullanılarak müşteri yorumlarından otomatik puan tahmini yapmak amacıyla geliştirilmiştir.

​ Projenin Amacı
​Bir e-ticaret sitesindeki müşteri yorumlarını analiz ederek bu yorumun sonucunda kaç puan verilebileceğini tahmin etmek.
​Müşterinin yorumunda yazdığı kelimelere bakarak vereceği puanı 1 ile 5 arasında sayısal olarak tahmin etmek.

​ Veri Seti Yapısı
​Veri setinde toplam 10 kolon bulunmasına rağmen, analiz için en kritik 2 kolona odaklanılmıştır:
​Müşterinin yazdığı yorum (Girdi/Feature).
​Verdiği sayısal değer (Hedef/Label).

​ İzlenen Adımlar (Pipeline)
​Tokenizer: Cümleleri kelimelere ayırdı.
​Stopwords: Tahmine etkisi olmayan (ve, ama, de gibi) kelimeleri temizledi.
​Hashing: Temizlenen kelimeleri bilgisayarın anlayacağı matematiksel değerlere dönüştürdü.
​Linear Regression: Yorumdaki kelimelerin ağırlığına göre puan üretti.

​ Neden Lineer Regresyon?
​Puanlar 1'den 5'e kadar ölçekli olduğundan bir değer tahmini yapmak istedim.
​Lojistik Regresyon yerine bunu seçtim çünkü ara değerleri de görmek istedim.
​Lojistik sadece "4" veya "5" puan derken, Lineer modeli 4.7 gibi sonuçlar verebilir.
​Bu da müşterinin 4 puandan çok mutlu olduğunu ama 5 puan kadar kusursuz bulmadığını gösterir.
​Yani sadece gruplandırmak yerine memnuniyet şiddetini ölçmek istedim.
