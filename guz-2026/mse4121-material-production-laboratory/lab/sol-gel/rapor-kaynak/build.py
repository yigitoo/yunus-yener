import math, sys, os
D=os.path.dirname(os.path.abspath(__file__))
cryst=open(D+'/cryst.svg').read(); amorph=open(D+'/amorph.svg').read()
BL='#1f3a93'; RD='#c0392b'

# ---------- Fig 1: process flow ----------
def box(x,y,w,h,t,fill='#eef2fb'):
    lines=t.split('|'); n=len(lines)
    s=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fill}" stroke="{BL}" stroke-width="1.2"/>'
    for i,l in enumerate(lines):
        yy=y+h/2+(i-(n-1)/2)*12+4
        s+=f'<text x="{x+w/2}" y="{yy}" text-anchor="middle" font-size="10">{l}</text>'
    return s
def arr(x1,y1,x2,y2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#333" stroke-width="1.3" marker-end="url(#ah)"/>'
f1=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 150" font-family="Liberation Sans">',
 '<defs><marker id="ah" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker></defs>']
f1.append(box(5,8,120,34,'Sol I|3 mL TEOS + 5 mL EtOH'))
f1.append(box(5,52,120,34,'Sol II|3 mL H₂O + 5 mL EtOH'))
f1.append(arr(125,25,160,40)); f1.append(arr(125,69,160,54))
f1.append(box(162,26,130,44,'Sol II → Sol I (dropwise)|+ stock NH₄F/NH₄OH|3+3 drops, total 12'))
f1.append(arr(292,48,325,48))
f1.append(box(327,26,105,44,'Sol → Gel|dip coating (before gel)|Tyndall test (after)'))
f1.append(arr(432,48,465,48))
f1.append(box(467,26,100,44,'Drying|100 °C, 24 h'))
f1.append(arr(567,48,598,48))
f1.append(box(600,26,95,44,'Calcination|500 °C, 1 h',fill='#fbeeee'))
f1.append(arr(647,70,647,100))
f1.append(box(470,102,225,40,'SiO₂ nanopowder (0.5 g / 1 g) + PVA + Triton X|→ spin coating · contact angle · Ostwald',fill='#fbeeee'))
f1.append('</svg>'); fig1='\n'.join(f1)

# ---------- Fig 2: Tyndall ----------
f2=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 130" font-family="Liberation Sans" font-size="10">',
 '<rect x="8" y="52" width="60" height="18" rx="3" fill="#555"/><text x="38" y="88" text-anchor="middle">laser</text>',
 f'<line x1="68" y1="61" x2="160" y2="61" stroke="{RD}" stroke-width="2"/>',
 # beaker 1
 '<path d="M160 20 L160 110 L260 110 L260 20" fill="#eaf4ff" stroke="#333" stroke-width="1.5"/>',
 '<line x1="160" y1="32" x2="260" y2="32" stroke="#7aa7d6" stroke-dasharray="4 3"/>',
 f'<line x1="160" y1="61" x2="260" y2="61" stroke="{RD}" stroke-width="0.6" stroke-dasharray="2 5" opacity="0.5"/>',
 '<text x="210" y="124" text-anchor="middle">distilled water: beam NOT visible</text>',
 f'<line x1="260" y1="61" x2="330" y2="61" stroke="{RD}" stroke-width="2"/>',
 # beaker 2 gel
 '<path d="M330 20 L330 110 L430 110 L430 20" fill="#f1f1f1" stroke="#333" stroke-width="1.5"/>',
 '<rect x="331" y="32" width="98" height="77" fill="#e3e3e3"/>',
 f'<line x1="330" y1="61" x2="430" y2="61" stroke="{RD}" stroke-width="5" opacity="0.85"/>']
import random; random.seed(3)
for i in range(9):
    x=338+i*11; a=random.uniform(-2.6,2.6)
    f2.append(f'<line x1="{x}" y1="61" x2="{x+9*math.cos(a)}" y2="{61+12*math.sin(a)}" stroke="{RD}" stroke-width="1" opacity="0.8"/>')
for i in range(14):
    f2.append(f'<circle cx="{random.uniform(336,424):.1f}" cy="{random.uniform(38,104):.1f}" r="1.6" fill="#888"/>')
f2+=[f'<line x1="430" y1="61" x2="500" y2="61" stroke="{RD}" stroke-width="2"/>',
 '<text x="380" y="124" text-anchor="middle">SiO₂ gel: beam clearly visible</text>',
 '<text x="380" y="14" text-anchor="middle">colloidal SiO₂ particles scatter light</text>','</svg>']
fig2='\n'.join(f2)

# ---------- Fig 4: contact angle ----------
def drop(cx,base,a,theta_deg,label,sub,color='#7fb3e6'):
    th=math.radians(theta_deg); R=a/math.sin(th)
    large=1 if theta_deg>90 else 0
    d=f'M{cx-a},{base} A{R:.1f},{R:.1f} 0 {large} 1 {cx+a},{base} Z'
    s=f'<path d="{d}" fill="{color}" stroke="#2c5d8f" stroke-width="1.2"/>'
    s+=f'<line x1="{cx-a-35}" y1="{base}" x2="{cx+a+35}" y2="{base}" stroke="#333" stroke-width="2"/>'
    # tangent line at right contact point
    tx,ty=cx+a,base; L=26
    s+=f'<line x1="{tx}" y1="{ty}" x2="{tx-L*math.cos(th):.1f}" y2="{ty-L*math.sin(th):.1f}" stroke="{RD}" stroke-width="1.2"/>'
    s+=f'<text x="{cx}" y="{base+16}" text-anchor="middle" font-weight="bold">{label}</text>'
    s+=f'<text x="{cx}" y="{base+29}" text-anchor="middle">{sub}</text>'
    return s
f4=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 128" font-family="Liberation Sans" font-size="10">']
f4.append(drop(90,80,48,28,'High SiO₂ (1 g)','small θ → hydrophilic'))
f4.append(drop(275,80,38,55,'Low SiO₂ (0.5 g)','larger θ'))
# superhydrophobic on rough surface
for i in range(12):
    x=405+i*10
    f4.append(f'<rect x="{x}" y="74" width="5" height="6" fill="#555"/>')
f4.append(drop(465,74,10,160,'','',color='#7fb3e6'))
f4.append('<text x="465" y="96" text-anchor="middle" font-weight="bold">Target: superhydrophobic</text>')
f4.append('<text x="465" y="109" text-anchor="middle">θ &gt; 150°, rough + low surface energy</text>')
f4.append('</svg>'); fig4='\n'.join(f4)

html=open(D+'/template.html').read()
for k,v in {'FIG1':fig1,'FIG2':fig2,'CRYST':cryst,'AMORPH':amorph,'FIG4':fig4}.items():
    html=html.replace('{{'+k+'}}',v)
open(D+'/report.html','w').write(html)
print('built')
