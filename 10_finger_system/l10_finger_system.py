import string
import random


def generate_random_strings(characters: str, length: int, num_strings: int) -> list:
    strings_array = []
    for _ in range(num_strings):
        string_chars = ''.join(random.choice(characters) for _ in range(length))
        strings_array.append(string_chars)
    return strings_array


if __name__ == "__main__":
    array_size = 100
    file_1 = "./10_finger_system/text_to_typ/file_1.txt"
    file_2 = "./10_finger_system/text_to_typ/file_2.txt"
    file_3 = "./10_finger_system/text_to_typ/file_3.txt"
    file_4 = "./10_finger_system/text_to_typ/file_4.txt"
    file_5 = "./10_finger_system/text_to_typ/file_5.txt"
    level_1_chars = "asdfjklöä"
    level_2_chars = level_1_chars + "qwertzuiopü"
    level_3_chars = level_2_chars + "yxcvbnm"
    level_4_chars = level_3_chars + "ß" + string.digits
    level_5_chars = level_1_chars + level_2_chars + level_3_chars + string.ascii_uppercase + "ÖÄÜß"
    print(f"Level 1: {level_1_chars}")
    print(f"Level 2: {level_2_chars}")
    print(f"Level 3: {level_3_chars}")
    print(f"Level 4: {level_4_chars}")
    print(f"Level 5: {level_5_chars}")

    text_1_arr = generate_random_strings(characters=level_1_chars, length=4, num_strings=array_size)
    text_1 = " ".join(text_1_arr)
    text_2_arr = generate_random_strings(characters=level_2_chars, length=4, num_strings=array_size)
    text_2 = " ".join(text_2_arr)
    text_3_arr = generate_random_strings(characters=level_3_chars, length=4, num_strings=array_size)
    text_3 = " ".join(text_3_arr)
    text_4_arr = generate_random_strings(characters=level_4_chars, length=4, num_strings=array_size)
    text_4 = " ".join(text_4_arr)
    text_5_arr = generate_random_strings(characters=level_5_chars, length=4, num_strings=array_size)
    text_5 = " ".join(text_5_arr)

    with open(file=file_1, mode="w", encoding="UTF-8") as file_obj:
        file_obj.write(text_1)

    with open(file=file_2, mode="w", encoding="UTF-8") as file_obj:
        file_obj.write(text_2)

    with open(file=file_3, mode="w", encoding="UTF-8") as file_obj:
        file_obj.write(text_3)

    with open(file=file_4, mode="w", encoding="UTF-8") as file_obj:
        file_obj.write(text_4)

    with open(file=file_5, mode="w", encoding="UTF-8") as file_obj:
        file_obj.write(text_5)
