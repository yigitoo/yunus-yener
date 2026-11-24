# Hafta 9 · Korozyon Türleri I

Kuru ve ıslak korozyon, uniform ve lokal korozyon, galvanik korozyon ve alan oranı, aralık (crevice), filiform ve çukur (pitting) korozyonu, PREN.

*Kaynak: Hafta 9 çalışma kâğıdı (kaynaklar/hafta09-worksheet-tr.pdf) ve ders slaytları.*

## 1. Kuru ve ıslak korozyon

| | Kuru | Islak |
|---|---|---|
| Ortam | Sıcak gazlar, sıvı su yok | İletken sıvı: su, nem filmi, toprak |
| Mekanizma | Doğrudan kimyasal tepkime | Anot ve katotlu elektrokimyasal hücre |
| Ürün | Saldırının olduğu yerde tabaka (oksit, Hafta 11) | Pas, anottan uzakta da çökebilir |

Bu haftanın bütün türleri **ıslaktır**: anot ve katodun çalışması için elektrolit gerekir.

## 2. Uniform ve lokal korozyon

- **Uniform:** Tüm yüzeyde eşit kayıp; anot ve katotlar sürekli yer değiştirir. Tonaj olarak en büyük ama en az tehlikeli; mm/y ile kolay tahmin edilir.
- **Lokal:** Anot bir yerde sabit kalır, kayıp küçük bir alanda toplanır. Ortalama kayıp küçükken bir çukur duvarı delebilir. **Önemli olan en derin noktadır** (oyuklanma faktörü, Hafta 7).

## 3. Galvanik korozyon

**Üç koşul:** (1) iki farklı metal, (2) elektriksel temas, (3) ortak elektrolit.

- **Aktif** metal anottur, tek başına olduğundan daha hızlı korozyona uğrar. **Soy** metal katottur, korunur.
- Hasar birleşimin hemen yanında yoğunlaşır.

### Galvanik seri (deniz suyu, E_corr V vs SCE, yaklaşık)

| Aktif (anodik) ↑ | | Soy (katodik) ↓ | |
|---|---|---|---|
| Magnezyum | −1.60 | Bakır | −0.33 |
| Çinko | −1.00 | 70/30 bakır-nikel | −0.20 |
| Alüminyum alaşımları | −0.85 | Paslanmaz 316 (pasif) | −0.05 |
| Karbon çeliği, dökme demir | −0.65 | Titanyum | 0.00 |
| Paslanmaz 316 (aktif) | −0.50 | Grafit | +0.25 |
| Pirinçler | −0.35 | | |

- Mühendisler emf tablosunu değil galvanik seriyi kullanır: emf tablosu 1 M kendi iyonundaki saf metaller içindir; galvanik seri gerçek alaşımların gerçek ortamda ölçülmüş değerleridir.
- Pasif alaşımlar iki kez yer alır (aktif ve pasif).
- Alüminyumun oksit filmi vardır ama deniz suyunda klorür filmi bozar; Al yine de çelik, bakır ve paslanmaza karşı **anottur**.
- Serideki uzaklık **eğilimi** verir, **hızı** değil. Hız ayrıca alan oranına, katottaki O₂ beslemesine ve iletkenliğe bağlıdır.

### Evans diyagramıyla galvanik çift

A (aktif) ile B (soy) birleşince O₂ artık B üzerinde de indirgenir → toplam katodik doğru sağa kayar:
- Yeni karışık potansiyelde **A daha hızlı** korozyona uğrar.
- B kendi E_corr'unun altına iner → katodik polarize olur, **korozyonu durur** (katodik koruma).
- B'nin alanı ↑ → katodik doğru daha da sağa → A'nın saldırısı ↑

### Alan oranı

$$I_a = I_c \qquad i_a = i_c\,\frac{A_c}{A_a}$$

- Katotta kullanılan her elektron anottan gelmek zorundadır.
- **Küçük anot + büyük katot = çok hızlı saldırı.** Anodu asla küçük parça yapmayın.
- LaQue deneyi (deniz suyu): bakır levhadaki çelik perçinler yenip biter; çelik levhadaki bakır perçinler sadece hafif, eşit paslanma yapar.
- Tek metal boyanacaksa **katot (soy metal)** boyanır. Anot boyanırsa her boya kusuru, büyük bir katoda karşı minicik bir anot olur.

### Üç vaka

| Vaka | Ne oldu? | Ders |
|---|---|---|
| **HMS Alarm** | Bakır kaplamalı gemide demir çiviler (küçük anot) hızla korozyona uğradı, levhalar gevşedi. Kahverengi kâğıtla yalıtılan çiviler daha az hasar gördü. | Yalıtım hücreyi kırar |
| **Özgürlük Heykeli** | Tuzlu nemde dövme demir iskelet anot, bakır kabuk katot oldu. Eiffel'in şellaklı asbest yalıtımı bir asırda bozuldu. Yeni çubuklar 316L: galvanik seride bakıra yakın, itici güç neredeyse yok. | Seride yakın metaller seç |
| **Guadalajara** | Çinko kaplı bakır su borusu: çinko tükenince bakır, nemli toprakta çelik benzin hattıyla karşılaştı; çelik anot oldu ve delindi. | Sorular: hangi metal anot, elektrolit var mı, yanında ne var? |

## 4. Farklı havalanma

Aynı metalin bir yerinde daha çok O₂ varsa **oksijence fakir kısım anot** olur (Hafta 3). Aralık ve filiform korozyonunu başlatan mekanizma budur.

## 5. Aralık korozyonu (crevice)

Durgun çözeltiyle dolu dar bir boşlukta (≈ 0.025–0.1 mm) saldırı: contalar, cıvata başları, bindirme birleşimler, tortular. **İkinci bir metal gerektirmez**: fark metalde değil ortamdadır (O₂, pH, Cl⁻).

**Asit cebine dönüşme adımları (otokatalitik):**
1. Aralık içindeki O₂ tükenir, katodik reaksiyon dışarı kayar.
2. İçeride metal çözünmeye devam eder: $M \rightarrow M^{n+} + ne^-$
3. Pozitif yük birikir, aralığa $Cl^-$ göç eder.
4. Hidroliz: $MCl + H_2O \rightarrow MOH + HCl$ → pH 1–3'e düşer.
5. Asit ve Cl⁻ pasif filmi çökertir → çözünme hızlanır → süreç kendini besler.

- **Paslanmaz çelik ve Al daha çok risk altında:** pasif filme dayanırlar; içerideki asit ve Cl⁻ onları pasif aralığın dışına çıkarır → küçük aktif anot, büyük pasif katot.
- **Önlemler:** boşluk bırakmamak (cıvata/perçin yerine kaynak), su emmeyen contalar ve sızdırmazlık malzemeleri, temiz yüzeyler, daha çok Mo içeren alaşımlar.

## 6. Filiform korozyon

- **Nerede:** Al, çelik ve Mg üzerinde **boya veya vernik altında**, tuzla birlikte **%65–95 bağıl nemde**, bir kaplama kusurundan başlar.
- **Yapı:** Aktif, asidik **kafa** (ön ucu oksijence fakir → **anot**) + kuru, gözenekli **kuyruk**. O₂ kuyruktan gelir ve kafanın arkasında indirgenir (katot).
- **Hep ileriye büyür:** metal yalnızca oksijence fakir ön uçta çözünebilir; arka kısım katot olur ve kurur.
- **İplikler birbirini kesmez:** başka bir ipliğin kuyruğu kuru ve oksijence zengindir, kafa oraya ilerleyemez.
- **Önlem:** boyamadan önce iyi ön işlem (dönüşüm kaplaması), kesik kenarları kapatmak.

## 7. Çukur korozyonu (pitting)

Aksi hâlde **pasif** bir yüzeyde, çoğunlukla klorürde küçük ve derin delikler. Çukur, kendi oluşturduğu bir aralıktır.

### Çukur nerede başlar?

Çalışma kâğıdına göre üç yol vardır (kesin):

1. **Mekanik hasar:** filmin çizilmesi
2. **İkinci fazlar:** MnS inklüzyonları, ara bileşikler
3. **Ortam:** Cl⁻, O₂ ve tortulardaki yerel farklar

Derste bu konu bir slaytta üç sütun hâlinde anlatıldı. Fotoğraf bulanık olduğu için ayrıntıları kesin okunamadı; seçilebilen kadarı (doğrulanmadı):

| 1 · Mekanik hasar | 2 · İkinci fazlar | 3 · Ortam |
|---|---|---|
| Çizik filmi kaldırır | İnklüzyonlar, ara bileşikler, segregasyon | Cl⁻, O₂, tortulardaki yerel farklar |
| Açıkta kalan metal = anot | Çoğu zaman tane sınırları boyunca | "The film dissolves…" (devamı okunamadı) |
| Çevredeki pasif yüzey = katot | Filmde yerel anot veya zayıf nokta | (okunamadı) |

### Büyüyen çukurdaki tepkimeler (çelik)

- **İçeride (anot):** $Fe \rightarrow Fe^{2+} + 2e^-$
- **Dışarıda (katot):** $\tfrac{1}{2}O_2 + H_2O + 2e^- \rightarrow 2OH^-$
- **Hidroliz:** $FeCl_2 + 2H_2O \rightarrow Fe(OH)_2 + 2HCl$
- **Pas kapağı:** $Fe^{2+} \rightarrow Fe(OH)_2 \rightarrow Fe(OH)_3$

- İçerideki pozitif yük Cl⁻ çeker, hidroliz HCl üretir → **pH ≈ 6'dan 2–3'e düşer** → film onarılamaz, çözünme hızlanır.
- **Fe(OH)₃ kapağı:** çukurun ağzını kapatır, asidi içeride tutar ve çukuru gizler.
- **Küçük anot (çukur) + büyük pasif katot** → çok yüksek yerel akım yoğunluğu.

### Çukur şekilleri (ASTM G46)

Dar-derin, eliptik, geniş-sığ, yüzey altı, alttan oyan, mikroyapısal. **En tehlikelileri dar-derin ve alttan oyan:** küçük bir ağız büyük bir boşluğu gizler, görmesi zordur, duvarı beklenmedik biçimde deler.

### Aralık ve çukur karşılaştırması

- **Aynı:** asitleşme ve Cl⁻ göçü saldırıyı otokatalitik yapar.
- **Farklı:** aralık, var olan bir boşlukta O₂ tükenmesiyle başlar; çukur, açık yüzeyin zayıf noktasında film bozulmasıyla başlar.
- **Aralık daha kolay başlar** (geometri hazır): daha düşük sıcaklık ve klorürde.
- Aralığa dayanan alaşım çukura da dayanır; **tersi doğru değildir**.

## 8. PREN (çukurlaşma direnci eşdeğer sayısı)

$$\text{PREN} = \%Cr + 3.3\,\%Mo + 16\,\%N$$

| Kalite | Tür | PREN |
|---|---|---|
| 304 | östenitik, Mo yok | ≈ 19 |
| 316L | östenitik, ~%2 Mo | ≈ 25 |
| 904L | süper östenitik, yüksek Mo | ≈ 35 |
| 2205 | dupleks, yüksek Cr ve N | ≈ 35 |
| 2507 | süper dupleks | ≈ 42 |

- Yüksek PREN → yüksek kritik çukurlaşma sıcaklığı (CPT).
- **Deniz suyu için pratik kural: PREN ≥ 40** → ılık deniz suyunda 2507.
- 316, kıyıda 304'ün yerini aldı: %2 Mo pasif filmi klorüre karşı güçlendirir.
- PREN sadece bir **sıralama aracıdır**: yüzey durumu, kaynak, ısıl işlem, sıcaklık ve aralıklar da gerçek davranışı belirler.

## Bilinmesi gereken tepkimeler

| Nerede | Tepkime |
|---|---|
| Anot (metal çözünür) | $M \rightarrow M^{n+} + ne^-$; $Fe \rightarrow Fe^{2+} + 2e^-$ |
| Nötr, havalı suda katot | $\tfrac{1}{2}O_2 + H_2O + 2e^- \rightarrow 2OH^-$ |
| Asitte katot | $2H^+ + 2e^- \rightarrow H_2$ |
| Aralık / çukurda hidroliz | $MCl + H_2O \rightarrow MOH + HCl$; $FeCl_2 + 2H_2O \rightarrow Fe(OH)_2 + 2HCl$ |
| Pas kapağı | $Fe^{2+} \rightarrow Fe(OH)_2 \rightarrow Fe(OH)_3$ |

::: sinav
## Sınavda çıkabilir

- Galvanik korozyonun üç koşulu; galvanik seriden anodu bulma; neden emf tablosu değil galvanik seri.
- Alan oranı: bakır levhada çelik perçin / çelik levhada bakır perçin; hangisi boyanmalı?
- Aralık korozyonunun otokatalitik adımları ve hidroliz tepkimesi; neden ikinci metal gerekmez.
- Çukurun başladığı üç yol (mekanik hasar, ikinci fazlar, ortam) ve çukurdaki tepkimeler; pH neden düşer.
- PREN hesabı ve paslanmaz kalite seçimi (deniz suyu: PREN ≥ 40).
:::
