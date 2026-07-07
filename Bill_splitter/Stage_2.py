# write your code here
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
    print(friends)
