from yogi import tokens


# paraules: list[str] = []
# for paraula in tokens(str):
#    paraules.append(paraula)

# paraules = [paraula for paraula in tokens(str)]

paraules = list(tokens(str))
paraules_ordenades = sorted(paraules)

n = len(paraules_ordenades)
i = 0
while i < n:
    c = 1
    j = i + 1
    while j < n and paraules_ordenades[j] == paraules_ordenades[i]:
        c += 1
        j += 1
    print(paraules_ordenades[i], c)
    i = j
