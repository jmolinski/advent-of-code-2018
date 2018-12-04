from collections import defaultdict, Counter
from copy import deepcopy


with open("data.txt") as f:
    rows = sorted(  # split into sanitized parts & sort chronologically
        [
            x.strip().replace("[", "").replace("]", " ").replace(":", " ").split()
            for x in f.readlines()
        ],
        key=lambda x: x[0] + x[1] + x[2],
    )

    guards_sleep_minutes = defaultdict(list)
    guard_id = None

    for i, row in enumerate(rows):
        if row[3] == "Guard":
            guard_id = row[4][1:]
        elif row[3] == "falls":
            start = int(row[2])
            stop = int(rows[i + 1][2]) if rows[i + 1][3] == "wakes" else 59

            guards_sleep_minutes[guard_id].extend(list(range(start, stop)))

    guard_sleep_stats = {
        int(guard): {
            "total_time": len(sleep_minutes),
            "top_minute": Counter(sleep_minutes).most_common(1)[0],
        }
        for guard, sleep_minutes in guards_sleep_minutes.items()
    }


def part1():
    guard_info = max(guard_sleep_stats.items(), key=lambda s: s[1]["total_time"])
    return guard_info[0] * guard_info[1]["top_minute"][0]


def part2():
    guard_info = max(guard_sleep_stats.items(), key=lambda s: s[1]["top_minute"][1])
    return guard_info[0] * guard_info[1]["top_minute"][0]


print("1)", part1(), "\n2)", part2())
