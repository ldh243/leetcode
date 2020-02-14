s = "00110011"
count = [0] * len(s) * 2
c0 = c1 = ans = 0
count[len(s)] = 1
for i in s:
	if int(i): c1 += 1
	else: c0 += 1
	ans += count[c1-c0+len(s)]
	count[c1-c0+len(s)] += 1
	print(i, ans)
print(count)
print(ans)
