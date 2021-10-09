arr=[1,3,5,6]
k=len(arr)+2
#XOR=arr[0]
XOR=arr[0]
for i in range(1,len(arr)):
    XOR^=arr[i]
for i in range(1,k+1):
    XOR^=i
#print(XOR)
set_bit_no = XOR & ~(XOR-1)
#print(set_bit_no)
x=0
y=0
for i in range(0,len(arr)):
    if(arr[i] & set_bit_no):
        x^=arr[i]
    else:
        y^=arr[i]
for i in range(1,k+1):
    if(i & set_bit_no):
        x^=i
    else:
        y^=i
print(x,y)
    
