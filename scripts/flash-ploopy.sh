#!/usr/bin/env bash
set -u
UF2=/home/neo/Documents/qmk-gallium/ploopy-toggle.uf2
[ -f "$UF2" ] || { echo "Firmware introuvable: $UF2"; exit 1; }
DEV=$(lsblk -rno NAME,LABEL | awk '$2=="RPI-RP2"{print "/dev/"$1}' | head -1)
[ -z "$DEV" ] && { echo "Aucun disque RPI-RP2. Mets le Ploopy Nano 2 en bootloader (double-appui reset / maintien BOOT en branchant) puis relance."; exit 1; }
echo "Disque bootloader: $DEV"
MP=$(mktemp -d); umount "$DEV" 2>/dev/null
mount "$DEV" "$MP" || { echo "mount echec"; rmdir "$MP"; exit 1; }
cp "$UF2" "$MP/"; sync
echo "OK -> firmware Ploopy envoye, il redemarre. (erreur I/O finale = normale)"
umount "$MP" 2>/dev/null; rmdir "$MP" 2>/dev/null
