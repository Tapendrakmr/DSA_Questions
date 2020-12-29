R = int(input('Enter number of row :'))
C = int(input('Enter number of column :'))
full = []
for _ in range(R):
    arr = [int(x) for x in input().split(' ')]
    full.append(arr)
