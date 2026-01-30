# 🪄 Execute the magical language
# We have already distributed all the gifts! Back at the workshop, preparations for next year are already beginning.
#
# A genius elf is creating a magical programming language 🪄 that will help streamline the delivery of gifts to children in 2025.
#
# Programs always start with the value 0, and the language is a string where each character represents an instruction:
#
# >: Moves to the next instruction.
# +: Increments the current value by 1.
# -: Decrements the current value by 1.
# [and]: Loop. If the current value is 0, jump to the instruction after ]. If it is not 0, go back to the instruction after [.
# {and}: Conditional. If the current value is 0, jump to the instruction after }. If it is not 0, continue to the instruction after {.
# You need to return the value of the program after executing all the instructions.
#
# execute("+++"); // 3
# execute("+--"); // -1
# execute(">+++[-]"); // 0
# execute(">>>+{++}"); // 3
# execute("+{[-]+}+"); // 2
# execute("{+}{+}{+}"); // 0
# execute("------[+]++"); // 2
# execute("-[++{-}]+{++++}"); // 5
# Note: A conditional can have a loop inside, and a loop can also have a conditional inside. But two loops or two conditionals are never nested.


def execute(program: str) -> int:
    res: int = 0

    if not program:
        return 0

    def is_current_value_0(res: int) -> bool:
        return res == 0

    def is_skip_instruction(instruction: str):
        return ">" in instruction

    def is_start_of_loop_or_conditional(instruction: str) -> bool:
        return "[" in instruction or "{" in instruction

    def is_arithmetic_instruction(instruction: str):
        return "+" in instruction or "-" in instruction

    def find_start_and_end_of_loop_or_conditional(
        instructions: str, initial_index=None
    ) -> tuple[int, int]:
        # We need to do it with a stack for managing the nested loops or conditionals...
        stack = []

        for i, char in enumerate(instructions):
            if char == "[":
                stack.append(i)
            elif char == "]":
                stack.pop()
                if len(stack) == 0:
                    return initial_index, initial_index + i, "loop"
            elif char == "{":
                stack.append(i)

            elif char == "}":
                stack.pop()
                if len(stack) == 0:
                    return initial_index, initial_index + i, "conditional"

        return None, None, None

    arithmetic_instructions = {
        "+": lambda res: res + 1,
        "-": lambda res: res - 1,
    }

    left = 0
    right = len(program)

    def proccess_instructions(res: int, left: int, right: int):
        if left >= right:
            return res

        instruction = program[left]

        if is_arithmetic_instruction(instruction):
            new_res = arithmetic_instructions[instruction](res)
            res = new_res
            left += 1
            return proccess_instructions(res, left, right)

        if is_skip_instruction(instruction):
            left += 1
            return proccess_instructions(res, left, right)

        if is_start_of_loop_or_conditional(instruction):
            start, end, type = find_start_and_end_of_loop_or_conditional(
                program[left:], left
            )
            if type == "loop":
                if is_current_value_0(res):
                    left = end + 1
                    return proccess_instructions(res, left, right)
                while not is_current_value_0(res):
                    res = proccess_instructions(res, start + 1, end)
                left = end + 1
                return proccess_instructions(res, left, right)
            elif type == "conditional":
                if is_current_value_0(res):
                    left = end + 1
                    return proccess_instructions(res, left, right)
                else:
                    res = proccess_instructions(res, start + 1, end)
                    left = end + 1
                    return proccess_instructions(res, left, right)
        left += 1
        return proccess_instructions(res, left, right)

    return proccess_instructions(res, left, right)


print(execute("+++"))
print(execute("+--"))
print(execute(">+++[-]"))