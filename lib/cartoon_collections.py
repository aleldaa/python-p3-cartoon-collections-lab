def roll_call_dwarves(dwarf_names):
    for i, name in enumerate(dwarf_names):
        print(f'{i+1}. {name}')

def summon_captain_planet(planeteer_calls):
    return [f'{call.title()}!' for call in planeteer_calls]

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(foods):
    cheeses = ["cheddar", "gouda", "camembert"]
    for food in foods:
        if food in cheeses:
            return food
    return None
