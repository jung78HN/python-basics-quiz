from default_quizzes import default_quizzes
from quiz import Quiz


def read_number(prompt: str, minimum: int, maximum: int) -> int:
    while True:
        value = input(prompt).strip()
        try:
            number = int(value)
        except ValueError:
            print(f"{minimum}~{maximum} 사이의 숫자를 입력하세요.")
            continue

        if minimum <= number <= maximum:
            return number
        print(f"{minimum}~{maximum} 사이의 숫자를 입력하세요.")


def read_text(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("공백을 제외한 내용을 입력하세요.")


def show_menu() -> None:
    print("\n=== Python 기초 퀴즈 ===")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")


def play(quizzes: list[Quiz]) -> None:
    if not quizzes:
        print("\n등록된 퀴즈가 없습니다.")
        return

    correct = 0
    total = len(quizzes)
    print(f"\n퀴즈를 시작합니다. 총 {total}문제입니다.")
    for number, quiz in enumerate(quizzes, start=1):
        quiz.display(number)
        selected = read_number("정답 번호 (1~4): ", 1, 4)
        if quiz.is_correct(selected):
            correct += 1
            print("정답입니다!")
        else:
            print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

    score = round(correct / total * 100)
    print(f"\n결과: {total}문제 중 {correct}문제 정답 ({score}점)")


def add_quiz(quizzes: list[Quiz]) -> None:
    print("\n새로운 퀴즈를 추가합니다.")
    question = read_text("문제: ")
    choices = [read_text(f"선택지 {number}: ") for number in range(1, 5)]
    answer = read_number("정답 번호 (1~4): ", 1, 4)
    quizzes.append(Quiz(question, choices, answer))
    print("퀴즈가 추가되었습니다.")


def main() -> None:
    quizzes = default_quizzes()
    try:
        while True:
            show_menu()
            choice = read_number("선택: ", 1, 5)
            if choice == 5:
                break
            elif choice == 1:
                play(quizzes)
            elif choice == 2:
                add_quiz(quizzes)
            else:
                print("아직 준비 중인 기능입니다.")
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되었습니다.")
    print("퀴즈 게임을 종료합니다.")


if __name__ == "__main__":
    main()
