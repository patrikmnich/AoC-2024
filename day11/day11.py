from collections import Counter


def calculate_stones(stones, r):
    stone_count = Counter(stones)

    for i in range(r):
        new_stone_count = Counter()

        for stone, count in stone_count.items():
            if stone == 0:
                new_stone_count[1] += count
            else:
                stone_str = str(stone)
                if len(stone_str) % 2 == 0:
                    half = len(stone_str) // 2
                    left = stone // (10 ** half)
                    right = stone % (10 ** half)
                    new_stone_count[left] += count
                    new_stone_count[right] += count
                else:
                    new_stone_count[stone * 2024] += count

        stone_count = new_stone_count

    return sum(stone_count.values())


contents = list(map(int, open("day11.txt").read().split()))

# Part 1
result = calculate_stones(contents, 25)
print(result)

# Part 2
result2 = calculate_stones(contents, 75)
print(result2)
