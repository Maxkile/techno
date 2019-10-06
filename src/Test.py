import sys

def safe_input():
    try:
        return input()
    except EOFError:
        sys.exit(0)
        
def getAnswers(q_num,money):
    answers = list()
    for i in range(0,q_num):
        answers.append(int(safe_input()))
    return answers
    
def guessNumber():
    seg = [1,50000,100000] #low,mid,high
    divide_into = 15
    money = 100
    cur_turn = 1
    divide_coff = 4#divide each segment into divide_into subsegments divide_coff times
    questions = list()#list of numbers(a). It means that the question looks like "is a < x"
    answers = list()#list of answers
    while(True):
        if (seg[2] - seg[0] < 1):
            print('!',seg[1],sep=' ')
            return 
        elif seg[1] == seg[0]:
            questions.append(seg[2]) 
            print('?',questions[0],sep=' ')
            money -= 1
        elif cur_turn <= divide_coff:
            delta = (seg[2] - seg[0]) // divide_into
            for i in range(1,divide_into):
                questions.append(seg[0] + delta*i)
                print('?',questions[i-1],sep=' ')
                money -= 1   
        else:
            questions.append(seg[1]) 
            print('?',questions[0],sep=' ')
            money -= 1
        
        # print(seg)
        print('+',flush=True)#end of question phase
        
        # print("Money left",money)
        answers = getAnswers(len(questions),money)
        if (seg[0] == seg[1]) or (seg[2] == seg[1]):#we compared with seg[2]: x < seg[2]
            for j in range(0,len(answers)):       
                if answers[j] == 1:
                    print('!',seg[0],sep=' ')
                    return
                else:
                    print('!',seg[2],sep=' ')
                    return
        else:
            for j in range(0,len(answers)):       
                if answers[j] == 1:
                        seg[2] = questions[j] - 1
                        seg[1] = seg[0] + (seg[2] - seg[0]) // 2
                        break #found necessary segment
                else:
                    seg[0] = questions[j]
                    seg[1] = seg[0] + (seg[2] - seg[0]) // 2 
        cur_turn += 1
        money -= 10
        questions.clear()
    
if __name__ == "__main__":
    guessNumber()