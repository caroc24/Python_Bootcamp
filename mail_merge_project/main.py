#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

f = open("./Input/Names/invited_names.txt", mode="r")
namelist = f.readlines()


with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()
    print(letter)

# Replaces "name with new line" with "name"
for name in range(0, len(namelist)):
    clean_name = namelist[name].strip("\n")
    namelist[name] = clean_name
    with open(f"./Output/ReadyToSend/{namelist[name]}", mode="w") as file:
        new_letter = letter.replace("[name]", namelist[name])
        file.write(new_letter)
