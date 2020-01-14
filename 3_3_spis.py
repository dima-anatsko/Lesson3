m = [1, 2, 5, 7, 9]
n = [1, 2, 3, 4, 5]
ms = set(m)
ns = set(n)
s1 = list(ms & ns)
s2 = list(ms - ns)
s3 = list(ms ^ ns)
print(s1, s2, s3, sep='\n')
