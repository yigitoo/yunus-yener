# Sol-Gel Deneyi — Deney Sırasında Alınan Notlar (ham)

- **Öğrenci:** Yunus Yener — 2205C046 — **Grup 5**
- **Deneyi yürüten:** Serra Hoca (tam adı/unvanı: bilinmiyor)
- **Tarih:** Kasım 2026, ilk hafta (kesin gün bilinmiyor)
- **Föy:** [`../foy.pdf`](../foy.pdf)
- **El yazısı orijinaller:** [ham-not-1.jpg](ham-not-1.jpg), [ham-not-2.jpg](ham-not-2.jpg)

> Bu dosya el yazısı notların birebir dökümüdür; rapor bunlardan yazılacak.
> Rapor formatı referansı: [`../exp8-ore-dressing-yunus-yener.pdf`](../exp8-ore-dressing-yunus-yener.pdf) (Yunus'un kendi Exp 8 raporu).

## Rapor konsepti (Exp 8 örneğinden)

- **Dil:** İngilizce, el yazısı, ~3–4 sayfa. Kısa ve öz.
- **Başlık bloğu:** `Experiment N: <Konu> – Lab Report` / `Name: Yunus Yener` / `Student No: 2205C046   Group-5`
- **Bölümler:**
  1. **Aim** — tek paragraf, spesifik amaçlar
  2. **Materials and Devices** — madde işaretli malzeme + cihaz listesi
  3. **Experimental Procedure** — alt başlıklar (3.1, 3.2…), geçmiş zaman edilgen ("was weighed…")
  4. **Data Derived from the Experiment** — numaralı tablolar (Table 1, Table 2…), elle çizilmiş grafik, hesaplar formülüyle
  5. **Discussion and Evaluation of the Results** — tek-iki paragraf: sonuçlar, teorik/beklenen ile fark, hata kaynakları
  6. **References** — Türkçe ders kitapları + "Experiment N: …, MSE4121 Laboratory Manual"

## Rapor kararları (Yunus, 12.11.2026)

- **Ana veri kaynağı: bu notlar.** Çelişkide Yunus'un notu geçerli (kurutma 100 °C, stok toplam 12 damla, spin coating 3 damla FTO/ITO cam, test sırası aşağıdaki tablodaki gibi).
- Notlarda olmayan miktarlar föyden alınır: Sol I = 3 mL TEOS + 5 mL etanol; Sol II = 3 mL su + 5 mL etanol; stok = 1.9 g NH₄F + 23 mL NH₄OH / 100 mL su.
- Föyde Exp 4 için soru listesi **yok** (Exp 5'te "Post-lab questions" var, Exp 4'te yok) → sorular derste sözlü verildi.
- Notlardan çıkan sorular: % ağırlık kaybı · spin coating'de hangi parametre neden etkisiz (geçen sene finalde) · süperhidrofobik silika yüzey · Ostwald viskozitesi.
- Sınıf arkadaşının raporunda ek olarak: Tyndall etkisi ve SiO₂ nanotozun yapısı (amorf/kristal). Bunlar da kısa cevaplanacak.
- Teori/Aim kısa; deney süreci ve sorular ağırlıklı. Sorularda kaynak gösterilecek. Benzerlik cezası var → özgün metin.

## Teori notları

- **Colloidal structure** (kolloidal yapı): iki faz birbiri içinde tam çözünmüyor. Ör. sisli hava, köpük. Dispersion medium → sıvı.
- **pH etkisi:** bazik ortamda bond daha kuvvetli, asidik ortamda daha zayıf. pH değişince process hızlanıyor; catalyst (katalizör) hızlandırıyor.
- Hydrolysis (hidroliz): $\equiv\text{Si–OR} + \text{H}_2\text{O} \rightleftharpoons \equiv\text{Si–OH} + \text{ROH}$
- **Solvent:** metal alkoxide'i (metal alkoksit) çözmesi lazım.
- **Calcination** (kalsinasyon): organikler uzaklaşır, kısa sürer.
- **Sintering** (sinterleme): dense (yoğun) malzeme oluşur.
- **Tyndall effect** (Tyndall etkisi): jel olduktan sonra lazer tutuyoruz — [jel | saf su] kapları yan yana, lazer geçirildi.
- Dip / spin coating: RPM ve süre (time) etkisi kaplamaya.

## 1) Sentez — Silica nanopartikül + dip coating

- Sol-2'den Sol-1'e damla damla eklenecek → alkoxide hidrolizi başlıyor.
- Stok (katalizör solüsyonu) ekleniyor: 3 damla + 3 damla şeklinde. Cam üzerinde kaplama olmaya başladığında (dip coating) durup stok eklemeyi bırakıyoruz. **Toplam 12 damla.**

**Kütle ölçümleri (yüzde ağırlık kaybı hesabı rapor için):**

| Aşama | Kütle |
|-------|-------|
| Jel (ıslak) | 10.9 g |
| 100 °C, 24 h kurutma sonrası (su uçtu) | 0.576 g |
| 500 °C, 1 h calcination sonrası → silica nanoparticle | 0.394 g |

## 2) PVA çözeltisi — Spin coating, viskozite, contact angle

- 0.5 g PVA ve 1 g PVA saf suda çözüldü (spin coating, viskozite ölçümü, contact angle için).
- **Spin coating** (0.5 g PVA ile), 4 test, FTO/ITO cam, 3 damla:

| Test | RPM | Süre |
|------|-----|------|
| 1 | 500 | 5 s |
| 2 | 500 | 10 s |
| 3 | 800 | 10 s |
| 4 | 800 | 5 s |

- Gözlem: "Süre etkilemiyor." Hoca notu: bu parametrelerden birinin etkisi işe yaramıyor — **geçen sene finalde sorulmuş, araştırılacak.**

## 3) Contact angle (temas açısı)

Yüzeylere 1 damla saf su damlatıldı:
- Çok silikalı yüzey, az silikalı yüzey, grafit yüzey kâğıt, nanofiber kâğıt.
- Silika arttıkça angle azalıyor → hydrophilic (hidrofilik) oluyor.
- Nanofiber kâğıt: suyu direkt emmiyor → hydrophobic (hidrofobik).
- **Rapor sorusu:** "Silikayla superhydrophobic bir yapı yapmak istiyorum; yağmur suyu gelince akıp gitsin. Ne yapmam lazım?"

## 4) Ostwald viskozimetresi deneyi

- U-tüp; C, A, B işaretleri. Sıvı C'ye gelene kadar dolduruluyor; balon sıkılarak sıvı A–B arasına çekiliyor, akış süresi ölçülüyor.
- Su referans: $V = 5\ \text{ml} = 5\ \text{cm}^3$, $t_0 = 1.45\ \text{s}$, $\rho_0 = 1\ \text{g/cm}^3$, $\eta_0 = 0.89\ \text{mPa·s}$

$$\eta = \eta_0 \frac{\rho\, t}{\rho_0\, t_0}$$

| Numune | Kütle (5 ml) | $\rho = m/V$ | Akış süresi $t$ |
|--------|--------------|--------------|-----------------|
| Silika çok | 5.1332 g | 1.02664 g/cm³ | 8.34 s |
| Silika az | 5.1293 g | 1.02586 g/cm³ | 8.06 s |

→ Formülde yerine koyup hesaplanacak (rapor).
