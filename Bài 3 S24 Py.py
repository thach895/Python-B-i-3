import re


class MemberCard:
    point_value_vnd = 1000

    def __init__(self, card_id, customer_name):
        self.card_id = card_id
        self.customer_name = customer_name.title()
        self.__points = 0
        self.__tier = "Standard"

    @property
    def points(self):
        return self.__points

    @property
    def tier(self):
        return self.__tier

    @staticmethod
    def is_valid_card_id(card_id):
        pattern = r"^RC\d{2}$"
        return bool(re.match(pattern, card_id))

    def earn_points(self, bill_amount):
        earned = bill_amount // 10000
        self.__points += earned

        upgraded = False

        if self.__points >= 100 and self.__tier != "VIP":
            self.__tier = "VIP"
            upgraded = True

        return earned, upgraded

    def redeem_points(self, points_to_use):
        if points_to_use <= 0:
            return False, 0

        if points_to_use > self.__points:
            return False, 0

        self.__points -= points_to_use

        discount = points_to_use * MemberCard.point_value_vnd

        return True, discount

    @classmethod
    def update_point_value(cls, new_value):
        if new_value > 0:
            cls.point_value_vnd = new_value


cards_database = [
    MemberCard("RC01", "Nguyen Van A"),
    MemberCard("RC02", "Tran Thi B")
]

cards_database[0]._MemberCard__points = 150
cards_database[0]._MemberCard__tier = "VIP"

cards_database[1]._MemberCard__points = 20


def find_card(card_id):
    for card in cards_database:
        if card.card_id == card_id:
            return card
    return None


while True:
    print("\n===== HỆ THỐNG THẺ THÀNH VIÊN RIKKEI COFFEE =====")
    print("1. Xem danh sách thẻ thành viên")
    print("2. Đăng ký thẻ mới")
    print("3. Khách mua hàng (Tích điểm)")
    print("4. Khách dùng điểm (Đổi ưu đãi)")
    print("5. Cập nhật tỷ giá quy đổi điểm")
    print("6. Thoát chương trình")
    print("================================================")

    choice = input("Chọn chức năng (1-6): ")

    if choice == "1":
        print("\n--- DANH SÁCH THẺ THÀNH VIÊN ---")

        if not cards_database:
            print("Chưa có thẻ nào.")
            continue

        for index, card in enumerate(cards_database, start=1):
            print(
                f"{index}. "
                f"Mã: {card.card_id} | "
                f"Tên: {card.customer_name:<20} | "
                f"Điểm: {card.points:<3} | "
                f"Hạng: {card.tier}"
            )

    elif choice == "2":
        print("\n--- ĐĂNG KÝ THẺ THÀNH VIÊN MỚI ---")

        card_id = input("Nhập mã thẻ: ").strip()

        if not MemberCard.is_valid_card_id(card_id):
            print("\nMã thẻ không hợp lệ!")
            print("Định dạng đúng: RC01, RC99...")
            continue

        if find_card(card_id):
            print("\nMã thẻ đã tồn tại trong hệ thống!")
            print("Vui lòng kiểm tra lại.")
            continue

        customer_name = input("Nhập tên khách hàng: ")

        new_card = MemberCard(card_id, customer_name)

        cards_database.append(new_card)

        print("\nĐăng ký thẻ thành viên thành công!")
        print(f"Mã thẻ: {new_card.card_id}")
        print(f"Tên khách hàng: {new_card.customer_name}")
        print(f"Điểm ban đầu: {new_card.points}")
        print(f"Hạng thẻ: {new_card.tier}")

    elif choice == "3":
        print("\n--- KHÁCH MUA HÀNG - TÍCH ĐIỂM ---")

        card_id = input("Nhập mã thẻ: ").strip()

        card = find_card(card_id)

        if not card:
            print("Không tìm thấy thẻ!")
            continue

        try:
            bill_amount = int(input("Nhập tổng tiền hóa đơn: "))
        except ValueError:
            print("Dữ liệu không hợp lệ!")
            continue

        earned, upgraded = card.earn_points(bill_amount)

        print(f"\nKhách hàng: {card.customer_name}")
        print(f"Hóa đơn: {bill_amount:,} VNĐ")
        print(f"Số điểm được tích: {earned}")
        print(f"Tổng điểm hiện tại: {card.points}")

        if upgraded:
            print("\nChúc mừng! Khách hàng đã được nâng hạng lên VIP.")

        print(f"Hạng thẻ hiện tại: {card.tier}")

    elif choice == "4":
        print("\n--- KHÁCH DÙNG ĐIỂM - ĐỔI ƯU ĐÃI ---")

        card_id = input("Nhập mã thẻ: ").strip()

        card = find_card(card_id)

        if not card:
            print("Không tìm thấy thẻ!")
            continue

        try:
            points_to_use = int(input("Nhập số điểm muốn sử dụng: "))
        except ValueError:
            print("Dữ liệu không hợp lệ!")
            continue

        success, discount = card.redeem_points(points_to_use)

        if success:
            print(f"\nĐã trừ {points_to_use} điểm.")
            print(
                f"Khách hàng được giảm giá "
                f"{discount:,} VNĐ vào hóa đơn!"
            )
            print(f"Số điểm còn lại: {card.points}")
            print(f"Hạng thẻ hiện tại: {card.tier}")

        else:
            print("\nKhông thể đổi điểm!")

            if points_to_use > card.points:
                print("Số điểm muốn sử dụng vượt quá số điểm hiện có.")

            elif points_to_use <= 0:
                print("Số điểm sử dụng phải lớn hơn 0.")

            print(f"Điểm hiện tại của khách: {card.points}")
            print(f"Số điểm sau giao dịch: {card.points}")

    elif choice == "5":
        print("\n--- CẬP NHẬT TỶ GIÁ QUY ĐỔI ĐIỂM ---")

        print(
            f"Tỷ giá hiện tại: "
            f"1 điểm = {MemberCard.point_value_vnd:,} VNĐ"
        )

        try:
            new_value = int(
                input("Nhập tỷ giá mới cho 1 điểm: ")
            )
        except ValueError:
            print("Dữ liệu không hợp lệ!")
            continue

        MemberCard.update_point_value(new_value)

        print("\nCập nhật tỷ giá thành công!")
        print(
            f"Tỷ giá mới: "
            f"1 điểm = {MemberCard.point_value_vnd:,} VNĐ"
        )

    elif choice == "6":
        print(
            "\nCảm ơn bạn đã sử dụng hệ thống "
            "thẻ thành viên Rikkei Coffee!"
        )
        break

    else:
        print("Vui lòng chọn từ 1 đến 6.")