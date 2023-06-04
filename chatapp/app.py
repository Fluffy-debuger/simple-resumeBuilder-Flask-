'''name = input("Enter name: ")
email = input("Enter email: ")
degree = input("Enter degree: ")
university = input("Enter university: ")
yrs = int(input("Enter year: "))
skills = input("Enter skill: ")
exp = input("Enter experience: ")

l = [name, email, degree, university, yrs, skills, exp]

l = [item for item in l if item != '' and item is not None]

print(l)
'''

my_dict = {
    'name': 'John',
    'email': '',
    'degree': 'Diploma',
    'university': '',
    'yrs': 3,
    'skills': 'Python',
    'exp': '5 years'
}

filtered_dict = {key: value for key, value in my_dict.items() if value != '' and value is not None}

print(filtered_dict)
