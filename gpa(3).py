# 과목 코드와 과목명을 저장하는 사전
subject_dict = {'12345': '오픈소스SW와 파이썬 프로그래밍', '23456': '기초컴퓨터프로그래밍', '34567': '글쓰기'}

# 수강목록을 저장하는 리스트
course_list = []

# 학점을 계산하는 함수
def calculate_GPA(courses, include_F):
    total_credit = 0
    total_grade = 0
    for course in courses:
        if course[2] == 'F' and not include_F:
            continue
        credit = course[1]
        grade = course[2]
        if grade == 'A+':
            total_grade += credit * 4.5
        elif grade == 'A':
            total_grade += credit * 4.0
        elif grade == 'B+':
            total_grade += credit * 3.5
        elif grade == 'B':
            total_grade += credit * 3.0
        elif grade == 'C+':
            total_grade += credit * 2.5
        elif grade == 'C':
            total_grade += credit * 2.0
        elif grade == 'D+':
            total_grade += credit * 1.5
        elif grade == 'D':
            total_grade += credit * 1.0
        elif grade == 'F':
            total_grade += credit * 0.0
        total_credit += credit
    GPA = total_grade / total_credit
    return (total_credit, round(GPA, 2))

# 입력 작업 함수
def input_course():
    while True:
        input_str = input("과목명과 학점, 평점을 입력하세요 (종료는 q): ")
        if input_str == 'q':
            break
        input_list = input_str.split(',')
        code = input("과목 코드를 입력하세요: ")
        name = subject_dict.get(code)
        if name is None:
            print("해당하는 과목이 없습니다.")
            continue
        credit = int(input_list[1])
        grade = input_list[2].strip()
        # 이미 수강한 과목인지 확인
        for i, course in enumerate(course_list):
            if course[0] == code:
                if grade > course[2]:
                    course_list[i] = (code, credit, grade)
                break
        else:
            course_list.append((code, credit, grade))
        print("입력되었습니다.")

# 출력 작업 함수
def print_course(include_F):
    for course in course_list:
        if course[2] == 'F' and not include_F:
            continue
        code = course[0]
        name = subject_dict.get(code)
        credit = course[1]
        grade = course[2]
        print("[{}] {}학점: {}".format(name, credit, grade))

# 조회 작업 함수
def search_course():
    name = input("과목명을 입력하세요: ")
    for course in course_list:
        code = course[0]
        if subject_dict.get(code) == name:
            print("[{}] {}학점: {}".format(name, course[1], course[2]))
            break
    else:
        print("해당하는 과목이 없습니다.")

# 계산 작업 함수
def calculate_GPA_task():
    submit_credit, submit_GPA = calculate_GPA(course_list, False)
    view_credit, view_GPA = calculate_GPA(course_list, True)
    print("제출용: {}학점 (GPA: {})".format(submit_credit, submit_GPA))
    print("열람용: {}학점 (GPA: {})".format(view_credit, view_GPA))

# 메인 함수
def main():
    while True:
        print("작업을 선택하세요.")
        print("1. 입력")
        print("2. 출력")
        print("3. 조회")
        print("4. 계산")
        print("5. 종료")
        choice = input()
        if choice == '1':
            input_course()
        elif choice == '2':
            print_course(False)
        elif choice == '3':
            search_course()
        elif choice == '4':
            calculate_GPA_task()
        elif choice == '5':
            break
        else:
            print("잘못된 입력입니다.")



