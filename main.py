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


class QuizGame:
    """메뉴 흐름, 문제 목록과 최고 점수를 관리한다."""

    def __init__(self):
        self.quizzes = default_quizzes()
        self.best_score: int | None = None

    def show_menu(self) -> None:
        print("\n=== Python 기초 퀴즈 ===")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")

    def run(self) -> None:
        try:
            while True:
                self.show_menu()
                choice = read_number("선택: ", 1, 5)
                if choice == 5:
                    break
                elif choice == 1:
                    self.play()
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.show_quizzes()
                else:
                    self.show_score()
        except (KeyboardInterrupt, EOFError):
            print("\n입력이 중단되었습니다.")
        print("퀴즈 게임을 종료합니다.")

    def play(self) -> None:
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다.")
            return None

        correct = 0
        total = len(self.quizzes)
        print(f"\n퀴즈를 시작합니다. 총 {total}문제입니다.")
        for number, quiz in enumerate(self.quizzes, start=1):
            quiz.display(number)
            selected = read_number("정답 번호 (1~4): ", 1, 4)
            if quiz.is_correct(selected):
                correct += 1
                print("정답입니다!")
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        score = round(correct / total * 100)
        print(f"\n결과: {total}문제 중 {correct}문제 정답 ({score}점)")
        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("새로운 최고 점수입니다!")

    def add_quiz(self) -> None:
        print("\n새로운 퀴즈를 추가합니다.")
        question = read_text("문제: ")
        choices = [read_text(f"선택지 {number}: ") for number in range(1, 5)]
        answer = read_number("정답 번호 (1~4): ", 1, 4)
        self.quizzes.append(Quiz(question, choices, answer))
        print("퀴즈가 추가되었습니다.")

    def show_quizzes(self) -> None:
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다.")
            return

        print(f"\n등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"  {number}. {quiz.question}")

    def show_score(self) -> None:
        if self.best_score is None:
            print("\n아직 완료한 퀴즈가 없습니다.")
        else:
            print(f"\n최고 점수: {self.best_score}점")


if __name__ == "__main__":
    QuizGame().run()
