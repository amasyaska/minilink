from random import randint

RELAY_RANDOM_MAX = 64**8

def get_tetrasexagesimal_representation() -> str:
    tetrasexagesimal_representation = ""
    # 0-9   (10 characters)
    for i in range(48, 48 + 10):
        tetrasexagesimal_representation = tetrasexagesimal_representation + chr(i)
    # a-z   (26 characters)
    for i in range(97, 97 + 26):
        tetrasexagesimal_representation = tetrasexagesimal_representation + chr(i)
    # A-Z   (26 characters)
    for i in range(65, 65 + 26):
        tetrasexagesimal_representation = tetrasexagesimal_representation + chr(i)
    # -, _  (2 characters)
    tetrasexagesimal_representation = tetrasexagesimal_representation + "-_"

    return tetrasexagesimal_representation


def convert_decimal_to_tetrasexagesimal(tetrasexagesimal_representation: str, number: int=randint(1, RELAY_RANDOM_MAX)) -> str:
    """
    returns decimal number in tetrasexagesimal base according to tetrasexagesimal_representation
    """
    tetrasexagesimal_number = ""
    while (number > 0):
        tetrasexagesimal_number = tetrasexagesimal_representation[number % 64] + tetrasexagesimal_number
        number = number // 64
    return tetrasexagesimal_number