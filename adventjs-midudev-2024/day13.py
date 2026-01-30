# 🤖 Is the robot back?
# The elves at the North Pole have created a special robot 🤖 that helps Santa Claus distribute gifts inside a
# large warehouse. The robot moves on a 2D plane and we start from the origin (0, 0).
# We want to know if, after executing a series of movements, the robot returns to exactly where it started.

# The robot's basic commands are:
# L: Move to the left
# R: Move to the right
# U: Move upwards
# D: Move downwards

# But it also has certain modifiers for the movements:
# *: The movement is done with double intensity (e.g., *R means RR)
# !: The next movement is inverted (e.g., R!L is considered as RR)
# ?: The next movement is done only if it hasn't been done before (e.g., R?R means R)
# Note: When the movement is inverted with ! the inverted movement is counted and not the original one.
# For example, !U?U inverts the U movement, so it counts as having done the D movement but not the U. Thus,
# !U?U translates to D?U, and therefore, the final U movement is done.

# You must return:
# true: if the robot returns exactly to where it started
# [x, y]: if the robot does not return to where it started, return the position where it stopped
# isRobotBack("R"); // [1, 0]
# isRobotBack("RL"); // true
# isRobotBack("RLUD"); // true
# isRobotBack("*RU"); // [2, 1]
# isRobotBack("R*U"); // [1, 2]
# isRobotBack("LLL!R"); // [-4, 0]
# isRobotBack("R?R"); // [1, 0]
# isRobotBack("U?D"); // true
# isRobotBack("R!L"); // [2,0]
# isRobotBack("U!D"); // [0,2]
# isRobotBack("R?L"); // true
# isRobotBack("U?U"); // [0,1]
# isRobotBack("*U?U"); // [0,2]
# isRobotBack("U?D?U"); // true
#
# // Step-by-step examples:
# isRobotBack("R!U?U"); // [1,0]
# // 'R'  -> moves to the right
# // '!U' -> inverts and becomes 'D'
# // '?U' -> moves upwards, because the 'U' movement hasn't been done yet
#
# isRobotBack("UU!U?D"); // [0,1]
# // 'U'  -> moves upwards
# // 'U'  -> moves upwards
# // '!U' -> inverts and becomes 'D'
# // '?D' -> does not move, since the 'D' movement has already been done


def is_robot_back(instructions: str) -> bool | list[int, int]:
    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

    inversed_directions = {"R": "L", "L": "R", "U": "D", "D": "U"}

    special_chars = {"*": 0, "!": 0, "?": 0}

    def is_special_char(instruction):
        return instruction in special_chars

    def validate_next_instruction_is_a_valid_direction(
        index: int,
    ) -> tuple[bool, str | None]:
        next_instruction = (
            instructions[index + 1] if index + 1 < len(instructions) else None
        )
        if next_instruction and is_special_char(next_instruction):
            return False, None
        return True, next_instruction

    def apply_movement(instruction: str, index: int, initial_position: tuple[int, int] | None):
        is_valid_direction, next_direction = (
            validate_next_instruction_is_a_valid_direction(index) 
        )

        if not is_valid_direction:
            return None

        if instruction == "?" and next_direction in seen_directions:
            return None

        seen_directions.add(next_direction) if instruction != "!" else seen_directions.add(inversed_directions[next_direction])
        row_to_add, col_to_add = (
            directions[next_direction]
            if instruction != "!"
            else directions[inversed_directions[next_direction]]
        )

        if instruction == "*":
            row_to_add *= 2
            col_to_add *= 2

        updated_position = update_coords(initial_position, (row_to_add, col_to_add))
        return updated_position

    def update_coords(
        current_position: tuple[int, int], coords_to_add: tuple[int, int]
    ) -> tuple[int, int]:
        row_to_add, col_to_add = coords_to_add
        new_row = current_position[0] + row_to_add
        new_col = current_position[1] + col_to_add
        return new_row, new_col

    # For the ? instruction, just in case
    seen_directions = set()

    initial_position = (0, 0)

    was_applied_by_special_char = False
    for index, instruction in enumerate(instructions):
        # If it's not a special char add it to the set of seen directions
        if not is_special_char(instruction):
            if was_applied_by_special_char:
                # restart the flag
                was_applied_by_special_char = False
                continue
            seen_directions.add(instruction)
            row_to_add, col_to_add = directions[instruction]
            updated_position = update_coords(initial_position, (row_to_add, col_to_add))
            initial_position = updated_position
            continue

        if instruction == "*":
            updated_position = apply_movement(instruction, index, initial_position)
            initial_position = updated_position if updated_position else initial_position
            was_applied_by_special_char = True

        if instruction == "!":
           updated_position = apply_movement(instruction, index, initial_position)
           initial_position = updated_position if updated_position else initial_position
           was_applied_by_special_char = True

        if instruction == "?":
            updated_position = apply_movement(instruction, index, initial_position)
            initial_position = updated_position if updated_position else initial_position
            was_applied_by_special_char = True

    return bool(initial_position == (0, 0)) or [
        initial_position[0],
        initial_position[1],
    ]
 
print(is_robot_back("R")) # [1, 0]
print(is_robot_back("RL")) # true
print(is_robot_back("*RU")) # [2, 1]
print(is_robot_back("R*U")) # [1, 2]
print(is_robot_back("LLL!R")) # [-4, 0]
print(is_robot_back("R?R")) # [1, 0]
print(is_robot_back("U?D")) # true
print(is_robot_back("R!L")) # [2,0]
print(is_robot_back("U!D")) # [0,2]
print(is_robot_back("R?L")) # true
print(is_robot_back("U?U")) # [0,1]
print(is_robot_back("*U?U")) # [0,2]
print(is_robot_back("U?D?U")) # true