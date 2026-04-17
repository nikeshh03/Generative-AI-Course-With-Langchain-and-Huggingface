from typing import TypedDict

class Person(TypedDict):  # The typedict help is anotating the dict key with a specific data strcuture. 
    name : str
    age : int

#But the TypeDict does not validates the data in the dict so if "age : int" is given it will still accept str as the input

new_person: Person = {'name':'nikesh', 'age': 20}

print(new_person)