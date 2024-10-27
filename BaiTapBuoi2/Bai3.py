# 1. In ra chuỗi “Chao mung den CLB Tin Hoc HIT”
print("Chao mung den CLB Tin Hoc HIT")

# 2. In ra câu: CLB Tin Hoc HIT truc thuoc Khoa CNTT  - “10 diem”
print("CLB Tin Hoc HIT truc thuoc Khoa CNTT - \"10 diem\"")

# 3. Cho chuỗi: “CLB Tin Hoc HIT truc thuoc Khoa CNTT ”. In ra tất cả các chữ cái in hoa trong chuỗi.
chuoi = "CLB Tin Hoc HIT truc thuoc Khoa CNTT"
chu_cai_hoa = ''.join(filter(str.isupper, chuoi))
print("Các chữ cái in hoa:", chu_cai_hoa)

# 4. In ra các chữ cái thường của chuỗi trên.
chu_cai_thuong = ''.join(filter(str.islower, chuoi))
print("Các chữ cái thường:", chu_cai_thuong)

# 5. Kiểm tra xem từ ‘CNTT’ có thuộc chuỗi không, nếu có in ra ‘Yes’, ngược lại in ra ‘No’
if 'CNTT' in chuoi:
    print("Yes")
else:
    print("No")

# 6. Thay thế các chữ hoa thành thường và ngược lại, sau đó in ra màn hình.
chuoi_dao_nguoc = chuoi.swapcase()
print("Chuỗi sau khi thay đổi chữ hoa thành thường và ngược lại:", chuoi_dao_nguoc)
