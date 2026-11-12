# MSE3271 Cheat Sheet: Lecture 1 + Lecture 2

> Kaynak: hocanın slaytları (L1, L2). L3 ile çakışan formüller ayrıca işaretlendi.
> Kullanım: Soruyu oku → **hangi şablon?** → şablonu doldur.

---

## A. KAVRAM ŞABLONLARI ("Bu hangisi?" soruları)

### Şablon A1: Metrolojinin 3 dalı
> Soru: "Bu ölçüm yanlış olursa **kim** zarar görür?"

| Zarar gören | Dal | Anahtar kelimeler |
|---|---|---|
| Tüm sistemin referansı | **Scientific** | standart yaratır/korur, en üst seviye · BIPM, NIST, NPL, UME · atomic clock |
| Üretilen ürün | **Industrial** | cihaz kalibrasyonu, CMM, tolerans · ISO 9001 / ISO 17025 |
| Tüketici / halk | **Legal** | kanunla denetlenir · benzin pompası, market terazisi, taksimetre, hazır ambalaj |

### Şablon A2: Measurement procedure'ın 6 bileşeni
`Principle → Method → Model → Steps → Uncertainty → SOP`

| Bileşen | Sorduğu soru | Örnek |
|---|---|---|
| **Principle** | Hangi **fizik**? | thermoelectric effect (sıcaklık), Josephson effect (voltaj) |
| **Method** | Hangi **mantık**? direct / indirect | cetvel = direct · $V=abc$ = indirect |
| **Model** | Hangi **formül**? | $V = a\cdot b\cdot c$, $\rho = m/V$ |
| **Steps** | Nasıl **uygulanır**? | hazırlık → kalibrasyon → ölç → kaydet |
| **Uncertainty** | Ne kadar **güvenilir**? | ±0.1 °C |
| **SOP** | **Belgelenmiş** standart hali | ilaç / sağlık sektörü |

### Şablon A3: Base mı, derived mı?
> Test: Birimi aşağıdaki 7 birimden **biri mi**? → Evet: **base**. Hayır: **derived**.

| Base quantity | Unit | Sembol | Boyut |
|---|---|---|---|
| length | metre | m | L |
| mass | kilogram | kg | M |
| time | second | s | T |
| electric current | ampere | A | I |
| thermodynamic temperature | kelvin | K | Θ |
| amount of substance | mole | mol | N |
| luminous intensity | candela | cd | J |

Sık sorulan derived'lar: force N = kg·m/s² · pressure Pa = N/m² · energy J = N·m · power W = J/s · frequency Hz = 1/s · density kg/m³ · velocity m/s
Supplementary (boyutsuz): **rad** (düzlem açı, m/m) · **sr** (katı açı, m²/m²)

**Ön ekler:** G 10⁹ · M 10⁶ · k 10³ · m 10⁻³ · µ 10⁻⁶ · n 10⁻⁹ · p 10⁻¹²

### Şablon A4: Value kavramları
| Terim | Tanım (kısa) | Bilinir mi? |
|---|---|---|
| **Value** | sayı × birim (5.2 m) | ✔ |
| **True value** | tanıma tam uyan ideal değer | ✘ hiçbir zaman |
| **Conventional true value** | amaca yeterli belirsizlikle "doğru" **kabul edilen** değer | ✔ (ör. referans standardın değeri, CODATA $N_A$) |

### Şablon A5: Ölçümün aktörleri
| Terim | = | Örnek |
|---|---|---|
| **Measurand** | ölçmek **istediğimiz** nicelik | 20 °C'deki su numunesinin buhar basıncı |
| **Influence quantity** | ölçmediğimiz ama **sonucu etkileyen** | mikrometrenin sıcaklığı |
| **Measurement signal** | measurand'ı temsil eden sinyal | basınç transducer'ının elektrik çıkışı |

### Şablon A6: Error türü
> Soru: Tekrar ölçünce hata **aynı mı kalıyor**?

| | **Systematic** | **Random** |
|---|---|---|
| Davranış | aynı yön, aynı miktar | her seferinde farklı |
| Bozduğu | **accuracy** | **precision** |
| Tekrar ölçmek | işe yaramaz | ortalama alınca azalır |
| Çözüm | **correction** / kalibrasyon | çok ölçüm + ortalama |
| Örnek | terazi hep +0.1 kg, sıfırı kaymış kumpas | paralaks, el titremesi, rüzgâr |

### Şablon A7: Accuracy / Precision (4 kutu)
|  | **Precise** (σ küçük) | **Imprecise** (σ büyük) |
|---|---|---|
| **Accurate** (ortalama ≈ true) | 🎯 Olimpik okçu | Kızılderili: merkez etrafında dağınık |
| **Inaccurate** (ortalama ≠ true) | Robin Hood'un adamı: sıkı grup, merkez dışı | Taş devri adamı |

> Karar: ① ortalama true'ya yakın mı? → accuracy. ② değerler birbirine yakın mı? → precision.

### Şablon A8: Repeatability / Reproducibility
> Soru: Koşullardan **herhangi biri değişti mi**?

| **Repeatability** (hiçbir şey değişmedi) | **Reproducibility** (en az biri değişti) |
|---|---|
| aynı prosedür, gözlemci, cihaz, koşul, yer, kısa süre | farklı principle, method, gözlemci, cihaz, referans standard, yer, kullanım koşulu, zaman |
| | ⚠ değişen koşul **belirtilmeli** |

### Şablon A9: Standard (etalon) hiyerarşisi
```
BIPM (Sèvres, Paris)
  └─ Primary standard   → en yüksek kalite, başka standarda referans vermez (NMI: NIST, UME)
      └─ Secondary standard → primary'ye karşı kalibre
          └─ Working standard  → günlük kullanım, secondary'ye karşı periyodik kalibre
              └─ Lab / sanayideki cihazlar
```
Diğer türler: **National** (ülkede yasal temel) · **Reference** (bir kurumdaki en iyi standart) · **Transfer** (standartları karşılaştırmak için aracı)
⚠ Kural: Aşağı indikçe uncertainty **büyür**; hiçbir seviye altındaki seviyeden daha küçük uncertainty'ye sahip olamaz.

### Şablon A10: Calibration ↔ Traceability
| | **Calibration** | **Traceability** |
|---|---|---|
| Ne? | cihazın gösterdiği ile referans standard arasındaki ilişkiyi kurmak | sonucu ulusal/uluslararası standarda **kesintisiz kalibrasyon zinciriyle** bağlamak |
| Kapsam | tek bir halka | tüm zincir |
| Şart | — | her halkada: belirtilmiş **uncertainty** + belgelenmiş prosedür + yetkinlik + geçerlilik süresi |
| Örnek | teraziyi bilinen kütlelerle kontrol etmek | aşı dolabı termometresi → referans termometre → ulusal standart (ITS) |

Bir halka eksikse **traceability tower** çöker.

### Şablon A11: Uluslararası sistem
```
Metre Convention (1875, 17 ülke, diplomatik antlaşma)
 └─ CGPM: genel konferans, üye devletlerin delegeleri; SI'ı kabul eder
     └─ CIPM: 18 kişilik komite, BIPM'i denetler
         ├─ CC: Consultative Committees, teknik danışma
         └─ BIPM: Sèvres'teki laboratuvar; görevi dünya çapında ölçüm birliği
Regional (RMO): EURAMET, APMP, COOMET, SIM, AFRIMETS, GULFMET
National (NMI): UME (TR), NIST (ABD), NPL (UK)
CIPM MRA: NMI sertifikalarının karşılıklı tanınması
```

---

## B. HESAP ŞABLONLARI

> Her soruda: **Verilenler → İstenen → Formül → Çözüm → Birim kontrolü**

### Şablon B1: Error ve % error
$$E = x_{\text{ölçülen}} - x_{\text{true}}$$
$$\%\,\text{error}_{\text{(L2 slaytı)}} = \frac{x_{\text{true}} - x_{\text{ölçülen}}}{x_{\text{true}}}\times 100 \qquad E_r{}_{\text{(L3 slaytı)}} = \frac{x_i - x_t}{x_t}\times 100$$
- $x_{\text{true}}$ ($x_t$): true / conventional true value [ölçülen birimiyle aynı]
- $x_{\text{ölçülen}}$ ($x_i$): ölçülen değer

⚠ İki slayt **işaret** olarak ters. Büyüklük aynı. Hangi formülü kullandığını yaz.

```
Verilen:  x_true = ____  , x_ölç = ____
E       = x_ölç − x_true                      = ____ [birim]
% error = (x_true − x_ölç)/x_true × 100       = ____ %   (boyutsuz)
```

### Şablon B2: Systematic error ve correction
$$\text{Sist. error} \approx \bar{x} - x_{\text{true}} \qquad \text{Correction} = -\,\text{Sist. error} \qquad \text{Corrected} = \text{Uncorrected} + \text{Correction}$$
```
x̄          = Σx / n                = ____
Sist. error = x̄ − x_true            = ____
Correction  = −(Sist. error)         = ____
Corrected   = okunan + Correction    = ____
Yorum: σ küçük mü (precise?) · x̄ ≈ true mu (accurate?)
```

### Şablon B3: Ortalama, sapma, precision
$$\bar{x} = \frac{\sum x_i}{n} \qquad \sigma = \sqrt{\frac{\sum (x_i-\bar{x})^2}{N}}$$
- L4-5 slaytı varyansı **N'ye** bölüyor (population). Örneklem için $s$'de payda $n-1$ olur. Soru "sample" diyorsa $n-1$ kullan.
- Ortalama sapma (L2): $\dfrac{\sum |x_i-\bar{x}|}{n}$

### Şablon B4: Uncertainty
$$u_A = \frac{s}{\sqrt{n}}\ \text{(Type A: tekrarlı ölçümlerin istatistiği)} \qquad u_B:\ \text{sertifika, üretici spek., deneyim}$$
$$u_c = \sqrt{u_1^2 + u_2^2 + \dots}\quad\text{(root-sum-square)} \qquad U = k\cdot u_c,\ \ k=2 \Rightarrow \%95$$
$$\text{Relative uncertainty} = \frac{U}{x}\times 100$$
- L3: Type A'nın standard uncertainty'si = "standard deviation of the mean". $s/\sqrt{n}$ budur.

```
Type A:  s = ____ , n = ____  →  u_A = s/√n = ____
Type B:  (kaynak: ____)      →  u_B = ____
u_c = √(u_A² + u_B²)          = ____
U   = 2·u_c                   = ____
Sonuç:  x = ____ ± ____ [birim]  (k = 2, ≈ %95)
        aralık: [x − U , x + U]
```

### Şablon B5: Tolerance
$$\text{Tolerance range} = \text{Upper limit} - \text{Lower limit}$$
```
Nominal = ____ , tolerans ± ____
Upper = nominal + t = ____ ;  Lower = nominal − t = ____
Range = Upper − Lower = ____
Parça ölçüsü ____ → [Lower, Upper] içinde mi?  KABUL / RED
```
⚠ **Tolerance ≠ Uncertainty.** Tolerance tasarımın **izin verdiği** aralık, uncertainty ölçümün **şüphesi**.

---

## C. KARIŞTIRILAN ÇİFTLER (tek satırda)

| A | B | Fark |
|---|---|---|
| Accuracy | Precision | true'ya yakınlık ↔ birbirine yakınlık |
| Systematic | Random | sabit yön ↔ dağınık |
| Repeatability | Reproducibility | aynı koşul ↔ değişen koşul |
| Error | Uncertainty | tek bir sayı farkı (bilinemez) ↔ şüphe aralığı (tahmin edilir) |
| Principle | Method | hangi fizik ↔ hangi mantık |
| True value | Conventional true value | bilinemez ↔ kabul edilen |
| Calibration | Traceability | tek halka ↔ kesintisiz zincir |
| Primary | Working standard | en iyi, referanssız ↔ günlük, periyodik kalibre |
| Tolerance | Uncertainty | tasarım izni ↔ ölçüm şüphesi |
| Type A | Type B | istatistik ↔ başka bilgi (sertifika, üretici) |

---

## D. EZBER KUTUSU
- 7 base unit: **m · kg · s · A · K · mol · cd**
- Metre Convention: **1875**, **17** ülke · CIPM: **18** kişi · BIPM: **Sèvres / Paris**
- Expanded uncertainty: **k = 2 → %95**
- NASA Mars sondası: İngiliz ↔ metrik birim çevrilmedi → ~60 mil sapma
- Egyptian cubit: firavunun dirseğinden orta parmak ucuna, ~MÖ 3000
