# Properties of list
# 1. Hetro: put any data type inside list
# 2. ordering -> indexing
# 3. editing/mutability
# 4. slicing


fruits = ['apple', 'mango', 'orange', 'kiwi']
          # 0th      1st      2nd       3rd
# add at the end of the list

fruits.append('pineapple')

fruits.append(45)

print(fruits)

# extending the list items by other list items

numbers = [34, 44, 55]


fruits.extend(numbers)

print("after extending numbers", fruits)

print("0th index item", fruits[0])

print("1st index item", fruits[1])

fruits[0] = 'shyam'

print("after replacing 0th item", fruits)

# fruits[start: end + 1]

print("slice from 0 to 2", fruits[0:3])

fruits.pop()  # removes item from the end

print('after pop', fruits)
#
# fruits.remove('mango')
#
# print('after remove mango', fruits)

fruits = ['mango', 'mango', 'apple', 'mango']

fruits.remove('mango')

print('after remove mango', fruits)

count_result = fruits.count('mango')

print('count result', count_result)
