age = int(input("Enter your age: "))

if age <=13:
    group_age = 'Dziecko'
elif 13 <= age <= 19:
    group_age ='Nastolatki'
elif 20 <= age <= 64:
    group_age ='Dorosły'
else:
    group_age = 'Senior'

print(f'Your age group is {group_age}')