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

# print(list_length, ade_position, festus_count);
# print(sorted_cars);
# print(descending_cars);
print(max_of_cars);
print(min_of_cars);

