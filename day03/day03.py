import re

contents = open("day03.txt").read()

pattern = "mul\\((\\d+),(\\d+)\\)"

# Part 1
result1 = 0
for match in re.findall(pattern, contents):
    result1 += int(match[0]) * int(match[1])

print(result1)

# Part 2

copy = contents[:]
enabled = True
result2 = 0

while True:
    match = re.search(pattern, copy)
    if not match:
        break

    do_match = re.search("do\\(\\)", copy)
    dont_match = re.search("don't\\(\\)", copy)

    if do_match and do_match.span(0)[0] < match.span(0)[0]:
        enabled = True

    if dont_match and dont_match.span(0)[0] < match.span(0)[0]:
        enabled = False

    print(enabled)
    print(copy)
    if enabled:
        result2 += int(match.groups()[0]) * int(match.groups()[1])

    copy = copy[match.span(0)[1]:]

print(result2)
