# You are in a very special market where Christmas trees 🎄 are sold. Each one comes decorated with a series 
# of very peculiar ornaments, and the price of the tree is determined by the ornaments it has.
# 
# *: Snowflake - Value: 1
# o: Christmas Ball - Value: 5
# ^: Decorative Tree - Value: 10
# #: Shiny Garland - Value: 50
# @: Polar Star - Value: 100
# Normally, you would sum up all the values of the ornaments and that's it…
# 
# But, watch out! If an ornament is immediately to the left of another of greater value, instead of adding, 
# its value is subtracted.
# 
# Examples:
# 
# calculatePrice("***"); // 3   (1 + 1 + 1)
# calculatePrice("*o"); // 4   (5 - 1)
# calculatePrice("o*"); // 6   (5 + 1)
# calculatePrice("*o*"); // 5  (-1 + 5 + 1)
# calculatePrice("**o*"); // 6  (1 - 1 + 5 + 1)
# calculatePrice("o***"); // 8   (5 + 3)
# calculatePrice("*o@"); // 94  (-5 - 1 + 100)
# calculatePrice("*#"); // 49  (-1 + 50)
# calculatePrice("@@@"); // 300 (100 + 100 + 100)
# calculatePrice("#@"); // 50  (-50 + 100)
# calculatePrice("#@Z"); // undefined (Z is unknown)

def calculate_price(ornaments: str) -> int | None:
    values = {
    "*": 1,
    "o": 5,
    "^": 10,
    "#": 50,
    "@": 100
    }
    
    total = 0
    # The algorithm is very simple, we iterate through the string and compare the current ornament with the next one
    # if is value is lower than the next one, we substract, otherwise we add it
    for i, ornament in enumerate(ornaments):
        if ornament not in values:
            return None
        
        current_value = values[ornament]
        
        if i + 1 < len(ornaments):
            if ornaments[i + 1] in values:
                next_value = values[ornaments[i + 1]]
                if current_value < next_value:
                    total -= current_value
                else:
                    total += current_value