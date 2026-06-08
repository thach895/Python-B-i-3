patients = [
    ["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
    ["BN002", "Tran Thi B", "Nu", "Sot Xuat Huyet"]
]


def validate_gender(gender_input):
    """
    Kiểm tra giới tính hợp lệ.
    """
    gender = gender_input.strip().lower()
    return gender in ["nam", "nu"]


def find_patient_index(patient_list, patient_id):
    """
    Tìm vị trí bệnh nhân theo mã.
    """
    patient_id = patient_id.strip().upper()

    for index, patient in enumerate(patient_list):
        if patient[0] == patient_id:
            return index

    return -1


def display_patients(patient_list):
    """
    Hiển thị danh sách bệnh nhân.
    """
    if len(patient_list) == 0:
        print("Hiện không có bệnh nhân nào đang điều trị.")
        return

    print("----- DANH SÁCH BỆNH NHÂN ĐANG ĐIỀU TRỊ -----")

    for i, patient in enumerate(patient_list, start=1):
        print(
            f"{i}. Mã: {patient[0]} | "
            f"Tên: {patient[1]} | "
            f"Giới tính: {patient[2]} | "
            f"Bệnh: {patient[3]}"
        )


def add_patient(patient_list):
    """
    Tiếp nhận bệnh nhân mới.
    """
    print("----- TIẾP NHẬN BỆNH NHÂN MỚI -----")

    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()

    if len(patient_id) == 0:
        print("Mã bệnh nhân không được để trống!")
        return

    if find_patient_index(patient_list, patient_id) != -1:
        print(
            "Mã bệnh nhân đã tồn tại trong hệ thống, "
            "vui lòng kiểm tra lại!"
        )
        return

    patient_name = input("Nhập tên bệnh nhân: ").strip().title()

    if len(patient_name) == 0:
        print("Tên bệnh nhân không được để trống!")
        return

    while True:
        gender_input = input("Nhập giới tính Nam/Nu: ")

        if validate_gender(gender_input):
            gender = gender_input.strip().capitalize()
            break

        print("Giới tính không hợp lệ, vui lòng nhập lại!")

    diagnosis = input("Nhập chẩn đoán bệnh: ").strip().capitalize()

    new_patient = [
        patient_id,
        patient_name,
        gender,
        diagnosis
    ]

    patient_list.append(new_patient)

    print("Tiếp nhận bệnh nhân thành công!")


def update_diagnosis(patient_list):
    """
    Cập nhật chẩn đoán bệnh.
    """
    print("----- CẬP NHẬT CHẨN ĐOÁN BỆNH -----")

    patient_id = input(
        "Nhập mã bệnh nhân cần cập nhật: "
    ).strip()

    if len(patient_id) == 0:
        print("Mã bệnh nhân không được để trống!")
        return

    index = find_patient_index(patient_list, patient_id)

    if index == -1:
        print(
            f"Không tìm thấy hồ sơ mang mã "
            f"{patient_id.strip().upper()}!"
        )
        return

    print(
        f"Tìm thấy bệnh nhân: "
        f"{patient_list[index][1]}"
    )

    print(
        f"Chẩn đoán hiện tại: "
        f"{patient_list[index][3]}"
    )

    new_diagnosis = input(
        "Nhập chẩn đoán mới: "
    ).strip()

    if len(new_diagnosis) == 0:
        print("Chẩn đoán bệnh không được để trống!")
        return

    patient_list[index][3] = new_diagnosis.capitalize()

    print("Cập nhật chẩn đoán bệnh thành công!")


def search_by_disease(patient_list):
    """
    Tìm kiếm bệnh nhân theo tên bệnh.
    """
    print("----- TÌM KIẾM BỆNH NHÂN THEO TÊN BỆNH -----")

    keyword = input(
        "Nhập từ khóa tên bệnh: "
    ).strip()

    if len(keyword) == 0:
        print("Từ khóa tìm kiếm không được để trống!")
        return

    result_count = 0

    print("Kết quả tìm kiếm:")

    for patient in patient_list:
        if keyword.lower() in patient[3].lower():
            result_count += 1

            print(
                f"{result_count}. Mã: {patient[0]} | "
                f"Tên: {patient[1]} | "
                f"Giới tính: {patient[2]} | "
                f"Bệnh: {patient[3]}"
            )

    if result_count == 0:
        print("Không tìm thấy bệnh nhân nào phù hợp.")

    print(
        f"\nCó tổng cộng {result_count} bệnh nhân "
        f"mắc bệnh liên quan đến '{keyword}'."
    )


while True:
    print("\n===== HỆ THỐNG QUẢN LÝ BỆNH NHÂN RIKKEI =====")
    print("1. Hiển thị danh sách bệnh nhân")
    print("2. Tiếp nhận bệnh nhân mới")
    print("3. Cập nhật chẩn đoán bệnh theo mã BN")
    print("4. Tìm kiếm và thống kê theo tên bệnh")
    print("5. Thoát chương trình")
    print("===========================================")

    choice = input("Nhập lựa chọn của bạn: ")

    if choice == "1":
        display_patients(patients)

    elif choice == "2":
        add_patient(patients)

    elif choice == "3":
        update_diagnosis(patients)

    elif choice == "4":
        search_by_disease(patients)

    elif choice == "5":
        print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
        break

    else:
        print(
            "Lựa chọn không hợp lệ, "
            "vui lòng nhập số từ 1-5!"
        )