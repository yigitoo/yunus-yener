---
name: ders-notu
description: Ham ders notu, slayt, PDF ya da tahta fotoğrafından düzenli haftalık ders notu oluşturur ve dersin README'sine işler. Kullanıcı bir derse not eklemek istediğinde kullan.
---

# Ders Notu Oluştur

Argümanlar: ders (kod veya ad), hafta numarası, kaynak materyal (dosya yolu, yapıştırılmış metin veya görsel).

1. Dersi `guz-2026/` veya `bahar-2027/` altında bul. Bulamazsan sor.
2. Dersin `README.md` ve `kaynaklar/README.md` dosyalarını oku; notasyonu ana kitaba uydur.
3. Materyali oku. Görselse içeriği metne dök; okunamayan kısımları `[okunamadı]` diye işaretle, uydurma.
4. `_sablon/ders/notlar/hafta-01.md` yapısını izleyerek `notlar/hafta-NN.md` yaz:
   - Ana kavramlar (terim İngilizce, ilk geçişte Türkçesi parantezde)
   - Formüller (LaTeX, sembol + birim açıklamalı)
   - Diyagram/şekil açıklamaları
   - En az bir çözümlü örnek
   - "Sınavda çıkabilir": 3–5 madde
   - "Anlaşılmayanlar / Hocaya sorulacak"
5. Dosya zaten varsa üzerine yazma; yeni içeriği ilgili bölümlere ekle.
6. Dersin `README.md` haftalık konu tablosundaki satırı güncelle (konu + `[hafta-NN](notlar/hafta-NN.md)`).
7. Ham materyal dosyaysa `kaynaklar/` altına taşı ve `kaynaklar/README.md` → "Hocanın Materyalleri" tablosuna ekle.
