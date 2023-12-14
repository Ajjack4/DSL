dict1={}

while True:
    data=input("Enter name and phone number seperated by comma:\n")
    if "Exit"==data:
        break
    name,num=data.split(",")
    num=int(num)
    dict1[num]=name
print(dict1)
list1=dict1.keys()
list1=list(list1)
list1.sort()
print(list1)

key=int(input("The number to search for: "))
print("Binary Search using Non-Recursive Method\n")

def binary_search1(list1, key):
    start=0
    end=len(list1)
    
    while start<end:
        mid=(start+end)//2
        if list1[mid]>key:
            end=mid
        elif list1[mid]<key:
            start=mid+1   
        else:
            return mid
    return -1
    
index=binary_search1(list1,key)
if index<0:
    print("{} was not found.".format(key))
else:
    print("{} was found at index {}.".format(key,index))
    print("Details of number found:")
    print(dict1[key]) 
    
print("Binary Search using Recursive Method\n")    

def binary_search(arr,low,high,x):
    if high>=low:
        mid=(high+low)//2
        
        if arr[mid]==x:
            return mid  
        elif arr[mid]>x:
            return binary_search(arr,low,mid-1,x)
        else:
            return binary_search(arr,mid+1,high,x)
            
    else:
        return -1
        
'''while True:
    data=input("Enter name and phone number seperated by comma")
    if data=="Exit":
        break
    name,num=data.split(",")
    num=int(num)
    dict1[num]=name
print(dict1)
list1=dict1.keys()
list1=list(list1)
list1.sort()
print(list1)

key=int(input("The number to search for: "))


result=binary_search(list1,0,len(list1)-1,key)

if result != -1:
    print("Element is present at6 index",str(result))
else:
    print("Element is not present in the array")
    
data1=input("Enter name and mobile number not present in the array")
name,num=data1.split(",")
num=int(num)
dict1[num]=name

print(dict1)
list1=dict1.keys()
list1=list(list1)
list.sort()
print(list1)'''

