# corne-gallium

Config perso pour un **Keebart Corne Choc Pro** (filaire, QMK) + un **Ploopy Nano 2**.

- **Alphabet** : Gallium
- **Layout** : Miryoku officiel (home-row mods GACS, layers Nav/Mouse/Media/Num/Sym/Fun/Button)
- **Écrans OLED** : firmware Keebart (contrôleur **SSD1312**), logo **Miryoku** au boot + « CORNE CHOC PRO »
- **Ploopy Nano 2** : bouton = toggle scroll, **+** scroll pilotable depuis le clavier (pont NumLock)

## Matériel

| | |
|---|---|
| Clavier | Keebart Corne Choc Pro filaire — Corne V4.1, RP2040, OLED 1.3" 128×64 **SSD1312** |
| Cible QMK | `keebart/corne_choc_pro/standard` |
| Trackball | Ploopy Nano 2 (RP2040) — `ploopyco/nano_2/rev2_003` |

## Contenu

```
firmware/   .uf2 prêts à flasher (clavier + Ploopy)
keyboard/   keymap OLED (miryoku_oled) + custom_config.h (Gallium + NumLock sur Button)
ploopy/     keymap Nano 2 (toggle scroll + NumLock scroll)
scripts/    flash.sh / flash-ploopy.sh (auto-détection du disque RPI-RP2)
logo/       scripts de génération du splash NixOS
```

## Flasher (rapide, firmware fourni)

**Clavier** — mettre une moitié en bootloader (maintenir `BOOT` en branchant → disque `RPI-RP2`), puis dans un vrai terminal :
```sh
sudo bash scripts/flash.sh    # répéter pour la 2e moitié
```
> `flash.sh` copie `firmware/gallium-miryoku.uf2`. Adapter le chemin dans le script si besoin.

**Ploopy Nano 2** — maintenir le bouton en branchant → `RPI-RP2` :
```sh
sudo bash scripts/flash-ploopy.sh
```

## Utilisation

- **Base** = Gallium (`b l d c v / n r t s g / x q m w z …`), home-row mods GACS.
- **Layers** Miryoku via les pouces (Nav, Mouse, Media, Num, Sym, Fun) + Button (maintien touche du bas extérieure).
- **Scroll Ploopy** — deux moyens :
  1. **Bouton du Ploopy** : un clic = bascule scroll ↔ curseur.
  2. **Clavier** : sur le layer **Button**, la touche à côté de Shift (position « G ») = **NumLock** → bascule le scroll du Ploopy.
- **OLED** : au boot, flocon NixOS + « CORNE CHOC PRO » ; puis stats (layer, WPM, uptime…).

## Rebuild depuis les sources

Le firmware clavier dépend du **fork Keebart** (driver OLED SSD1312 absent du QMK mainline).

### Clavier
```sh
git clone --recurse-submodules --shallow-submodules --depth 1 --branch vial \
  https://github.com/Keebart/vial-qmk-keebart.git keebart-qmk
cd keebart-qmk
# copier les fichiers de config/ de ce repo :
cp ../corne-gallium/keyboard/{keymap.c,config.h,bitmaps.h,rules.mk} \
   keyboards/keebart/corne_choc_pro/keymaps/miryoku_oled/
cp ../corne-gallium/keyboard/custom_config.h users/manna-harbour_miryoku/
# build (SKIP_VERSION obligatoire, sinon "multiple target patterns") :
docker run --rm -v "$PWD":/qmk_firmware -w /qmk_firmware ghcr.io/qmk/qmk_cli \
  bash -c "git config --global --add safe.directory /qmk_firmware; \
  qmk compile -c -kb keebart/corne_choc_pro/standard -km miryoku_oled -e SKIP_VERSION=yes"
```
`custom_config.h` définit Gallium (`MIRYOKU_LAYER_BASE`) — absent du babel de ce fork — et met NumLock sur le layer Button.

### Ploopy Nano 2 (QMK mainline)
```sh
# dans un clone de qmk_firmware mainline :
cp ../corne-gallium/ploopy/keymap.c keyboards/ploopyco/nano_2/keymaps/default/
# IMPORTANT : commenter cette ligne dans keyboards/ploopyco/nano_2/config.h
#   #define PLOOPY_DRAGSCROLL_MOMENTARY   -> pour que le bouton soit un TOGGLE (pas maintien)
qmk compile -kb ploopyco/nano_2/rev2_003 -km default
```
Le `keymap.c` du Ploopy ajoute `pointing_device_task_user` : si NumLock est allumé, la boule scrolle (calcul identique au drag scroll natif). Il s'exécute avant le drag scroll du bouton → jamais de double scroll.

## Crédits

- [Miryoku](https://github.com/manna-harbour/miryoku) (manna-harbour)
- [Keebart vial-qmk](https://github.com/Keebart/vial-qmk-keebart) (driver SSD1312, keymap miryoku_oled)
- Logo : [Miryoku](https://github.com/manna-harbour/miryoku) (`data/logos/miryoku-roa-32.png`)
- Idée scroll clavier : pont NumLock ([QMK PR #13013](https://github.com/qmk/qmk_firmware/pull/13013)), alternative [wiggleball](https://github.com/pandrr/wiggleball)
