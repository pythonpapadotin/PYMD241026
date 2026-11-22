import time

list_data = []
dict_data = {}

for i in range(1, 10000000):
    key = "BlaBla"+str(i)
    list_data.append(key)
    dict_data[key] = i

print('len of list_data', len(list_data))

print('len of dict_data', len(dict_data))


# Aim: To search an item for example BlaBla9999999
search_key = "BlaBla999999"

start_list_time = time.time()

count = 0
found = False
for item in list_data:
    if item == search_key:
        print('Found! in list', count)
        found = True
        break
    count += 1
if not found:
    print('Not Found! in list')

end_list_time = time.time()

total_time_list = end_list_time-start_list_time
print("Time for list soln", total_time_list)

start_dict_time = time.time()

result = dict_data.get(search_key)
if result is None:
    print("Not found in dict!")
else:
    print("Found in dict", result)

end_dict_time = time.time()

total_time_dict = end_dict_time-start_dict_time
print("Time for dict soln", total_time_dict)

print('Ratio of list to dict', total_time_list/total_time_dict)