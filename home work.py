
#My favorite food

foodList = ["Banku with Okra", "Rice with Tomatoes stew","Fufu with Groundnut soup",
            "Yam with Taro leaves stew","Cocoyam with light soup"]
print(foodList)

print("Rice with Tomatoes stew" in foodList)

myFavorite = input("Enter a food: ")

if myFavorite in foodList:
    print("yes! it is in the list.")

else:
    print("sorry, it is not in the list.")


#My dictionary

aboutMe = {"name": "Toffick", "age": "95", "city": "Takoradi",
           "language": "python", "hobbies": "coding"}
print(aboutMe["name"])

aboutMe["Occupation"]= "programmer"
print(aboutMe)

aboutMe["name"]= "Hanshimi"
print(aboutMe)




