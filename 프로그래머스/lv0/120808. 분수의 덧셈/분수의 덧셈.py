import fractions

def solution(denum1, num1, denum2, num2):
    answer = []
    solution = 0
    bunsu1 = fractions.Fraction(denum1, num1)
    bunsu2 = fractions.Fraction(denum2, num2)
    solution = bunsu1 + bunsu2
    answer.append(solution.numerator)
    answer.append(solution.denominator)

    return answer
