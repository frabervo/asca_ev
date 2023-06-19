"""Python code to evaluate typing competition candidates
    For calcutating purpose: https://www.speedtypingonline.com/typing-equations 
    and 
    https://support.sunburst.com/hc/en-us/articles/229335208-Type-to-Learn-How-are-Words-Per-Minute-and-Accuracy-Calculated-
"""

# How many Functions do i need
# 1. charge the original text
# 2. Counts the words of the orginal text
# 3. Information about the canditate
# 4. store the score of the canditate
# 5. calculate the words per minutes
# 6. calcuteate the accuracy
from termcolor import colored
import string
import os
import sys
import Levenshtein

ori_file_path = "./original_text.txt"
ergebnis_path = "./ergebnis.txt"
path_teilnehmer = "./Teilnehmer"

minutes = 3  # 3 minutes
# participant = {"ID":"", "characters":0, "words":0, "errors":[]} # store participants Information


def count_words_characters(file_path) -> list:
    """count the number of characters and words in the given file

    Args:
        full_text (str): The Full content of the given File

    Returns:
        list: 0 -> number characters, 1 -> number words, 2 -> word array
    """
    try:
        with open(file_path, "r") as file:
            full_content = file.read()
    except FileExistsError as error_1:
        print(colored(f"First Line= {error_1}", "red"))
        sys.exit(error_1.errno)
    except FileNotFoundError as error_2:
        print(colored(f"First Line= {error_2}", "red"))
        sys.exit(error_2.errno)

    caracter_nbr = len(full_content)
    word_array = full_content.split()
    word_nbr = len(word_array)
    # print(f"The original Text contains: {characters_nbr} characters and {len(word_array)} words")
    return [caracter_nbr, word_nbr, word_array, full_content]


def participats_list():
    return os.listdir(path=f"{path_teilnehmer}")


def canditat_info(canditat: dict):
    id = canditat["ID"]
    file_path = path_teilnehmer + f"/{id}.txt"
    infos = count_words_characters(file_path=file_path)
    canditat["characters"] = infos[0]
    canditat["words"] = infos[1]
    canditat["word_array"] = infos[2]
    canditat["full"] = infos[3]


def evaluation(canditat_par: dict, ori: list):
    total_char = canditat_par["characters"]
    errors = Levenshtein.distance(canditat_par["full"], ori[3][:total_char])
    canditat_par["errors"] = errors
    canditat_par["gross_wpm"] = (total_char / 5)/minutes
    canditat_par["net_wpm"] = ((total_char / 5) - errors) / minutes
    canditat_par["accuracy"] = ((total_char - errors) / total_char) * 100


def canditats_evaluation(canditats_list:list, ori_infos_par):
    for canditat in canditats_list:
        evaluation(canditat_par=canditat, ori=ori_infos_par)
        id = canditat["ID"]
        nbr_char = canditat["characters"]
        nbr_word = canditat["words"]
        ew = canditat["errors"]
        gw = canditat["gross_wpm"]
        nw = canditat["net_wpm"]
        acc = canditat["accuracy"]
        print(f"| ID: {id} | number of chars: {nbr_char} | number of words: {nbr_word} | number of errors: {ew} | gross wpm: {gw:.1f} | net wpm: {nw:.1f} | accuracy: {acc:.2f}")


def canditats_ranking(participants:dict) -> list:
    """The ranking i based on the "net wpm" values, with higher values indicating a better typing speed taking into account the number of errors made.

    Args:
        participants (dict): list of participants

    Returns:
        list: a ordered List of participants ID
    """
    last_canditat = 0
    list_nw = []
    for canditat in participants: 
        list_nw.append(canditat["net_wpm"])
    list_nw.sort
    



if __name__ == "__main__":
    print("")
    # Get Original Text Information List: 0 -> number characters, 1 -> number words, 2 -> word array
    ori_infos = count_words_characters(ori_file_path)
    # Get list of participants
    list_parts_file = participats_list()
    list_parts = []
    # Extract canditate information
    for canditat in list_parts_file:
        participant = {"ID": "", "characters": 0, "words": 0, "errors": 0,
                       "error_array": [], "word_array": [], "gross_wpm": 0, "net_wpm": 0, "accuracy": 0, "full": ""}  # store participants Information
        participant["ID"] = canditat[:(canditat.find(".txt"))]
        canditat_info(canditat=participant)
        list_parts.append(participant)
    # Evaluate each Canditat
    canditats_evaluation(canditats_list=list_parts, ori_infos_par=ori_infos)
    # Ranking
