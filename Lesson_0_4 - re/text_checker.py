import re

patter = re.compile(r'[A-Z][a-z]*')
matches = []

with open('test.txt') as f:
    lines = f.readlines()

for line in lines:
    match = patter.findall(line)
    if not match:
        continue
    else:
        for mch in match:
            matches.append(mch)

print(matches)
print(len(matches))