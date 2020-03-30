# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name

name = input('Hi! What is your name? ').capitalize();
distance = input('How many miles away are you? ');

distance_in_miles = float(distance) * 1.609
print('Hi', name, 'You\'re',  distance_in_miles,'miles' 'away from here')
