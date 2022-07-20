#1
a="Yashan"
print(len(a))
#2
str="yashan"
str_count=str.count('y')
print(str_count)
str_count=str.count('a')
print(str_count)
str_count=str.count('s')
print(str_count)
str_count=str.count('h')
print(str_count)
str_count=str.count('n')
print(str_count)
#3
b="Knowledge"
print(b[:2]+b[7:9])
#5
a="abc"
b="xyz"
new_a=b[:2]+a[2:]
new_b=a[:2]+b[2:]
print(new_a+' '+new_b)
#6
a="special"
if len(a)<=3:
  a+="ing"
else:
  a+="ly"
  print(a)
#9
a="abcde"
n=2
new_a=''
for i in range(0,len(a)):
  if(i!=n):
   new_a+=a[i]
print(new_a)
#10
a="abcd"
print(a[3:]+a[1:3]+a[:1])
#11
a="Virat Kohli"
new_a=''
for i in range (len(a)):
  if i%2==0:
    new_a+=a[i]
print(new_a)
#13
a="YasHanPal"
print(a.lower())
print(a.upper())
print()
#14
#items = input("Input comma separated sequence of words")
#words = [word for word in items.split(",")]
#print(",".join(sorted(list(set(words)))))
print()
#16
print("To add string in middle of another string:")
def insert_string_middle(str,word):
  if len(str)>2:
   return str[:2]+word+str[2:]
print(insert_string_middle('yaan','sh'))
print()
#17
print("TO get a string made of 4 copies of last 2 words:")
str='yashan'
print(str)
if(len(str)>2):
   print(str[-2:]+str[-2:]+str[-2:]+str[-2:])
else:
    print("word contains only 2 characters")
print()    
#18
str='Yashan'
new_str=str[:3]
if len(str)>3:
  print(new_str)
else:
  print(str)