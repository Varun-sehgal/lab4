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
Open lab4 and implement the functions. Here are some key concepts we want to explain:

**Make a copy** vs **Modify in place**:

**Make a copy** requires you to return a new object, which is a different object from the given list, but with the same value.
**Modify in place** requires you to modify the given list, without creating any new object.


**Selection Sort:**

The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.
```
arr = 64 25 12 22 11

// Find the minimum element in arr[0...4] and place it at beginning
11 25 12 22 64

// Find the minimum element in arr[1...4] and place it at beginning of arr[1...4]
11 12 25 22 64

// Find the minimum element in arr[2...4] and place it at beginning of arr[2...4]
11 12 22 25 64

// Find the minimum element in arr[3...4] and place it at beginning of arr[3...4]
11 12 22 25 64 
```
[Here](https://www.youtube.com/watch?v=xWBP4lzkoyM) is a video that illustrates how selection sort works.
## Test your functions
To test our functions, we are going to use pytest as covered in [Lab3](https://github.com/eecs230/lab3/blob/master/README.md).
First check the Python interpreter on your computer to be one of the below:
- ```py``` (Windows)
- ```python3``` (Mac?)
- ```python3.7``` (Windows?)
- ```python37``` (Mac)
- ```C:\Python37\python.exe``` (definitely Windows)
- ```python```
Now, from within the lab3 directory, run this (replacing $PY with your Python):
```
Mac$ $PY -m pipenv install --dev
Win> $PY -m pipenv install --dev
```
Once it’s ready, check that it's good to go by running pytest:
```
Mac$ $PY -m pipenv run pytest
Win> $PY -m pipenv run pytest
```
If all functions are implemented correctly, your code should pass all tests.

