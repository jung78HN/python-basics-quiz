# Python 기초 퀴즈

Python 기초 개념을 복습하는 한국어 터미널 퀴즈 게임입니다. 기본 문제 6개로 시작하며, 문제를 직접 등록해 퀴즈를 확장할 수 있습니다.

## 주제 선정 이유

자료형, 반복문, 클래스, 예외 처리는 이 게임의 코드에도 쓰입니다. 문제를 푼 뒤 구현에서 같은 개념이 어디에 쓰이는지 찾아볼 수 있도록 Python 기초를 주제로 선택했습니다.

## 실행 방법

Python 3.10 이상이 필요합니다. 게임은 표준 라이브러리만 사용합니다.

```console
git clone https://github.com/jung78HN/python-basics-quiz.git
cd python-basics-quiz
python main.py
```

Windows에서 Python Launcher가 설치되어 있다면 `py -3 main.py`로도 실행할 수 있습니다.

다른 폴더에서도 프로젝트의 main.py 경로를 지정해 실행할 수 있습니다.

## 기능

| 메뉴 | 동작 |
| --- | --- |
| 1. 퀴즈 풀기 | 등록 순서대로 전 문제를 풀고, 문제별 정답 여부와 라운드 점수를 확인합니다. |
| 2. 퀴즈 추가 | 문제, 선택지 4개, 정답 번호를 입력해 등록합니다. |
| 3. 퀴즈 목록 | 등록된 문제 제목과 개수를 확인합니다. |
| 4. 점수 확인 | 완료한 라운드에서 받은 최고 점수를 확인합니다. |
| 5. 종료 | 변경사항을 저장하고 게임을 끝냅니다. Ctrl+C나 입력 종료 시에도 저장을 시도합니다. |

점수는 정답 수를 전체 문제 수로 나눈 백분율을 정수로 반올림해 계산합니다. 완료한 라운드가 없으면 점수 메뉴에 안내가 표시됩니다. 풀이 도중 중단한 라운드는 점수에 반영되지 않습니다.

## 파일 구조

```text
python-basics-quiz/
├── main.py              # QuizGame, 메뉴, 사용자 입력과 저장 처리
├── quiz.py              # Quiz, 정답 판정, JSON 변환
├── default_quizzes.py   # 기본 문제 6개
├── state.json           # 실행 시 생성되는 로컬 저장 파일
├── docs/screenshots/    # 개발 환경과 실행 결과 이미지
├── .gitignore
└── README.md
```

## 저장 데이터

`state.json`은 실행한 터미널의 현재 디렉터리와 관계없이 `main.py`가 있는 프로젝트 루트에 UTF-8로 저장됩니다.

| 필드 | 저장 내용 |
| --- | --- |
| `quizzes` | 퀴즈 목록. 각 항목은 문제 문자열 `question`, 선택지 문자열 4개의 배열 `choices`, 1~4 사이의 정답 번호 `answer`를 담습니다. |
| `best_score` | 0~100 사이의 최고 점수. 완료한 라운드가 없으면 `null`입니다. |

저장 파일이 없으면 기본 문제를 사용합니다. JSON 구문이나 데이터 구조가 손상되면 안내를 표시하고 기본 문제와 초기 점수로 복구합니다. 디스크에 기록할 때는 임시 파일에 쓰기를 마친 뒤 기존 파일을 교체합니다. 개인 실행 데이터인 `state.json`은 Git에서 제외합니다.

## 실행 화면

실제 실행에서 수집한 터미널 출력을 PNG로 정리했습니다.

[개발 환경](docs/screenshots/environment.png) · [메뉴](docs/screenshots/menu.png) · [퀴즈 추가](docs/screenshots/add_quiz.png) · [퀴즈 목록](docs/screenshots/list.png) · [퀴즈 풀이](docs/screenshots/play.png) · [최고 점수와 재시작](docs/screenshots/score.png)
