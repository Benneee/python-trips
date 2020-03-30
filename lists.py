friends = ['ade', 'sam', 'chris', 'festus', 'felix'];
cars = [911,130,328,535,740,308]

list_length = len(friends);
ade_position = friends.index('ade');
festus_count = friends.count('festus');

# cars.sort() does not work here
sorted_cars = sorted(cars)
descending_cars = sorted(cars, reverse=True);

max_of_cars = max(cars);
min_of_cars = min(cars);
sum_of_cars = sum(cars);

# print(list_length, ade_position, festus_count);
# print(sorted_cars);
# print(descending_cars);
# print(max_of_cars);
# print(min_of_cars);
# print(sum_of_cars);


# List Manipulation methods
friends.append('benneee');
# print(friends);

# cars.insert(2, 504);
# print(cars);

# friends[5] = 'sola';
# print(friends);

# friends.extend(cars);
# print(friends);

# friends.remove('benneee');
# print(friends);

# Here, pop can take an argument
# popped_friend = friends.pop();
# popped_friend = friends.pop(5);
# print(popped_friend);

# del cars[2]


# Copying List Content
# new_cars = cars[:]
# new_cars = cars.copy() #This method doesn't work for me
# new_cars = list(cars);
# print(new_cars)
