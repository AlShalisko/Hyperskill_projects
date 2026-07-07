# write your code here
import random
friends = {}
n_friends = int(input("Enter the number of friends joining (including you):"))
if n_friends < 1:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range (0,n_friends):
        name = input()
        friends[name] = 0
    bill = int(input("Enter the total bill value:"))
    for i in friends:
        friends[i] = round(bill/n_friends,2)
    answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No')
    if answer == "Yes":
        friend_list = list(friends.keys())
        random.shuffle(friend_list)
        print(friend_list[0] + " is the lucky one!")
        for i in friends:
            friends[i] = round(bill/(n_friends-1),2)
        friends[friend_list[0]] = 0
        print(friends)
    else:
        print("No one is going to be lucky")
        print(friends)
    
