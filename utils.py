import collections


# returns new position based on current position and an anticlockwise more (Left)
def anticlockwise(p):
    if p == "W":
        return "S"
    elif p == "S":
        return "E"
    elif p == "E":
        return "N"
    elif p == "N":
        return "W"

# returns new position based on current position and a clockwise more (Right)


def clockwise(p):
    if p == "W":
        return "N"
    elif p == "N":
        return "E"
    elif p == "E":
        return "S"
    elif p == "S":
        return "W"

# Checks the bots desired movement direction against max X perimeter, to know if it is going to be LOST


def perimeter_checker_x(active_x, perimeter_x):
    if int(active_x) > int(perimeter_x) or int(active_x) < 0:
        return False
    else:
        return True

# Checks the bots desired movement direction against max y perimeter, to know if it is going to be LOST


def perimeter_checker_y(active_y, perimeter_y):
    if int(active_y) > int(perimeter_y) or int(active_y) < 0:
        return False
    else:
        return True


# Checks if a bot has been lost in this zone, so the instruction to move in the same direction is avoided
def smell_zone(x, y, p, lost_coordinates):
    for lc in lost_coordinates:
        if collections.Counter(lc) == collections.Counter([x, y, p]):
            return True
        else:
            return False


# Converts list to a dictionary, in the desired format
def convert_to_dict(ls_in):
    new_dict = {}
    for i in range(0, len(ls_in), 2):
        new_dict[ls_in[i]] = ls_in[i + 1]
    return new_dict

# Converts input file, to a dictionary and outlines the max perimeter


def convert_input_file(input_f):
    with input_f:
        input_data = input_f.readlines()
        input_list = []
        perimeter_x, perimeter_y = input_data[0].split()
        print("Your max x axis is " + perimeter_x)
        print("Your max y axis is " + perimeter_y)

        for i in input_data[1:]:
            i = i.strip()
            input_list.append(i)

        robots_dict = convert_to_dict(input_list)

        return robots_dict, perimeter_x, perimeter_y


# Cleans output from dictionary, removing unwanted strings to give the exact requested output
def clean_output(active_x, active_y, active_p, active_state):
    clean_out = (str((active_x, active_y, active_p, active_state))
                 .replace("GOOD", "")
                 .replace("'", "")
                 .replace(",", "")
                 .replace("(", "")
                 .replace(")", "")
                 )
    return clean_out + "\n"


def input_coordinates_validate(perimeter_x, perimeter_y):
    if int(perimeter_x) > 50 or int(perimeter_y) > 50:
        print("Error! your initial coordinate value has exceeded maximum of 50")
        exit()
