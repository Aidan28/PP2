arr1=set(input().split())
arr2=set(input().split())
arr1.intersection_update(arr2)
print(len(arr1))