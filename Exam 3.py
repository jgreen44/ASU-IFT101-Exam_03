#   Filename:           Exam 3
#   Created by:         jasongreen
#   Date:               Tuesday, February 12, 2019
#   Time of Creation:   22:48
#   ---

# loop = 0
# average = 0
# total_number = 0
# number_array = []
# while loop < 10:
#     number = int(input("Enter a number: "))
#     number_array.append(number)
#     total_number = total_number + number
#     loop += 1
#
# print("The average is {}.".format(total_number / 10))
# print("The max value was {}.".format(max(number_array)))
# print("The min value was {}.".format(min(number_array)))


temp = int(input("Enter a temperature: "))
green_light = True
warning = True

if temp < 34:
    print("Warning Sound = {}".format(warning))
    print("Warning sound turned on!")
    green_light = False
    print("Green Light = {}".format(green_light))
    print("Green light turned off!")
elif (temp > 33) or (temp < 41):
    warning = False
    green_light = True
    print("Warning Sound = {}".format(warning))
    print("Warning sound turned off!")
    print("Green Light = {}".format(green_light))
    print("Green light turned on!")
else:
    print("Yeah, you're fine bro.")
