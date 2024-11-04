# Nhập thông tin
ho_ten = input(" Họ và Tên: ")
gioi_tinh = input("Giới tính: ")
tinh_trang_hon_nhan = input("Tình trạng hôn nhân : ")

# In thông tin và kiểm tra điều kiện tìm người yêu
print("\n--- Thông TinD ---")
print(f"Họ và Tên: {ho_ten}")
print(f"Giới tính: {gioi_tinh}")
print(f"Tình trạng hôn nhân: {tinh_trang_hon_nhan}")

# Kiểm tra điều kiện
if gioi_tinh.lower() in ["nam", "nữ"] and tinh_trang_hon_nhan.lower() == "độc thân":
    print("💖 Bạn phù hợp để tìm người yêu cho Hùng! 💖")
else:
    print("Bạn chưa phù hợp với tiêu chí tìm người yêu cho Hùng.")
