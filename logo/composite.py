import subprocess,re
# splash original (texte CORNE CHOC PRO à garder)
src=subprocess.check_output(["git","-C","/home/neo/Documents/keebart-qmk","show",
  "HEAD:keyboards/keebart/corne_choc_pro/keymaps/miryoku_oled/bitmaps.h"]).decode()
by=[int(x,16) for x in re.findall(r"0x[0-9a-fA-F]+",re.search(r"STARTUP_BITMAP \[\] PROGMEM = \{(.*?)\};",src,re.S).group(1))]
W,H=64,128
orig=[[ (by[(r//8)*W+c]>>(r%8))&1 for c in range(W)] for r in range(H)]
# nouvelle image : garder texte (rows>=62), effacer le logo Keebart (haut), poser NixOS
SPLIT=62
new=[[0]*W for _ in range(H)]
for r in range(SPLIT,H): new[r]=orig[r][:]
lg=open("/tmp/logo.gray","rb").read()   # NixOS 50x50 gris
for r in range(50):
    for c in range(50):
        if lg[r*50+c]>110:
            Y,Xc=4+r,7+c
            if 0<=Y<H and 0<=Xc<W: new[Y][Xc]=1
out=[]
for pg in range(H//8):
    for col in range(W):
        b=0
        for bit in range(8):
            if new[pg*8+bit][col]: b|=1<<bit
        out.append(b)
body="\n".join("    "+", ".join("0x%02x"%v for v in out[i:i+16])+"," for i in range(0,len(out),16)).rstrip(",")
# patch STARTUP_BITMAP
bm=open("/home/neo/Documents/keebart-qmk/keyboards/keebart/corne_choc_pro/keymaps/miryoku_oled/bitmaps.h").read()
bm=re.sub(r"(static const char STARTUP_BITMAP \[\] PROGMEM = \{)(.*?)(\};)",lambda m:m.group(1)+"\n"+body+"\n"+m.group(3),bm,flags=re.S)
open("/home/neo/Documents/keebart-qmk/keyboards/keebart/corne_choc_pro/keymaps/miryoku_oled/bitmaps.h","w").write(bm)
# aperçu
print("=== NOUVEAU SPLASH (NixOS + CORNE CHOC PRO conservé) ===")
for row in range(0,128,3):
    print("".join("#" if new[row][c] else " " for c in range(W)))
