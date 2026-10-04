"""Fetch one public Scholar profile and publish only citation statistics.

No proxy or CAPTCHA handling. A blocked/invalid response leaves saved data intact.
"""
import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urlsplit
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

SCHOLAR_ID = "rAgss7MAAAAJ"


def number(value):
    text = value.strip().replace(",", "").replace("\u00a0", "")
    if not re.fullmatch(r"\d+", text):
        raise ValueError("Missing or invalid citation count")
    return int(text)


def parse_profile(html, updated=None):
    soup = BeautifulSoup(html, "html.parser")
    # Find the English Citations row, with or without an intervening tbody.
    rows = soup.select("#gsc_rsb_st tr")
    total = next((row.select_one(".gsc_rsb_std") for row in rows
                  if row.select_one(".gsc_rsb_sc1") and
                  row.select_one(".gsc_rsb_sc1").get_text(strip=True) == "Citations"), None)
    if not soup.select_one("#gsc_prf_in") or total is None:
        raise ValueError("Scholar profile unavailable or verification required")
    papers = {}
    for row in soup.select(".gsc_a_tr"):
        title = row.select_one(".gsc_a_at")
        count = row.select_one(".gsc_a_ac")
        if title is None or count is None:
            raise ValueError("Incomplete publication row")
        publication_id = parse_qs(urlsplit(title.get("href", "")).query).get("citation_for_view", [""])[0]
        if not publication_id.startswith(SCHOLAR_ID + ":"):
            raise ValueError("Unexpected Scholar profile identifier")
        value = count.get_text(strip=True)
        papers[publication_id] = {"title": title.get_text(" ", strip=True), "num_citations": number(value) if value else 0}
    if not papers:
        raise ValueError("No publications found; existing data retained")
    return {"scholar_id": SCHOLAR_ID, "source": "Google Scholar", "citedby": number(total.get_text()),
            "publications": papers, "updated": updated or datetime.now(timezone.utc).isoformat(timespec="seconds")}


def write_stats(data, output):
    output.mkdir(parents=True, exist_ok=True)
    badge = {"schemaVersion": 1, "label": "citations", "message": str(data["citedby"]), "color": "163e40"}
    for name, payload in [("gs_data.json", data), ("gs_data_shieldsio.json", badge)]:
        target = output / name
        temporary = output / (name + ".tmp")
        temporary.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
        temporary.replace(target)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("results"))
    parser.add_argument("--html-file", type=Path, help="Parse a saved profile for offline validation")
    args = parser.parse_args()
    try:
        if args.html_file:
            html = args.html_file.read_text()
        else:
            url = "https://scholar.google.com/citations?" + urlencode({"user": SCHOLAR_ID, "hl": "en", "pagesize": 100})
            request = Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept-Language": "en"})
            with urlopen(request, timeout=30) as response:
                html = response.read().decode("utf-8")
        write_stats(parse_profile(html), args.output)
    except Exception as exc:
        raise SystemExit(f"Scholar refresh failed; existing data retained: {exc}")
