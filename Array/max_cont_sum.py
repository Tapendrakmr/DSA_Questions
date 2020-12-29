def max_sum(Arr):
    print(Arr)
    meh = 0
    msf = -999999
    for i in range(len(Arr)):
        meh = meh+Arr[i]
        if (meh < Arr[i]):
            meh = Arr[i]
        if msf < meh:
            msf = meh
    return msf


Arr = [int(x) for x in input().split(' ')]
print(max_sum(Arr))
