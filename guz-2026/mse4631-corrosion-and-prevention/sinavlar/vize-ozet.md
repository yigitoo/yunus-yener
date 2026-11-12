# Vize Tekrarı · Yedi Hafta Tek Sayfada

## Her haftadan ne yapabiliyor olmalısın?

| Hafta · konu | Yapabilmen gerekenler |
|---|---|
| 1 · Giriş | Korozyonu tanımla; kimyasal ve elektrokimyasal reaksiyon; hücrenin dört koşulu; neden $\Delta G < 0$ |
| 2 · Faraday ve hücre | $m = MIt/(zF)$, akım verimi, kaplama kalınlığı; anot/katot; referans skalası dönüşümü; $E^\circ_{cell}$, $\Delta G^\circ = -zFE^\circ$ |
| 3 · Termodinamik | Nernst; korozyon mümkün mü ($H_2$ ve $O_2$ çizgileri)? galvanik seri; derişim ve havalanma hücreleri; soğuk deformasyon; alan oranı |
| 4 · Pourbaix | Diyagram okuma: bağışıklık, korozyon, pasiflik; su çizgileri a ve b; Fe, Al ve Cu; sınırlamalar |
| 5 · Kinetik I | Aşırı gerilim ve işareti; üç polarizasyon tipi; $i_0$; Tafel merdiveni; $i_L = zFDC/\delta$; IR düşüşü |
| 6 · Kinetik II | Evans diyagramında $E_{corr}$ ve $i_{corr}$; kontrol tipi; $O_2$ difüzyonu; galvanik çift; $i_{corr}$ → mm/y, mpy |
| 7 · Hızlar ve pasiflik | ASTM G31 kütle kaybı; oyuklanma faktörü ve ömür; aktif–pasif eğri; Flade; kendiliğinden pasifleşme; klorür |

## Tüm formüller

| Konu | Formül |
|---|---|
| Faraday | $m = \dfrac{MIt}{zF}$, $\;I_{eff} = \eta I$, $\;h = \dfrac{m}{\rho A}$ |
| Hücre | $E^\circ_{cell} = E^\circ_{cathode} - E^\circ_{anode}$, $\;\Delta G = -zFE$ |
| Referans | $E_{SHE} = E_{ref} + E^{SHE}_{ref}$ (SCE +0.241, Ag/AgCl +0.197, CSE +0.316 V) |
| Termodinamik | $\Delta G = \Delta G^\circ + RT\ln Q$, $\;\Delta G^\circ = -RT\ln K$, $\;E^\circ = -\Delta G^\circ/(zF)$ |
| Nernst | $E = E^\circ - \dfrac{0.0592}{z}\log Q$; tek elektrot: $E = E^\circ + \dfrac{0.0592}{z}\log a_{M^{z+}}$ |
| Su çizgileri | $E_H = -0.0592\,\text{pH}$, $\;E_O = 1.229 - 0.0592\,\text{pH} + \dfrac{0.0592}{4}\log P_{O_2}$ |
| Kriter | $E_{cell} = E_{cathodic} - E_{metal} > 0$ |
| Derişim hücresi | $\Delta E = \dfrac{0.0592}{z}\log\dfrac{a_{high}}{a_{low}}$ |
| Pourbaix | $E = E^\circ - \dfrac{0.0592\,m}{z}\text{pH} - \dfrac{0.0592}{z}\log\dfrac{a_B^b}{a_A^a}$; $10^{-6}$'da $E = E^\circ - 0.355/z$ |
| Aşırı gerilim | $\eta = E - E_{eq}$; Tafel $\eta = b\log(|i|/i_0)$ |
| Difüzyon | $i_L = \dfrac{zFDC_b}{\delta}$, $\;\eta_{conc} = \dfrac{2.303RT}{zF}\log(1 - i/i_L)$ |
| Evans | $i_{corr} = i_0\times10^{\eta_c/b_c}$; $\;A_a i_a = A_c|i_c|$ |
| Hız | $CR\ (\text{mm/y}) = 3.27\times10^{-3}\dfrac{i_{corr}M}{z\rho}$ ($i$: µA/cm²); Fe: 1 µA/cm² = 0.0116 mm/y |
| Kütle kaybı | $CR = \dfrac{KW}{ATD}$ ($T$: saat; $K_{mm/y} = 8.76\times10^4$) |
| Ömür | $\dfrac{t_{wall} - t_{min}}{(P/p)\times CR}$ |
| Flade | $E_F = 0.63 - 0.059\,\text{pH}$ (Fe) |

## Kontrol listesi

- [ ] Faraday problemlerinde süre saniye, verim çarpan, alan cm².
- [ ] $z$'yi istenen maddenin yarı reaksiyonundan al.
- [ ] Potansiyeller katsayılarla çarpılmaz.
- [ ] SCE okumasını önce SHE'ye çevir (+0.241).
- [ ] Nernst'te $Q$ = ürünler/girenler; katılar ve su 1.
- [ ] Suyun dört reaksiyonu: asitte ve bazda $H_2$ ve $O_2$ çizgileri.
- [ ] Pourbaix'da elektron yoksa (dikey çizgi) Nernst değil $K$.
- [ ] Katodik $\eta$ ve $b_c$ negatif.
- [ ] $i_L$ formülünde $C_b$ mol/cm³.
- [ ] $E_{corr}$ karışık bir potansiyeldir; "daha soy" ≠ "daha yavaş".
- [ ] Pasif ≠ bağışık; pasifleşme koşulu: katodik akım > $i_{crit}$.
- [ ] Ömür için ortalama değil en derin oyuk.
