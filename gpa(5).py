class CourseRecord:
    def __init__(self, course_id, course_name, credit, grade):
        self.course_id = course_id
        self.course_name = course_name
        self.credit = credit
        self.grade = grade
    def __str__(self):
        string = f'[{self.course_name}] {self.credit}학점: {self.grade}'
        return string
    @classmethod
    def get_gpa_score(cls, gpa):
        match gpa:
            case 'A+':
                return 4.5
            case 'A':
                return 4
            case 'B+':
                return 3.5
            case 'B':
                return 3
            case 'C+':
                return 2.5
            case 'C':
                return 2
            case 'D+':
                return 1.5
            case 'D':
                return 1
            case 'F':
                return 0
class CourseHistory:    
    def __init__(self):
        self.history = []
        self.course_id_map = {'id': 10000}
        self.submit_grade = {}
        self.archive_grade = {}
        
        self.filename = "course_history.csv"
    def allocate_course_id(self, course_name):
        if course_name not in self.course_id_map:
            new_id = str(int(self.course_id_map['id']) + 1)
            self.course_id_map['id'] = new_id
            self.course_id_map[course_name] = new_id
            self.course_id_map[new_id] = course_name

            return new_id

        else:
            return self.course_id_map[course_name]
    def input_process(self):
        course_name = input('과목명을 입력하세요: ')
        course_id = self.allocate_course_id(course_name)

        credit = input('학점을 입력하세요: ')
        credit = int(credit)
        
        gpa = input('평점을 입력하세요: ')
        gpa_score = CourseRecord.get_gpa_score(gpa)
        if course_id in self.archive_grade:
            if gpa_score > self.archive_grade[course_id][1]:
                self.archive_grade[course_id] = (credit, gpa_score)
        else:
            self.archive_grade[course_id] = (credit, gpa_score)
        if gpa_score > 0.0:
            if course_id in self.submit_grade:
                if gpa_score > self.submit_grade[course_id][1]:
                    self.submit_grade[course_id] = (credit, gpa_score)
            else:
                self.submit_grade[course_id] = (credit, gpa_score)

        course_record = CourseRecord(course_id, course_name, credit, gpa)
        self.history.append(course_record)
    def print_process(self):
        for course_record in self.history:
            print(course_record)
    def query_process(self):
        course_name = input('과목명을 입력하세요: ')
        for course_record in self.history:
            if course_name == course_record.course_name:
                print(course_record)
        else:
            print('해당하는 과목이 없습니다.')
    def calculate_process(self):
        submit_gpa, archive_gpa = 0.0, 0.0
        submit_credit, archive_credit = 0, 0
        for course_id in self.submit_grade:
            submit_gpa += self.submit_grade[course_id][0] * self.submit_grade[course_id][1]
            submit_credit += self.submit_grade[course_id][0] 
        for course_id in self.archive_grade:
            archive_gpa += self.archive_grade[course_id][0] * self.archive_grade[course_id][1]
            archive_credit += self.archive_grade[course_id][0]
        submit_gpa /= submit_credit
        archive_gpa /= archive_credit
        print(f'제출용: {submit_credit} 학점(GPA: {submit_gpa})')
        print(f'열람용: {archive_credit} 학점(GPA: {archive_gpa})')
    def save_process(self):
        with open(self.filename, 'w') as file:
            for course in self.history:
                file.write(f'{course.course_id},{course.course_name},{course.credit},{course.grade}\n')
                print(f'파일로 저장되었습니다.')
    def load_process(self):
        with open(self.filename, 'r') as file:
            file_string = file.readline()
            while file_string != '':
                if file_string[-1] == '\n':
                    file_string = file_string[:-1]
                tokens = file_string.split(',')
                course_id = int(tokens[0])
                course_name = tokens[1]
                credit = int(tokens[2])
                grade = tokens[3]
                course_record = CourseRecord(course_id, course_name, credit, grade)
                self.history.append(course_record)
                if self.course_id_map['id'] < course_id:
                    self.course_id_map['id'] = course_id
                self.course_id_map[course_name] = course_id
                self.course_id_map[course_id] = course_name
                file_string = file.readline()
                
            print(f'파일을 불러왔습니다.')
course_history = CourseHistory()
while True:
    print('작업을 선택하세요')
    print('    1. 입력')
    print('    2. 출력')
    print('    3. 조회')
    print('    4. 계산')
    print('    5. 파일 저장')
    print('    6. 파일 불러오기')
    print('    7. 종료')
    user_input = input()
    if user_input == '1':
        try:
            course_history.input_process()
        except Exception as exception:
            print('[' + type(exception).__name__ + '] 오류가 발생했습니다: ' + str(exception))
        else:
            print('입력되었습니다.')
        finally:
            print('')
        
    elif user_input == '2':
        course_history.print_process()
        
    elif user_input == '3':
        course_history.query_process()

    elif user_input == '4':
        course_history.calculate_process()
        
    elif user_input == '5':
        course_history.save_process()
        
    elif user_input == '6':
        course_history.load_process()
        
    elif user_input == '7':
        break

    else:
        continue
print('프로그램을 종료합니다.')
