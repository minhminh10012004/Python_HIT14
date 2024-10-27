# Nhập một chuỗi ký tự
string = input("Nhập một chuỗi ký tự: ")

#Kiểm tra xem có chữ "hit" hoặc "HIT" trong chuỗi hay không
if "hit" in string.lower():
    print("True")
else:
    print("False")

#Kiểm tra xem không có chữ số "15" trong chuỗi hay không
if "15" not in string:
    print("True")
else:
    print("False")
