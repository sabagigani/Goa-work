n=input("enter your name ")
print(n.upper())
list=["name","name","name","name","name","name","name"]
print(list[0].capitalize()[1].upper()[2].lower()[3].count(1))
print([list[4]].replace("name","r")[5].title())
# .Lower() აპატარავებს ასოებს სტრინგში მაგ "HELLO".Lower() = "hello"
5
# .upper() ადიდებს ასოებს სტრინგში მაგ "hello".lower() = "HELLO"
5
# .capitalize() ადიდებს პირველ ასოს მთლაინ სტრინგში მაგ "hello".capitalize()= "Hello"


# .count(argument) იმ სტრინგში რომელსაც გავუწერეთ ითვლის იმ სტრინგის რაოდენობას რომელიც გადავეცით არგუმნტში, აბრუნებს რიცხვს საბოლოოდ

# .reaplce(argument1, argument2) იმ სტრინგში რომელსაც გავუწერეთ შეცვლის ყველა იმ სტრინგ რომელიც პირველ არგყმენტში გადავეცით იმი სტრინგით რომელიც მეორე აგუმენტშ გადავეცით

# .title() სტრინგში გაადიდებს ყველა სოიტყვის(არააქვს მნიშვნოლობა რითი დავყოფთ) პირველ ასოს
