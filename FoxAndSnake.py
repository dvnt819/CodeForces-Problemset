l = input().split()
rows = int(l[0])
cols = int(l[1])

for i in range(rows):
    if i % 2 == 0: 
        print('#' * cols)
    else:
        if i % 4 == 1:  
            print('.' * (cols - 1) + '#')
        else: 
            print('#' + '.' * (cols - 1))
