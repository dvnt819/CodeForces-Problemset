x=int(input())
z=input().split()
y=[int(a) for a in z]
maximum=max(y)
minimum=min(y)
max_index=y.index(maximum)
count=max_index
y.pop(max_index)
y.insert(0,maximum)
min_index=y[::-1].index(minimum)
count=count+min_index
print(count)
