def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_nums = []
    operators = []
    second_nums = []
    answers = []
    max_lengths = []

    for problem in problems:
        parts = problem.split()
        first_num, operator, second_num = parts[0], parts[1], parts[2]

        # Check for valid operators
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check if operands are digits and within size limit
        if not first_num.isdigit() or not second_num.isdigit():
            return "Error: Numbers must only contain digits."
        if len(first_num) > 4 or len(second_num) > 4:
            return "Error: Numbers cannot be more than four digits."

        first_nums.append(first_num)
        operators.append(operator)
        second_nums.append(second_num)

        if operator == '+':
            answer = str(int(first_num) + int(second_num))
        else:
            answer = str(int(first_num) - int(second_num))

        answers.append(answer)
        max_lengths.append(max(len(first_num), len(second_num)) + 2)  # 2 extra spaces for operator and space

    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""

    for i in range(len(problems)):
        if i > 0:
            first_line += "    "
            second_line += "    "
            third_line += "    "
            fourth_line += "    "

        first_line += first_nums[i].rjust(max_lengths[i])
        second_line += operators[i] + " " + second_nums[i].rjust(max_lengths[i] - 2)
        third_line += "-" * max_lengths[i]
        fourth_line += answers[i].rjust(max_lengths[i])

    problems = first_line + "\n" + second_line + "\n" + third_line
    if show_answers:
        problems += "\n" + fourth_line

    return problems


print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
