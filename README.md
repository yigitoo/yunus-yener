# Yunus Yener — YTÜ Metalurji ve Malzeme Mühendisliği 4. Sınıf

2026–2027 eğitim-öğretim yılı ders notları, ödevler, lab raporları, sınav hazırlıkları ve bitirme projesi.

## Claude ile Kullanım

Bu repo Claude ile ders asistanı olarak kullanılmak üzere düzenlendi. Bağlam ve kurallar [`CLAUDE.md`](CLAUDE.md) dosyasında.
Hazır komutlar: `/ders-notu`, `/soru-coz`, `/sinav-hazirlik`, `/haftalik-durum`, `/ders-ekle` (`.claude/skills/`).

## Hızlı Erişim

- [Ders Programı](DERS-PROGRAMI.md) — haftalık program, dersler, hocalar, kredi
- [Takvim](TAKVIM.md) — vize, final, ödev ve rapor teslim tarihleri
- [Bitirme Projesi](bitirme-projesi/README.md)

## Klasör Yapısı

```
.
├── CLAUDE.md                 → Claude için bağlam ve çalışma kuralları
├── .claude/skills/           → Hazır komutlar
├── DERS-PROGRAMI.md
├── TAKVIM.md
├── guz-2026/                 → Güz dönemi dersleri
│   └── mse4xxx-ders-adi/
│       ├── README.md         → Ders künyesi (hoca, saat, değerlendirme, kaynak kitap)
│       ├── notlar/           → Haftalık ders notları (hafta-01.md, ...)
│       ├── odevler/          → Ödev soruları ve çözümleri
│       ├── lab/              → Deney föyleri ve lab raporları
│       ├── sinavlar/         → Çıkmış sorular, özetler, formül kağıdı
│       └── kaynaklar/        → Slaytlar, makaleler, kitap bölümleri
├── bahar-2027/               → Bahar dönemi dersleri (aynı yapı)
├── bitirme-projesi/          → Yıl boyu süren bitirme projesi
├── _sablon/ders/             → Yeni ders şablonu (doğrudan düzenleme)
└── scripts/yeni-ders.sh      → Şablondan ders klasörü oluşturur
```

## Yeni Ders Ekleme

```bash
./scripts/yeni-ders.sh guz "MSE4631" "Corrosion and Prevention"
./scripts/yeni-ders.sh bahar "MSE4xxx" "Ders Adı"
# → guz-2026/mse4631-corrosion-and-prevention/ oluşturulur, DERS-PROGRAMI.md'ye satır eklenir
```

## İsimlendirme Kuralları

- Ders klasörü: `derskodu-ders-adi` (küçük harf, tire, Türkçe karakter yok)
- Haftalık not: `notlar/hafta-01.md`, `hafta-02.md` ...
- Ödev: `odevler/odev-01-konu.pdf` / `.md`
- Lab raporu: `lab/deney-01-konu-rapor.pdf`
- Sınav: `sinavlar/vize-2025.pdf`, `sinavlar/final-ozet.md`
