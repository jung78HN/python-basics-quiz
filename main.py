import json
from pathlib import Path
from tempfile import NamedTemporaryFile

from default_quizzes import default_quizzes
from quiz import Quiz


STATE_PATH = Path(__file__).resolve().with_name("state.json")


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

    def __init__(self, state_path: Path = STATE_PATH):
        self.state_path = state_path
        self.quizzes = default_quizzes()
        self.best_score: int | None = None
        self.can_save = True
        self.state_changed = False

    def show_menu(self) -> None:
        print("\n=== Python 기초 퀴즈 ===")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")

    def run(self) -> None:
        try:
            self.load_state()
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
            print("\n입력이 중단되었습니다. 현재 데이터를 저장하고 종료합니다.")
        try:
            self.save_state()
        except KeyboardInterrupt:
            print("\n저장이 중단되었습니다.")
        print("퀴즈 게임을 종료합니다.")

    def play(self) -> None:
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다.")
            return

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
            self.state_changed = True
            print("새로운 최고 점수입니다!")
            self.save_state()

    def add_quiz(self) -> None:
        print("\n새로운 퀴즈를 추가합니다.")
        question = read_text("문제: ")
        choices = [read_text(f"선택지 {number}: ") for number in range(1, 5)]
        answer = read_number("정답 번호 (1~4): ", 1, 4)
        self.quizzes.append(Quiz(question, choices, answer))
        self.state_changed = True
        if self.save_state():
            print("퀴즈가 추가되었습니다.")
        else:
            print("이번 실행에 퀴즈가 추가되었습니다. 파일 저장을 완료하지 못했습니다.")

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

    def load_state(self) -> None:
        try:
            with self.state_path.open(encoding="utf-8") as state_file:
                data = json.load(state_file)
            if not isinstance(data, dict) or not isinstance(data.get("quizzes"), list):
                raise ValueError("퀴즈 목록이 올바르지 않습니다.")
            best_score = data["best_score"]
            if best_score is not None and (
                type(best_score) is not int or not 0 <= best_score <= 100
            ):
                raise ValueError("최고 점수가 올바르지 않습니다.")
            quizzes = [Quiz.from_dict(item) for item in data["quizzes"]]
        except FileNotFoundError:
            self.state_changed = True
            return
        except (ValueError, KeyError, RecursionError):
            print("저장 파일이 손상되었습니다. 기본 퀴즈로 복구합니다.")
            self.state_changed = True
            return
        except OSError:
            print("저장 파일을 읽을 수 없습니다. 이번 실행에서는 파일을 저장하지 않습니다.")
            self.can_save = False
            return

        self.quizzes = quizzes
        self.best_score = best_score
        print(f"저장된 데이터를 불러왔습니다. (퀴즈 {len(quizzes)}개)")

    def save_state(self) -> bool:
        if not self.can_save:
            return False
        if not self.state_changed:
            return True

        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score,
        }
        pending_path = None
        try:
            # 기존 파일을 보존하도록 쓰기를 마친 뒤 한 번에 교체한다.
            with NamedTemporaryFile(
                mode="w",
                encoding="utf-8",
                dir=self.state_path.parent,
                prefix=".state-",
                suffix=".tmp",
                delete=False,
            ) as pending_file:
                pending_path = Path(pending_file.name)
                json.dump(data, pending_file, ensure_ascii=False, indent=2)
                pending_file.write("\n")
            pending_path.replace(self.state_path)
        except (OSError, UnicodeError):
            print("저장 파일을 쓸 수 없습니다. 저장 위치와 권한을 확인하세요.")
            return False
        finally:
            if pending_path is not None:
                try:
                    pending_path.unlink(missing_ok=True)
                except OSError:
                    pass
        self.state_changed = False
        return True


if __name__ == "__main__":
    QuizGame().run()
