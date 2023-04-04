#함수 정의
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
          
#입력
archive_credit,submit_credit=0,0
archive_gpa,submit_gpa=0.0,0.0
while True:
    print("작업을 선택하세요.")
    print("1.입력")
    print("2.산산")

    user_value=input()
    value=int(user_value)

    match value:
        #연산
        case 1:
            user_value=input("학점을 입력하세요:")
            credit= int(user_value)

            user_value=input("평점을 입력하세요:")
            gpa= convert_score(user_value)

            if gpa>0:
                submit_credit += credit
                submit_gpa +=credit*gpa
            archive_credit+=credit
            archive_gpa+=credit*gpa
            print("입력되었습니다.")
        #출력
        case 2:
            submit_gpa/=submit_credit
            archive_gpa/=archive_credit

            print("제출용:"+str(submit_credit)+"학점(gpa:"+str(submit_gpa)+")")
            print("열람용:"+str(archive_credit)+"학점(gpa:"+str(round(archive_gpa,2))+")")
            print("프로그램을 종료합니다")
            break
