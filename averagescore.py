def inputmark():
    print("ENTER STUDENT ID: ")
    id=int(input())
    print("ENTER EXAM SCORE: ")
    exam=int(input())
    print("ENTER ALL TEST SCORES: ")
    mark1=int(input())
    mark2=int(input())
    mark3=int(input())
    mark4=int(input())
    mark5=int(input())
    mark6=int(input())
    mark7=int(input())
    sum=(mark1+mark2+mark3+mark4+mark5+mark6+mark7)
    avge=sum/7
    print('TEST AVERAGE IS:     ' +str(avge))
    print('FINAL MARK IS:   ',compute_mark(avge,exam))
    print('Letter Grade is:     ',getgrade(compute_mark(avge,exam)))
    print_Remark(getgrade(compute_mark(avge,exam)))
    return avge

def compute_mark(avge,exam):
    final_mark=0.4*avge+0.6*exam
    return final_mark
def getgrade(final_mark):
    if 90<=final_mark<=100:
        grade='A'
    elif 80<=final_mark<=89:
        grade='B'
    elif 70<=final_mark<=79:
        grade='C'
    elif 60<=final_mark<=69:
        grade='D'
    else:
        grade='F'
    return grade
def print_Remark(grade):
    if grade=='A':
        print('Remark : Excellent')
    elif grade=='B':
        print('Remark : Good')
    elif grade=='C':
        print('Remark : Satisfactory')
    elif grade=='D':
        print('Remark : Fair')
    elif grade=='F':
        print('Remark : Poor')
inputmark()
    
