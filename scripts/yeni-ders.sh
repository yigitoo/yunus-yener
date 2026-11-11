#!/usr/bin/env bash
# Kullanım: ./scripts/yeni-ders.sh <guz|bahar> "<DERS KODU>" "<Ders Adı>"
set -euo pipefail

if [ $# -lt 3 ]; then
  echo "Kullanım: $0 <guz|bahar> \"MSE4631\" \"Ders Adı\"" >&2
  exit 1
fi

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
case "$1" in
  guz)   KLASOR="guz-2026";   DONEM="Güz 2026";   ISARET="<!-- GUZ -->" ;;
  bahar) KLASOR="bahar-2027"; DONEM="Bahar 2027"; ISARET="<!-- BAHAR -->" ;;
  *) echo "Dönem 'guz' veya 'bahar' olmalı" >&2; exit 1 ;;
esac
KOD="$2"; DERS="$3"

slug() {
  printf '%s' "$1" | sed 'y/çğıöşüÇĞİÖŞÜ/cgiosuCGIOSU/' | tr '[:upper:]' '[:lower:]' \
    | sed -E 's/[^a-z0-9]+/-/g; s/^-+|-+$//g'
}
AD="$(slug "$KOD")-$(slug "$DERS")"
HEDEF="$ROOT/$KLASOR/$AD"

[ -e "$HEDEF" ] && { echo "Zaten var: $KLASOR/$AD" >&2; exit 1; }
cp -R "$ROOT/_sablon/ders" "$HEDEF"

sedi() { sed -i '' "$@" 2>/dev/null || sed -i "$@"; }
sedi -e "s|{{KOD}}|$KOD|g" -e "s|{{DERS}}|$DERS|g" -e "s|{{DONEM}}|$DONEM|g" "$HEDEF/README.md" "$HEDEF/kaynaklar/README.md"

SATIR="| $KOD | [$DERS]($KLASOR/$AD/README.md) | | | |"
awk -v m="$ISARET" -v s="$SATIR" '$0==m{print s} {print}' "$ROOT/DERS-PROGRAMI.md" > "$ROOT/DERS-PROGRAMI.md.tmp"
mv "$ROOT/DERS-PROGRAMI.md.tmp" "$ROOT/DERS-PROGRAMI.md"

echo "Oluşturuldu: $KLASOR/$AD"
