import logging

logging.basicConfig(
    filename="tournament_app.log",
    level=logging.INFO,
    format="[%(asctime)s] - [%(levelname)s] - %(message)s"
)

matches = [
    {
        "match_id": "M01",
        "team_a": "T1",
        "team_b": "GenG",
        "score_a": 2,
        "score_b": 1,
        "status": "Completed"
    },
    {
        "match_id": "M02",
        "team_a": "JDG",
        "team_b": "BLG",
        "score_a": 0,
        "score_b": 0,
        "status": "Pending"
    }
]


def determine_winner(match):
    """
    Xác định đội thắng.
    """
    if match["status"] == "Pending":
        return "Not Started"

    if match["score_a"] > match["score_b"]:
        return match["team_a"]

    if match["score_b"] > match["score_a"]:
        return match["team_b"]

    return "Draw"


def find_match_by_id(match_list, match_id):
    """
    Tìm trận đấu theo mã.
    """
    for match in match_list:
        if match["match_id"] == match_id:
            return match
    return None


def input_score(team_name):
    """
    Nhập điểm hợp lệ.
    """
    while True:
        try:
            score = int(input(f"Nhập điểm {team_name}: "))

            if score < 0:
                print("Điểm số phải lớn hơn hoặc bằng 0.")
                logging.error(
                    f"Negative score input detected: {score}"
                )
                continue

            return score

        except ValueError as error:
            print("Điểm số phải là số nguyên. Vui lòng nhập lại.")
            logging.error(
                f"Invalid score input. Error: {error}"
            )


def display_matches(match_list):
    """
    Hiển thị danh sách trận đấu.
    """
    logging.info("User viewed the match list.")

    if not match_list:
        print("Hiện chưa có trận đấu nào trong hệ thống.")
        return

    print("\n--- LỊCH THI ĐẤU & KẾT QUẢ ---")
    print(
        f"{'Mã trận':<10} | {'Đội A':<15} | {'Đội B':<15} | {'Tỷ số':<8} | {'Trạng thái'}"
    )
    print("-" * 70)

    for match in match_list:
        try:
            print(
                f"{match['match_id']:<10} | "
                f"{match['team_a']:<15} | "
                f"{match['team_b']:<15} | "
                f"{match['score_a']}-{match['score_b']:<6} | "
                f"{match['status']}"
            )
        except KeyError as error:
            logging.error(f"Missing key: {error}")
            print("Dữ liệu trận đấu bị lỗi.")


def add_match(match_list):
    """
    Thêm trận đấu mới.
    """
    print("\n--- THÊM TRẬN ĐẤU MỚI ---")

    match_id = input("Nhập mã trận đấu: ").strip()

    if not match_id:
        print("Mã trận đấu không được để trống.")
        logging.warning(
            "User tried to add a match with empty match ID."
        )
        return

    if find_match_by_id(match_list, match_id):
        print(f"Lỗi: Mã trận đấu {match_id} đã tồn tại.")
        logging.warning(
            f"Match ID {match_id} already exists."
        )
        return

    team_a = input("Nhập tên Đội A: ").strip()
    team_b = input("Nhập tên Đội B: ").strip()

    if not team_a or not team_b:
        print("Tên đội không được để trống.")
        logging.warning(
            "User tried to add a match with empty team name."
        )
        return

    match_list.append({
        "match_id": match_id,
        "team_a": team_a,
        "team_b": team_b,
        "score_a": 0,
        "score_b": 0,
        "status": "Pending"
    })

    print(f"Thành công: Đã thêm trận đấu {match_id}.")
    logging.info(f"Match {match_id} added successfully")