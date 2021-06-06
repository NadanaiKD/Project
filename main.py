# import helper
# from helper import is_apple_in, name, say
# from jinjohn.helper import is_apple_in, name, say
import jinjohn

a = 20
b = 20
c = [1,2,3]
d = (1,2,3)

print(a,b,c,d)

if a == 10:
    print("a is 10")
elif a == 20 and b ==20:
    print("a is 20")
elif a == 30:
    print("a is 30")
else:
    print("a is nothing")

fruits = ["Orange", "Apple", "Pineapple"]
for fruit in fruits:
    if fruit == "Apple":
        print("Yes, I like it")

# print(helper.is_apple_in(fruits))
# print(helper.name)
# print(helper.say())

# print(is_apple_in(fruits))
# print(name)
# print(say())

print(jinjohn.helper.is_apple_in(fruits))