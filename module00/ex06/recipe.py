cookbook = {
    "sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10 
    },
    "cake":  {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60 
    },
    "salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15  
    }
}

def add_recipe():
    name = input("Enter recipe name: ").lower()
    print("Enter ingredients seperated by comma")
    print("example:")
    print(">> flour,sugar,eggs")
    ingredients = [ing for ing in input(">> ").split(",")]
    meal = input("meal name: ")
    try:
        duration = int(input("Enter duration in munite: "))
    except:
        add_recipe()
    else:
        values = {
            "ingredients": ingredients,
            "meal": meal,
            "prep_time": duration
        }
        cookbook[name] = values

def delete_recipe():
    name = input("Enter recipe name: ").lower()
    if not cookbook.pop(name.lower(), None):
        print("Recipe name not found")
    else:
        print('Done!')

def print_recipe():
    name = input("Enter recipe name: ").lower()
    recipe = cookbook.get(name, None)
    if not recipe:
        print("Recipe not found!")
        return
    print("Recipe for {}:".format(name.lower()))
    print("Ingredients list: {}".format(recipe['ingredients']))
    print("To be eaten for {}.".format(recipe["meal"]))
    print("Takes {} minutes of cooking.".format(recipe["prep_time"]))

def usage():
    print("Please select an option by typing the corresponding number:")
    print("""1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit""")

def get_number():
    try:
        number = int(input(")>> "))
    except:
        number = get_number()
    return number

def check_number(num):
    if num == 5:
        return True
    elif num == 1:
        add_recipe()
    elif num == 2:
        delete_recipe()
    elif num == 3:
        print_recipe()
    elif num == 4:
        print(cookbook)

if __name__ == '__main__':
    usage()
    while True:
        number = get_number()
        if check_number(number):
            break
