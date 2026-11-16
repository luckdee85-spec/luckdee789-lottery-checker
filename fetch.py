import urllib.request
import json

url = "https://lotto.api.rayriffy.com/latest"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req) as res:
    raw = json.loads(res.read().decode("utf-8"))["response"]

formatted = {
    "draw_date": raw["date"],
    "source": "สำนักงานสลากกินแบ่งรัฐบาล",
    "prizes": {
        "first": raw["prizes"][0]["number"],
        "near_first": raw["prizes"][1]["number"],
        "prize_2": raw["prizes"][2]["number"],
        "prize_3": raw["prizes"][3]["number"],
        "prize_4": raw["prizes"][4]["number"],
        "prize_5": raw["prizes"][5]["number"],
        "front3": raw["runningNumbers"][0]["number"],
        "last3": raw["runningNumbers"][1]["number"],
        "last2": raw["runningNumbers"][2]["number"]
    }
}

with open("data/results.json", "w", encoding="utf-8") as f:
    json.dump(formatted, f, ensure_ascii=False, indent=2)
