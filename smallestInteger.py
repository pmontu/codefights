def SmallestInteger(m):
	m = sum(m,[])
	set(m) - set(range(max(m)))
	return  min(set(range(max(m))) - set(m))

print(SmallestInteger([[0, 2], [5, 1]]))