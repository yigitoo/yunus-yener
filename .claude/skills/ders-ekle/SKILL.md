---
name: ders-ekle
description: Yeni bir ders için klasör açar, künyeyi ve kaynak listesini doldurur, programa ve takvime işler. Yeni dönem başında veya ders eklendiğinde kullan.
---

# Ders Ekle

Argümanlar: dönem (guz/bahar), ders kodu, ders adı; varsa hoca, gün/saat/derslik, kaynak kitap. Ders programı ekran görüntüsü verilirse bilgileri oradan çıkar.

1. `./scripts/yeni-ders.sh <guz|bahar> "<KOD>" "<Ders Adı>"` çalıştır.
2. Oluşan `README.md` künyesini doldur (hoca, gün/saat/derslik). Bilinmeyen alanları boş bırak.
3. `DERS-PROGRAMI.md`'de dersin satırına hocayı ekle; haftalık program tablosuna saatini ekle.
4. `kaynaklar/README.md`: kullanıcı kaynak verdiyse ekle. Vermediyse alan için yerleşik standart ders kitaplarını öner ve "Önerilen, izlenceyle doğrulanacak" notunu koy.
5. İzlence (syllabus) verildiyse değerlendirme ağırlıklarını ve 14 haftalık konu tablosunu doldur; sınav tarihlerini `TAKVIM.md`'ye ekle.
