def areRotation(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    if l1 != l2:
        return 'No'
    temp = ''
    temp = str1+str1
    if(temp.count(str2) > 0):
        return 'Yes'

    return 'No'


str1 = input("Enter String1 :")
str2 = input("Enter String2 :")

print(areRotation(str1, str2))
