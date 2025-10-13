k,d,a = map(int,input().split("/"))

if ((k+a) < d) or (d == 0):
    he = 'hasu'
else:
    he = 'gosu'

print(he)