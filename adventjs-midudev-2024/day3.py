# 🏗️ Organizing the inventory
# Santa Claus 🎅 is checking his workshop inventory to prepare gift delivery. The elves have recorded the toys
# in an array of objects, but the information is a bit disorganized. You need to help Santa organize the inventory.

# You will receive an array of objects, where each object represents a toy and has the properties:
# name: the name of the toy (string).
# quantity: the available quantity of that toy (integer).
# category: the category to which the toy belongs (string).

# Write a function that processes this array and returns an object that organizes the toys as follows:  
# The keys of the object will be the categories of toys.
# The values will be objects that have the toy names as keys and the total quantities of each toy in that category 
# as values.

# If there are toys with the same name in the same category, you must sum their quantities.
# If the array is empty, the function should return an empty object {}.

# const inventary = [
#   { name: "doll", quantity: 5, category: "toys" },
#   { name: "car", quantity: 3, category: "toys" },
#   { name: "ball", quantity: 2, category: "sports" },
#   { name: "car", quantity: 2, category: "toys" },
#   { name: "racket", quantity: 4, category: "sports" },
# ];
# organizeInventory(inventary);
# // Expected result:
# // {
# //   toys: {
# //     doll: 5,
# //     car: 5
# //   },
# //   sports: {
# //     ball: 2,
# //     racket: 4
# //   }
# 
# const inventary2 = [
#   { name: "book", quantity: 10, category: "education" },
#   { name: "book", quantity: 5, category: "education" },
#   { name: "paint", quantity: 3, category: "art" },
# ];
# 
# organizeInventory(inventary2);
# 
# // Expected result:
# // {
# //   education: {
# //     book: 15
# //   },
# //   art: {
# //     paint: 3
# //   }
# // }

from functools import reduce

def organize_inventory(inventory: list[dict]) -> dict:
    
    if not inventory:
        return {}

 #   res = {}
#
 #   for item in inventory:
 #       if item['category'] not in res:
 #           res[item['category']] = {}
 #       if item['name'] not in res[item['category']]:
 #           res[item['category']][item['name']] = 0
 #       res[item['category']][item['name']] += item['quantity']
 
    res = reduce(
            lambda acc, curr: {
            **acc,
            curr['category']: {
                **acc.get(curr['category'], {}),
                curr['name']: acc.get(curr['category'], {}).get(curr['name'], 0) + curr['quantity']
            }
        },
        inventory, {})
        
    return res

print(organize_inventory([
    { 'name': 'doll', 'quantity': 5, 'category': 'toys' },
    { 'name': 'car', 'quantity': 3, 'category': 'toys' },
    { 'name': 'ball', 'quantity': 2, 'category': 'sports' },
    { 'name': 'car', 'quantity': 2, 'category': 'toys' },
    { 'name': 'racket', 'quantity': 4, 'category': 'sports' },
]))