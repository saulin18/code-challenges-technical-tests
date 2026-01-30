# 📇 Santa's Magic Agenda
# Santa Claus has a magic diary 📇 where he keeps the addresses of the children to deliver the presents.
# The problem: the diary's information is mixed and incorrectly formatted. The lines contain a magic phone number,
# a child's name, and their address, but everything is surrounded by strange characters.
#
# Santa needs your help to find specific information from the diary. Write a function that, given the diary's
# content and a phone number, returns the child's name and address.
#
# Keep in mind that in the diary:
#
# Phone numbers are formatted as +X-YYY-YYY-YYY (where X is one or two digits, and Y is a digit).
# Each child's name is always between < and >.
# The idea is for you to write a function that, given the full phone number or part of it, returns the child's name
# and address. If it doesn't find anything or there is more than one result, you must return null.
#
# const agenda = `+34-600-123-456 Calle Gran Via 12 <Juan Perez>
# Plaza Mayor 45 Madrid 28013 <Maria Gomez> +34-600-987-654
# <Carlos Ruiz> +1-800-555-0199 Fifth Ave New York`;
#
# findInAgenda(agenda, "34-600-123-456");
# // { name: "Juan Perez", address: "Calle Gran Via 12" }
#
# findInAgenda(agenda, "600-987");
# // { name: "Maria Gomez", address: "Plaza Mayor 45 Madrid 28013" }
#
# findInAgenda(agenda, "111");
# // null
# // Explanation: No results
#
# findInAgenda(agenda, "1");
# // null
# // Explanation: Too many results
import re


def find_in_agenda(agenda: str, phone_number: str) -> dict | None:
    if not agenda or not phone_number:
        return None

    agenda = agenda.split("\n")
    phone_regex = r"[\+?][0-9]{1,2}-[0-9]{3}-[0-9]{3}-[0-9]{3}"
    name_regex = r"<([^>]+)>"
    

    # The key will be the phone number
    result = None
  
    for line in agenda:
       
        phone_match: re.Match = re.search(phone_regex, line)
        name_match: re.Match = re.search(name_regex, line)
        
    
        if phone_match and name_match:
            phone = phone_match.group() 
            name = name_match.group(1)  
            address = line.replace(phone, "").replace(f"<{name}>", "").strip()
        

            if phone_number in phone or phone_number in phone.replace('+', ''):
                if result is not None:  
                    return None
                
                result = {
                    "name": name,
                    "address": address
                }

    return result
            
    

agenda = """+34-600-123-456 Calle Gran Via 12 <Juan Perez>
Plaza Mayor 45 Madrid 28013 <Maria Gomez> +34-600-987-654
<Carlos Ruiz> +1-800-555-0199 Fifth Ave New York"""

print(find_in_agenda(agenda, "34-600-123-456"))
print(find_in_agenda(agenda, "600-987"))
print(find_in_agenda(agenda, "111"))
print(find_in_agenda(agenda, "1"))
