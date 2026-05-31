

raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "



def get_standardized_data():
    employees = raw_data.split("|")
    employee_list = []

    for employee in employees:
        fields = employee.split(";")

        employee_id = fields[0].strip().upper()
        full_name = fields[1].strip().title()
        phone = fields[2].strip().replace("-", "")
        department = fields[3].strip().upper()

        if phone.isdigit():
            phone = "******" + phone[6:]
        else:
            phone = "Invalid Format"

        employee_list.append(
            [employee_id, full_name, phone, department]
        )

    return employee_list



while True:

    print("\n===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa dữ liệu và in báo cáo")
    print("3. Tìm kiếm nhân viên theo mã ID")
    print("4. Thoát chương trình")

    try:
        choice = int(input("Nhập lựa chọn: "))
    except:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue
    if choice == 1:
        print("\nDỮ LIỆU GỐC:")
        print(raw_data)

    elif choice == 2:

        employee_list = get_standardized_data()

        print("\nBÁO CÁO NHÂN SỰ")
        print("-" * 70)

        print(
            f"{'ID':<12}"
            f"{'HỌ TÊN':<25}"
            f"{'SĐT':<18}"
            f"{'PHÒNG BAN':<10}"
        )

        print("-" * 70)

        for employee in employee_list:
            print(
                f"{employee[0]:<12}"
                f"{employee[1]:<25}"
                f"{employee[2]:<18}"
                f"{employee[3]:<10}"
            )

    elif choice == 3:

        search_id = input(
            "Nhập mã nhân viên cần tìm: "
        ).strip().upper()

        employee_list = get_standardized_data()

        found = False

        for employee in employee_list:

            if employee[0] == search_id:

                print("\nTHÔNG TIN NHÂN VIÊN")

                print(f"ID        : {employee[0]}")
                print(f"Họ tên    : {employee[1]}")
                print(f"SĐT       : {employee[2]}")
                print(f"Phòng ban : {employee[3]}")

                found = True
                break

        if not found:
            print("Không tìm thấy nhân viên")

    elif choice == 4:
        print("Thoát chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")