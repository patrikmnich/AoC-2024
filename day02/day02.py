contents = [[int(item) for item in line.split()] for line in open("day02.txt")]


def is_report_safe(report) -> bool:
    return (all(report[i] < report[i + 1] and report[i + 1] - report[i] <= 3 for i in range(len(report) - 1)) or
            all(report[i] > report[i + 1] and report[i] - report[i + 1] <= 3 for i in range(len(report) - 1)))


# Part 1
safe_count = 0
for line in contents:
    if is_report_safe(line):
        safe_count += 1

print(safe_count)

# Part 2
safe_count = 0
for line in contents:
    if is_report_safe(line):
        safe_count += 1
    else:
        iterations = [line[:i] + line[i+1:] for i in range(len(line))]
        if any(is_report_safe(iteration) for iteration in iterations):
            safe_count += 1

print(safe_count)
