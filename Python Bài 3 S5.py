
for branch in range(1, 4):

    total_students = 0

    print(f"\n===== Chi nhánh {branch} =====")

    for classroom in range(1, 4):

        students = int(
            input(f"Nhập số học viên lớp {classroom}: ")
        )

        total_students += students

    print(
        f"Chi nhánh {branch}: "
        f"{total_students} học viên"
    )