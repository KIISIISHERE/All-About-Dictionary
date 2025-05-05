codes = {'Kenya': '00254', 'Nigeria': '00234', 'Ghana': '00233'}
country = input("Enter the Country Name: ")
if country in codes:
    print(f"The code for {country} is {codes[country]}")
else:
    print("Country not found in dictionary.")
    