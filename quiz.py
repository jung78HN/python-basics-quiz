class Quiz:
    """문제, 네 개의 선택지, 1부터 시작하는 정답 번호를 갖는 퀴즈."""

    def __init__(self, question: str, choices: list[str], answer: int):
        if not isinstance(question, str) or not question.strip():
            raise ValueError("문제는 빈 문자열일 수 없습니다.")
        if not isinstance(choices, list) or len(choices) != 4:
            raise ValueError("선택지는 4개여야 합니다.")
        if any(not isinstance(choice, str) or not choice.strip() for choice in choices):
            raise ValueError("선택지는 빈 문자열일 수 없습니다.")
        if type(answer) is not int or not 1 <= answer <= len(choices):
            raise ValueError("정답 번호는 1~4 사이의 정수여야 합니다.")

        self.question = question.strip()
        self.choices = [choice.strip() for choice in choices]
        self.answer = answer

    def display(self, number: int) -> None:
        print(f"\n[문제 {number}] {self.question}")
        for index, choice in enumerate(self.choices, start=1):
            print(f"  {index}. {choice}")

    def is_correct(self, selected: int) -> bool:
        return selected == self.answer

    def to_dict(self) -> dict:
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }

    @classmethod
    def from_dict(cls, item: dict) -> "Quiz":
        if not isinstance(item, dict):
            raise ValueError("퀴즈는 JSON 객체여야 합니다.")
        return cls(item["question"], item["choices"], item["answer"])
