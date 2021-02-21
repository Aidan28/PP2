arr1=set(input().split())
arr2=set(input().split())
arr3=arr1.intersection(arr2)
print(*sorted(arr3,key=int))