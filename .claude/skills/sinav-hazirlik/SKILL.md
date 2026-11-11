---
name: sinav-hazirlik
description: Bir dersin notlarından ve kaynaklarından sınav özeti, formül kağıdı ve deneme soruları hazırlar. Vize/final/quiz hazırlığında kullan.
---

# Sınav Hazırlık

Argümanlar: ders, sınav türü (vize/final/quiz), kapsam (hafta aralığı; verilmezse README'deki tabloya göre: vize 1–7, final tümü).

1. Dersin `README.md` (değerlendirme, haftalık konular), kapsamdaki tüm `notlar/hafta-*.md`, `sinavlar/` (çıkmış sorular) ve `kaynaklar/README.md` dosyalarını oku.
2. `TAKVIM.md`'den sınav tarihini kontrol et; varsa kaç gün kaldığını belirt.
3. `sinavlar/<tur>-ozet.md` oluştur:
   - **Konu haritası:** kapsamdaki konular, önem sırasıyla (çıkmış sorularda sık geçen = yüksek)
   - **Formül kağıdı:** tüm denklemler, sembol/birim tablosu
   - **Kritik kavramlar:** her biri 1–2 cümle
   - **Sık hatalar**
   - **Deneme soruları:** 5–10 soru (kavramsal + sayısal karışık), cevaplar en sonda `<details>` içinde
4. Notu eksik haftalar varsa listele, uydurma içerikle doldurma.
5. Çıkmış sorular varsa soru tiplerini analiz et ve özetin başına yaz.
