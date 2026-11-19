from quiz import Quiz


def default_quizzes() -> list[Quiz]:
    """첫 실행과 데이터 복구에 쓸 기본 문제를 새로 생성한다."""
    return [
        Quiz(
            "정수 7을 문자열 '7'로 바꾸는 함수는?",
            ["int(7)", "bool(7)", "str(7)", "list(7)"],
            3,
        ),
        Quiz(
            "키와 값의 쌍으로 자료를 저장하는 자료형은?",
            ["list", "str", "bool", "dict"],
            4,
        ),
        Quiz(
            "리스트 items에 원소를 하나 추가하는 메서드는?",
            ["items.append()", "items.index()", "items.pop()", "items.clear()"],
            1,
        ),
        Quiz(
            "range(3)을 for 반복문으로 순회할 때 나오는 값은?",
            ["1, 2, 3", "0, 1, 2", "0, 1, 2, 3", "3만 나온다"],
            2,
        ),
        Quiz(
            "인스턴스의 초기 상태를 설정하는 메서드의 이름은?",
            ["__str__", "__main__", "__name__", "__init__"],
            4,
        ),
        Quiz(
            "발생한 예외를 처리하는 코드를 작성하는 절은?",
            ["elif", "except", "with", "for"],
            2,
        ),
    ]
