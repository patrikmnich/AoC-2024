contents = open("day05.txt").read().split("\n")

pairs, page_sets = [pair.split("|") for pair in contents[:contents.index("")]], [page_set.split(",") for page_set in  contents[contents.index("") + 1:]]

# Part 1
result1 = 0

for pages in page_sets:
    included = [pair for pair in pairs if any([page in pair for page in pages])]
    left = [pair[0] for pair in included]
    right = [pair[1] for pair in included]

    if any([l in pages and r in pages and pages.index(r) < pages.index(l) for l, r in zip(left, right)]):
        continue
    result1 += int(pages[int(len(pages)/2)])

print(result1)

# Part 2

result2 = 0

for pages in page_sets:
    included = [pair for pair in pairs if any([page in pair for page in pages])]
    left = [pair[0] for pair in included]
    right = [pair[1] for pair in included]

    page_cpy = pages[:]
    while any([l in page_cpy and r in page_cpy and page_cpy.index(r) < page_cpy.index(l) for l, r in zip(left, right)]):
        for l, r in zip(left, right):
            if l in page_cpy and r in page_cpy and page_cpy.index(r) < page_cpy.index(l):
                l_index = page_cpy.index(l)
                r_index = page_cpy.index(r)

                page_cpy[l_index], page_cpy[r_index] = page_cpy[r_index], page_cpy[l_index]

    result2 += int(page_cpy[int(len(page_cpy) / 2)]) if page_cpy != pages else 0

print(result2)