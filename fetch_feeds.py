#!/usr/bin/env python3
"""Download the three NHL feeds the Game Center uses and write them as wrapped JSON.
Only valid responses overwrite files; a failed download leaves the previous good file in place."""
import json, sys, time, urllib.request
BASE = "https://api-web.nhle.com/v1/"
FEEDS = {
    "schedule.json":   ("club-schedule-season/MIN/now", "games"),
    "standings.json":  ("standings/now", "standings"),
    "club-stats.json": ("club-stats/MIN/now", "skaters"),
}
failed = 0
for fname, (path, key) in FEEDS.items():
    try:
        req = urllib.request.Request(BASE + path, headers={"Accept": "application/json", "User-Agent": "notb-game-center-mirror/1.0"})
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.load(r)
        if not isinstance(data.get(key), list) or not data[key]:
            raise ValueError("missing or empty '%s'" % key)
        with open(fname, "w") as f:
            json.dump({"fetched_at": int(time.time()), "source": BASE + path, "data": data}, f, separators=(",", ":"))
        print("OK  ", fname)
    except Exception as e:
        failed += 1
        print("FAIL", fname, e, file=sys.stderr)
sys.exit(1 if failed == len(FEEDS) else 0)
