letters = ["c", "f", "j"]
target = 'k'
minDis = 30
ans = letters[0]

for i in letters:
	dis = ord(i) - ord(target)
	dis = dis + 26 if dis < 0 else dis
	if 0 < dis < minDis:
		minDis = dis
		ans = i
print(ans)