
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

    for key, value in sorted(restaurant_ratings_dict.iteritems()):
        print "{} is rated at {}.".format(key, value)


def add_user_rating(restaurant_ratings_dict):
    restaurant = raw_input("What is the name of the restaurant?: ").title()
    rating = raw_input("What is the rating of the restaurant?: ")
    restaurant_ratings_dict[restaurant] = rating


def prompt_user_for_info():

    while True:
        if raw_input("Do you want to add a restaurant to the list? y/n: ").lower() == "y":
            user_added_rating(restaurant_ratings_dict)
            return restaurant_ratings_dict
        else:
            

print_restaurant_ratings(get_restaurant_ratings(filename))
