
print("===== HỆ THỐNG PHÂN LUỒNG BỆNH NHÂN =====")

patient_name = input(
    "Nhập họ tên bệnh nhân (Ví dụ: Nguyễn Văn A): "
)

patient_age = int(
    input("Nhập tuổi bệnh nhân (0 - 150): ")
)

if patient_name.strip() == "":
    print("\nLỖI: Tên bệnh nhân không hợp lệ!")
    
elif patient_age < 0 or patient_age > 150:
    print("\nLỖI: Tuổi nằm ngoài phạm vi con người (0-150)!")

else:

    if patient_age < 6:
        priority_result = (
            "ƯU TIÊN: Bệnh nhi - "
            "Chuyển thẳng phòng khám Nhi."
        )

    elif patient_age >= 80:
        priority_result = (
            "ƯU TIÊN: Người cao tuổi - "
            "Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."
        )

    else:
        priority_result = (
            "KHÁM THƯỜNG: "
            "Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."
        )

    print("\n===== PHIẾU KHÁM BỆNH ĐIỆN TỬ =====")

    print("Tên bệnh nhân :", patient_name)
    print("Tuổi           :", patient_age)
    print("Phân luồng     :", priority_result)
