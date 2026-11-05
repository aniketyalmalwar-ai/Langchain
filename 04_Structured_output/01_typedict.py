from typing import TypedDict

class Person(TypedDict):
    name:str
    age:int

new_person : Person = {'name':"Aniket",'age':25}
new_person1 : Person = {'name':"Aniket",'age':'25'} # not perform validation

print(new_person,new_person1)