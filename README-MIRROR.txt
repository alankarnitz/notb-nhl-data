OPTIONAL NHL JSON MIRROR (only needed if Playground / your host cannot reach api-web.nhle.com)
Status: UNTESTED by the author of this kit — see the report. Test steps below prove or disprove it in ~5 minutes.

1. Create a NEW public GitHub repo (e.g. notb-nhl-mirror). Upload every file from this folder
   (fetch_feeds.py and .github/workflows/refresh.yml).
2. Repo > Actions > "Refresh NHL mirror" > Run workflow. If it's green, schedule.json, standings.json
   and club-stats.json appear in the repo. If the run FAILS with a 403/timeout, GitHub's servers are also
   blocked by the NHL and this route is dead (use hosting you control instead; the files are plain JSON).
3. In your browser open: https://raw.githubusercontent.com/YOURNAME/notb-nhl-mirror/main/standings.json
   You should see JSON starting {"fetched_at":...
4. WordPress > Tools > NOTB Game Center Health > paste  https://raw.githubusercontent.com/YOURNAME/notb-nhl-mirror/main/
   (with trailing slash) > Save > "Check feeds now".
Contains only public NHL data. No keys or secrets. Plugin rejects mirror data older than 24h.
