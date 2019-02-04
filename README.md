# lab4
# Lab 4: List Functions
In this lab, we are going to furthur explore the data structure List and practice writing functions with List. Start by forking this lab into your repository or cloning it to your local machine as we covered in Lab 3. You can find [clone instruction](https://github.com/eecs230/lab3/blob/master/README.md) here.

## Review on List
Create a list:
```
empty_list = []
fruits = ["apple", "banana", "cherry"]
```
Access items:
```
my_fruit = fruits[1] //"banana"
```
Change item value:
```
fruits[0] = "strawberry"
print(fruits) //["strawberry", "banana", "cherry"]
```
Loop through a list:
```
for x in fruits:
    print(x)
```
List length:
```
print(len(fruits)) //3
```
Add item:
```
fruits.append("dragon fruit") //["strawberry", "banana", "cherry", "dragon fruit"]
fruits.insert(1, "mango") //["strawberry", "mango", "banana", "cherry", "dragon fruit"]
```
Remove item:
```
fruits.remove("strawberry") //["mango", "banana", "cherry", "dragon fruit"]
fruits.pop() //["mango", "banana", "cherry"]
```
Filter:
```
num_list = [-2, -1, -4, 1, 2]
positive_list = list(filter(lambda x: x > 0, num_list)) // [1, 2]
```
## Write functions
