import time

contents = open("day06.txt").read().split("\n")


def starting_pos(guard, map) -> (int, int):
    for i in map:
        if guard in i:
            return map.index(i), map[map.index(i)].index(guard)
    return -1


# Part 1

direction = "U"
guard_pos = starting_pos("^", contents)
visited = [guard_pos]

while True:
    match direction:
        case "U":
            if contents[guard_pos[0] - 1][guard_pos[1]] != "#":
                guard_pos = (guard_pos[0] - 1, guard_pos[1])
            else:
                direction = "R"
        case "R":
            if contents[guard_pos[0]][guard_pos[1] + 1] != "#":
                guard_pos = (guard_pos[0], guard_pos[1] + 1)
            else:
                direction = "D"
        case "D":
            if contents[guard_pos[0] + 1][guard_pos[1]] != "#":
                guard_pos = (guard_pos[0] + 1, guard_pos[1])
            else:
                direction = "L"
        case "L":
            if contents[guard_pos[0]][guard_pos[1] - 1] != "#":
                guard_pos = (guard_pos[0], guard_pos[1] - 1)
            else:
                direction = "U"
        case _:
            raise Exception("error occurred")

    if guard_pos[0] < 0 or guard_pos[1] < 0:
        break

    if guard_pos not in visited:
        visited.append(guard_pos)

print(len(visited))

# Part 2

result2 = 0
# print(result2)
