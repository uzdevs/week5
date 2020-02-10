def greet(name):
    print("Welcome  " + name.title()+"!")

def talk(name):
    print(f"Hey, {name}! How are you?")

def invite_to_dinner():
    print(f'We are having a dinner tonight. Please come over.')

def goodbye(name, score):
    print(f"Thank for coming, see you next time, {name}.")
    if  score > 5:
        return True
    else:
        return False

def test_review_dinner():
    greet("john")
    talk("john")
    invite_to_dinner()
    satisfied = goodbye("John",6) == True    
    assert satisfied == True




