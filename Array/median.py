def find_median(self, v):
    # Code here
    v.sort()
    if len(v) % 2 != 0:
        return v[(int(((len(v)+1)/2)-1))]
    else:
        x = v[int(len(v)/2)-1]
        y = v[int((len(v)/2)+1)-1]
        return (x+y)//2
