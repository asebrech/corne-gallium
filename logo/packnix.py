import struct
def read_gray(path,w,h):
    d=open(path,'rb').read()
    return [[1 if d[r*w+c]>110 else 0 for c in range(w)] for r in range(h)]
def pack(grid,w,h):
    o=[]
    for pg in range(h//8):
        for col in range(w):
            b=0
            for bit in range(8):
                if grid[pg*8+bit][col]: b|=1<<bit
            o.append(b)
    return o
def fmt(a,per=16): return "\n".join("    "+", ".join("0x%02x"%v for v in a[i:i+per])+"," for i in range(0,len(a),per)).rstrip(",")
# emblème 24x24
eg=read_gray("/tmp/emb.gray",24,24); emb=pack(eg,24,24)
# splash: logo 50x50 placé en (7,4), + texte
lg=read_gray("/tmp/logo.gray",50,50)
S=[[0]*64 for _ in range(128)]
ox,oy=7,4
for r in range(50):
    for c in range(50):
        if lg[r][c] and 0<=oy+r<128 and 0<=ox+c<64: S[oy+r][ox+c]=1
F={'G':["..####..",".#....#.","#.......","#..###..","#....#..",".#...#..","..####..","........"],'A':["..###...",".#...#..","#.....#.","#.....#.","#######.","#.....#.","#.....#.","........"],'L':["#.......","#.......","#.......","#.......","#.......","#.......","#######.","........"],'I':["#####...","..#.....","..#.....","..#.....","..#.....","..#.....","#####...","........"],'U':["#.....#.","#.....#.","#.....#.","#.....#.","#.....#.","#.....#.",".#####..","........"],'M':["#.....#.","##...##.","#.#.#.#.","#..#..#.","#.....#.","#.....#.","#.....#.","........"],'R':["######..","#.....#.","#.....#.","######..","#.##....","#..##...","#...##..","........"],'Y':["#.....#.",".#...#..","..#.#...","...#....","...#....","...#....","...#....","........"],'O':["..###...",".#...#..","#.....#.","#.....#.","#.....#.",".#...#..","..###...","........"],'K':["#....#..","#...#...","#..#....","###.....","#..#....","#...#...","#....#..","........"],' ':["........"]*8}
def ct(s,y):
    x0=(64-len(s)*8)//2
    for j,ch in enumerate(s):
        g=F.get(ch,F[' '])
        for r in range(8):
            for c in range(8):
                if g[r][c]=='#' and 0<=y+r<128 and 0<=x0+j*8+c<64: S[y+r][x0+j*8+c]=1
ct("GALLIUM",96); ct("MIRYOKU",110)
splash=pack(S,64,128)
open("/tmp/nix.out","w").write("===SPLASH===\n"+fmt(splash)+"\n===EMBLEM===\n"+fmt(emb)+"\n")
print("=== EMBLÈME 24x24 (NixOS officiel) ===")
for row in range(24):
    pg=row//8;bit=row%8;print("".join("#" if (emb[pg*24+col]>>bit)&1 else "." for col in range(24)))
