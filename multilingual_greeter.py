from typing import Dict

# Populate this dictionary with at least two languages.
# Use integers for keys and strings for values.
# Example: Key = 1. Value = 'English'.
lang_dict = {
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'What is your name?'.
name_prompt_dict = {
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'Hello'.
greetings_dict = {
}


def print_language_options(lang_options: Dict[int, str]) -> None:
    """
    Given a dictionary, this functions iterates through the values and prints them out.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language
    :return: None
    """
    # Loop through each key value pair
    for key, value in lang_options.items():
        # Print language id (key) and name of language value
        print(key, 'corresponds to', value)



def language_input() -> int:
    """
    This function prompts the user for a language choice.

    :return: An integer representing the language choice made by the user
    """
    # Display available language options
    print_language_options(lang_dict)
    # Prompt user until valid choice is made
    while True:
        try:
            # Have user input their preferred language of choice
            lang_choice = int(input("Enter your preferred language: "))

            # Check if input language choice is valid
            if language_choice_is_valid(lang_dict, lang_choice):
                # Return valid language choice and exit loop
                return  lang_choice
            else:
                # Print an error message if choice is incorrect
                print("Invalid. Please select a valid language")
        except ValueError:
            # Print error message for invalid input by user
            print("Invalid input. Please enter a number")



def language_choice_is_valid(lang_options: Dict[int, str], lang_choice: int) -> bool:
    """
    This method determines if the choice the user made is valid.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language

    :param lang_choice: An integer representing the value the user selected
    :return: A boolean representing the validity of the lang_choice
    """
    # Check if the users language choice (lang_choice) is valid in lang_options dictionary
    # The expression "lang_choice in lang_options" returns true if lang_choice is a valid key, False if not
    return lang_choice in lang_options


def get_name_input(name_prompt_options: Dict[int, str], lang_choice: int) -> str:
    """
    This method takes in a dictionary and a key. It returns the value in the dictionary that has a key corresponding to
    the lang_choice parameter.

    :param name_prompt_options: A dictionary where the key is an integer representing an id and the value is a prompt
    in the users chosen language
    :param lang_choice: The language the user has chosen
    :return:
    """
    # Use get() method to retrieve users input for chosen language
    # If lang_choice is a valid key, return the corresponding prompt and the default prompt
    return name_prompt_options.get(lang_choice, "Name prompt not available for chosen language")



def name_input(name_prompt: str) -> str:
    """
    This function takes in a string and uses it to prompt the user for their name.

    :param name_prompt: A string in the user's chosen language that asks them for their name
    :return: The user's response when asked for their name
    """
    # Prompt user for input using the name prompt in their chosen language
    # input function displays name prompt to the user and waits for response
    # Users input is returned by the function
    return input(name_prompt)


def greet(name: str, greetings_options: Dict[int, str], lang_choice: int) -> None:
    """
    Using the parameters provided, this function greets the user.

    :param name: The name the user provided
    :param greetings_options: A dictionary where the key is an integer representing a greeting and the value is a string
    with a greeting in the user's chosen language
    :param lang_choice: The language the user has chosen.
    :return:
    """
    greeting = greetings_options.get(lang_choice, "No greeting for chosen language")

    # Print greeting along with users name
    print(f"{greeting}, {name}!")



if __name__ == '__main__':
    print_language_options(lang_dict)
    chosen_lang = language_input()
    while language_choice_is_valid(lang_dict, chosen_lang) is False:
        print("Invalid selection. Try again.")
        chosen_lang = language_input()

    selected_prompt = f"{get_name_input(name_prompt_dict, chosen_lang)} \n"
    chosen_name = name_input(selected_prompt)
    greet(chosen_name, greetings_dict, chosen_lang)
