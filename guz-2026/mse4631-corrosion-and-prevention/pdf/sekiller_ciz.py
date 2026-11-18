"""MSE4631 ders notlari icin sekilleri (SVG) uretir.

Kullanim:  python3 sekiller_ciz.py
Cikti:     ../kaynaklar/sekiller/*.svg
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, Polygon, FancyArrowPatch, Ellipse

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "kaynaklar", "sekiller")
os.makedirs(OUT, exist_ok=True)

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "axes.linewidth": 0.8,
    "axes.edgecolor": "#333",
    "axes.labelcolor": "#222",
    "xtick.color": "#333",
    "ytick.color": "#333",
    "svg.fonttype": "path",
    "mathtext.fontset": "dejavusans",
})

AN = "#d2602a"     # anodik
KA = "#2f6fb0"     # katodik
YE = "#3b9460"     # pasif / yesil
GR = "#7a8288"
SU = "#5aa0c8"
C_KOR = "#f6d3c4"  # korozyon bolgesi
C_PAS = "#cfe8d2"  # pasiflik bolgesi
C_BAG = "#cfe0f3"  # bagisiklik bolgesi


def kaydet(fig, ad):
    fig.savefig(os.path.join(OUT, ad + ".svg"), bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)
    print("  ", ad)


def ok(ax, x1, y1, x2, y2, renk="#333", lw=1.2, ms=10, stil="-|>"):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=stil, mutation_scale=ms,
                                 color=renk, lw=lw, shrinkA=0, shrinkB=0))


def catmull(points, n=40):
    p = np.asarray(points, float)
    p = np.vstack([p[0], p, p[-1]])
    out = []
    for i in range(1, len(p) - 2):
        p0, p1, p2, p3 = p[i - 1], p[i], p[i + 1], p[i + 2]
        t = np.linspace(0, 1, n, endpoint=False)[:, None]
        out.append(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t ** 2
                          + (-p0 + 3 * p1 - 3 * p2 + p3) * t ** 3))
    out.append(p[-2][None, :])
    return np.vstack(out)


def su_cizgileri(ax, ph=(0, 14), etiket=True, renk=SU):
    x = np.array(ph, float)
    ax.plot(x, -0.0592 * x, "--", color=renk, lw=1.1)
    ax.plot(x, 1.229 - 0.0592 * x, "--", color=renk, lw=1.1)
    if etiket:
        ax.text(x[1] + 0.15, -0.0592 * x[1], "a", color=renk, va="center", fontsize=10, fontweight="bold")
        ax.text(x[1] + 0.15, 1.229 - 0.0592 * x[1], "b", color=renk, va="center", fontsize=10, fontweight="bold")


# ---------------------------------------------------------------- Hafta 1
def korozyon_hucresi():
    fig, ax = plt.subplots(figsize=(6.2, 2.6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 4.2); ax.axis("off")
    ax.add_patch(Rectangle((0.5, 0.4), 9, 1.0, fc="#b9c0c6", ec="#555"))
    ax.text(5, 0.55, "çelik (elektriksel yol)", ha="center", fontsize=9)
    ax.add_patch(Rectangle((0.5, 1.4), 9, 1.5, fc="#e3f0f8", ec="none"))
    ax.text(5, 2.6, "nemli ortam (elektrolit)", ha="center", color="#2c5d7c", fontsize=9)
    ax.add_patch(Rectangle((1.2, 1.4), 2.6, 0.18, fc=AN, ec="none"))
    ax.add_patch(Rectangle((6.2, 1.4), 2.6, 0.18, fc=KA, ec="none"))
    ax.text(2.5, 3.35, "ANOT (oksidasyon)", ha="center", color=AN, fontweight="bold")
    ax.text(2.5, 3.0, r"$Fe \rightarrow Fe^{2+} + 2e^-$", ha="center", color=AN)
    ax.text(7.5, 3.35, "KATOT (redüksiyon)", ha="center", color=KA, fontweight="bold")
    ax.text(7.5, 3.0, r"$O_2 + 2H_2O + 4e^- \rightarrow 4OH^-$", ha="center", color=KA)
    ok(ax, 2.5, 1.65, 2.5, 2.25, AN); ax.text(2.65, 1.9, r"$Fe^{2+}$", color=AN, fontsize=8)
    ok(ax, 7.5, 2.25, 7.5, 1.65, KA); ax.text(7.65, 1.9, r"$O_2$", color=KA, fontsize=8)
    ok(ax, 3.2, 1.05, 6.8, 1.05, "#222"); ax.text(5, 1.12, r"$e^-$", ha="center", fontsize=9)
    ok(ax, 6.6, 2.05, 3.4, 2.05, "#2c5d7c", lw=0.9, stil="<|-|>")
    ax.text(5, 2.13, "iyon akımı", ha="center", color="#2c5d7c", fontsize=8)
    kaydet(fig, "korozyon-hucresi")


# ---------------------------------------------------------------- Hafta 2
def daniell():
    fig, ax = plt.subplots(figsize=(6.8, 3.3))
    ax.set_xlim(-2.2, 12.2); ax.set_ylim(0, 6); ax.axis("off")
    for x0, renk, ad in [(0.6, "#dbe7ef", r"$ZnSO_4$"), (6.4, "#cfe2f3", r"$CuSO_4$")]:
        ax.add_patch(Rectangle((x0, 0.4), 3.0, 2.6, fc=renk, ec="#555"))
        ax.text(x0 + 1.5, 0.7, ad, ha="center", fontsize=9)
    ax.add_patch(Rectangle((1.6, 1.2), 0.45, 3.2, fc="#9aa3ab", ec="#444"))
    ax.add_patch(Rectangle((7.95, 1.2), 0.45, 3.2, fc="#c98a52", ec="#444"))
    ax.text(1.82, 4.55, "Zn", ha="center", fontweight="bold")
    ax.text(8.17, 4.55, "Cu", ha="center", fontweight="bold")
    # tuz koprusu
    ax.add_patch(Polygon([[2.9, 2.3], [2.9, 3.6], [7.1, 3.6], [7.1, 2.3], [6.75, 2.3], [6.75, 3.25],
                          [3.25, 3.25], [3.25, 2.3]], closed=True, fc="#f3e6c4", ec="#8a7a4a"))
    ax.text(5, 3.36, "tuz köprüsü (KCl)", ha="center", fontsize=8)
    ok(ax, 5.3, 3.05, 6.3, 3.05, "#8a5a00", lw=0.9, ms=8); ax.text(5.8, 2.75, r"$K^+$", ha="center", fontsize=8, color="#8a5a00")
    ok(ax, 4.7, 3.05, 3.7, 3.05, "#8a5a00", lw=0.9, ms=8); ax.text(4.2, 2.75, r"$Cl^-$", ha="center", fontsize=8, color="#8a5a00")
    # tel ve voltmetre
    ax.plot([1.82, 1.82, 4.6], [4.4, 5.4, 5.4], color="#333", lw=1)
    ax.plot([5.4, 8.17, 8.17], [5.4, 5.4, 4.4], color="#333", lw=1)
    ax.add_patch(Ellipse((5, 5.4), 0.8, 0.8, fc="white", ec="#333"))
    ax.text(5, 5.4, "V", ha="center", va="center", fontweight="bold")
    ok(ax, 2.4, 5.65, 4.2, 5.65, "#222"); ax.text(3.3, 5.75, r"$e^-$", ha="center")
    ax.text(0.5, 1.95, "ANOT (−)", color=AN, fontweight="bold", fontsize=8.5, ha="right")
    ax.text(0.5, 1.6, r"$Zn \rightarrow Zn^{2+}+2e^-$", color=AN, fontsize=8, ha="right")
    ax.text(9.5, 1.95, "KATOT (+)", color=KA, fontweight="bold", fontsize=8.5)
    ax.text(9.5, 1.6, r"$Cu^{2+}+2e^- \rightarrow Cu$", color=KA, fontsize=8)
    ax.text(5, 0.05, r"$Zn\,|\,Zn^{2+}\,\|\,Cu^{2+}\,|\,Cu \qquad E^\circ_{cell} = 0.337-(-0.763) = +1.100$ V",
            ha="center", fontsize=9)
    kaydet(fig, "daniell")


def referans_dogrusu():
    fig, ax = plt.subplots(figsize=(6.4, 1.9))
    ax.set_xlim(-0.95, 0.8); ax.set_ylim(-1.3, 2.4); ax.axis("off")
    ax.plot([-0.9, 0.7], [0, 0], color="#333", lw=1)
    for t in np.arange(-0.9, 0.71, 0.1):
        ax.plot([t, t], [-0.08, 0.08], color="#333", lw=0.7)
        ax.text(t, -0.32, f"{t:+.1f}".replace("+0.0", "0.0").replace("-0.0", "0.0"), ha="center", fontsize=7)
    ax.text(0.7, -0.62, "V (SHE)", fontsize=7.5, ha="right")
    refs = [("SHE", 0.0, 0.0), ("Ag/AgCl", 0.197, 0.0), ("SCE", 0.241, 0.55), ("CSE", 0.316, 1.1),
            ("Hg/Hg$_2$SO$_4$", 0.64, 0.0)]
    for ad, v, dy in refs:
        ax.plot([v, v], [0, 0.55 + dy], color=KA, lw=1.2)
        ax.text(v, 0.62 + dy, f"{ad}\n{v:+.3f}" if v else f"{ad}\n0.000", ha="center", fontsize=7.5, color=KA)
    ax.plot([-0.259, -0.259], [0, -0.75], color=AN, lw=1.2)
    ax.text(-0.259, -1.15, "deniz suyunda çelik: −0.500 V(SCE) = −0.259 V(SHE) = −0.575 V(CSE)",
            ha="center", fontsize=7.5, color=AN)
    kaydet(fig, "referans-dogrusu")


# ---------------------------------------------------------------- Hafta 3
def gibbs_tepe():
    fig, ax = plt.subplots(figsize=(6.2, 2.7))
    c = catmull([(0, 0.3), (2.4, 0.3), (3.4, 1.3), (4.4, 2.25), (5.6, 2.3), (6.4, 3.0), (7.2, 2.1),
                 (8.2, 0.8), (10, 0.6)], n=60)
    ax.plot(c[:, 0], c[:, 1], color="#333", lw=1.6)
    ax.set_xlim(0, 10); ax.set_ylim(0, 3.6)
    ax.set_xticks([]); ax.set_yticks([]); ax.set_ylabel("Gibbs serbest enerjisi G")
    for sp in ["top", "right"]:
        ax.spines[sp].set_visible(False)
    ax.text(1.2, 0.45, "cevher (oksit)\nkararlı, düşük G", ha="center", fontsize=8)
    ok(ax, 2.2, 0.45, 2.2, 2.25, KA)
    ax.text(2.05, 1.35, "enerji verilir\n(ergitme)", ha="right", fontsize=8, color=KA)
    ax.text(5.0, 2.45, "metal", ha="center", fontsize=8)
    ax.text(6.4, 3.15, "aktivasyon bariyeri", ha="center", fontsize=8)
    ax.plot([5.6, 9.3], [2.3, 2.3], ":", color=GR, lw=0.9)
    ok(ax, 9.3, 2.3, 9.3, 0.68, AN)
    ax.text(9.2, 1.5, r"$\Delta G<0$" + "\nkorozyon", fontsize=8, color=AN, ha="right")
    ax.text(8.9, 0.2, "korozyon ürünü (pas)", ha="center", fontsize=8)
    kaydet(fig, "gibbs-tepe")


def nernst_dogrular():
    fig, ax = plt.subplots(figsize=(5.6, 3.2))
    la = np.linspace(-8, 0, 50)
    for ad, e0, renk in [("Cu²⁺/Cu  (E° = +0.337 V)", 0.337, "#b5651d"),
                         ("Fe²⁺/Fe  (E° = −0.440 V)", -0.440, "#5a6b78"),
                         ("Zn²⁺/Zn  (E° = −0.763 V)", -0.763, "#6d4fa1")]:
        ax.plot(la, e0 + 0.0296 * la, color=renk, lw=1.6, label=ad)
    ax.axvline(-6, color=GR, ls=":", lw=1)
    ax.text(-5.9, 0.42, r"$a = 10^{-6}$", fontsize=8, color=GR)
    ax.annotate("eğim = 0.0592/z V/dekad\n(z = 2: 29.6 mV)", xy=(-3, 0.337 - 0.0888), xytext=(-7.8, -0.25),
                fontsize=8, arrowprops=dict(arrowstyle="->", color="#333", lw=0.8))
    ax.set_xlabel(r"$\log a_{M^{z+}}$"); ax.set_ylabel("E (V vs SHE)")
    ax.set_xlim(-8, 0); ax.set_ylim(-1.05, 0.5)
    ax.legend(fontsize=7.5, loc="center right", bbox_to_anchor=(1.0, 0.42), frameon=False)
    ax.grid(alpha=0.25)
    kaydet(fig, "nernst-dogrular")


def su_cizgileri_sekil():
    fig, ax = plt.subplots(figsize=(5.6, 3.3))
    ph = np.array([0, 14.0])
    a = -0.0592 * ph; b = 1.229 - 0.0592 * ph
    ax.fill_between(ph, a, b, color="#dcecf6")
    ax.fill_between(ph, b, 1.6, color="#fbeee4")
    ax.fill_between(ph, -1.0, a, color="#eef1f3")
    ax.plot(ph, a, color=KA, lw=1.6); ax.plot(ph, b, color=AN, lw=1.6)
    ax.text(7, 0.35, "su kararlı", ha="center", fontsize=9, color="#2c5d7c", fontweight="bold")
    ax.text(9.5, 1.15, r"$O_2$ çıkar (su oksitlenir)", ha="center", fontsize=8.5, color=AN)
    ax.text(4.3, -0.82, r"$H_2$ çıkar (su indirgenir)", ha="center", fontsize=8.5, color=KA)
    ax.text(2.3, 1.2, r"b: $O_2+4H^++4e^-\rightarrow 2H_2O$", fontsize=8, color=AN)
    ax.text(2.3, -0.07, r"a: $2H^++2e^-\rightarrow H_2$", fontsize=8, color=KA)
    for x, y, t in [(0, 1.229, "1.229"), (14, 0.401, "0.401"), (0, 0, "0.000"), (14, -0.829, "−0.829")]:
        ax.plot(x, y, "o", color="#333", ms=3)
        ax.text(x + (0.2 if x == 0 else -0.2), y + 0.05, t, fontsize=7.5, ha="left" if x == 0 else "right")
    ok(ax, 10.5, -0.0592 * 10.5, 10.5, 1.229 - 0.0592 * 10.5, "#333", lw=0.8, ms=7, stil="<|-|>")
    ax.text(10.65, 0.3, "1.23 V", fontsize=8)
    ax.set_xlim(0, 14); ax.set_ylim(-1.0, 1.6)
    ax.set_xlabel("pH"); ax.set_ylabel("E (V vs SHE)")
    ax.set_title("eğim: −59.2 mV / pH (iki çizgi paralel)", fontsize=8.5, color="#444")
    kaydet(fig, "su-cizgileri")


def korozyon_kriteri():
    fig, ax = plt.subplots(figsize=(5.8, 3.2))
    ax.set_xlim(0, 10); ax.set_ylim(-0.75, 1.08); ax.axis("off")
    ax.plot([2, 2], [-0.7, 0.9], color="#333", lw=1)
    for v in np.arange(-0.6, 0.81, 0.2):
        ax.plot([1.9, 2.0], [v, v], color="#333", lw=0.8)
        ax.text(1.8, v, f"{v:+.1f}", ha="right", va="center", fontsize=7.5)
    ax.text(0.2, 1.0, "E (V vs SHE), pH 7, 25 °C", fontsize=8)
    seviyeler = [(0.805, r"$O_2/H_2O$ (hava, 0.21 atm): +0.805", KA),
                 (0.159, r"$Cu^{2+}/Cu$ ($a=10^{-6}$): +0.159", "#b5651d"),
                 (-0.414, r"$H^+/H_2$ (pH 7): −0.414", KA),
                 (-0.618, r"$Fe^{2+}/Fe$ ($a=10^{-6}$): −0.618", "#5a6b78")]
    for v, t, r in seviyeler:
        ax.plot([2, 5.2], [v, v], color=r, lw=2)
        ax.text(2.1, v + 0.03, t, fontsize=8, color=r)
    ok(ax, 6.0, 0.159, 6.0, 0.78, YE); ax.text(6.15, 0.47, "Cu + O₂: evet", fontsize=8, color=YE)
    ok(ax, 7.5, 0.159, 7.5, -0.39, "#b23b3b", lw=1, stil="-")
    ax.text(7.65, -0.12, "Cu + H⁺: hayır\n(H⁺/H₂ Cu'nun altında)", fontsize=8, color="#b23b3b")
    ok(ax, 6.0, -0.618, 6.0, -0.44, YE); ax.text(6.15, -0.56, "Fe + H⁺: evet", fontsize=8, color=YE)
    ax.text(5.0, -0.74, "Bir metal, üstünde bir katodik reaksiyon varsa korozyona uğrayabilir.",
            ha="center", fontsize=8, style="italic")
    kaydet(fig, "korozyon-kriteri")


def galvanik_cift():
    fig, ax = plt.subplots(figsize=(6.2, 2.4))
    ax.set_xlim(0, 10); ax.set_ylim(0, 3.6); ax.axis("off")
    ax.add_patch(Rectangle((0.5, 0.5), 4.5, 1.0, fc="#c3c9ce", ec="#555"))
    ax.add_patch(Rectangle((5.0, 0.5), 4.5, 1.0, fc="#8e969c", ec="#555"))
    ax.text(2.75, 0.85, "Al alaşımı (daha aktif)", ha="center", fontsize=8.5)
    ax.text(7.25, 0.85, "çelik (daha soy)", ha="center", fontsize=8.5, color="white")
    ax.add_patch(Rectangle((1.5, 1.5), 7, 0.55, fc="#e3f0f8", ec="none"))
    ax.text(5, 1.68, "ıslak tuz filmi (elektrolit)", ha="center", fontsize=8, color="#2c5d7c")
    ax.text(3.0, 2.95, "ANOT", ha="center", color=AN, fontweight="bold")
    ax.text(3.0, 2.55, r"$Al \rightarrow Al^{3+} + 3e^-$", ha="center", color=AN)
    ax.text(7.2, 2.95, "KATOT", ha="center", color=KA, fontweight="bold")
    ax.text(7.2, 2.55, r"$O_2 + 2H_2O + 4e^- \rightarrow 4OH^-$", ha="center", color=KA)
    ok(ax, 3.6, 0.3, 6.4, 0.3, "#222"); ax.text(5, 0.05, "elektronlar metalik bağlantıdan geçer", ha="center", fontsize=7.5)
    kaydet(fig, "galvanik-cift")


# ---------------------------------------------------------------- Hafta 4
def pourbaix_cerceve(ax, ylim):
    ax.set_xlim(0, 14); ax.set_ylim(*ylim)
    ax.set_xlabel("pH"); ax.set_ylabel("E (V vs SHE)")
    ax.set_xticks(range(0, 15, 2))


def pourbaix_fe():
    fig, ax = plt.subplots(figsize=(5.8, 4.2))
    Y0, Y1 = -1.2, 1.6
    poly = {
        "bag": ([(0, Y0), (0, -0.617), (9, -0.617), (14, -0.912), (14, Y0)], C_BAG),
        "fe2": ([(0, -0.617), (0, 0.771), (1.76, 0.771), (7.29, -0.21), (9, -0.617)], C_KOR),
        "fe3": ([(0, 0.771), (0, Y1), (1.76, Y1), (1.76, 0.771)], "#f0bba6"),
        "fe3o4": ([(7.29, -0.21), (14, -0.606), (14, -0.912), (9, -0.617)], "#b8dcc0"),
        "fe2o3": ([(1.76, Y1), (14, Y1), (14, -0.606), (7.29, -0.21), (1.76, 0.771)], C_PAS),
    }
    for p, c in poly.values():
        ax.add_patch(Polygon(p, closed=True, fc=c, ec="none"))
    L = dict(color="#333", lw=1.3)
    ax.plot([0, 9], [-0.617, -0.617], **L)
    ax.plot([0, 1.76], [0.771, 0.771], **L)
    ax.plot([1.76, 1.76], [0.771, Y1], **L)
    ax.plot([1.76, 7.29], [0.771, -0.21], **L)
    ax.plot([7.29, 14], [-0.21, -0.606], **L)
    ax.plot([9, 14], [-0.617, -0.912], **L)
    ax.plot([7.29, 9], [-0.21, -0.617], **L)
    su_cizgileri(ax)
    ax.text(0.5, 1.35, r"$Fe^{3+}$", fontsize=9)
    ax.text(1.0, 0.1, r"$Fe^{2+}$" + "\n(korozyon)", fontsize=9)
    ax.text(8.5, 0.75, r"$Fe_2O_3$" + "\n(pasiflik)", fontsize=9, ha="center")
    ax.text(12.3, -0.69, r"$Fe_3O_4$", fontsize=8.5, ha="center")
    ax.text(4, -0.95, "Fe (bağışıklık)", fontsize=9, ha="center")
    for x, y, ad in [(7.5, -0.617, "①"), (0.85, 0.80, "②"), (1.9, 1.2, "③"), (4.3, 0.37, "④"),
                     (11.5, -0.40, "⑤"), (11.3, -0.80, "⑥"), (8.05, -0.43, "⑦")]:
        ax.text(x, y, ad, fontsize=9, color="#333")
    noktalar = {"A": (7, -0.80), "B": (4, -0.42), "C": (10, -0.50), "D": (7, 0.50), "E": (0.8, 0.95)}
    for ad, (x, y) in noktalar.items():
        ax.plot(x, y, "o", color="#7b2d8b", ms=5)
        ax.text(x + 0.18, y + 0.04, ad, color="#7b2d8b", fontweight="bold", fontsize=9)
    pourbaix_cerceve(ax, (Y0, Y1))
    ax.set_title(r"Fe–H$_2$O, 25 °C, çözünmüş türler $10^{-6}$ (sadeleştirilmiş)", fontsize=8.5, color="#444")
    kaydet(fig, "pourbaix-fe")


def pourbaix_al():
    fig, ax = plt.subplots(figsize=(5.6, 3.9))
    Y0, Y1 = -2.6, 1.6
    e3 = lambda p: -1.55 - 0.0591 * p
    e5 = lambda p: -1.380 - 0.0788 * p
    ax.add_patch(Polygon([(0, Y0), (0, -1.78), (3.9, -1.78), (8.6, e3(8.6)), (14, e5(14)), (14, Y0)], fc=C_BAG))
    ax.add_patch(Polygon([(0, -1.78), (0, Y1), (3.9, Y1), (3.9, -1.78)], fc=C_KOR))
    ax.add_patch(Polygon([(3.9, -1.78), (3.9, Y1), (8.6, Y1), (8.6, e3(8.6))], fc=C_PAS))
    ax.add_patch(Polygon([(8.6, e3(8.6)), (8.6, Y1), (14, Y1), (14, e5(14))], fc=C_KOR))
    L = dict(color="#333", lw=1.3)
    ax.plot([0, 3.9], [-1.78, -1.78], **L); ax.plot([3.9, 3.9], [-1.78, Y1], **L)
    ax.plot([3.9, 8.6], [e3(3.9), e3(8.6)], **L); ax.plot([8.6, 8.6], [e3(8.6), Y1], **L)
    ax.plot([8.6, 14], [e5(8.6), e5(14)], **L)
    su_cizgileri(ax)
    ax.text(0.4, 0.4, r"$Al^{3+}$" + "\n(korozyon)", fontsize=9)
    ax.text(6.25, -0.6, r"$Al_2O_3$" + "\n(pasiflik)", fontsize=9, ha="center")
    ax.text(11.3, -0.9, r"$AlO_2^-$" + "\n(korozyon)", fontsize=9, ha="center")
    ax.text(5, -2.4, "Al (bağışıklık)", fontsize=9, ha="center")
    for x, y, ad in [(1.6, -1.72, "①"), (3.95, 0.9, "②"), (6.0, -1.82, "③"), (8.65, 0.9, "④"), (11.3, -2.07, "⑤")]:
        ax.text(x, y, ad, fontsize=9)
    pourbaix_cerceve(ax, (Y0, Y1))
    ax.set_title(r"Al–H$_2$O, 25 °C, $10^{-6}$ (şematik)", fontsize=8.5, color="#444")
    kaydet(fig, "pourbaix-al")


def pourbaix_cu():
    fig, ax = plt.subplots(figsize=(5.6, 3.9))
    Y0, Y1 = -1.0, 1.6
    cu2o_cu = lambda p: 0.471 - 0.0591 * p
    cu2_cu2o = lambda p: -0.152 + 0.0591 * p
    cuo_cu2o = lambda p: 0.669 - 0.0591 * p
    ax.add_patch(Polygon([(0, Y0), (0, 0.159), (5.27, 0.159), (14, cu2o_cu(14)), (14, Y0)], fc=C_BAG))
    ax.add_patch(Polygon([(0, 0.159), (0, Y1), (6.95, Y1), (6.95, cu2_cu2o(6.95)), (5.27, 0.159)], fc=C_KOR))
    ax.add_patch(Polygon([(5.27, 0.159), (6.95, cu2_cu2o(6.95)), (14, cuo_cu2o(14)), (14, cu2o_cu(14))], fc="#b8dcc0"))
    ax.add_patch(Polygon([(6.95, cu2_cu2o(6.95)), (6.95, Y1), (12.83, Y1), (12.83, cuo_cu2o(12.83))], fc=C_PAS))
    ax.add_patch(Polygon([(12.83, cuo_cu2o(12.83)), (12.83, Y1), (14, Y1), (14, cuo_cu2o(14))], fc=C_KOR))
    L = dict(color="#333", lw=1.3)
    ax.plot([0, 5.27], [0.159, 0.159], **L)
    ax.plot([5.27, 14], [cu2o_cu(5.27), cu2o_cu(14)], **L)
    ax.plot([5.27, 6.95], [cu2_cu2o(5.27), cu2_cu2o(6.95)], **L)
    ax.plot([6.95, 6.95], [cu2_cu2o(6.95), Y1], **L)
    ax.plot([6.95, 14], [cuo_cu2o(6.95), cuo_cu2o(14)], **L)
    ax.plot([12.83, 12.83], [cuo_cu2o(12.83), Y1], **L)
    su_cizgileri(ax)
    ax.text(1.2, 0.85, r"$Cu^{2+}$" + "\n(korozyon)", fontsize=9)
    ax.text(9.9, 0.95, "CuO\n(pasiflik)", fontsize=9, ha="center")
    ax.text(10.6, -0.02, r"$Cu_2O$", fontsize=8.5, ha="center")
    ax.text(13.4, 1.25, r"$HCuO_2^-$", fontsize=7.5, ha="center", rotation=90)
    ax.text(3.5, -0.75, "Cu (bağışıklık)", fontsize=9, ha="center")
    for x, y, ad in [(2.5, 0.19, "①"), (8.6, cu2o_cu(8.6) - 0.12, "②"), (5.5, 0.3, "③"), (7.0, 1.3, "④"),
                     (11.5, cuo_cu2o(11.5) + 0.05, "⑤"), (12.9, 1.3, "⑥")]:
        ax.text(x, y, ad, fontsize=9)
    pourbaix_cerceve(ax, (Y0, Y1))
    ax.set_title(r"Cu–H$_2$O, 25 °C, $10^{-6}$ (şematik)", fontsize=8.5, color="#444")
    kaydet(fig, "pourbaix-cu")


# ---------------------------------------------------------------- Hafta 5
def daniell_polarizasyon():
    fig, ax = plt.subplots(figsize=(5.4, 3.0))
    I = np.linspace(0, 1, 50)
    ax.plot(I, 0.337 - 0.67 * I ** 0.8, color=KA, lw=1.8, label="bakır katot")
    ax.plot(I, -0.763 + 0.43 * I ** 0.8, color=AN, lw=1.8, label="çinko anot")
    ax.axhline(0.337, color=KA, ls=":", lw=0.9); ax.axhline(-0.763, color=AN, ls=":", lw=0.9)
    ax.text(0.02, 0.36, r"$E_{eq}(Cu^{2+}/Cu) = +0.337$ V", fontsize=7.5, color=KA)
    ax.text(0.02, -0.82, r"$E_{eq}(Zn^{2+}/Zn) = -0.763$ V", fontsize=7.5, color=AN)
    x = 0.45
    ok(ax, x, -0.763 + 0.43 * x ** 0.8, x, 0.337 - 0.67 * x ** 0.8, "#333", lw=0.9, ms=7, stil="<|-|>")
    ax.text(x + 0.02, -0.25, r"$E_{cell}$" + "\nakımla düşer", fontsize=7.5)
    ax.text(0.83, 0.05, r"$\eta_{Cu}<0$", color=KA, fontsize=8)
    ax.text(0.8, -0.55, r"$\eta_{Zn}>0$", color=AN, fontsize=8)
    ax.plot(1, -0.333, "o", color="#333", ms=4); ax.text(0.86, -0.42, r"$I_{max}$", fontsize=8)
    ax.set_xlabel("hücre akımı I"); ax.set_ylabel("elektrot potansiyeli E (V vs SHE)")
    ax.set_xticks([]); ax.set_ylim(-0.9, 0.45); ax.set_xlim(0, 1.05)
    ax.legend(fontsize=7.5, frameon=False, loc="center left")
    kaydet(fig, "daniell-polarizasyon")


def tafel_merdiven():
    fig, ax = plt.subplots(figsize=(5.4, 3.0))
    xs = [-6, -5, -4, -3, -2]
    for k in range(4):
        ax.plot([xs[k], xs[k + 1]], [0.12 * k, 0.12 * k], color=AN, lw=1.6)
        ax.plot([xs[k + 1], xs[k + 1]], [0.12 * k, 0.12 * (k + 1)], color=AN, lw=1.6)
        ax.text(xs[k + 1] + 0.05, 0.12 * k + 0.05, "+0.12 V", fontsize=7.5, color=AN)
    ax.plot([-6, -2], [0, 0.48], "--", color="#555", lw=1)
    ax.plot(-6, 0, "o", color="#333", ms=4); ax.text(-5.9, -0.035, r"$i_0$, $\eta = 0$", fontsize=8)
    ax.plot(-2, 0.48, "o", color="#333", ms=4); ax.text(-2.6, 0.5, "4 basamak: 0.48 V", fontsize=8)
    ax.set_xticks(xs); ax.set_xticklabels([r"$10^{%d}$" % v for v in xs])
    ax.set_yticks([0, 0.12, 0.24, 0.36, 0.48])
    ax.set_xlabel(r"akım yoğunluğu $|i|$ (A/cm$^2$, log)"); ax.set_ylabel(r"$|\eta|$ (V)")
    ax.set_title("Demir üzerinde H₂: her ×10 akım 0.12 V'a mal olur", fontsize=8.5, color="#444")
    ax.set_xlim(-6.2, -1.6); ax.set_ylim(-0.06, 0.56)
    kaydet(fig, "tafel-merdiven")


def difuzyon_tabakasi():
    fig, ax = plt.subplots(figsize=(5.4, 2.8))
    ax.add_patch(Rectangle((-0.35, 0), 0.35, 1.15, fc="#9aa3ab", ec="#444"))
    ax.text(-0.175, 0.5, "elektrot\n(katot)", rotation=90, ha="center", va="center", fontsize=8)
    d = 1.0
    ax.plot([0, 2.2], [1, 1], color=GR, lw=1.4, label=r"akım yok: $C_s = C_b$")
    ax.plot([0, d, 2.2], [0.5, 1, 1], color=KA, lw=1.4, label=r"$i = \frac{1}{2}i_L$: $C_s = \frac{1}{2}C_b$")
    ax.plot([0, d, 2.2], [0, 1, 1], color="#b23b3b", lw=1.4, label=r"$i = i_L$: $C_s = 0$")
    ax.axvline(d, color="#333", ls=":", lw=0.9)
    ok(ax, 0.02, 1.08, d, 1.08, "#333", lw=0.8, ms=7, stil="<|-|>")
    ax.text(d / 2, 1.11, r"difüzyon tabakası $\delta$", ha="center", fontsize=8)
    ax.text(1.6, 1.06, "çözelti (bulk)", ha="center", fontsize=8)
    ok(ax, 0.8, 0.3, 0.2, 0.3, "#555", lw=0.9, ms=8); ax.text(0.5, 0.18, "iyon akısı", ha="center", fontsize=7.5)
    ax.set_xlim(-0.4, 2.2); ax.set_ylim(-0.05, 1.22)
    ax.set_yticks([0, 0.5, 1]); ax.set_yticklabels(["0", r"$\frac{1}{2}C_b$", r"$C_b$"])
    ax.set_xticks([0, d]); ax.set_xticklabels(["0", r"$\delta$"])
    ax.set_xlabel("yüzeyden uzaklık x"); ax.set_ylabel("reaktan derişimi")
    ax.legend(fontsize=7.5, frameon=False, loc="lower right")
    kaydet(fig, "difuzyon-tabakasi")


def oksijen_katodik(E, iL, i0=1e-10, Eeq=0.815, b=-0.12, i0h=1e-6, ebh=-0.414, bh=-0.12):
    ik = i0 * 10 ** ((E - Eeq) / b)
    io2 = ik * iL / (ik + iL)
    ih = np.where(E < ebh, i0h * 10 ** ((E - ebh) / bh), 0.0)
    return io2 + ih


def polarizasyon_egrisi():
    fig, ax = plt.subplots(figsize=(5.4, 3.3))
    E = np.linspace(0.78, -1.0, 600)
    i = oksijen_katodik(E, 3e-5)
    ax.plot(np.log10(i), E, color=KA, lw=1.8)
    ax.axvline(np.log10(3e-5), color=GR, ls=":", lw=0.9)
    ax.axhline(-0.414, color=SU, ls="--", lw=0.9); ax.text(-8.9, -0.39, "a çizgisi (pH 7): −0.414 V", fontsize=7.5, color=SU)
    ax.text(-7.6, 0.45, r"$O_2$ redüksiyonu:" + "\naktivasyon (Tafel)", fontsize=8)
    ax.text(-4.35, 0.05, r"$O_2$ difüzyon sınırı" + "\n(plato, $i_L$)", fontsize=8)
    ax.text(-4.4, -0.8, r"$H_2$ çıkışı" + "\nakımı artırır", fontsize=8)
    ax.set_xlim(-9, -2); ax.set_ylim(-1.0, 0.8)
    ax.set_xlabel(r"$\log|i|$ ($i$: A/cm$^2$)"); ax.set_ylabel("E (V vs SHE)")
    ax.set_title("Havalandırılmış nötr suda çelik, katodik eğri (şematik)", fontsize=8.5, color="#444")
    kaydet(fig, "polarizasyon-egrisi")


# ---------------------------------------------------------------- Hafta 6
def tafel_dogru(x, Eeq, logi0, b):
    return Eeq + b * (x - logi0)


def evans_zn():
    fig, ax = plt.subplots(figsize=(5.6, 3.4))
    xc = np.linspace(-10, -3, 10); xa = np.linspace(-7, -3, 10)
    ax.plot(xc, tafel_dogru(xc, 0, -10, -0.12), color=KA, lw=1.8)
    ax.plot(xa, tafel_dogru(xa, -0.76, -7, 0.06), color=AN, lw=1.8)
    xi = -4.78; Ei = -0.627
    ax.plot([xi, xi], [-0.85, Ei], ":", color="#333", lw=0.9); ax.plot([-10, xi], [Ei, Ei], ":", color="#333", lw=0.9)
    ax.plot(xi, Ei, "o", color="#333", ms=5)
    ax.text(-9.9, Ei + 0.02, r"$E_{corr} = -0.63$ V", fontsize=8)
    ax.text(xi + 0.1, -0.83, r"$\log i_{corr} = -4.8$", fontsize=8)
    ax.plot(-10, 0, "s", color=KA, ms=5); ax.text(-9.8, 0.0, r"$H^+/H_2$ (Zn üzerinde): $E_{eq}=0$, $i_0=10^{-10}$", fontsize=7.5, color=KA)
    ax.plot(-7, -0.76, "s", color=AN, ms=5); ax.text(-9.9, -0.72, r"$Zn^{2+}/Zn$: $E_{eq}=-0.76$, $i_0=10^{-7}$", fontsize=7.5, color=AN)
    ax.text(-6.6, -0.35, r"katodik: $b_c = -0.12$ V/dek", fontsize=8, color=KA, rotation=-24)
    ax.text(-4.6, -0.48, r"anodik: $b_a = +0.06$", fontsize=8, color=AN)
    ax.set_xlim(-10, -3); ax.set_ylim(-0.85, 0.08)
    ax.set_xlabel(r"$\log|i|$ ($i$: A/cm$^2$)"); ax.set_ylabel("E (V vs SHE)")
    kaydet(fig, "evans-zn")


def evans_zn_fe():
    fig, ax = plt.subplots(figsize=(5.6, 3.4))
    x = np.linspace(-10, -2.5, 10)
    ax.plot(x, tafel_dogru(x, 0, -10, -0.12), "--", color="#6d4fa1", lw=1.4, label=r"$H_2$, Zn üzerinde ($i_0=10^{-10}$)")
    ax.plot(x, tafel_dogru(x, 0, -6, -0.12), "--", color="#5a6b78", lw=1.4, label=r"$H_2$, Fe üzerinde ($i_0=10^{-6}$)")
    xa = np.linspace(-7, -2.5, 10)
    ax.plot(xa, tafel_dogru(xa, -0.76, -7, 0.06), color="#6d4fa1", lw=1.9, label=r"Zn anodik ($E_{eq}=-0.76$)")
    ax.plot(xa, tafel_dogru(xa, -0.44, -7, 0.06), color="#5a6b78", lw=1.9, label=r"Fe anodik ($E_{eq}=-0.44$)")
    for xi, Ei, t, r in [(-4.78, -0.627, r"Zn: $i_{corr}=1.7\times10^{-5}$", "#6d4fa1"),
                         (-3.89, -0.253, r"Fe: $i_{corr}=1.3\times10^{-4}$", "#5a6b78")]:
        ax.plot(xi, Ei, "o", color=r, ms=6); ax.text(xi - 0.2, Ei + 0.06, t, fontsize=8, color=r, ha="right")
    ax.set_xlim(-10, -2.5); ax.set_ylim(-0.85, 0.1)
    ax.set_xlabel(r"$\log|i|$ ($i$: A/cm$^2$)"); ax.set_ylabel("E (V vs SHE)")
    ax.legend(fontsize=7, frameon=False, loc="lower left")
    ax.set_title("Aynı asit (pH 0): emf serisinde daha soy olan demir daha hızlı çözünür", fontsize=8.2, color="#444")
    kaydet(fig, "evans-zn-fe")


def kontrol_tipleri():
    fig, axs = plt.subplots(1, 4, figsize=(7.0, 2.1))
    x = np.linspace(0, 1, 10)
    ayar = [("Anodik kontrol", 1.6, -0.35), ("Katodik kontrol", 0.35, -1.6),
            ("Karışık kontrol", 0.8, -0.8), ("Direnç kontrolü", 0.35, -0.35)]
    for ax, (ad, ba, bc) in zip(axs, ayar):
        ax.plot(x, -0.5 + ba * x, color=AN, lw=1.6)
        ax.plot(x, 0.5 + bc * x, color=KA, lw=1.6)
        if ad.startswith("Direnç"):
            ax.plot([0.55, 0.55], [-0.5 + 0.35 * 0.55, 0.5 - 0.35 * 0.55], color="#333", lw=1.2)
            ax.text(0.6, -0.02, "IR", fontsize=8)
            ax.text(0.5, -0.78, "doğrular kesişmez", ha="center", fontsize=7)
        else:
            xi = 1.0 / (ba - bc); Ei = -0.5 + ba * xi
            ax.plot(xi, Ei, "o", color="#333", ms=4)
        ax.set_title(ad, fontsize=8.5)
        ax.set_xlim(0, 1); ax.set_ylim(-0.9, 0.9)
        ax.set_xticks([]); ax.set_yticks([])
        ax.set_xlabel(r"$\log|i|$", fontsize=8)
    axs[0].set_ylabel("E", fontsize=8)
    fig.tight_layout()
    kaydet(fig, "kontrol-tipleri")


def o2_difuzyon():
    fig, ax = plt.subplots(figsize=(5.6, 3.4))
    E = np.linspace(0.8, -0.75, 600)
    for iL, ls, ad in [(2e-5, "-", "durgun su"), (8e-5, "--", "akan su")]:
        ax.plot(np.log10(oksijen_katodik(E, iL)), E, color=KA, lw=1.7, ls=ls, label=f"$O_2$ redüksiyonu, {ad}")
    xa = np.linspace(-9, -2.5, 10)
    Ea = tafel_dogru(xa, -0.617, -9, 0.06)
    ax.plot(xa, Ea, color=AN, lw=1.7, label=r"$Fe \rightarrow Fe^{2+} + 2e^-$")
    ax.legend(fontsize=7, frameon=False, loc="upper right")
    for iL in (2e-5, 8e-5):
        xi = np.log10(iL); ax.plot(xi, tafel_dogru(xi, -0.617, -9, 0.06), "o", color="#333", ms=5)
    ax.text(-4.55, 0.22, r"$i_{corr} = i_L$", fontsize=8.5)
    ax.text(-9.8, 0.2, r"$O_2+2H_2O+4e^-\rightarrow 4OH^-$" + "\n" + r"($E_{eq}=+0.815$ V, pH 7)", fontsize=7.5, color=KA)
    ax.set_xlim(-10, -2.5); ax.set_ylim(-0.75, 0.85)
    ax.set_xlabel(r"$\log|i|$ ($i$: A/cm$^2$)"); ax.set_ylabel("E (V vs SHE)")
    ax.legend(fontsize=7, frameon=False, loc="lower left")
    ax.set_title("Kesişme katodik eğrinin dikey kısmında: hızı oksijen beslemesi belirler", fontsize=8.2, color="#444")
    kaydet(fig, "o2-difuzyon")


def evans_galvanik():
    fig, ax = plt.subplots(figsize=(5.6, 3.3))
    x = np.linspace(-10, -2, 10)
    ax.plot(x, tafel_dogru(x, 0, -10, -0.12), "--", color="#6d4fa1", lw=1.4, label=r"$H_2$, çinko üzerinde ($i_0 = 10^{-10}$)")
    ax.plot(x, tafel_dogru(x, 0, np.log10(2e-7), -0.12), "--", color=YE, lw=1.5, label=r"$H_2$, bakır üzerinde ($i_0 = 2\times10^{-7}$)")
    xa = np.linspace(-7, -2, 10)
    ax.plot(xa, tafel_dogru(xa, -0.76, -7, 0.06), color=AN, lw=1.8, label=r"$Zn \rightarrow Zn^{2+} + 2e^-$")
    ax.plot(-4.78, -0.627, "o", color="#333", ms=5); ax.text(-4.65, -0.69, "1: yalnız çinko", fontsize=8)
    x2 = (-0.34 - 0.12 * np.log10(2e-7)) / -0.18
    x2 = (0.12 * np.log10(2e-7) + 0.34) / (-0.18) * -1
    # kesisme: -0.12(x - log2e-7) = -0.76 + 0.06(x + 7)
    x2 = (0.12 * np.log10(2e-7) + 0.76 - 0.42) / 0.18
    E2 = tafel_dogru(x2, -0.76, -7, 0.06)
    ax.plot(x2, E2, "o", color="#333", ms=5); ax.text(x2 + 0.12, E2 + 0.03, "2: Zn–Cu çifti", fontsize=8)
    ax.set_xlim(-10, -2); ax.set_ylim(-0.85, 0.08)
    ax.set_xlabel(r"$\log|I|$ ($I$: A; her levha 1 cm$^2$)"); ax.set_ylabel("E (V vs SHE)")
    ax.legend(fontsize=7, frameon=False, loc="upper right")
    kaydet(fig, "evans-galvanik")


def uc_elektrot():
    fig, ax = plt.subplots(figsize=(5.6, 2.9))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5.4); ax.axis("off")
    ax.add_patch(FancyBboxPatch((1.5, 0.3), 5.5, 3.0, boxstyle="round,pad=0.05", fc="#e3f0f8", ec="#555"))
    ax.add_patch(Rectangle((2.3, 1.0), 0.5, 2.9, fc="#8e969c", ec="#444"))
    ax.add_patch(Rectangle((5.6, 1.0), 0.5, 2.9, fc="#d9d9d9", ec="#444"))
    ax.add_patch(Polygon([(3.6, 3.9), (3.9, 3.9), (3.9, 1.9), (3.0, 1.45), (2.9, 1.6), (3.6, 2.0)], fc="#f3e6c4", ec="#8a7a4a"))
    ax.text(2.55, 0.65, "WE", ha="center", fontweight="bold", fontsize=8.5)
    ax.text(3.75, 0.65, "RE", ha="center", fontweight="bold", fontsize=8.5)
    ax.text(5.85, 0.65, "CE", ha="center", fontweight="bold", fontsize=8.5)
    ax.text(4.05, 1.55, "Luggin\nucu", fontsize=7, ha="left")
    ax.add_patch(FancyBboxPatch((7.4, 3.6), 2.4, 1.4, boxstyle="round,pad=0.05", fc="white", ec="#333"))
    ax.text(8.6, 4.3, "potansiyostat\nE'yi ayarlar,\nI'yı okur", ha="center", va="center", fontsize=8)
    for x0, yy in [(2.55, 4.85), (3.75, 4.45), (5.85, 4.05)]:
        ax.plot([x0, x0, 7.4], [3.9, yy, yy], color="#555", lw=0.9)
    ax.text(7.3, 2.7, "WE: numune (alanı bilinen)\nRE: SCE veya Ag/AgCl\nCE: Pt veya grafit", fontsize=8, va="top")
    kaydet(fig, "uc-elektrot")


def tafel_ekstrapolasyon():
    fig, ax = plt.subplots(figsize=(5.4, 3.3))
    Ecorr, icorr, ba, bc = -0.48, 1e-5, 0.06, -0.12
    E = np.linspace(-0.73, -0.26, 4001)
    inet = icorr * (10 ** ((E - Ecorr) / ba) - 10 ** ((E - Ecorr) / bc))
    an = inet > 0
    ax.plot(np.log10(inet[an]), E[an], color=AN, lw=1.8, label="anodik kol")
    ax.plot(np.log10(-inet[~an]), E[~an], color=KA, lw=1.8, label="katodik kol")
    xa = np.linspace(-5, -3, 5); ax.plot(xa, Ecorr + ba * (xa + 5), "--", color=AN, lw=1)
    xc = np.linspace(-5, -3, 5); ax.plot(xc, Ecorr + bc * (xc + 5), "--", color=KA, lw=1)
    ax.axhline(Ecorr, color=GR, ls=":", lw=0.9); ax.text(-7.9, Ecorr + 0.01, r"$E_{corr}$", fontsize=8.5)
    ax.plot(-5, Ecorr, "o", color="#333", ms=5); ax.text(-5.1, Ecorr + 0.03, r"$\log i_{corr}$", fontsize=8.5, ha="right")
    ax.text(-3.4, -0.29, r"eğim $b_a$", fontsize=8, color=AN); ax.text(-3.6, -0.69, r"eğim $b_c$", fontsize=8, color=KA)
    ax.set_xlim(-7, -2.5); ax.set_ylim(-0.75, -0.25)
    ax.set_xlabel(r"$\log|i_{net}|$ ($i$: A/cm$^2$)"); ax.set_ylabel("E (V vs SHE)")
    ax.legend(fontsize=7.5, frameon=False, loc="upper left")
    ax.set_title("Kesikli: düz Tafel kısımlarının $E_{corr}$'a geri uzatılması", fontsize=8.5, color="#444")
    kaydet(fig, "tafel-ekstrapolasyon")


# ---------------------------------------------------------------- Hafta 7
AP = [(-7, -0.62), (-5.6, -0.57), (-4.3, -0.50), (-3.3, -0.40), (-3.0, -0.30), (-3.6, -0.22),
      (-5.0, -0.17), (-5.9, -0.10), (-6.0, 0.05), (-6.0, 0.55), (-5.95, 0.80), (-5.5, 0.92),
      (-4.3, 1.02), (-2.8, 1.10)]


def aktif_pasif_egri(ax, pts=AP, renk=AN, lw=1.9, label=None):
    c = catmull(pts)
    ax.plot(c[:, 0], c[:, 1], color=renk, lw=lw, label=label)
    return c


def aktif_pasif():
    fig, ax = plt.subplots(figsize=(5.6, 3.6))
    aktif_pasif_egri(ax)
    ax.axhspan(-0.75, -0.30, color="#fbe6dc", alpha=0.6, lw=0)
    ax.axhspan(-0.30, 0.85, color="#e3f2e5", alpha=0.6, lw=0)
    ax.axhspan(0.85, 1.25, color="#efe6f5", alpha=0.7, lw=0)
    ax.text(-7.85, -0.55, "AKTİF", fontsize=9, fontweight="bold", color=AN)
    ax.text(-7.85, 0.35, "PASİF\n(ince oksit film)", fontsize=9, fontweight="bold", color=YE)
    ax.text(-7.85, 1.05, "TRANSPASİF", fontsize=9, fontweight="bold", color="#6d4fa1")
    ax.plot(-3.0, -0.30, "o", color="#333", ms=5)
    ax.annotate(r"$E_{pp}$, $i_{crit}$", xy=(-3.0, -0.30), xytext=(-2.7, 0.0), fontsize=8.5,
                arrowprops=dict(arrowstyle="->", lw=0.8))
    ax.annotate(r"$i_{pass}$", xy=(-6.0, 0.3), xytext=(-5.0, 0.3), fontsize=8.5,
                arrowprops=dict(arrowstyle="->", lw=0.8))
    ax.set_xlim(-8, -2); ax.set_ylim(-0.75, 1.25)
    ax.set_xlabel(r"$\log i$ ($i$: A/cm$^2$)"); ax.set_ylabel("E (V vs SHE)")
    kaydet(fig, "aktif-pasif")


def flade():
    fig, ax = plt.subplots(figsize=(5.4, 2.9))
    t = np.linspace(0, 10, 500)
    base = 0.63 + 0.37 * np.exp(-3 * t) - 0.012 * t
    s = 1 / (1 + np.exp(-(t - 6.3) * 9))
    E = base * (1 - s) - 0.45 * s
    ax.plot(t, E, color="#333", lw=1.8)
    ax.axhline(0.63, color=YE, ls=":", lw=1)
    ax.text(2.5, 0.78, r"Flade potansiyeli $E_F \approx 0.63$ V (pH 0)", fontsize=8, color=YE)
    ax.text(2.8, 0.42, "pasif: film var ama bozuluyor", fontsize=8)
    ax.text(7.0, -0.38, "aktif: film çözündü", fontsize=8, color=AN)
    ax.text(0.15, -0.15, "t = 0'da\npasifleştirme\nakımı kesildi", fontsize=7.5)
    ax.set_xlim(0, 10); ax.set_ylim(-0.6, 1.1)
    ax.set_xticks([]); ax.set_xlabel("zaman"); ax.set_ylabel("E (V vs SHE)")
    ax.set_title(r"1 M H$_2$SO$_4$ içinde demir (şematik)", fontsize=8.5, color="#444")
    kaydet(fig, "flade")


def kendiliginden_pasiflesme():
    fig, ax = plt.subplots(figsize=(5.6, 3.6))
    aktif_pasif_egri(ax, label="anodik aktif–pasif eğri")
    x = np.linspace(-8, -2, 10)
    for E6, ad, r in [(-0.45, "1 · zayıf", KA), (0.02, "2 · orta", "#6d4fa1"), (0.5, "3 · güçlü", YE)]:
        ax.plot(x, E6 - 0.12 * (x + 6), "--", color=r, lw=1.4)
        ax.text(-7.9, E6 - 0.12 * (-7.9 + 6) + 0.05, ad, color=r, fontsize=8)
    ax.set_xlim(-8, -2); ax.set_ylim(-0.75, 1.25)
    ax.set_xlabel(r"$\log|i|$ ($i$: A/cm$^2$)"); ax.set_ylabel("E (V vs SHE)")
    ax.legend(fontsize=7.5, frameon=False, loc="upper right")
    ax.set_title("Düz: anodik eğri · Kesikli: farklı oksitleyicilerin katodik eğrileri", fontsize=8.2, color="#444")
    kaydet(fig, "kendiliginden-pasiflesme")


def paslanmaz():
    fig, ax = plt.subplots(figsize=(5.6, 3.5))
    demir = [(-6.5, -0.55), (-4.0, -0.40), (-2.2, -0.15), (-1.4, 0.10), (-1.2, 0.25), (-2.5, 0.35),
             (-4.6, 0.42), (-5.3, 0.50), (-5.3, 0.85), (-4.8, 0.97), (-3.5, 1.07), (-2.2, 1.15)]
    pasl = [(-8, -0.55), (-6.4, -0.48), (-5.3, -0.40), (-5.0, -0.32), (-5.6, -0.27), (-6.2, -0.22),
            (-6.2, 0.10), (-6.2, 0.80), (-6.1, 0.92), (-5.4, 1.02), (-4.0, 1.10)]
    aktif_pasif_egri(ax, demir, renk="#8a6d4b", label="demir")
    aktif_pasif_egri(ax, pasl, renk=YE, label="Fe-18Cr (paslanmaz)")
    ax.text(-4.9, -0.12, r"daha düşük $E_{pp}$," + "\n" + r"daha küçük $i_{crit}$", fontsize=8, color=YE)
    ax.set_xlim(-8, -1); ax.set_ylim(-0.75, 1.25)
    ax.set_xlabel(r"$\log i$ ($i$: A/cm$^2$)"); ax.set_ylabel("E (V vs SHE)")
    ax.legend(fontsize=7.5, frameon=False, loc="upper left")
    kaydet(fig, "paslanmaz")


def klorur_pit():
    fig, ax = plt.subplots(figsize=(5.6, 3.5))
    c = catmull(AP)
    ax.plot(c[:, 0], c[:, 1], color=YE, lw=1.8, label=r"klorürsüz: ~1.0 V'a kadar pasif")
    for Ep, r, ad in [(0.4, KA, r"$E_{pit}$, az $Cl^-$"), (0.1, "#b23b3b", r"$E_{pit}$, çok $Cl^-$")]:
        ax.axhline(Ep, color=r, ls="--", lw=1)
        xx = np.linspace(-6.0, -3.2, 30)
        ax.plot(xx, Ep + 0.03 * (xx + 6.0) ** 2, color=r, lw=1.5)
        ax.text(-7.9, Ep + 0.03, ad, fontsize=8, color=r)
    ax.text(-5.5, 0.6, "oyuklar büyür:\nakım sıçrar", fontsize=8)
    ax.set_xlim(-8, -2); ax.set_ylim(-0.75, 1.25)
    ax.set_xlabel(r"$\log i$ ($i$: A/cm$^2$)"); ax.set_ylabel("E (V vs SHE)")
    ax.legend(fontsize=7.5, frameon=False, loc="upper left")
    kaydet(fig, "klorur-pit")


def oyuklanma():
    fig, ax = plt.subplots(figsize=(6.0, 2.5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 4.85); ax.axis("off")
    ax.text(0, 4.6, "Aynı kütle kaybı…", fontsize=8.5, fontweight="bold")
    ax.add_patch(Rectangle((0.3, 2.6), 9.4, 1.0, fc="#b9c0c6", ec="#555"))
    ax.plot([0.3, 9.7], [4.05, 4.05], "--", color="#555", lw=0.9); ax.text(9.7, 4.12, "orijinal yüzey", ha="right", fontsize=7.5)
    ok(ax, 1.0, 4.05, 1.0, 3.6, "#333", lw=0.8, ms=6, stil="<|-|>"); ax.text(1.15, 3.72, "p (ortalama penetrasyon)", fontsize=7.5)
    ax.text(0, 1.95, "…çok farklı hasar: oyuklanma faktörü = P / p", fontsize=8.5, fontweight="bold")
    yuz = [(0.3, 1.65), (2.6, 1.65), (2.85, 1.25), (3.1, 1.65), (5.2, 1.65), (5.45, 0.35), (5.75, 0.35),
           (6.0, 1.65), (7.8, 1.65), (8.0, 1.35), (8.2, 1.65), (9.7, 1.65), (9.7, 0.15), (0.3, 0.15)]
    ax.add_patch(Polygon(yuz, closed=True, fc="#b9c0c6", ec="#555"))
    ax.plot([0.3, 9.7], [1.65, 1.65], "--", color="#555", lw=0.9)
    ok(ax, 6.5, 1.65, 6.5, 0.35, "#b23b3b", lw=0.9, ms=6, stil="<|-|>"); ax.text(6.65, 0.85, "P (en derin oyuk)", fontsize=7.5, color="#b23b3b")
    kaydet(fig, "oyuklanma")


if __name__ == "__main__":
    for f in [korozyon_hucresi, daniell, referans_dogrusu, gibbs_tepe, nernst_dogrular, su_cizgileri_sekil,
              korozyon_kriteri, galvanik_cift, pourbaix_fe, pourbaix_al, pourbaix_cu, daniell_polarizasyon,
              tafel_merdiven, difuzyon_tabakasi, polarizasyon_egrisi, evans_zn, evans_zn_fe, kontrol_tipleri,
              o2_difuzyon, evans_galvanik, uc_elektrot, tafel_ekstrapolasyon, aktif_pasif, flade,
              kendiliginden_pasiflesme, paslanmaz, klorur_pit, oyuklanma]:
        f()
