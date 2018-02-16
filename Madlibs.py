"""
This mad libs app will request input from the user to then populate into a story that is printed out at the end.
"""
print "Welcome to Flintus Mad Libs!"
print
print "The application will now begin!"
name = raw_input("What is your name?")

first_adj = raw_input("Enter your first adjective: ")
second_adj = raw_input("Enter your second adjective: ")
third_adj = raw_input("Enter your third adjective: ")

first_verb = raw_input("Enter your first verb: ")
second_verb = raw_input("Enter your second verb: ")
third_verb = raw_input("Enter your third verb: ")

first_noun = raw_input("Enter your first noun: ")
second_noun = raw_input("Enter your second noun: ")
third_noun = raw_input("Enter your third noun: ")
fourth_noun = raw_input("Enter your fourth noun: ")

animal = raw_input("Now input an animal: ")
food = raw_input("Now input a food: ")
fruit = raw_input("Now input a fruit: ")
number = raw_input("Now input a number: ")
hero_name = raw_input("Now input a superhero name: ")
country = raw_input("Now input a counrty: ")
dessert = raw_input("Now input a dessert: ")
year = raw_input("Now input a year: ")


#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rhythm of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world."

print STORY % (first_adj, name, first_verb, second_adj, first_noun, second_noun, animal, food, second_verb, third_noun, fruit, third_adj, name, third_verb, number, name, hero_name, hero_name, name, country, name, dessert, name, year, fourth_noun)