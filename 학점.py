def convert_score(grade):
    match grade:
        case'A+':
            gpa=4.5
        case'A':
            gpa=4.0
        case'B+':
            gpa=3.5
        case'B':
            gpa=3.0
        case'C+':
            gpa=2.5    
        case'C':
            gpa=2.0  
        case'D+':
            gpa=1.5 
        case'D':
            gpa=1.0
        case'F':
            gpa=0.0
    return gpa

course_map={'base_id':10000}

def get_code(course_name):
    if course_name not in course_map:
        course_map['base_id']=course_map[course_name]
        course_map['base_id']+=1
        return course_map[course_name]


          

archive_credit,submit_credit=0,0
archive_gpa,submit_gpa=0.0,0.0
while True:
    print("작업을 선택하세요.")
    print("1.입력")
    print("2.출력")
    print("3.계산")

    user_value=input()
    value=int(user_value)

    match value:
        
        case 1:
            print('과목명을 입력하세요: ')
            course_name = input()
            course_id = course_map[course_name]
            print("학점을 입력하세요:")
            user_value=input()
            credit=int(user_value)

            print("평점을 입력하세요:")
            user_value=input()
            gpa= convert_score(user_value)

            course_grade=(course_id,credit,gpa)
            

            if gpa>0:
                submit_credit += credit
                submit_gpa +=credit*gpa
            archive_credit+=credit
            archive_gpa+=credit*gpa
            print("입력되었습니다.")
        case 2:
        

        case 3:
            submit_gpa/=submit_credit
            archive_gpa/=archive_credit

            print("제출용:"+str(submit_credit)+"학점(gpa:"+str(submit_gpa)+")")
            print("열람용:"+str(archive_credit)+"학점(gpa:"+str(round(archive_gpa,2))+")")
            print("프로그램을 종료합니다")
            break
