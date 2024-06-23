from sympy import sympify, symbols
def process_form_data(rownania, solutions):
    equations = rownania.split('\n')
    left_sides = [eq.split('=')[0].strip() for eq in equations]
    right_sides = [sympify(eq.split('=')[1].strip()) for eq in equations]
    x, y, z = symbols('x y z')

    results = []

    for sol in solutions:
        numbers_parts = sol.split(',')
        x_value = sympify(numbers_parts[0].strip())
        y_value = sympify(numbers_parts[1].strip())
        z_value = sympify(numbers_parts[2].strip())

        all_correct = True

        for left_side, right_side in zip(left_sides, right_sides):
            left_expr = sympify(left_side.strip())
            left_evaluated = left_expr.subs({x: x_value, y: y_value, z: z_value})

            if left_evaluated != right_side:
                all_correct = False
                break

        if all_correct:
            results.append((x_value, y_value, z_value, all_correct))

    return results
