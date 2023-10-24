from utils import *

# hardcoded file name can be removed and stored in a config file, or pass arguments at runtime
input_f = open("files/input_robots.txt", 'r')
output_f = open("files/output_robots.txt", 'w')

robots_dict, perimeter_x, perimeter_y = convert_input_file(input_f)

input_coordinates_validate(perimeter_x, perimeter_y)

lost_coordinates = []
acceptable_commands = ["L", "R", "F"]

# Main for loop in iterate through all robot start points and their respective instructions
for robot_start_point, robot_instructions in robots_dict.items():

    print("Starting: ", robot_start_point, robot_instructions)
    starting_x, starting_y, starting_p = robot_start_point.split()

# All robots are to start at their specified coordinates and in a good state
    starting_state = "GOOD"

    current_position = {
        "active_x": starting_x,
        "active_y": starting_y,
        "active_p": starting_p,
        "active_state": starting_state
    }

# iterating to all the instructions and applying the correct update which will determine the next position
    for instruction in robot_instructions:

        active_x = int(current_position.get("active_x"))
        active_y = int(current_position.get("active_y"))
        active_p = current_position.get("active_p")
        active_state = current_position.get("active_state")

        if instruction == "L":
            p_updated = anticlockwise(active_p)
            current_position.update({"active_p": p_updated})

        elif instruction == "R":
            p_updated = clockwise(active_p)
            current_position.update({"active_p": p_updated})

        elif instruction == "F":

            if active_p == "N":
                # Checks if bot is to be within perimeter or will be LOST, so we can record the last known coordinates hence leave a 'smell'
                if perimeter_checker_y(active_y + 1, perimeter_y) is True:
                    # Check if robot has been lost here before
                    if smell_zone(active_x, active_y, active_p, lost_coordinates) is True:
                        pass
                    else:
                        # if the robots next instruction is not to take it out of the perimeter or it is not currenly about to go in the...
                        # same direction as a lost robot then the instrction will update its position in the dictionary accordinngly
                        current_position.update({"active_y": (active_y + 1)})
                else:
                    if smell_zone(active_x, active_y, active_p, lost_coordinates) is True:
                        pass
                    else:

                        # If not in a smell zone but still going out of the perimeter then record ...
                        # last coordinates (not updated) and set status to lost
                        current_position.update({"active_y": active_y, "active_state": " LOST"})
                        lost_coordinates.append([active_x, active_y, active_p])
                        break

            elif active_p == "S":

                if perimeter_checker_y(active_y - 1, perimeter_y) is True:
                    # Check if robot has been lost here before
                    if smell_zone(active_x, active_y, active_p, lost_coordinates) is True:
                        pass
                    else:
                        current_position.update({"active_y": (active_y - 1)})
                else:

                    if smell_zone(active_x, active_y, active_p, lost_coordinates) is True:
                        pass
                    else:
                        current_position.update({"active_y": active_y, "active_state": " LOST"})
                        lost_coordinates.append([active_x, active_y, active_p])
                        break

            elif active_p == "E":

                if perimeter_checker_x(active_x + 1, perimeter_x) is True:
                    # Check if robot has been lost here before
                    if smell_zone(active_x, active_y, active_p, lost_coordinates) is True:
                        pass
                    else:
                        current_position.update({"active_x": (active_x + 1)})
                else:
                    if smell_zone(active_x, active_y, active_p, lost_coordinates) is True:
                        pass
                    else:
                        current_position.update({"active_x": active_x, "active_state": " LOST"})
                        lost_coordinates.append([active_x, active_y, active_p])
                        break

            elif active_p == "W":
                # Checking to see if it is going to be within the perimeter
                if perimeter_checker_x(active_x - 1, perimeter_x) is True:
                    # Check if robot has been lost here before
                    if smell_zone(active_x, active_y, active_p, lost_coordinates) is True:
                        pass
                    else:
                        current_position.update({"active_x": (active_x - 1)})
                else:
                    if smell_zone(active_x, active_y, active_p, lost_coordinates) is True:
                        pass
                    else:
                        current_position.update({"active_x": active_x, "active_state": " LOST"})
                        lost_coordinates.append([active_x, active_y, active_p])
                        break

    # Printing & writing to output file the new position/status of the robot
    print(clean_output(**current_position))
    output_f.write(clean_output(**current_position))
