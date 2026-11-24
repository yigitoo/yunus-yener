# MSE4631 Korozyon · Formül Kağıdı

## Sabitler ve dönüşümler

| | |
|---|---|
| $F = 96\,485$ C/mol | $R = 8.314$ J/(mol·K) |
| $T = 25\ ^\circ\text{C} = 298$ K | $N_A = 6.022\times10^{23}$ mol⁻¹ |
| $RT/2F = 0.01284$ V | $RT/4F = 0.00642$ V |
| $\ln x = 2.303\log x$ | $(10^a)^b = 10^{ab}$, $\;10^a/10^b = 10^{a-b}$ |
| 1 A = 1 C/s; 1 mA = $10^{-3}$ A; 1 µA = $10^{-6}$ A | 1 h = 3600 s; 1 gün = 86 400 s; 1 yıl = $3.154\times10^7$ s |
| 1 dm² = 100 cm²; 1 m² = $10^4$ cm² | 1 cm = $10^4$ µm; 1 L = 1000 cm³ |
| 1 mm/y = 39.4 mpy | Fe: 1 µA/cm² = 0.0116 mm/y |

## Faraday yasası

| Formül | Açıklama |
|---|---|
| $Q = It$ | yük (C); $I$ amper, $t$ saniye |
| $n_e = Q/F$ | elektron mol sayısı |
| $m = \dfrac{M\,I\,t}{z\,F}$ | çözünen / biriken kütle (g) |
| $Z = \dfrac{M}{zF}$, $\;m = ZQ$ | elektrokimyasal eşdeğer (g/C) |
| $\eta = \dfrac{m_{ölçülen}}{m_{Faraday}} = \dfrac{I_{teorik}}{I_{gerçek}}$ | akım verimi (0–1) |
| $I_{eff} = \eta\,I$ | efektif akım (verim **çarpılır**) |
| $V = m/\rho$, $\;h = V/A$ | kaplama / kayıp kalınlığı |
| $N = n\,N_A$ | atom sayısı |

$z$: istenen maddenin yarı reaksiyonundan ($Cu^{2+}$ 2, $Al^{3+}$ 3, $O_2$ 4)

## Hücre ve termodinamik

| Formül | Açıklama |
|---|---|
| $E^\circ_{cell} = E^\circ_{katot} - E^\circ_{anot}$ | E° küçük olan anot; potansiyel katsayıyla çarpılmaz |
| $\Delta G = -zFE$, $\;\Delta G^\circ = -zFE^\circ$ | $E > 0 \Rightarrow \Delta G < 0$: kendiliğinden |
| $\Delta G = \Delta H - T\Delta S$ | |
| $\Delta S = zF\,(\partial E/\partial T)$ | |
| $\Delta G^\circ = \sum\nu\mu^\circ_{ürün} - \sum\nu\mu^\circ_{giren}$ | elementler için $\mu^\circ = 0$ |
| $E^\circ = -\Delta G^\circ/(zF)$ | ($\Delta G^\circ$ joule) |
| $\Delta G = \Delta G^\circ + RT\ln Q$ | |
| $\Delta G^\circ = -RT\ln K$, $\;E^\circ = \dfrac{RT}{zF}\ln K$ | denge: $\Delta G = 0$, $Q = K$ |
| $\mu = \mu^\circ + RT\ln a$, $\;a = \gamma c$ | aktivite; katı = su = 1, gaz = P (atm) |

## Referans elektrotlar

$$E_{SHE} = E_{okunan} + E_{ref}$$

| SHE | Ag/AgCl | SCE | CSE (Cu/CuSO₄) | Hg/Hg₂SO₄ |
|---|---|---|---|---|
| 0.000 | +0.197 | +0.241 | +0.316 | ≈ +0.64 V |

Başka referansa geçiş: önce SHE'ye çevir, sonra yeni referansın değerini **çıkar**.

## Standart redüksiyon potansiyelleri (V, SHE)

| Au³⁺/Au | O₂/H₂O | Ag⁺/Ag | Cu²⁺/Cu | H⁺/H₂ | Pb²⁺/Pb | Sn²⁺/Sn | Ni²⁺/Ni | Fe²⁺/Fe | Zn²⁺/Zn | Al³⁺/Al | Mg²⁺/Mg |
|---|---|---|---|---|---|---|---|---|---|---|---|
| +1.50 | +1.229 | +0.799 | +0.337 | 0.000 | −0.126 | −0.136 | −0.250 | −0.440 | −0.763 | −1.662 | −2.363 |

## Nernst denklemi

$$E = E^\circ - \frac{RT}{zF}\ln Q \qquad Q = \frac{\text{ürünler}}{\text{girenler}}$$

| Durum | Reaksiyon | Q |
|---|---|---|
| Tek elektrot | $M^{z+} + ze^- \rightarrow M$ | $1/a_{M^{z+}}$ |
| Hücre | $A + B^{z+} \rightarrow A^{z+} + B$ | $a_{A^{z+}}/a_{B^{z+}}$ |
| Hidrojen | $2H^+ + 2e^- \rightarrow H_2$ | $P_{H_2}/a_{H^+}^2$ |
| Oksijen | $O_2 + 4H^+ + 4e^- \rightarrow 2H_2O$ | $1/(P_{O_2}\,a_{H^+}^4)$ |

Korozyon sınırı: $a_{M^{z+}} = 10^{-6}$ → Fe: −0.617 V, Cu: +0.160 V, Zn: −0.940 V

## Su çizgileri ve korozyon kriteri

| | Asitte | Bazda | Çizgi | pH 0 | pH 7 | pH 14 |
|---|---|---|---|---|---|---|
| a (H₂) | $2H^+ + 2e^- \rightarrow H_2$ | $2H_2O + 2e^- \rightarrow H_2 + 2OH^-$ | $E = -0.0592\,\text{pH}$ | 0.000 | −0.414 | −0.829 |
| b (O₂) | $O_2 + 4H^+ + 4e^- \rightarrow 2H_2O$ | $O_2 + 2H_2O + 4e^- \rightarrow 4OH^-$ | $E = 1.229 - 0.0592\,\text{pH}$ | 1.229 | 0.815 | 0.401 |

Havada ($P_{O_2} = 0.21$ atm), pH 7: $E_O = +0.805$ V

$$E_{cell} = E_{katot} - E_{metal} > 0 \;\Rightarrow\; \text{korozyon mümkün} \qquad E_{cell} = 0 \;\Rightarrow\; \text{denge (maksimum iyon aktivitesi)}$$

## Potansiyel farkı kaynakları

| Formül | Anot olan |
|---|---|
| $\Delta E = \dfrac{RT}{zF}\ln\dfrac{a_{yüksek}}{a_{düşük}}$ | metal iyonu derişim hücresi: **seyreltik** taraf |
| $\Delta E = \dfrac{RT}{4F}\ln\dfrac{P_{O_2,yüksek}}{P_{O_2,düşük}}$ | farklı havalanma: **oksijence fakir** taraf |
| $\Delta E = \dfrac{\Delta G_{stored}}{zF}$ | soğuk deformasyon: **deforme** bölge |
| $I_a = I_c$, $\;i_a = i_c\,\dfrac{A_c}{A_a}$ | alan oranı: **küçük anot** en çok zarar görür |

## Pourbaix

$$E = E^\circ - \frac{0.0592\,m}{z}\,\text{pH} - \frac{0.0592}{z}\log\frac{a_B^{\,b}}{a_A^{\,a}} \qquad aA + mH^+ + ze^- \rightarrow bB + cH_2O$$

| Reaksiyonda | Çizgi | Kullanılan |
|---|---|---|
| sadece $e^-$ | yatay ($E$ sabit) | Nernst |
| sadece $H^+$ | dikey (pH sabit) | $\log K = \ldots + (\text{katsayı})\,\text{pH}$ ($z = 0$, Nernst yok) |
| $e^-$ ve $H^+$ | eğik, eğim $-0.0592\,m/z$ | Nernst |

$10^{-6}$'da bağışıklık sınırı: $E = E^\circ - 0.355/z$; $\;m = z$ ise çizgi su çizgilerine paralel.

## Polarizasyon (kinetik)

| Formül | Açıklama |
|---|---|
| $\eta = E - E_{eq}$ | aşırı gerilim; $\eta > 0$ anot, $\eta < 0$ katot ($E_{eq}$ Nernst'ten) |
| $\eta = b\log\dfrac{|i|}{i_0}$ | Tafel ($|\eta| \gtrsim 0.1$ V); H₂ için $b \approx \pm0.12$ V/dekad |
| $i_L = \dfrac{zFDC_b}{\delta}$ | sınır akım yoğunluğu; $C_b$ **mol/cm³** |
| $\eta_{conc} = \dfrac{RT}{zF}\ln\left(1 - \dfrac{i}{i_L}\right)$ | derişim aşırı gerilimi |
| $\eta_{total} = \eta_{act} + \eta_{conc} + i\rho L$ | toplam polarizasyon |
| $r = \dfrac{iM}{zF}$ | akım yoğunluğundan kütle hızı |

$i_0$ (H₂, A/cm²): Pt $10^{-3}$, Fe $10^{-6}$, Cu $\sim10^{-7}$, Zn $\sim10^{-10}$, Hg $2\times10^{-12}$

## Evans diyagramı ve korozyon hızı

| Formül | Açıklama |
|---|---|
| $\sum I_a = \sum|I_c|$; $E_{corr}$'da $i_a = |i_c| = i_{corr}$ | karışık potansiyel |
| $E = E_{eq} + b\log\dfrac{|i|}{i_0}$ | Evans doğruları (anodik $b_a > 0$, katodik $b_c < 0$) |
| $\eta_c = E_{corr} - E_{eq,c}$ | katodik aşırı gerilim |
| $i_{corr} = i_0\times10^{\eta_c/b_c}$ | $E_{corr}$'dan $i_{corr}$ |
| $E - E_{corr} = b\log\dfrac{|i|}{i_{corr}}$ | Tafel ekstrapolasyonu |
| $i_{corr} = i_L$ | O₂ difüzyon kontrolü |
| $A_a\,i_a = A_c\,|i_c|$ | galvanik çift / alan oranı |
| $CR\ (\text{mm/y}) = 3.27\times10^{-3}\,\dfrac{i_{corr}\,M}{z\,\rho}$ | $i_{corr}$ µA/cm², $M$ g/mol, $\rho$ g/cm³ |
| $\dfrac{\Delta m}{A\,t} = \dfrac{i_{corr}\,M}{zF}$ | kütle kaybı hızı ($i$ A/cm²) |

## Korozyon hızı ölçümü ve ömür

| Formül | Açıklama |
|---|---|
| $CR = \dfrac{K\,W}{A\,T\,D}$ | ASTM G31; $W$ g, $A$ cm², $T$ **saat**, $D$ g/cm³ |
| $K = 8.76\times10^4$ (mm/y), $3.45\times10^6$ (mpy), $2.40\times10^6 D$ (mdd) | |
| $A = 2(ab + ac + bc)$ | dikdörtgen kuponun toplam alanı |
| oyuklanma faktörü $= P/p$ | en derin oyuk / ortalama penetrasyon |
| ömür $= \dfrac{t_{duvar} - t_{min}}{(P/p)\times CR}$ | en derin oyuğa göre |

| Fontana (mpy) | < 1 | 1–5 | 5–20 | 20–50 | 50–200 | > 200 |
|---|---|---|---|---|---|---|
| | outstanding | excellent | good | fair | poor | unacceptable |

## Pasiflik

| Formül / koşul | Açıklama |
|---|---|
| $E_F = 0.63 - 0.059\,\text{pH}$ | Flade potansiyeli (Fe); altında pasif film bozulur |
| $i_{katodik}(E_{pp}) > i_{crit}$ | kendiliğinden pasifleşme koşulu |
| $i_L > i_{crit}$ | havalı suda O₂ ile pasifleşme |
| Pasif hız $= i_{pass}$ | pasif bölgede korozyon hızı |

Semboller: $E_{pp}$ birincil pasifleşme potansiyeli, $i_{crit}$ kritik akım yoğunluğu, $i_{pass}$ pasif akım yoğunluğu, $E_{tp}$ transpasif potansiyel, $E_{pit}$ oyuklanma potansiyeli (Cl⁻ arttıkça düşer).
