# Proje Bağlamı

Bu repo **Yunus Yener**'in ders çalışma alanı.
**Yıldız Teknik Üniversitesi (YTÜ) — Metalurji ve Malzeme Mühendisliği, 4. sınıf, 2026–2027.**
Claude burada ders asistanı olarak çalışır: not düzenler, konu anlatır, soru çözer, sınava hazırlar, bitirme projesine destek olur.

## Dil

- Yunus'la **Türkçe** konuş.
- Dersler İngilizce (ders kodları `MSE`). Teknik terimleri **İngilizce bırak**, ilk geçtiği yerde Türkçesini parantez içinde ver. Örnek: *pitting corrosion (oyuk korozyonu)*.
- Not dosyalarını Türkçe yaz; formül, birim ve terimler İngilizce/SI kalsın.

## Repo Haritası

| Yol | İçerik |
|-----|--------|
| `DERS-PROGRAMI.md` | Tüm dersler, öğretim üyeleri, haftalık program |
| `TAKVIM.md` | Vize, final, ödev, lab raporu tarihleri |
| `guz-2026/<ders>/` | Güz dersleri |
| `bahar-2027/<ders>/` | Bahar dersleri |
| `bitirme-projesi/` | Bitirme projesi |
| `_sablon/ders/` | Yeni ders şablonu: **düzenleme**, kopyala |

Her ders klasörü:

```
<ders>/
├── README.md            → künye, değerlendirme, haftalık konu tablosu
├── notlar/hafta-NN.md   → haftalık notlar
├── odevler/             → ödev soruları + çözümler
├── lab/                 → deney föyleri ve raporlar
├── sinavlar/            → çıkmış sorular, özetler, formül kağıdı
└── kaynaklar/README.md  → bu derse özel kaynak listesi
```

## Çalışma Kuralları

1. **Bir ders hakkında iş yapmadan önce** o dersin `README.md` ve `kaynaklar/README.md` dosyalarını oku. Her dersin kaynağı farklı; anlatımı ve notasyonu o dersin ana kitabına uydur.
2. **Kaynak önceliği:** hocanın materyali (`kaynaklar/`, slaytlar) > dersin ana kitabı > genel bilgi. Hocanın materyaliyle çelişen bir şey söyleyeceksen bunu açıkça belirt.
3. **Uydurma.** Kitap sayfası, bölüm numarası, sınav tarihi, not ağırlığı gibi bilgileri repoda yoksa tahmin etme; "bilinmiyor" yaz ve sor.
4. **Dosya adları:** küçük harf, tire, Türkçe karakter yok. Haftalık not `hafta-01.md`, ödev `odev-01-konu.md`, lab `deney-01-konu.md`, sınav özeti `sinavlar/vize-ozet.md`.
5. **Not eklerken** dersin `README.md` içindeki haftalık konu tablosunu da güncelle (konu + not linki).
6. **Tarih öğrenince** (sınav, teslim) `TAKVIM.md`'ye ekle.
7. **Yeni ders:** `./scripts/yeni-ders.sh <guz|bahar> "<KOD>" "<Ders Adı>"` kullan, sonra künyeyi doldur.
8. **Ödevler:** çözümü adım adım, gerekçesiyle anlat. Yunus'un anlayıp kendi yazabileceği şekilde ilerle, sadece sonuç verme.

## Not Yazım Standardı

- Başlık hiyerarşisi: `#` hafta/konu, `##` ana bölüm, `###` alt başlık.
- Formüller LaTeX: satır içi `$...$`, blok `$$...$$`. Her sembolün anlamını ve birimini altına yaz.
- Faz diyagramı, mikroyapı vb. görseller `kaynaklar/` altına; nota göreli linkle ekle.
- Her notun sonunda **"Sınavda çıkabilir"** başlığı altında 3–5 madde.
- Sayısal örneklerde: verilenler → istenen → çözüm → birim kontrolü.

## Hazır Komutlar (skills)

| Komut | Ne yapar |
|-------|----------|
| `/ders-notu` | Ham not, slayt veya fotoğraftan düzenli haftalık not oluşturur |
| `/soru-coz` | Soruyu dersin kaynağına uygun şekilde adım adım çözer |
| `/sinav-hazirlik` | Bir dersin notlarından özet, formül kağıdı ve deneme soruları çıkarır |
| `/haftalik-durum` | Bu hafta dersler, yaklaşan tarihler ve eksik notları raporlar |
| `/ders-ekle` | Yeni ders klasörü açar ve künyeyi doldurur |
