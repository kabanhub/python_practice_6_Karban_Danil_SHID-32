from app.calculator import Calculator

def main():
    calc = Calculator(5, 2)

    # Арифметичних методів
    result_addition = calc.addition()
    result_subtraction = calc.subtraction()
    result_multiplication = calc.multiplication()
    result_division = calc.division()
    result_exponentiation = calc.exponentiation()

    print("Addition:", result_addition) # Додавання
    print("Subtraction:", result_subtraction) # Віднімання
    print("Multiplication:", result_multiplication) # Множення
    print("Division:", result_division) # Ділення
    print("Exponentiation:", result_exponentiation) # Піднесення до степеня

    # Статичний метод
    random_num = Calculator.random_number(1, 10)
    print("Random Number:", random_num)

if __name__ == "__main__":
    main()


