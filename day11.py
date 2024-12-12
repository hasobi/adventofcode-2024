from collections import Counter
from pathlib import Path

data = Counter(Path('/content/day11.txt.txt').read_text('utf-8').split())


def process(n: int) -> int:
    current = data

    for _ in range(n):
        result = Counter()

        for s, c in current.items():
            l, r = divmod(len(s), 2)
            for b in [1] if s == '0' else [int(s) * 2024] if r else [int(s[:l]), int(s[l:])]:
                result[str(b)] += c

        current = result

    return sum(current.values())


print("Part 1:", process(25))
print("Part 2:", process(75))
