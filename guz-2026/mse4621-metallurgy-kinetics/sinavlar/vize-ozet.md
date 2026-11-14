# MSE4621 Vize Özeti

**Vize:** 20.11.2026 Cuma 15:30–16:45 · KMB-317
**Kaynak:** Prof. Dr. Miray Çelikbilek Ersundu, ders slaytları ([part2](../kaynaklar/part2-metallugy-kinetics-lecture-notes.pdf), 82 slayt; ilk 71 slayt Part 1 ile aynı)

> Bu dosya blok blok çalıştıkça doldurulur. Hangi konunun hangi haftada işlendiği repoda yok; bu yüzden haftalık not yerine konu bloklarıyla ilerliyoruz.

| Blok | Konu | Slayt | Durum |
|---|---|---|---|
| 1 | Kinetik nedir, reaction rate | 5–15 | ✅ |
| 2 | Reaksiyonların sınıflandırılması | 16–23 | ✅ |
| 3 | 0., 1., 2., n. derece reaksiyonlar, half-life | 24–49 | ✅ |
| 4 | Reaksiyon derecesini bulma yöntemleri | 50–66 | ⏳ |
| 5 | Molecularity; reversible, consecutive, parallel reactions | 67–71 | ⏳ |
| 6 | Sıcaklık etkisi: Arrhenius, activation energy | 72–82 | ⏳ |

---

## Blok 1 — Kinetik ve reaction rate (reaksiyon hızı)

### Termodinamik vs kinetik

| Soru | Cevaplayan |
|---|---|
| Reaksiyon olur mu, denge nerede? | **Thermodynamics** (sadece başlangıç ve son hal) |
| Ne kadar hızlı, hangi mekanizmayla? | **Kinetics** (yol + süre) |

- $\Delta G^\circ \ll 0$ olup reaksiyonun ilerlememesi çelişki değildir: termodinamik olarak mümkün, kinetik olarak yavaş.
- Reaktörde kalış süresi (residence time) ve reaktör boyutu kinetik verilerle belirlenir. Reaksiyon hızlıysa termodinamik veri yeter, yavaşsa kinetik veri de gerekir.

### Hız tanımı

$$r = -\frac{dc}{dt}, \qquad x = C_0 - C, \qquad r = \frac{dx}{dt}$$

- $r$: reaksiyon hızı [mol·L⁻¹·s⁻¹], her zaman pozitiftir (reaktan için eksi işaret bu yüzden var)
- $c$, $C$: konsantrasyon [mol/L]; $C_0 = a$: başlangıç konsantrasyonu
- $x$: reaksiyona girmiş miktar [mol/L]

### Rate law ve rate constant (hız sabiti)

$$r = k\,c_A^{\alpha}c_B^{\beta}, \qquad k = f(T)$$

- $k$ yalnızca sıcaklığa (ve katalizöre) bağlıdır, konsantrasyona bağlı değildir.

**Stokiyometri:** $aA + bB \rightarrow cC$ için $\dfrac{-r_A}{a} = \dfrac{-r_B}{b} = \dfrac{r_C}{c}$
Örnek: $2A + B \rightarrow 4C$, $-r_A = 0.6$ ise $-r_B = 0.3$, $r_C = 1.2$ mol·L⁻¹·s⁻¹.

### Hızı etkileyen faktörler

1. Konsantrasyon (aslında aktivite)
2. Sıcaklık
3. Fiziksel durum / yüzey alanı (kızgın çivi O₂'de hafifçe parlar, aynı kütlede çelik yünü alev alır)
4. Catalyst (katalizör) / inhibitor (önleyici)
5. Uyarma: ışık, UV, radyasyon

---

## Blok 2 — Sınıflandırma

| Faz | Molekülarite | Derece | Mekanizma | Kataliz |
|---|---|---|---|---|
| Homojen | Bir moleküllü | 0 | Dönüşümsüz (irreversible) | Katalitik |
| Heterojen | İki moleküllü | 1 | Tersinir (reversible) | Katalitik olmayan |
| | Çok moleküllü | 2 | Paralel | |
| | | n | Seri (consecutive) | |

Sınıflar birbirini dışlamaz.

- **Homogeneous:** tek faz, ör. $\text{CO}_{(g)} + \tfrac12\text{O}_{2(g)} = \text{CO}_{2(g)}$
- **Heterogeneous:** en az iki faz, ör. $\text{C}_{(s)} + \text{O}_{2(g)} = \text{CO}_{2(g)}$, Boudouard reaksiyonu
- **Tüm pirometalurjik reaksiyonlar heterojendir.** Faz çiftleri: S-S, S-L, S-G, L-L, L-G

| Faz çifti | Örnek (slayt 20) |
|---|---|
| Gas–gas | H₂ + I₂ ⇌ 2HI |
| Gas–liquid | suyun buharlaşması |
| Liquid–liquid | yağ-su ayrışması |
| Gas–solid | CVD ile Si film |
| Liquid–solid | Cu'nun deniz suyunda korozyonu |
| Solid–solid | Cu–Al alaşımında CuAl₂ çökelmesi |

**Reaction order (reaksiyon derecesi):** rate law'da konsantrasyonun üssü. Başlangıç konsantrasyonları eşitse:

$$r = \frac{dx}{dt} = k(a-x)^n, \qquad n = \alpha+\beta+\gamma$$

Derece **deneyle belirlenir**, stokiyometrik katsayıdan okunmaz.

---

## Blok 3 — Derecelere göre hız denklemleri

Her derecede aynı yol izlenir: rate law → integrasyon ($z = a-x$, $dz = -dx$; $t=0$'da $x=0$) → $k$ → $x=a/2$ koyarak $t_{1/2}$.

### 0. derece

$$\frac{dx}{dt} = k_0 \;\Rightarrow\; x = k_0 t, \qquad t_{1/2} = \frac{a}{2k_0}$$

- Hız konsantrasyondan bağımsızdır. Kontrolü termal enerji ya da yüzey alanı yapar (ör. sıcak metal yüzeyinde NH₃ bozunması).
- $C$–$t$ grafiği doğrusaldır. $t_{1/2} \propto a$.

### 1. derece

$$\frac{dx}{dt} = k_1(a-x) \;\Rightarrow\; \ln\frac{a}{a-x} = k_1 t, \qquad k_1 = \frac{2.303}{t}\log\frac{C_0}{C}$$

$$t_{1/2} = \frac{0.693}{k_1}$$

- **$t_{1/2}$ başlangıç konsantrasyonundan bağımsızdır.** $n$ tane half-life geçtiğinde kalan oran $(1/2)^n$ olur. Örneğin %75 dönüşüm = 2 $t_{1/2}$.

### 2. derece

$$\frac{dx}{dt} = k_2(a-x)^2 \;\Rightarrow\; \frac{1}{a-x}-\frac1a = k_2 t, \qquad k_2 = \frac1t\,\frac{x}{a(a-x)}$$

$$t_{1/2} = \frac{1}{k_2\,a}$$

- $t_{1/2} \propto 1/a$.
- **Kısayol:** $t \propto \dfrac{x}{a-x}$. İki farklı dönüşüm oranı için süreler oranla bulunur.

### n. derece ($n \ne 1$)

$$k_n = \frac{1}{(n-1)t}\left[\frac{1}{(a-x)^{n-1}}-\frac{1}{a^{n-1}}\right], \qquad t_{1/2} = \frac{2^{n-1}-1}{(n-1)k_n a^{n-1}}$$

- 3. derece: $t_{1/2} = \dfrac{3}{2k_3a^2}$

### 🗂️ Formül kağıdı tablosu

| $n$ | İntegre form | Doğrusal grafik | $t_{1/2}$ | $t_{1/2}$ vs $a$ | $k$ birimi |
|---|---|---|---|---|---|
| 0 | $x = k_0t$ | $C$–$t$ | $a/2k_0$ | ∝ $a$ | M·s⁻¹ |
| 1 | $\ln\frac{a}{a-x} = k_1t$ | $\ln C$–$t$ | $0.693/k_1$ | bağımsız | s⁻¹ |
| 2 | $\frac{1}{a-x}-\frac1a = k_2t$ | $1/C$–$t$ | $1/k_2a$ | ∝ $1/a$ | M⁻¹·s⁻¹ |
| n | genel form | $1/C^{n-1}$–$t$ | $\frac{2^{n-1}-1}{(n-1)k_na^{n-1}}$ | ∝ $a^{1-n}$ | M$^{1-n}$·s⁻¹ |

Genel kural: $t_{1/2} \propto a^{\,1-n}$. Bu kural Blok 4'teki half-life yönteminin temelidir.

### Çözümlü örnekler

**Örnek 1: C-14 (slayt 38)**
- Verilenler: 1. derece, $t_{1/2} = 5730$ yıl
- İstenen: $k$
- Çözüm: $k = 0.693/5730 = 1.21\times10^{-4}$ yıl⁻¹ $= 3.83\times10^{-12}$ s⁻¹
- Birim kontrolü: 1. derecede $k$ = zaman⁻¹ ✓

**Örnek 2: Uranyum (slayt 48)**
- Verilenler: 1. derece, $t_{1/2} = 4.51\times10^9$ yıl
- İstenen: $k$ ve %75 bozunma süresi (gün)
- Çözüm:
  - $k = 0.693/(4.51\times10^9) = 1.54\times10^{-10}$ yıl⁻¹
  - %75 bozunmada $a-x = 0.25a$, dolayısıyla $t = \dfrac{1}{k}\ln 4 = \dfrac{1.386}{1.54\times10^{-10}} = 9.02\times10^9$ yıl
  - Gün cinsinden: $9.02\times10^9 \times 365 = 3.29\times10^{12}$ gün
  - Kısayol: %75 = 2 half-life → $2 \times 4.51\times10^9 = 9.02\times10^9$ yıl ✓
- Not: Slaytta $k = 1.532\times10^{-10}$ ve sonuç $330.4\times10^{10}$ gün yazıyor. Fark yuvarlamadan kaynaklanıyor, iki sonuç da yaklaşık $3.3\times10^{12}$ gün.

**Örnek 3: 2. derece (slayt 49)**
- Verilenler: $a = 0.4$ mol/L, $t = 80$ dk $= 4800$ s'de %30 dönüşüm
- İstenen: $k_2$ ve %80 dönüşüm süresi (s)
- Çözüm:
  - $x = 0.3\times0.4 = 0.12$, $a-x = 0.28$
  - $k_2 = \dfrac{1}{4800}\cdot\dfrac{0.12}{0.4\times0.28} = 2.232\times10^{-4}$ L·mol⁻¹·s⁻¹
  - %80 dönüşüm: $x = 0.32$, $a-x = 0.08$
  - $t = \dfrac{0.32}{2.232\times10^{-4}\times0.4\times0.08} = 4.48\times10^4$ s (≈ 12.4 saat)
  - Kısayol: $\dfrac{t_2}{t_1} = \dfrac{0.8/0.2}{0.3/0.7} = 9.33$, buradan $t_2 = 9.33\times4800 = 4.48\times10^4$ s ✓
- Birim kontrolü: $\dfrac{1}{\text{s}}\cdot\dfrac{\text{M}}{\text{M}^2} = $ M⁻¹·s⁻¹ ✓
- ⚠️ Slayttaki ve tekrar notundaki "liter·second/mol" birimi hatalı. Doğrusu L·mol⁻¹·s⁻¹.

---

## Sınavda çıkabilir

- Verilen $t_{1/2}$'den 1. derece $k$'yı hesaplamak ve %X dönüşüm süresini bulmak (C-14, uranyum tipi)
- 2. derece reaksiyonda bir dönüşüm oranından $k$'yı bulmak, sonra başka bir dönüşüm oranı için süreyi hesaplamak
- Stokiyometriye göre türlerin hızlarını birbirine çevirmek ($-r_A/a = r_C/c$)
- $t_{1/2}$'nin başlangıç konsantrasyonuna bağlılığından reaksiyon derecesini yorumlamak (0: ∝ $a$, 1: bağımsız, 2: ∝ $1/a$)
- Homojen/heterojen ayrımı ve neden tüm pirometalurjik reaksiyonların heterojen olduğu
