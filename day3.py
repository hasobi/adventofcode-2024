import re


def main():
    with open("day3.txt", "rt", encoding="utf-8") as f:
        memory = f.read()

    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    sum_of_muls = sum(
        int(match.group(1)) * int(match.group(2)) for match in pattern.finditer(memory)
    )

    print(f"Part 1: {sum_of_muls}")

    sum_of_muls = 0
    do_start, do_end = 0, memory.find("don't()")

    while True:
        sum_of_muls += sum(
            int(match.group(1)) * int(match.group(2))
            for match in pattern.finditer(memory, do_start, do_end if do_end != -1 else len(memory))
        )

        if do_end == -1:
            break

        do_start = memory.find("do()", do_end)
        do_end = memory.find("don't()", do_start)

    print(f"Part 2: {sum_of_muls}")


if __name__ == "__main__":
    main()