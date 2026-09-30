num=input().split()

print(num)
x=int (num[0])
y=int (num[1])
z=int (num[2])

max=x
min=x

if y>max:
    max=y
if z>max:
    max=z

if y<min:
    min=y
if z<min:
    min=z

print(min,max)
