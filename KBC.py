print("welcome to the game\nlets start\nhere  are your questions")
questions_list=["how many continents are there in the world?","what is the capital city of india?","who invented computer?","identify which place belongs to telangana?","identify which is proper noun?"]
options_list=[["four","nine","seven","eight"],["hyderabad","bhopal","sikkim","delhi"],["charles babbage","thomas","issac newton","euler"],["lucknow","golconda","rayala seema","nandi hills"],["car","laptop","new york","mountain"]]
solutions_list=["seven","delhi","charles babbage","golconda","new york"]
i=0
lifeline=0
cash=0
while i<len(questions_list):
    print(questions_list[i])
    print(options_list[i])
    user_answer=input("enter your answer: \n enter 50-50 lifeline\n")   
    if user_answer=="50-50":
        lifeline=lifeline+1
        j=0
        options=0
        while j<len(options_list[i]):
            a=options_list[i][j]
            if lifeline==1:
                if a not in solutions_list:
                    options=options+1
                    options_list[i].pop(j)  
                    print(options_list[i])
                if options==2:
                    break                 
            if lifeline>1:
                print("you have used a lifeline .so, there are no lifelines")
                break
            j=j+1
        user_answer=input("enter your answer: ")
    if user_answer==solutions_list[i]:
        cash=10**(i+1)
        print("congratulations")
    if user_answer!=solutions_list[i] :
        print("sorry:)\nbetter luck next time\n your answer is wrong quit the game\ncash won",cash)
        break
    print("you have won total cash prize",cash)
    i=i+1     
