data = {"a": 10, "b": 20, "c": 10, "d": 30, "e": 20, "f": 10,}
value = int(input("Enter a value to check it's frequency: "))
count = list(data.values()).count(value)
print(f"The value '{value} appears {count} time(s) in the dictionary.")
