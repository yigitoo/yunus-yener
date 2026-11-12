import math, random, sys
random.seed(7)
S3=math.sqrt(3)
def honeycomb(nx, ny):
    pts=[]
    for i in range(-2,nx+2):
        for j in range(-2,ny+2):
            ox=i*S3+j*S3/2; oy=j*1.5
            pts.append((ox,oy)); pts.append((ox,oy+1))
    W=nx*S3; H=ny*1.5
    pts=[p for p in pts if -0.1<=p[0]<=W+0.1 and -0.1<=p[1]<=H+0.1]
    # dedupe
    uniq=[]
    for p in pts:
        if all((p[0]-q[0])**2+(p[1]-q[1])**2>1e-4 for q in uniq): uniq.append(p)
    pts=uniq
    edges=set()
    for a in range(len(pts)):
        for b in range(a+1,len(pts)):
            d=math.dist(pts[a],pts[b])
            if abs(d-1)<0.02: edges.add((a,b))
    return pts,edges,W,H
def nbrs(edges,n):
    nb={i:set() for i in range(n)}
    for a,b in edges: nb[a].add(b); nb[b].add(a)
    return nb
def stone_wales(pts,edges,a,b):
    nb=nbrs(edges,len(pts))
    if len(nb[a])!=3 or len(nb[b])!=3: return False
    an=[x for x in nb[a] if x!=b]; bn=[x for x in nb[b] if x!=a]
    # choose a1 and b1 on same side of line a-b
    ax,ay=pts[a]; bx,by=pts[b]
    side=lambda p:(bx-ax)*(p[1]-ay)-(by-ay)*(p[0]-ax)
    a1=[x for x in an if side(pts[x])>0]; b1=[x for x in bn if side(pts[x])>0]
    a2=[x for x in an if side(pts[x])<0]; b2=[x for x in bn if side(pts[x])<0]
    if not(a1 and b1 and a2 and b2): return False
    a1,a2,b1,b2=a1[0],a2[0],b1[0],b2[0]
    rm=lambda u,v: edges.discard((min(u,v),max(u,v)))
    ad=lambda u,v: edges.add((min(u,v),max(u,v)))
    rm(a,a1); rm(b,b2); ad(a,b2); ad(b,a1)
    mx,my=(ax+bx)/2,(ay+by)/2
    pts[a]=(mx-(ay-my),my+(ax-mx)); pts[b]=(mx-(by-my),my+(bx-mx))
    return True
def relax(pts,edges,fixed,it=400):
    n=len(pts); nb=nbrs(edges,n)
    P=[list(p) for p in pts]
    for _ in range(it):
        F=[[0,0] for _ in range(n)]
        for a,b in edges:
            dx=P[b][0]-P[a][0]; dy=P[b][1]-P[a][1]; d=math.hypot(dx,dy) or 1e-6
            f=(d-1)*0.5
            F[a][0]+=f*dx/d; F[a][1]+=f*dy/d; F[b][0]-=f*dx/d; F[b][1]-=f*dy/d
        for a in range(n):
            for b in range(a+1,n):
                if b in nb[a]: continue
                dx=P[b][0]-P[a][0]; dy=P[b][1]-P[a][1]; d=math.hypot(dx,dy)
                if d<1.6 and d>1e-6:
                    f=(d-1.6)*0.3
                    F[a][0]+=f*dx/d; F[a][1]+=f*dy/d; F[b][0]-=f*dx/d; F[b][1]-=f*dy/d
        for a in range(n):
            if a in fixed: continue
            P[a][0]+=0.3*F[a][0]; P[a][1]+=0.3*F[a][1]
    return [tuple(p) for p in P]
def svg(pts,edges,W,H,scale=26,pad=14):
    sx=lambda x: pad+x*scale; sy=lambda y: pad+(H-y)*scale
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W*scale+2*pad:.0f} {H*scale+2*pad:.0f}">']
    for a,b in edges:
        out.append(f'<line x1="{sx(pts[a][0]):.1f}" y1="{sy(pts[a][1]):.1f}" x2="{sx(pts[b][0]):.1f}" y2="{sy(pts[b][1]):.1f}" stroke="#333" stroke-width="1.3"/>')
    for a,b in edges:
        mx=(pts[a][0]+pts[b][0])/2; my=(pts[a][1]+pts[b][1])/2
        out.append(f'<circle cx="{sx(mx):.1f}" cy="{sy(my):.1f}" r="4.6" fill="#fff" stroke="#c0392b" stroke-width="1.6"/>')
    nb=nbrs(edges,len(pts))
    for i,p in enumerate(pts):
        if nb[i]: out.append(f'<circle cx="{sx(p[0]):.1f}" cy="{sy(p[1]):.1f}" r="3.4" fill="#1f3a93"/>')
    out.append('</svg>')
    return '\n'.join(out)
nx,ny=5,5
pts,edges,W,H=honeycomb(nx,ny)
open(sys.argv[1]+'/cryst.svg','w').write(svg(pts,edges,W,H))
# amorphous
pts2=list(pts); e2=set(edges)
cx,cy=W/2,H/2
cand=sorted(e2,key=lambda e: math.dist(((pts2[e[0]][0]+pts2[e[1]][0])/2,(pts2[e[0]][1]+pts2[e[1]][1])/2),(cx,cy)))
done=[]
for e in cand:
    m=((pts2[e[0]][0]+pts2[e[1]][0])/2,(pts2[e[0]][1]+pts2[e[1]][1])/2)
    if m[0]<1.2 or m[0]>W-1.2 or m[1]<1.2 or m[1]>H-1.2: continue
    if any(math.dist(m,d)<2.6 for d in done): continue
    if stone_wales(pts2,e2,*e): done.append(m)
    if len(done)>=4: break
pts2=[(x+random.uniform(-.18,.18),y+random.uniform(-.18,.18)) for x,y in pts2]
nb=nbrs(e2,len(pts2))
pts2=relax(pts2,e2,fixed=set())
open(sys.argv[1]+'/amorph.svg','w').write(svg(pts2,e2,W,H))
print(len(pts),len(edges),len(done))
