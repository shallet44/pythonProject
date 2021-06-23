a, b = map(int, input().split())
if a < b :
    a, b = b, a
gcd = 0
lcm = 0
r = b
ab = a*b
while a % r != 0:
    r = a % b
    a = b
    b = r
gcd = r
lcm = int(ab/gcd)
print(gcd),print(lcm)
