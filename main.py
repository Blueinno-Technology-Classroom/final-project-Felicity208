import requests
from random import *



def check_def(word):
    if word != "checkdef":
        dict_response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}").json()
        if "No Definitions Found" and "title" in dict_response:
            print(f"Computer: That's not a valid word! Enter a new word beginning with {computer[-1]}")
            return False
        else:
            return dict_response
    else:
        dict_def = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{computer}").json()
        return dict_def[0]

def generate_computer_word(c):
    computer = requests.get(
        f"https://random-word-api.vercel.app/api?letter={c}").json()[0]

    while not (check_def(computer)) or computer in used_words:
        computer = requests.get(
            f"https://random-word-api.vercel.app/api?letter={c}").json()[0]

    used_words.append(computer)

    return computer

used_words = []

max_interval = randint(30, 60)


computer = generate_computer_word(choice("abcdefghijklmnopqrstuvwy"))


print("Computer: To end the game, type any string that ends with 'x' or 'z'! I will start first")
print()

print(
    f"Computer: The first word is {computer}, now type a word starting with {computer[-1]}, or type 'checkdef' for the definition of the word")


while 1:
    player = input("Enter your word: ")

    if player == "checkdef":
        for words in check_def(computer):
            for meanings in words['meanings']:
                print(f"Parts of Speech:{meanings['partOfSpeech']}")
                for defs in meanings["definitions"]:
                    print(f'\tDefinition:{defs['definition']}')
                print("-"*20)

        print(f"Computer: Now type a word beginning with {computer[-1]}")
    elif player[-1] == "x" or player[-1] == "z":
        print(f"Computer: You typed a word ending with {player[-1]}, Game end!")
        break
    elif player in used_words:
        print(f"Computer: '{player}' was used already! Try a new word")
    else:
        player = player.lower()
        if player == "":
            print("Computer: Enter a valid word")

        if player[0] != computer[-1]:
            print(f"Computer: It doesn't start with {computer[-1]}! Try again!") 
        else:
            check_result = check_def(player)
            if check_result:
                used_words.append(player)


                if len(used_words) >= max_interval:
                    print("Computer: You win!")
                    print("We used:")
                    for word in range (len(used_words)):
                        print(f'- {used_words[word]}')
                    break

                
                computer = generate_computer_word(player[-1])
                
                print(
                    f"Computer: {computer}, now type a word beginning with {computer[-1]}, or type 'checkdef' for the definition of the word")



