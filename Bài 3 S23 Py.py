import math
import os
from datetime import datetime, timedelta

flights = [
    {
        "flight_id": "RA001",
        "passengers": 154,
        "depart_time": "2026-06-15 08:00:00",
        "duration_min": 120
    },
    {
        "flight_id": "RA002",
        "passengers": 85,
        "depart_time": "2026-06-15 13:30:00",
        "duration_min": 45
    }
]


def show_flights():
    print("----- DANH SÁCH CHUYẾN BAY & HẬU CẦN -----")

    for index, flight in enumerate(flights, start=1):
        water_boxes = math.ceil(
            flight["passengers"] / 10
        )

        print(
            f"{index}. Mã: {flight['flight_id']} | "
            f"Khởi hành: {flight['depart_time']} | "
            f"Số khách: {flight['passengers']} | "
            f"Dự phòng: {water_boxes} thùng nước."
        )


def check_duplicate_id(flight_id, flight_list):
    flight_id = flight_id.strip().upper()

    for flight in flight_list:
        if flight["flight_id"] == flight_id:
            return True

    return False


def add_flight():
    print("----- TIẾP NHẬN CHUYẾN BAY MỚI -----")

    flight_id = input(
        "Nhập mã chuyến bay: "
    ).strip().upper()

    if check_duplicate_id(
        flight_id,
        flights
    ):
        print(
            "Lỗi: Mã chuyến bay đã tồn tại!"
        )
        return

    try:
        passengers = int(
            input(
                "Nhập số lượng hành khách: "
            )
        )

        depart_time = input(
            "Nhập thời gian cất cánh (YYYY-MM-DD HH:MM:SS): "
        )

        datetime.strptime(
            depart_time,
            "%Y-%m-%d %H:%M:%S"
        )

        duration_min = int(
            input(
                "Nhập số phút bay: "
            )
        )

    except ValueError:
        print(
            "Sai định dạng thời gian! "
            "Vui lòng nhập đúng chuẩn "
            "YYYY-MM-DD HH:MM:SS"
        )
        return

    new_flight = {
        "flight_id": flight_id,
        "passengers": passengers,
        "depart_time": depart_time,
        "duration_min": duration_min
    }

    flights.append(new_flight)

    print(
        f">> Thêm chuyến bay "
        f"{flight_id} thành công!"
    )


def calculate_eta():
    print(
        "----- TÍNH TOÁN THỜI GIAN HẠ CÁNH (ETA) -----"
    )

    flight_id = input(
        "Nhập mã chuyến bay cần tính: "
    ).strip().upper()

    for flight in flights:

        if flight["flight_id"] == flight_id:

            depart_time = datetime.strptime(
                flight["depart_time"],
                "%Y-%m-%d %H:%M:%S"
            )

            eta = depart_time + timedelta(
                minutes=flight["duration_min"]
            )

            print(
                f"-> Chuyến bay {flight_id} "
                f"cất cánh lúc: "
                f"{flight['depart_time']}"
            )

            print(
                f"-> Thời gian hạ cánh "
                f"dự kiến (ETA): {eta}"
            )

            return

    print("Không tìm thấy chuyến bay.")


def create_log_directory():

    print(
        "----- KHỞI TẠO THƯ MỤC HỆ THỐNG -----"
    )

    folder_name = "aviation_logs"

    if not os.path.exists(folder_name):

        print(
            f"[SYSTEM] Thư mục "
            f"'{folder_name}' chưa tồn tại. "
            f"Đang tiến hành khởi tạo..."
        )

        os.mkdir(folder_name)

        print(
            "[SYSTEM] Tạo thư mục thành công!"
        )

    else:
        print(
            "Thư mục đã tồn tại, "
            "bỏ qua bước khởi tạo"
        )


while True:

    print("\n===== HỆ THỐNG ĐIỀU HÀNH BAY RIKKEI AVIATION =====")
    print("1. Hiển thị lịch trình và Thống kê hậu cần")
    print("2. Tiếp nhận chuyến bay mới")
    print("3. Tính thời gian hạ cánh dự kiến (ETA)")
    print("4. Khởi tạo thư mục lưu trữ log hệ thống")
    print("5. Thoát chương trình")
    print("==================================================")

    try:
        choice = int(
            input("Nhập lựa chọn của bạn: ")
        )

        if choice == 1:
            show_flights()

        elif choice == 2:
            add_flight()

        elif choice == 3:
            calculate_eta()

        elif choice == 4:
            create_log_directory()

        elif choice == 5:
            print(
                "Cảm ơn kỹ sư đã sử dụng hệ thống!"
            )
            break

        else:
            print(
                "Vui lòng nhập từ 1 đến 5."
            )

    except ValueError:
        print(
            "Lựa chọn không hợp lệ! "
            "Vui lòng nhập số từ 1 đến 5."
        )