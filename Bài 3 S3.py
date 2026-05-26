
for employee_number in range(1, 4):

    print(f"\n===== NHẬP THÔNG TIN NHÂN VIÊN THỨ {employee_number} =====")

    employee_id = input("Nhập mã nhân viên: ")
    full_name = input("Nhập họ và tên: ")
    department = input("Nhập phòng ban: ")


    if employee_id.strip() == "" or full_name.strip() == "":
        print(" CẢNH BÁO: Mã nhân viên hoặc Họ tên không hợp lệ!")
        print(" Hồ sơ bị từ chối. Chuyển sang nhân viên tiếp theo.")
        continue

    print("Mã nhân viên :", employee_id)
    print("Họ và tên    :", full_name)
    print("Phòng ban    :", department)
