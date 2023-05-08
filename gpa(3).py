# 과목 코드와 과목명을 사전으로 관리
subject_dict = {'12345': '오픈소스SW와 파이썬 프로그래밍', '23456': '기초컴퓨터프로그래밍', '34567': '글쓰기'}

# 수강목록 클래스 정의
class CourseList:
    def __init__(self):
        self.courses = []

    def add_course(self, code, credit, grade):
        self.courses.append((code, credit, grade))

    def get_course_list(self):
        return self.courses

    def get_course_by_code(self, code):
        for course in self.courses:
            if course[0] == code:
                return course
        return None

    def calculate_total_credit(self, include_f=False):
        total_credit = 0
        for course in self.courses:
            if include_f or course[2] != 'F':
                total_credit += course[1]
        return total_credit

    def calculate_gpa(self, include_f=False):
        total_grade_point = 0
        total_credit = 0
        for course in self.courses:
            if include_f or course[2] != 'F':
                total_credit += course[1]
                if course[2] == 'A+':
                    total_grade_point += 4.5 * course[1]
                elif course[2] == 'A':
                    total_grade_point += 4.0 * course[1]
                elif course[2] == 'B+':
                    total_grade_point += 3.5 * course[1]
                elif course[2] == 'B':
                    total_grade_point += 3.0 * course[1]
                elif course[2] == 'C+':
                    total_grade_point += 2.5 * course[1]
                elif course[2] == 'C':
                    total_grade_point += 2.0 * course[1]
                elif course[2] == 'D+':
                    total_grade_point += 1.5 * course[1]
                elif course[2] == 'D':
                    total_grade_point += 1.0 * course[1]
                else:
                    total_grade_point += 0.0 * course[1]
        if total_credit == 0:
            return 0
        else:
            return total_grade_point / total_credit

# 수강목록 객체 생성
course_list = CourseList()

# 메뉴 출력 함수 정의
def print_menu():
    print("작업을 선택하세요.")
    print("1. 입력")
    print("2. 출력")
    print("3. 조회")
    print("4. 계산")
    print("5. 종료")

# 입력 작업 함수 정의
def input_course():
    code, credit, grade = input("과목명과 학점, 평점을 입력하세요: ").split(',')
    if code not in subject_dict:
        print("잘못된 과목 코드입니다.")
    else:
        course_list.add_course(code, int(credit), grade)
        print("입력되었습니다.")

# 출력 작업 함수 정의
def print_course_list(include_grade=True):
    for course in course_list.get_course_list():
        if include_grade:
            print(f"[{subject_dict[course[0]]}] {course[1]}학점: {course[2]}")
        else:
            print(f"[{subject_dict[course[0]]}] {course[1]}학점")

# 조회 작업 함수 정의
def search_course():
    code = input("과목명을 입력하세요: ")
    course = course_list.get_course_by_code(code)
    if course:
        print(f"[{subject_dict[course[0]]}] {course[1]}학점: {course[2]}")
    else:
        print("해당하는 과목이 없습니다.")

# 계산 작업 함수 정의
def calculate_gpa():
    total_credit_submit = course_list.calculate_total_credit(include_f=False)
    total_credit_view = course_list.calculate_total_credit(include_f=True)
    gpa_submit = course_list.calculate_gpa(include_f=False)
    gpa_view = course_list.calculate_gpa(include_f=True)
    print(f"제출용: {total_credit_submit}학점 (GPA: {gpa_submit:.2f})")
    print(f"열람용: {total_credit_view}학점 (GPA: {gpa_view:.2f})")

# 메인 코드
while True:
    print_menu()
    choice = input()
    if choice == '1':
        input_course()
    elif choice == '2':
        print_course_list()
    elif choice == '3':
        search_course()
    elif choice == '4':
        calculate_gpa()
    elif choice == '5':
        break
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")



