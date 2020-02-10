# def describe_pet(animal_type, pet_name):
#     print(f"My pet is {animal_type.title()} and it name is {pet_name.title()}.")
# describe_pet('bulgod','alex')

# def make_shirt(size, text):
#     print("Your shirt size is " + size + " and text is " +text+".")
# make_shirt('42','Your name')
# make_shirt('medium','"I love Python"')


# def make_shirt(size, text='"I love Python"'):
#     for sizes in range(32,42):
#         if sizes > 34:
#             print("This is small")
#         elif sizes < 34:
#             print("This is medium" )
#         elif sizes > 38:
#             print("This is large")
#         else:
#             print("This is x-Large")

#         print(f"Your shirt size is {sizes} and text is {text}.")
# make_shirt('')

# def describe_city(capital, country='Uzbekistan'):
#     print(capital+" is the capital of " + country)
# describe_city('Tashkent')
# describe_city('Dushanbe', 'Tajikistan')
# describe_city('Moscow','Russia')

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted"""
#     full_name = first_name + ' '+last_name
#     return full_name.title()
# musician = get_formatted_name('jimmi', 'carter')
# print("\nThe best musician is " + musician+".")

# def get_formatted_name(first_name, last_name, middle_name=''):
#     """Return full name"""
#     full_name = first_name+' '+middle_name+' '+last_name
#     return full_name.title()

# name = get_formatted_name('John', 'Adams','Adamovich')
# print(name)

# def build_person(first_name, last_name, age = ''):
#     """Return dictionary information"""
#     person = {'first': first_name,'last':last_name}
#     if age:
#         person['age'] = age
#     return person

# name = build_person('jimi','carter', age = 27)
# print(name)


# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted"""
#     full_name = first_name + ' '+last_name
#     return full_name.title()

# while True:
#     print("\nPlease tell me your name: ")
#     f_name = input("First_name: ")
#     l_name = input("Last_name: ")
         
#     formatted_name = get_formatted_name(f_name,l_name)
#     print("\nHello, " + formatted_name+"!")

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted"""
#     full_name = first_name + ' '+last_name
#     return full_name.title()

# while True:
#     print("\nPlease tell me your name: ")
#     print("(enter 'q' at any time to quit)")

#     f_name = input("First_name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Last_name: ")
#     if l_name == 'q':
#         break
         
#     formatted_name = get_formatted_name(f_name,l_name)
#     print("\nHello, " + formatted_name+"!")

# def city_country(city,country):
#     """Return formatted city name"""
#     full_name = city+ ', ' +country
#     return full_name.title()

# while True:
#     print("\nPlease tell me city and country name:")
#     city_name = input("Enter city name: ")
#     count_name = input("Enter country name: ")

#     formatted_name = city_country(city_name,count_name)
#     print(f"{formatted_name.title()}")

# def city_country(city,country):
#     """Return formatted city name"""
#     return (city.title() + ', ' +country.title())

# while True:
#     print("\nPlease tell me city and country name:")
#     print("(enter 'q' at any time to quit)")
#     city_name = input("Enter city name: ")
#     if city_name == 'q':
#         break
#     count_name = input("Enter country name: ")
#     if count_name == 'q':
#         break

#     formatted_name = city_country(city_name,count_name)
#     print(f"{formatted_name.title()}")
    





