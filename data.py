from collections import Counter

history = []

def add_result(result):
    history.append(result)

def get_stats():
    total = len(history)
    c = Counter(history)
    return {
        "total": total,
        "P": c["P"],
        "B": c["B"],
        "T": c["T"],
        "P_pct": round(c["P"]/total*100, 2) if total else 0,
        "B_pct": round(c["B"]/total*100, 2) if total else 0,
        "T_pct": round(c["T"]/total*100, 2) if total else 0,
    }

def get_streaks():
    if not history:
        return {"P": 0, "B": 0, "T": 0}
    longest = {"P": 0, "B": 0, "T": 0}
    current = history[0]
    count = 1
    for r in history[1:]:
        if r == current:
            count += 1
        else:
            longest[current] = max(longest[current], count)
            current = r
            count = 1
    longest[current] = max(longest[current], count)
    return longest

def suggest():
    stats = get_stats()
    if stats["P_pct"] > stats["B_pct"]:
        return "Player"
    elif stats["B_pct"] > stats["P_pct"]:
        return "Banker"
    else:
        return "Sem tendência"