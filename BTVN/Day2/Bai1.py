# Nhập vào hai số a và b
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

# a cộng b
print("a + b =", a + b)

# a trừ b
print("a - b =", a - b)

# a nhân b
print("a * b =", a * b)

# a chia lấy nguyên b
print("a // b =", a // b)

# a mũ b
print("a ** b =", a ** b)

# a chia dư b
print("a % b =", a % b)

# so sánh a và b
if a > b:
    print("a lớn hơn b")
elif a < b:
    print("a nhỏ hơn b")
else:
    print("a bằng b")

# a AND b
print("a AND b =", a & b)

# a OR b
print("a OR b =", a | b)

# a XOR b
print("a XOR b =", a ^ b)

# NOT a == b
print("NOT a == b:", not (a == b))