from abc import ABC, abstractmethod


# ==========================
# LỚP TRỪU TƯỢNG CHAMPION
# ==========================
class Champion(ABC):
    def __init__(self, champion_id, name, base_hp, base_atk):
        self.champion_id = champion_id
        self.name = name

        # Edge Case 2
        self.base_hp = base_hp if base_hp > 0 else 100
        self.base_atk = base_atk if base_atk > 0 else 100

    @abstractmethod
    def calculate_skill_damage(self):
        pass

    def get_combat_power(self):
        return self.base_hp + self.calculate_skill_damage() * 1.5

    def __add__(self, other):
        if isinstance(other, Champion):
            return self.get_combat_power() + other.get_combat_power()

        elif isinstance(other, (int, float)):
            return self.get_combat_power() + other

        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __gt__(self, other):
        if isinstance(other, Champion):
            return self.get_combat_power() > other.get_combat_power()
        return NotImplemented


# ==========================
# WARRIOR
# ==========================
class Warrior(Champion):
    def __init__(self, champion_id, name, base_hp, base_atk, shield_bonus):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.shield_bonus = shield_bonus

    def calculate_skill_damage(self):
        return self.base_atk * 2 + self.shield_bonus


# ==========================
# MAGE
# ==========================
class Mage(Champion):
    def __init__(self, champion_id, name, base_hp, base_atk, ability_power):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.ability_power = ability_power

    def calculate_skill_damage(self):
        return self.base_atk * self.ability_power


# ==========================
# DỮ LIỆU BAN ĐẦU
# ==========================
champion_pool = [
    Warrior("WAR01", "Rikkei Knight", 1200, 300, 150),
    Warrior("WAR02", "Steel Guardian", 1500, 250, 200),
    Mage("MAG01", "Rikkei Wizard", 800, 500, 2.0)
]


# ==========================
# HÀM HỖ TRỢ
# ==========================
def find_champion(champion_id):
    for champion in champion_pool:
        if champion.champion_id.upper() == champion_id.upper():
            return champion
    return None


# ==========================
# CHỨC NĂNG 1
# ==========================
def show_champions():
    print("\n--- DANH SÁCH QUÂN CỜ TRONG BỂ TƯỚNG ---")

    print(
        f"{'Mã':<8}|{'Tên tướng':<20}|{'Hệ':<10}|{'HP':<8}|{'ATK':<8}|{'Chỉ số riêng':<20}|{'Chiến lực':<12}"
    )

    print("-" * 100)

    for champion in champion_pool:

        if isinstance(champion, Warrior):
            role = "Warrior"
            special = f"Armor: {champion.shield_bonus}"

        elif isinstance(champion, Mage):
            role = "Mage"
            special = f"Mana: {champion.ability_power}"

        print(
            f"{champion.champion_id:<8}|"
            f"{champion.name:<20}|"
            f"{role:<10}|"
            f"{champion.base_hp:<8}|"
            f"{champion.base_atk:<8}|"
            f"{special:<20}|"
            f"{champion.get_combat_power():.0f}"
        )

    print("-" * 100)


# ==========================
# CHỨC NĂNG 2
# ==========================
def add_champion():

    print("\n1. Warrior")
    print("2. Mage")

    choice = input("Chọn hệ tướng: ")

    champion_id = input("Nhập mã tướng: ").strip()

    # Edge Case 4
    if find_champion(champion_id):
        print("Lỗi: Mã tướng đã tồn tại!")
        return

    name = input("Nhập tên tướng: ")
    hp = int(input("Nhập HP: "))
    atk = int(input("Nhập ATK: "))

    if choice == "1":
        armor = int(input("Nhập Armor: "))

        champion = Warrior(
            champion_id,
            name,
            hp,
            atk,
            armor
        )

    elif choice == "2":
        ability_power = float(input("Nhập Ability Power: "))

        champion = Mage(
            champion_id,
            name,
            hp,
            atk,
            ability_power
        )

    else:
        print("Lựa chọn không hợp lệ!")
        return

    champion_pool.append(champion)

    print("\nThêm tướng thành công!")
    print(
        f"Mã: {champion.champion_id} | "
        f"Tên: {champion.name} | "
        f"Chiến lực: {champion.get_combat_power():.0f}"
    )


# ==========================
# CHỨC NĂNG 3
# ==========================
def compare_champions():

    print("\n--- SO SÁNH SỨC MẠNH 2 QUÂN CỜ ---")

    id1 = input("Nhập mã tướng thứ nhất: ").strip()
    id2 = input("Nhập mã tướng thứ hai: ").strip()

    champion1 = find_champion(id1)
    champion2 = find_champion(id2)

    if champion1 is None:
        print(f"Mã tướng {id1} không hợp lệ!")
        return

    if champion2 is None:
        print(f"Mã tướng {id2} không hợp lệ!")
        return

    print("\nThông tin so sánh:")

    print(
        f"{champion1.champion_id} - {champion1.name} "
        f"| Chiến lực: {champion1.get_combat_power():.0f}"
    )

    print(
        f"{champion2.champion_id} - {champion2.name} "
        f"| Chiến lực: {champion2.get_combat_power():.0f}"
    )

    if champion1 > champion2:
        print(
            f"\nKết quả: {champion1.champion_id} - {champion1.name} "
            f"mạnh hơn {champion2.champion_id} - {champion2.name}"
        )
    elif champion2 > champion1:
        print(
            f"\nKết quả: {champion2.champion_id} - {champion2.name} "
            f"mạnh hơn {champion1.champion_id} - {champion1.name}"
        )
    else:
        print("\nHai quân cờ có sức mạnh ngang nhau!")


# ==========================
# CHỨC NĂNG 4
# ==========================
def calculate_team_power():

    print("\n--- TÍNH TỔNG CHIẾN LỰC ĐỘI HÌNH ---")

    ids = input(
        "Nhập danh sách mã tướng (cách nhau bởi dấu phẩy): "
    ).split(",")

    team = []

    for champion_id in ids:
        champion_id = champion_id.strip()

        champion = find_champion(champion_id)

        if champion:
            team.append(champion)
        else:
            # Edge Case 3
            print(
                f"Mã tướng {champion_id} không hợp lệ, bỏ qua!"
            )

    if not team:
        print("Không có tướng hợp lệ!")
        return

    print("\nDanh sách đội hình:")

    for index, champion in enumerate(team, start=1):
        print(
            f"{index}. {champion.champion_id} - {champion.name}"
            f" | Chiến lực: {champion.get_combat_power():.0f}"
        )

    total_power = sum(team)

    print(f"\nTổng chiến lực đội hình: {total_power:.0f}")


# ==========================
# MENU CHÍNH
# ==========================
def main():
    while True:

        print("\n========== RIKKEI RPG ==========")
        print("1. Hiển thị bể tướng")
        print("2. Thêm quân cờ mới")
        print("3. So sánh 2 quân cờ")
        print("4. Tính tổng chiến lực đội hình")
        print("5. Thoát")

        choice = input("Chọn chức năng (1-5): ")

        if choice == "1":
            show_champions()

        elif choice == "2":
            add_champion()

        elif choice == "3":
            compare_champions()

        elif choice == "4":
            calculate_team_power()

        elif choice == "5":
            print(
                "\nCảm ơn bạn đã sử dụng "
                "Rikkei RPG - Auto-Battler Manager!"
            )
            break

        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()