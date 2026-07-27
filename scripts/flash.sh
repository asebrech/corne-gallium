#!/usr/bin/env bash
# Flashe gallium-miryoku.uf2 sur la moitie de Corne actuellement en bootloader.
# Detecte automatiquement le disque RPI-RP2 (pas de /dev/sdaX en dur).
set -u
UF2=/home/neo/Documents/qmk-gallium/gallium-miryoku.uf2

[ -f "$UF2" ] || { echo "Firmware introuvable: $UF2"; exit 1; }

DEV=$(lsblk -rno NAME,LABEL | awk '$2=="RPI-RP2"{print "/dev/"$1}' | head -1)
if [ -z "$DEV" ]; then
  echo "Aucun disque RPI-RP2 detecte."
  echo "-> Mets la moitie a flasher en bootloader (maintiens BOOT en branchant, ou double-appui RESET) puis relance."
  exit 1
fi
echo "Disque bootloader detecte : $DEV"

MP=$(mktemp -d)
umount "$DEV" 2>/dev/null
mount "$DEV" "$MP" || { echo "Echec du montage de $DEV"; rmdir "$MP"; exit 1; }

echo "Copie du firmware..."
cp "$UF2" "$MP/" ; sync
echo "OK -> firmware envoye. La moitie va redemarrer automatiquement."
echo "(Un message d'erreur I/O sur la toute derniere ligne est NORMAL : le clavier"
echo " se detache pendant l'ecriture. Le flash a bien eu lieu.)"

umount "$MP" 2>/dev/null
rmdir "$MP" 2>/dev/null
