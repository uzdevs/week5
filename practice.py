
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
    


# def make_album(artist, album_title, track=''):
#     """Return dictionary information to make_album"""
#     album = {
#   'name artist': artist,
#   'album':album_title}
#     if track:
#         album['track'] = track
#     return album

# name = make_album('jimi','love is love', track = 15)
# print(name)



# def make_album(artist,album_title):
#     """Return formatted city name"""
#     dict= {
#         'name artist': artist,
#         'title': album_title

#     }
#     return dict

# while True:
#     print("\nPlease tell me artist and album title:")
#     print("(enter 'q' at any time to quit)")
#     artist_name = input("Enter artist name: ")
#     if artist_name == 'q':
#         break
#     album_title = input("Enter album title: ")
#     if album_title == 'q':
#         break

#     formatted_name = make_album(artist_name,album_title)
#     print(formatted_name)

# def greet_users(names):
#     """Print a simple greeting to each user in the list."""
#     for name in names:
#         msg = "Hello, " + name.title()+"!"
#         print(msg)

# usernames = input("Please enter name: ")
# greet_users(usernames)

# unprinted_designes = ['iphone case','robot', 'rev toy']
# comleted_models = []

# while unprinted_designes:
#     current_design = unprinted_designes.pop()
#     print("Printing model: "+current_design)
#     comleted_models.append(current_design)
# print("\nThe following models have been printed:")
# for comleted_model in comleted_models:
#     print(comleted_model)


# def print_models(unprinted_designes, completed_models):
#     """
#     Simulate printing each design, until none are left.
#     Move each design to completed_models after printing.
#     """
#     while unprinted_designes:
#         current_design = unprinted_designes.pop()

#         print("Printing models: " + current_design)
#         completed_models.append(current_design)
# def show_completed_models(completed_models):
#     """Show all the models that were printed."""
#     print("\nThe following models have been printed.")
#     for completed_model in completed_models:
#         print(completed_model)
# unprinted_designes = ['iphone', 'android','samsung']
# completed_models = []
# print_models(unprinted_designes, completed_models)
# show_completed_models(completed_models)


# unshipped_orders = ['drone', 'toy','plane','book','computer']
# shipped_orders = []

# while unshipped_orders:
#     current_orders = unshipped_orders.pop()
#     print("We are shipping now: " + current_orders)
#     shipped_orders.append(current_orders)

# print("\nCurrent is shipped.")
# for shipped_order in shipped_orders:
#     print(shipped_order)

# unordered_pizza = ['cheese','pepporoni','vegan','steak','chicken']
# completed_orders = []

# while unordered_pizza:
#     current_order = unordered_pizza.pop()
#     print("Please wait we are working your: "+current_order+" pizza.")
#     completed_orders.append(current_order)

# print("Your order is ready: ")
# for completed_order in completed_orders:
#     print("Your "+completed_order[:]+" pizza is ready.")

# uninvited_guests = ['john','smith','adam','george','washington','bill']
# invited_guests = []

# while uninvited_guests:
#     current_guests = uninvited_guests.pop()
#     print("This is uninvited guest: " +current_guests.title())
#     invited_guests.append(current_guests)

# print("\nThese guests are now invited. ")
# for invited_guest in invited_guests:
#     print(invited_guest.title())


# unmovied_items = ['sofa','bed','mattress','table','frame','boxes','chairs','dishes','clothes']
# movied_items = []

# while unmovied_items:
#     current_items = unmovied_items.pop()
#     print("These item should move out of truck: " + current_items)
#     movied_items.append(current_items)

# print("\nThese items already moved:")
# for movied_item in movied_items:
#     print(movied_item)

# def moving_items(unmovied_items, moved_item):
#     """
#     Simulate moving items until none are left.
#     Move all items out of truck.
#     """
#     while unmovied_items:
#         current_items = unmovied_items.pop()
#         print("This item should move out of truck: " + current_items)
#         moved_item.append(current_items)

# def show_moved_items(moved_items):
#     """Show all moved items"""
#     print("\nFollowing items are moved.")
#     for moved_item in moved_items:
#         print(moved_item)

# unmovied_items = ['sofa','bed','frame','box', 'clothes']
# moved_items = []
# moving_items(unmovied_items, moved_items)
# show_moved_items(moved_items)

# def uninvited_guests(un_guests,inv_guests):
#     """
#     Simulate uninvited guests to
#     invited guests.
#     """
#     while un_guests:
#         current_guests = un_guests.pop()
#         print("This guest is uninvited: " + current_guests)
#         inv_guests.append(current_guests)

# def show_invited_guest(inv_guests):
#     """Show invited guests"""
#     print("These guests are invited: ")
#     for inv_guest in inv_guests:
#         print(inv_guest)

# un_guests = ['john','smish','amish', 'kanick','sanich']
# inv_guest = []
# uninvited_guests(un_guests, inv_guest)
# show_invited_guest(inv_guest)

# def magicians(names):
#     for name in names:
#         msg = "This magician "+name.title()+" is the best."
#         print(msg)

# magician=['james','david','copperfield','marlin']
# magicians(magician)


# def cars(names):
#     for name in names:
#         msg = "This "+name.title()+ " is best car"
#         print(msg)

# car = ['audi','toyota','nissan','lexus']
# cars(car)

# def show_magicians(magicians):
#     """Print the name of each magician in the list."""
#     for magician in magicians:
#         print(magician)

# def make_great(magicians):
#     """Add 'the Great!' to each magician's name."""
#     # Build a new list to hold the great musicians.
#     great_magicians = []

#     # Make each magician great, and add it to great_magicians.
#     while magicians:
#         magician = magicians.pop()
#         great_magician = magician + ' the Great'
#         great_magicians.append(great_magician)

#     # Add the great magicians back into magicians.
#     for great_magician in great_magicians:
#         magicians.append(great_magician)

# magicians = ['Harry Houdini', 'David Blaine', 'Teller']
# show_magicians(magicians)

# print("\n")
# make_great(magicians)
# show_magicians(magicians)



# def show_magicians(magicians):
#     """Print the name of each magicians in the list"""
#     for magician in magicians:
#         print(magician)

# def make_great(magicians):
#     """Add 'the Great' of each magicians"""
#     great_magicians = []

#     while magicians:
#         magician = magicians.pop()
#         great_magician = magician + " the Great"
#         great_magicians.append(great_magician)

#     #Add great magicians back into magicians
#     for great_magician in great_magicians:
#         magicians.append(great_magician)

#     return magicians

# magicians=['Toni David', 'Copperfield', 'Kasparov']
# show_magicians(magicians)

# print("\nGreat Magicians")
# great_magicians = make_great(magicians[:])
# show_magicians(great_magicians)

# print("\nOriginal magicians")
# show_magicians(magicians)

# def make_pizza(*toppings):
#     """Summarize the pizza we are about to make"""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print("- "+topping)

# make_pizza('pepporoni')
# make_pizza('cheese','vegan', 'green peppers', 'onion')
# make_pizza('chicken','lamb')

# Mixing positional and arbitary arguments
# def make_pizza(size, *toppings):
#     """Summarize the pizza we are about to make"""
#     print("\nMaking a "+str(size)+
#         "-inch pizza with the following toppings.")
#     for topping in toppings:
#         print("-" +topping)

# make_pizza(16, 'pepporoni')
# make_pizza(12, 'cheese', 'vegan','tomato')

# using arbitary keyword arguments

# def build_profile(first, last,**user_info):
#     """Build a dictionary containing everything we know about a user"""
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile

# user_profile = build_profile('albert', 'einstein',
#                             location='princeton',
#                             field='physics')
# print(user_profile)

# def make_sandwich(*toppings):
#     """making order"""
#     print("\nI'll make to you a great sandwich:")
#     for topping in toppings:
#         print("....adding " +topping+ " to your sandwich.")
#     print("Your sandwich is ready.")

# make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
# make_sandwich('turkey', 'apple slices', 'honey mustard')
# make_sandwich('peanut butter', 'strawberry jam')

# def make_car(model, make, color, **tow_package):
#     """Building a dictionary about a car"""
#     car = {}
#     car['model'] = model
#     car['make'] = make
#     car['color'] = color
#     for key, value in tow_package.items():
#         car[key] = value
#     return car

# user_info = make_car('subaru','outback','white', tow_package=True)
# print(user_info)

