string=input("enter sentence:")
char=input("enter character:")
count=0
for i in range(len(string)):
  if(string[i]==char):
   count=count+1
print("the total no of times ",char,"has occurred=",count)
longest=max(string.split(), key=len)
print("longest word is:",longest)
print("and its length is:",len(longest))
print("given string is "+string)
rev=reversed(string)
if list(string)==list(rev):
  print("its a palindrome")
else:
  print("its not a palindroe")
substring=str(input("enter word to display index of first appearance of the substring"))
print("index of first appearance of the substring"+string+" is")
print(string.find(string))
'''if(string.find(substring)):
  #print("substring not found")
else:
  print("substring found")'''	
#print("following are the count the frequency of each wordin a given string")
def freq(string):
  string=string.split()
  str2=[]
  for i in string:
    if i not in str2:
      str2.append(i)
  for i in range(0, len(str2)):
    print('count of frequency', str2[i], 'is:',string.cout(str2[i]))	
	   


