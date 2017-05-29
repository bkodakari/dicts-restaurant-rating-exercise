
import sys
filename = sys.argv[1]
# open file (scores.txt)
# creat empty dictionary
# iterate through the lines
# add each line to it's own list (throw away list within for loop)
# add list[0] as key, list[1] as value to empty dictionary
# print sorted(dictionary)
# "{key} is rated at {value}".format(key, value)


def get_restaurant_ratings(filename):
    """Restaurant rating lister."""

    restaurant_ratings_dict = {}

    with open(filename) as text_file:
        
        for line in text_file:
            restaurant_list = line.strip().split(":")
            restaurant_ratings_dict[restaurant_list[0]] = restaurant_list[1]

    return restaurant_ratings_dict


def print_restaurant_ratings(restaurant_ratings_dict):
    """Prints restaurant ratings"""

    sorted_dict = sorted(restaurant_ratings_dict)
    for key in sorted_dict:
        print "{} is rated at {}.".format(key, restaurant_ratings_dict[key])


print_restaurant_ratings(list_restaurant_ratings(filename))
