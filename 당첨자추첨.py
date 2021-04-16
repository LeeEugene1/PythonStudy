import random

list=[]
customer = ['A','B','C','D','G','K','F']
while len(list) < 5:
    winner = random.choice(customer)
    if winner not in list:
        list.append(winner)

for i in range(len(list)):
    print(i+1,'번째 당첨자는', list[i],'입니다')
    