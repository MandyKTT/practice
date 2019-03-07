## 遍历整个列表
下面使用 for 循环来打印魔术师名单中的所有名字：
```python
magicians=['alice','david','caroline']
for magician in magicians:
    print(magician)
```
这行代码让Python从列表 magicians 中取出一个名字，并将其存储在变量 magician 中。
输出很简单，就是列表中所有的姓名：

    alice
    david
    carolina

## 创建数值列表
列表非常适合用于存储数字集合，而Python提供了很多工具，可帮助你高效地处理数字列表。明白如何有效地使用这些工具后，即便列表包含数百万个元素，你编写的代码也能运行得很好。
### 使用range()函数
```python
for value in range(1,5):
    print(value)
```
在这个示例中， range() 只是打印数字1~4
函数 range() 让Python从你指定的第一个值开始数，并在到达你指定的第二个值后停止，因此输出不包含第二个值（这里为5）。
         
    1
    2
    3
    4
使用 range() 时，如果输出不符合预期，请尝试将指定的值加1或减1.
### 使用range()创建列表
要创建数字列表，可使用函数 list() 将 range() 的结果直接转换为列表。
```python
numbers=list(range(1,6))
print(numbers)
```
输出结果

    [1, 2, 3, 4, 5]
使用函数 range() 时，还可指定步长。例如，下面的代码打印1~10内的偶数：
```python
even_numbers=list(range(2,11,2))
print(even_numbers)
```
在这个示例中，函数 range() 从2开始数，然后不断地加2，直到达到或超过终值（11），因此输出如下：

    [2, 4, 6, 8, 10]

使用函数 range() 几乎能够创建任何需要的数字集，例如，创建一个列表，其中包含前
10个整数（即1~10）的平方。
```python
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)
```
在Python中，两个星号（ ** ）表示乘方运算。
输出结果

    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 

### 对数字列表执行简单的统计计算
找出数字列表的最大值、最小值和总和：
```python
digits=[1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))
```
输出结果：
    
    0
    9
    45
### 列表解析
列表解析将for循环和创建新元素的代码合并成一行，并且自动附加新元素。
下面的示例使用列表解析创建平方数列表：
```python
squares=[value**2 for value in range(1,11)]
print(squares)
```
要使用这种语法，首先指定一个描述性的列表名，如 squares ；然后，指定一个左方括号，并定义一个表达式，用于生成你要存储到列表中的值。在这个示例中，表达式为 value** 2 ，它计算平方值。接下来，编写一个 for 循环，用于给表达式提供值，再加上右方括号。在这个示例中，for 循环为 for value in range(1,11) ，它将值1~10提供给表达式 value ** 2 。请注意，这里的 for语句末尾没有冒号。
结果与你在前面看到的平方数列表相同：

    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    
## 使用列表的一部分
还可以处理列表的部分元素——Python称之为切片。
### 切片
要创建切片，可指定要使用的第一个元素和最后一个元素的索引。与函数 range() 一样，Python在到达你指定的第二个索引前面的元素后停止。要输出列表中的前三个元素，需要指定索引0~3，这将输出分别为 0 、 1 和 2 的元素。
下面的示例处理的是一个运动队成员列表：
```python
players=['charles','martina','michael','florence','eli']
print(players[0:3])
```
print(players[0:3])代码打印该列表的一个切片，其中只包含三名队员。

    ['charles', 'martina', 'michael']
如果你没有指定第一个索引，Python将自动从列表开头开始：
```python
players=['charles','martina','michael','florence','eli']
print(players[:4])
```
由于没有指定起始索引，Python从列表开头开始提取：

    ['charles', 'martina', 'michael', 'florence']
要让切片终止于列表末尾，也可使用类似的语法。例如，如果要提取从第3个元素到列表末尾的所有元素，可将起始索引指定为 2 ，并省略终止索引：
```python
players=['charles','martina','michael','florence','eli']
print(players[2:])
```
Python将返回从第3个元素到列表末尾的所有元素：

    ['michael', 'florence', 'eli']
    
### 遍历切片
```python
players=['charles','martina','michael','florence','eli']
print("Here are the first three players on my team:" )
for player in players[:3]:
    print(player.title())
```
以上代码没有遍历整个队员列表，而只遍历前三名队员：

    Here are the first three players on my team:
    Charles
    Martina
    Michael
### 复制列表
要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引（ [:] ）。这让Python创建一个始于第一个元素，终止于最后一个元素的切片，即复制整个列表。
例如，假设有一个列表，其中包含你最喜欢的四种食品，而你还想创建另一个列表，在其中包含一位朋友喜欢的所有食品。
```python
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
```
打印每个列表后，我们发现它们包含的食品相同：

    My favorite foods are:
    ['pizza', 'falafel', 'carrot cake']

    My friend's favorite foods are:
    ['pizza', 'falafel', 'carrot cake']

为核实我们确实有两个列表，下面在每个列表中都添加一种食品，并核实每个列表都记录了相应人员喜欢的食品：
```python
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
```
最后，打印这两个列表，核实这两种食品包含在正确的列表中。

    My favorite foods are:
    ['pizza', 'falafel', 'carrot cake', 'cannoli']

    My friend's favorite foods are:
    ['pizza', 'falafel', 'carrot cake', 'ice cream']
    

## 元组
列表非常适合用于存储在程序运行期间可能变化的数据集。Python将不能修改的值称为不可变的，而不可变的列表被称为元组。
### 定义元组
元组看起来犹如列表，但使用圆括号而不是方括号来标识。定义元组后，就可以使用索引来访问其元素，就像访问列表元素一样。
例，有一个长、宽固定的矩形
```python
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
```
使用的语法与访问列表元素时使用的语法相同

    200
    50

尝试修改元组 dimensions 中的一个元素
```python
dimensions=(200,50)
dimensions[0]=250
```
由于试图修改元组的操作是被禁止的，因此Python指出不能给元组的元素赋值：
    
    Traceback (most recent call last):
    50
    File "C:/Users/ASUS/PycharmProjects/practice/for_testing.py", line 52, in <module>
    dimensions[0]=250
    TypeError: 'tuple' object does not support item assignment

    Process finished with exit code 1
### 修改元组变量
虽然不能修改元组的元素，但可以给存储元组的变量赋值。因此，如果要修改前述矩形的尺寸，可重新定义整个元组：
```python
dimensions=(200,50)
print("Original dimensiona:")
for dimension in dimensions:
    print(dimension)

dimensions=(400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
```
这次，Python不会报告任何错误，因为给元组变量赋值是合法的：

    Original dimensiona:
    200
    50

    Modified dimensions:
    400
    100
相比于列表，元组是更简单的数据结构。如果需要存储的一组值在程序的整个生命周期内都
不变，可使用元组。

