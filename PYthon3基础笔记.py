1.变量。
   ---------------------------------
   e.g.
   message = "Hello Python world!"
   print(message)
   ---------------------------------
   Hello Python world!
   ---------------------------------

2.字符串。
   在Python中，用引号括起的都是字符串，其中的引号可以是单引号，也可以是双引号。
   ---------------------------------
   e.g. 
   "This is a string."
   'This is a string.'
   ---------------------------------

   2.1.改变字符串大小写。
      ---------------------------------
      e.g.
      name = "Ada lovelace" 
      print(name.title())     #首字母大写
      print(name.upper())     #全部大写
      print(name.lower())     #全部小写
      ---------------------------------
      Ada Lovelace
      ADA LOVELACE
      ada lovelace
      ---------------------------------

   2.2.合并（拼接）字符串。
      ---------------------------------
      e.g.
      first_name = "ada"
      last_nema = "lovelace"
      full_name = first_name + " " + last_name

      print(full_name)
      print("Hello," + full_name.title() + "!")
      ---------------------------------
      ada lovelace
      Hello,Ada Lovelace!
      ---------------------------------

   2.3.使用制表符或空行符添加空白。("\t \n")
      ---------------------------------
      略
      ---------------------------------

   2.4.删除空白。
      ---------------------------------
      e.g.
      >>> favorite_language = ' python '
      >>> favorite_language
      ' python '
      >>> favorite_language.rstrip() #删除字符串后面多余空白
      ' python'
      >>> favorite_language.lstrip() #删除字符串前面空白
      'python '
      >>> favorite_language.strip()  #删除字符串两端空白
      'python'
      ---------------------------------

3.数字。

   3.1.整数。
      ---------------------------------
      e.g.
      >>> 2 + 3
      5
      >>> 3 - 2
      1
      >>> 2 * 3
      6
      >>> 3 / 2
      1.5
      >>> 3 ** 2
      9
      >>> 2 + 3 * 4
      14
      ---------------------------------

   3.2.浮点数。带小数点的数都是浮点数。
      ---------------------------------
      e.g.
      >>> 0.1 + 0.1
      0.2
      >>> 0.2 + 0.2
      0.4
      >>> 2 * 0.1
      0.2
      ---------------------------------

   3.3.str()函数
      ---------------------------------
      e.g.
      age = 23
      message = "Happy " + str(age) + "rd Birthday!"
      print(message)
      ---------------------------------
      Happy 23rd Birthday!
      ---------------------------------

4.列表。
   列表是由一系列按照特定顺序排列的元素组成。
   ---------------------------------
   e.g.
   bicycles = ['trek','cannondale','redline','specialized']
   print(bicycles)
   ---------------------------------
   ['trek','cannondale','redline','specialized']
   ---------------------------------

   4.1.访问列表元素。
      ---------------------------------
      e.g.
      bicycles = ['trek','cannondale','redline','specialized']
      print(bicycles[0])
      ---------------------------------
      trek
      ---------------------------------
      索引可以从最后开始，最后一位索引为-1，倒数第二为-2，以此类推。

   4.2.使用列表里的值
      ---------------------------------
      e.g.
      bicycles = ['trek', 'cannondale', 'redline', 'specialized']
      message = "My first bicycle was a " + bicycles[0].title() + "."
      print(message)
      ---------------------------------
      My first bicycle was a Trek.
      ---------------------------------

   4.3.修改列表元素。
      ---------------------------------
      e.g.
      motorcycles = ['honda', 'yamaha', 'suzuki'] 
      print(motorcycles)

      motorcycles[0] = 'ducati' 
      print(motorcycles)
      ---------------------------------
      ['honda', 'yamaha', 'suzuki'] 
      ['ducati', 'yamaha', 'suzuki']
      ---------------------------------

   4.4.添加列表元素。
      append()在末尾添加元素。
      ---------------------------------
      e.g.
      motorcycles = ['honda','yamaha','suzuki']
      print(motorcycles)

      motorcycles.append('ducati')
      print(motorcycles)
      ---------------------------------
      ['honda','yamaha','suzuki']
      ['honda','yamaha','suzuki','ducati']
      ---------------------------------

      append()可以动态地创建列表。先创建一个空列表，再使用一系列的 append()语句添加元素。
      ---------------------------------
      e.g.
      motorcycles = []

      motorcycles.append('honda')
      motorcycles.append('yamaha')
      motorcycles.append('suzuki')

      print(motorcycles)
      ---------------------------------
      ['honda','yamaha','suzuki']
      ---------------------------------

      insert()插入元素。
      ---------------------------------
      e.g.
      motorcycles = ['honda', 'yamaha', 'suzuki']

      motorcycles.insert(0, 'ducati') 
      print(motorcycles)
      ---------------------------------
      ['ducati', 'honda', 'yamaha', 'suzuki']
      ---------------------------------

   4.5.删除列表元素。
      del()语句删掉指定位置的值。
      ---------------------------------
      e.g.
      motorcycles = ['honda', 'yamaha', 'suzuki'] 
      print(motorcycles)

      del motorcycles[0] 
      print(motorcycles)
      ---------------------------------
      ['honda', 'yamaha', 'suzuki'] 
      ['yamaha', 'suzuki']
      ---------------------------------

      pop()语句删除列表末尾位置的元素。
      ---------------------------------
      e.g.
      motorcycles = ['honda', 'yamaha', 'suzuki'] 
      print(motorcycles)

      popped_motorcycle = motorcycles.pop() 
      print(motorcycles)
      print(popped_motorcycle)
      ---------------------------------
      ['honda', 'yamaha', 'suzuki'] 
      ['honda', 'yamaha']
      suzuki
      ---------------------------------
      如果你不确定该使用 del 语句还是 pop() 方法，下面是一个简单的判断标准:如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用 del 语句;如果你要在删除元素后还能继续使用它，就使用方法 pop() 。

   4.6.根据值来删除元素。
      remove()
      --------------------------------
      e.g.
      motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
      print(motorcycles)

      motorcycles.remove('ducati') 
      print(motorcycles)
      --------------------------------
      ['honda', 'yamaha', 'suzuki', 'ducati']
      ['honda', 'yamaha', 'suzuki']
      --------------------------------

   4.7.对列表进行永久排序。
      sort()（按字母顺序排列）
      --------------------------------
      e.g.
      cars = ['bmw', 'audi', 'toyota', 'subaru'] 
      cars.sort()
         print(cars)
         --------------------------------
         ['audi','bmw','subaru','toyota']
         --------------------------------

         sort()（按字母逆序排列）
         --------------------------------
         e.g.
         cars = ['bmw', 'audi', 'toyota', 'subaru'] 
         cars.sort(reverse=True)
      print(cars)
      --------------------------------
      ['toyota','subaru','bmw','audi']
      --------------------------------

   4.8.对列表进行临时排序。
      sorted()临时排序，实际顺序并没有变化。
      --------------------------------
      e.g.
      cars = ['bmw', 'audi', 'toyota', 'subaru']
      print("Here is the original list:") 
      print(cars)
      print("\nHere is the sorted list:") 
      print(sorted(cars))
      print("\nHere is the original list again:") 
      print(cars)
      --------------------------------
      Here is the original list:
      ['bmw', 'audi', 'toyota', 'subaru']

      Here is the sorted list:
      ['audi', 'bmw', 'subaru', 'toyota']

      Here is the original list again: 
      ['bmw', 'audi', 'toyota', 'subaru']
      --------------------------------

   4.9.倒着打印列表。
      reverse()
      --------------------------------
      e.g.
      cars = ['bmw', 'audi', 'toyota', 'subaru'] 
      print(cars)

      cars.reverse() 
      print(cars)
      --------------------------------
      ['bmw', 'audi', 'toyota', 'subaru']
      ['subaru', 'toyota', 'audi', 'bmw']
      --------------------------------

   4.10.确定列表的长度。
      len()
      --------------------------------
      e.g.
      >>> cars = ['bmw', 'audi', 'toyota', 'subaru'] 
      >>> len(cars)
      4
      --------------------------------
      Python计算列表元素数时从1开始，因此确定列表长度时，你应该不会遇到差一错误。

   4.11.列表索引错误。
      索引从0开始，如果出现错误，可以将指定的索引先减1，然后运行程序，测试结果。
      需要访问列表最后一个元素时，都可使用索引 -1 。
      索引 -1 总是返回最后一个列表元素，仅当列表为空时，访问最后一个元素才会导致错误。

5.操作列表。
   5.1.遍历列表。
      使用for循环，将列表里的每个元素都打印出来。
      --------------------------------
      e.g.
      magicians = ['alice', 'david', 'carolina'] 
      for magician in magicians:
         print(magician) 
      --------------------------------
      alice 
      david 
      carolina
      --------------------------------

   5.2.数值列表。
      range()生成一系列数字。
      --------------------------------
      e.g.
      for  value in range(1,5):
         print(value)
      --------------------------------
      1
      2
      3
      4
      --------------------------------
      函数 range()从指定的第一个值开始数，到达第二个值之后结束，不会输出第二个值。

      使用 range()创建数字列表，可以使用函数 list()将 range()的结果直接转换为列表。
      --------------------------------
      e.g.
      numbers = list(range(1,6,2))
      print(numbers)
      --------------------------------
      [1,3,5]
      --------------------------------

   5.3.对数字列表执行简单的统计计算。
      --------------------------------
      e.g.
      >>>digits=[1,2,3,4,5,6,7,8,9,0] 
      >>> min(digits)
      0
      >>> max(digits)
      9
      >>> sum(digits) 
      45
      --------------------------------

   5.4.解析列表。
      列表解析可以用一行代码代替三四行代码，生成列表。
      --------------------------------
      e.g.
      squares = [value**2 for value in range(1,11)]
      print(squares)
      --------------------------------
      [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
      --------------------------------

   5.5.
      --------------------------------
      e.g.
      my_foods = ['pizza', 'falafel', 'carrot cake'] 
      friend_foods = my_foods[:]
      print("My favorite foods are:") 
      print(my_foods)
      print("\nMy friend's favorite foods are:") 
      print(friend_foods)
      --------------------------------

6.元组。
   元组犹如列表，但是使用圆括号。
   -------------------------------
   e.g.
   dimensions = (200, 50) 
   print(dimensions[0])
   print(dimensions[1])
   -------------------------------
   200
   50
   -------------------------------
   元组禁止修改。

7.条件测试。
   7.1.条件测试中检测特定值是否包含在列表中。
      关键字 in。
      --------------------------------
      e.g.
      >>> requested_toppings = ['mushrooms','onions','pineapple']
      >>> 'mushrooms' in requested_toppings
      True
      >>> 'pepperoni' in requested_toppings
      False
      --------------------------------
   7.2.条件测试中检测特定值是否不包含在列表中。
      --------------------------------
      e.g.
      anned_users = ['andrew', 'carolina', 'david'] 
      user = 'marie'

      if user not in banned_users:
         print(user.title() + ", you can post a response if you wish.")
      --------------------------------
      Marie, you can post a response if you wish.

8.字典。
   8.1.简单的字典。
      --------------------------------
      e.g. 
      alien_0 = {'color':'green','points': 5}

      print(alien_0['color'])
      print(alien_0['points'])
      --------------------------------
      green
      5
      --------------------------------

   8.2.添加字典的键值对。
      --------------------------------
      e.g.
      alien_0 = {'color': 'green', 'points': 5} 
      print(alien_0)

      alien_0['x_position'] = 0
      alien_0['y_position'] = 25
      print(alien_0) 
      --------------------------------
      {'color': 'green', 'points': 5}
      {'color': 'green', 'points': 5, 'y_position': 25, 'x_position': 0}
      --------------------------------

   8.3.修改字典的值。
      --------------------------------
      e.g.
      alien_0 = {'color': 'green'}
      print("The alien is " + alien_0['color'] + ".")

      alien_0['color'] = 'yellow'
      print("The alien is now " + alien_0['color'] + ".")
      --------------------------------
      The alien is green.
      The alien is now yellow.
      --------------------------------

   8.4.删除字典的键值对。
      --------------------------------
      e.g.
      alien_0 = {'color': 'green', 'points': 5} 
      print(alien_0)

      del alien_0['points'] 
      print(alien_0)
      --------------------------------
      {'color': 'green', 'points': 5}
      {'color': 'green'}
      --------------------------------

   8.5.有类似对象组成的字典。
      --------------------------------
      e.g.
      favorite_languages = { 'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
    
      alien_0 = {'color': 'green', 'points': 5} 
      print(alien_0)
      del alien_0['points'] 
      print(alien_0)
      --------------------------------
      ['color': 'green', 'points': 5]
      ['color': 'green']
      --------------------------------

   8.6.遍历字典。
      --------------------------------
      e.g.
      user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi',}

      for key, value in user_0.items():  
      print("\nKey: " + key)
      print("Value: " + value)
      --------------------------------
      Key: last 
      Value: fermi

      Key: first 
      Value: enrico

      Key: username 
      Value: efermi
      --------------------------------
      即便遍历字典时，键—值对的返回顺序也与存储顺序不同。Python不关心键—值对的存储顺序，而只跟踪键和值之间的关联关系。

   8.7.遍历字典的所有键。
      --------------------------------
      e.g.
      favorite_languages = { 'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
      for name in favorite_languages.keys(): 
         print(name.title())
      --------------------------------                                   
      Jen
      Sarah
      Edward
      Phil
      --------------------------------

   8.8.按顺序遍历字典的所有键。
      sorted()函数。
      --------------------------------
      e.g.
      favorite_languages = { 'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
      for name in sorted(favorite_languages.keys()): 
         print(name.title() + ", thank you for taking the poll.")
      --------------------------------
      Edward, thank you for taking the poll. 
      Jen, thank you for taking the poll. 
      Phil, thank you for taking the poll. 
      Sarah, thank you for taking the poll.
      --------------------------------

   8.9.遍历字典的所有值。
      遍历值，所以可以使用方法 values()。
      --------------------------------
      e.g.
      favorite_languages = { 'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
      print("The following languages have been mentioned:") 
      for language in favorite_languages.values():
         print(language.title())
      --------------------------------
      The following languages have been mentioned: Python
      C
      Python
      Ruby
      --------------------------------

9.input() & while 循环
  input()暂停程序，让用户输入一些文本。
  ----------------------------------
  e.g.
  message = input("Tell me something, and I will repeat it back to you: ")
  print(message)
  ----------------------------------
  Tell me something, and I will repeat it back to you: Hello everyone!
  Hello everyone!
  ----------------------------------

  int()获取数值输入。
  ----------------------------------
  e.g. 
  >>> age = input("How old are you? ")
  How old are you? 21
  >>> age 
  '21'
  >>> age = int(age)
  >>> age >= 18
  True
  ----------------------------------

  求模运算符（%）
  ----------------------------------
  e.g.
  >>> 4 % 3
  1
  >>> 5 % 3
  2
  >>> 6 % 3
  0
  >>> 7 % 3
  1
  ----------------------------------

  使用用户输入来填充字典。
  ----------------------------------
  e.g.
  responses = {}
  polling_active = True

  while polling_active:
   name = input("\nWhat is your name? ")
   response = input("Which mountain would you like to climb someday? ")

   responses[name] = response

   repeat = input("Would you like to let another person respond? (yes/ no) ")
   if repeat == 'no':
      polling_active = favorite_languages

  print("\n--- Poll Result ---")
  for name, response in responses.items():
   print(name + " would like to climb " + response + ".")
  ----------------------------------
  What is your name? Eric
  Which mountain would you like to climb someday? Denali
  Would you like to let another person respond? (yes/ no) yes

  What is your name? Lynn
  Which mountain would you like to climb someday? Devil`s Thumb
  Would you like to let another person respond? (yes/ no) no

  --- Poll Result ---
  Lynn would like to climb Devil`s Thumb.
  Eric would like to climb Denali.
  ----------------------------------

10.函数。
   10.1.简单函数。
      ------------------------------------
      e.g. 
      def greet user():
         print("Hello!")

      greet_user()
      ------------------------------------
      Hello!
      ------------------------------------

   10.2.传递信息。
      ------------------------------------
      e.g.
      def greet_user(username):
         print("Hello, " + username.title() + "!")

      greet_user('jesse')
      ------------------------------------
      Hello, Jesse!
      ------------------------------------

   10.3.传递参数。     
      鉴于函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参。向函数传递实参的方式很多，可使用位置实参，这要求实参的顺序与形参的顺序相同;也可使用关键字实参，其中每个实参都由变量名和值组成;还可使用列表和字典。
      ------------------------------------
      e.g.
      def describe_pet(animal_type, pet_name):
         print("\nI have a " + animal_type + ".")
         print("My " + animal_type + "'s name is " + pet_name.title() + ".")

      describe_pet('hamster', 'harry')
      ------------------------------------
      I have a hamster.
      My hamster`s name is Harry.
      ------------------------------------

   10.4.关键字实参。
      关键字实参是传递给函数的名称—值对。你直接在实参中将名称和值关联起来了，因此向函数传递实参时不会混淆（不会得到名为Hamster的harry这样的结果）。       
      ------------------------------------
      e.g.
      def describe_pet(animal_type, pet_name):
         print("\nI have a " + animal_type + ".")
         print("My " + animal_type + "'s name is " + pet_name.title() + ".")

      describe_pet(animal_type='hamster', pet_name='harry')
      ------------------------------------
      I have a hamster.
      My hamster`s name is Harry.
      ------------------------------------

   10.5.函数返回值。
      函数并非总是直接显示输出，相反，它可以处理一些数据，并返回一个或一组值。函数返回的值被称为返回值。
      ------------------------------------
      e.g.
      def get_formatted_name(first_name, last_name):
         full_name = first_name + ' ' + last_name
         return full_name.title()
      musician = get_formatted_name('jimi', 'hendrix') 
      print(musician)
      ------------------------------------
      Jimi Hendrix
      ------------------------------------

   10.6.传递列表。
      ------------------------------------
      e.g.
      def greet_users(names):
         for name in names:
            msg = "Hello, " + name.title() + "!" 
            print(msg)

      usernames = ['hannah', 'ty', 'margot'] 
      greet_users(usernames)
      ------------------------------------
      Hello, Hannah!
      Hello, Ty!
      Hello, Margot!
      ------------------------------------

11.创建和使用类。
   11.1.创建类。
      ------------------------------------
      e.g.
      class Dog():
         def _init_(self, name, age):
            self.name = name
            self.age = age

         def sit(self):
            print(self.name.title() + " is not sitting.")

         def roll_over(self):
            print(self.name.title() + " rolled over!")
      ------------------------------------

   11.2._init_()。
      方法 __init__()定义成了包含三个形参:self 、name 和 age 。在这个方法的定义中，因为Python调用这个 __init__() 方法来创建 Dog 实例时，将自动传入实参self，所以形参self必不可少，还必须位于其他形参的前面。

12.根据类创建实例。
   ----------------------------------
   e.g.
   class Dog():
      --snip--

   my_dog = Dog('willie', 6)

   print("My dog's name is " + my_dog.name.title() + ".")
   print("My dog is " + str(my_dog.age) + " years old.")
   ----------------------------------
   12.1.访问属性。
      要访问实例的属性，可使用句点表示法。句点表示法在Python中很常用，这种语法演示了Python如何获悉属性的值。在这里，Python先找到实例my_dog，再查找与这个实例相关联的属性name。在Dog类中引用这个属性时，使用的是self.name。
      ------------------------------------
      e.g.
      my_dog.name
      ------------------------------------
      My dog`s name is Willie.
      My dog is 6 years old.
      ------------------------------------

   12.2.调用方法。
      根据Dog类创建实例后，就可以使用句点表示法来调用Dog类中定义的任何方法。
      ------------------------------------
      e.g.
      class Dog(): 
         --snip--
      my_dog = Dog('willie', 6) 
      my_dog.sit() 
      my_dog.roll_over()
      ------------------------------------
      Willie is now sitting.
      Willie rolled over!
      ------------------------------------

   12.3.创建多个实例。
      可按需求根据类创建任意数量的实例。
      ------------------------------------
      e.g.
      class Dog(): 
         --snip--
      my_dog = Dog('willie', 6) 
      your_dog = Dog('lucy', 3)

      print("My dog's name is " + my_dog.name.title() + ".") 
      print("My dog is " + str(my_dog.age) + " years old.") 
      my_dog.sit()

      print("\nYour dog's name is " + your_dog.name.title() + ".") 
      print("Your dog is " + str(your_dog.age) + " years old.") 
      your_dog.sit()
      ------------------------------------
      My dog`s name is Willie. 
      My dog is 6 years old. 
      Willie is now sitting.

      Your dog`s name is Lucy. 
      Your dog is 3 years old. 
      Lucy is now sitting.
      ------------------------------------

13.使用类和实例。
   13.1.Car类。
      ------------------------------------
      e.g.
      class Car():

         def _init_(self,make,model,year):
            self.make = make
            self.model = model
            self.year = year

         def get_descriptive_name(self):
            long_name = str(self.year) + ' ' + self.make + ' ' + self.model
            return long_name.title()

      my_new_car = Car('audi', 'a4', 2016) 
      print(my_new_car.get_descriptive_name())
      ------------------------------------
      2016 Audi A4
      ------------------------------------

   13.2.修改属性。
      ------------------------------------
      e.g.
      class Car():
         --snip--

         def update_odometer(self, mileage):
            self.odometer_reading = mileage

      my_new_car = Car('audi', 'a4', 2016)
      print(my_new_car.get_descriptive_name())

      my_new_car.upper(23)
      my_new_car.read_odometer()
      ------------------------------------
      2016 Audi A4
      This car has 23 miles on it.
      ------------------------------------

14.






