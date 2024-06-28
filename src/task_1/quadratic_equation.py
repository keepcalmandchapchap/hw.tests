def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    D = b**2 - 4 * a * c
    return D

def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    result = 'корней нет'
    if discriminant(a, b, c) < 0:
        return(result)
    elif discriminant(a, b, c) == 0:
        result = -b / (2 * a)
        return(f'{result:.1f}')
    elif discriminant(a, b, c) > 0:
        result = []
        x1 = (-b + discriminant(a, b, c)**0.5) / (2*a)
        result.append(x1)
        x2 = (-b - discriminant(a, b, c)**0.5) / (2*a)
        result.append(x2)
        return(f'{result[0]:.1f} {result[1]:.1f}')

