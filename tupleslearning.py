habit = ("Exercise", "Daily", "Health")
completion = (True, False, True, True, False, True, True)

print(len(habit))
print(len(completion))

print(habit[0])
print(completion[0:5])

try:
    habit[0] = "Running"
except TypeError:
    print("Tuples cannot be changed directly after creation.")
