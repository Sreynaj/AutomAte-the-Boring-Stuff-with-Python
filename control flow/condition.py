def check_age(age):
    if age < 0:
        return "Age cannot be negative."
    elif age < 18:
        return "You are a minor."
    elif age < 65:
        return "You are an adult."
    else:
        return "You are a senior citizen."

ages_to_test = [-1, 10, 25, 70]

for age in ages_to_test:
    result = check_age(age)
    print(f"Age: {age} - Result: {result}")
