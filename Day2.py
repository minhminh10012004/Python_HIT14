print("Buoi hoc thu 2 ")
a=5
b=-1
c=3.3
d="Hi"

#print("a =",a,"b =",b,"c =",c)

#Xem kieu du lieu cua bien
#print("type(a)=",type(a))
#print("type(b)=",type(b))
#print("type(c)=",type(c))
#print("type(d)=",type(d))

#----------Toan tu so hoc----------------------------
print("a+b=",a+b)
print("a-b=",a-b)
print("a/b=",a/b)
print("a//b=",a//b)
print("a*b=",a*b)
print(d*5)
#----------Toan tu so sanh----------------------------
if(a==b):
    print("a bang b")
else:
    print("a khong bang b")

#----------Toan tu logic----------------------------
#String
string = "Python"
print(f"len(string)={len(string)}")
print(f"string[0]={string[0]}")
print(f"string[0:3]={string[0:3]}")
print(f"string[2]={string[2]}")
print(f"Chữ thường:={string.lower()}")
print(f"Chữ hoa:={string.upper()}")

#Tinh the tich hinh lap phuong
s=int(input("S = "))
volume = s**3
print("V=",volume)
l=int(input("L = "))
w=int(input("W = "))
h=int(input("H = "))
v=l*w*h
print("V_hinh_hop_chu_nhat",v)

