w1=input()
w2=input()
length_w1=len(w1)
length_w2=len(w2)
index=w1[:length_w1-length_w2]
stars=length_w1

second=w1[length_w1:]
result=index+("*"*stars)+second
print(result)
