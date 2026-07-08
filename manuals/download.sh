#!/usr/bin/env bash
# One-off downloader for the Fernwood manuals corpus. PDFs land in this dir (gitignored).
# Re-runnable; skips files already present and valid.
cd "$(dirname "$0")/pdf" || exit 1
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"

dl () {
  local name="$1" url="$2"
  if [ -f "$name" ] && [ "$(file -b --mime-type "$name")" = "application/pdf" ]; then
    printf '  skip (have)  %-34s %s\n' "$name" "$(du -h "$name" | cut -f1)"
    return
  fi
  curl -sSL --fail --retry 2 --max-time 180 -A "$UA" \
    -H "Accept: application/pdf,*/*" -H "Referer: https://www.google.com/" \
    -o "$name" "$url"
  if [ -f "$name" ] && [ "$(file -b --mime-type "$name")" = "application/pdf" ]; then
    printf '  OK          %-34s %s\n' "$name" "$(du -h "$name" | cut -f1)"
  else
    printf '  FAIL        %-34s (not a PDF)\n' "$name"
    [ -f "$name" ] && mv "$name" "$name.bad"
  fi
}

echo "== Vehicles =="
dl gti-2016.pdf                 "https://carworklog.com/stuff/Manual/Owners_Manual-Golf-GTI-Golf-R-US-Edition_Model-Year-2016_Edition-07_2015.pdf"
dl tiguan-2018.pdf              "https://www.vwmanuals.org/wp-content/uploads/2022/07/2017-volkswagen-tiguan.pdf"
dl f150-2006.pdf               "https://www.fordservicecontent.com/Ford_Content/catalog/owner_guides/06f12og1e.pdf"
dl bronco-1989.pdf             "https://archive.org/download/ford-bronco-operating-guide-1988/Ford%20Bronco%20Operating%20Guide%20-%201988.pdf"
dl dr200s-2017.pdf             "https://djebel-club.ru/_ld/0/DR-200-Owners-Manual.pdf"
dl drz400s-2001-service.pdf    "https://archive.org/download/manualzilla-id-6883861/6883861.pdf"
dl drz400s-2001-service-text.pdf "https://archive.org/download/manualzilla-id-6883861/6883861_text.pdf"
dl g22a-2005.pdf               "https://mygolfbuggy.com/maintenance/manuals/yamaha/Yamaha%20G22A%20Petrol%20Owners%20Manual.pdf"

echo "== Equipment =="
dl echo-pb7910t.pdf            "https://www.echo-usa.com/getattachment/c3cfd356-0286-4935-aed2-1d72a4ccb9ce/filev2_"
dl echo-pb250ln.pdf            "https://www.echo-usa.com/getattachment/0f5d7527-b62f-4811-8dcf-da1775a4a285/v2_PB-250LN_P39926_HdMx_010919_e.pdf"
dl echo-pb250ln-parts.pdf      "https://www.echo-usa.com/getattachment/f931f4d8-0bca-4a77-9d39-bc2e85129cd0/PB-250LNes_P40212_011714.pdf"
dl chainsaw-cs352.pdf          "https://www.echo-usa.com/getattachment/e7544d8b-7e45-43ee-94d9-f9f8e2d90270/v2_CS-352_15_090420_es.pdf"
dl chainsaw-cs352-parts.pdf    "https://www.echo-usa.com/getattachment/ed3c52c3-ada0-41d4-a71d-914e2793223d/v2_CS-352es_C19612_021517.pdf"
dl chainsaw-ms290.pdf          "https://ssc.stihl.com/tsa/techdoc-documents/DVS_STIHL/ZBA/ZBA/0458-209-0121-B_ZBA_03_01.pdf"
dl kobalt-km2040x-06.pdf       "https://pdf.lowes.com/useandcareguides/841821012045_use.pdf"
dl homelite-trimmer.pdf        "https://manuals.ttigroupna.com/system/files/7376/original/UT33600_UT33650_trilingual_05.pdf?2017"
dl homelite-blower-vac.pdf     "https://manuals.ttigroupna.com/system/files/9590/original/UT26HBV_HBVEMC_090155040_047_662_trilingual_05.pdf?2019"
dl husqvarna-mower-engine.pdf  "https://images.thdstatic.com/catalog/pdfImages/c5/c5581c61-d6d9-4d4c-9981-6d04d019fe54.pdf"
dl husqvarna-mower-yth24v54.pdf "https://www-static-nw.husqvarna.com/hbd/tdrdownload/v2/pub000080278/doc000141547/OM/gI_kX6EZNTIW0RUL8hkWgSxH2Js"

echo "== done =="
ls -la *.pdf 2>/dev/null | awk '{print $5, $9}'
