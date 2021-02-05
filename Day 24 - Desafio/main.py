
PLACEHOLDER = "[name]"

#lendo a linha 3 do arquivo do diretorio day 24
with open("./Day 24 - Desafio/Input/Names/invited_names.txt", "r") as a:
    names = a.readlines()
    print(names)

with open("./Day 24 - Desafio/Input/Letters/starting_letter.txt") as letter_file:
    letter_contentes = letter_file.read()
    for name in names:
        striped_name = letter_contentes.strip()
        new_letter = letter_contentes.replace(PLACEHOLDER, striped_name)
        with open(f"./Day 24 - Desafio/Output/ReadToSend/Letter_for{striped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

