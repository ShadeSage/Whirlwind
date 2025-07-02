def filter_positive(numbers : list):
    filter_numbers = [number for number in numbers if number > 0]
    return filter_numbers

print(filter_positive([-5, 10, 0, 3, -2]))

def update_age(person : dict, summand : int):
    old_age = person.get("возраст")
    person["возраст"] = old_age + summand

student = {"имя": "Мария", "возраст": 21}
update_age(student, 3)
print(student["возраст"])
