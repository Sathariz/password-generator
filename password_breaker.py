import random

def pass_guess():
    possible_chracters = "abcdefghijklmnopqrstuwvxyzABCDEFGHIJKLMNOPQRSTUWVXYZ"
    # way to generate, think abt it later
    paswd = "aDcol"
    guessed_pas = ""

    for letter in paswd:
        for char in possible_chracters:
            if letter == char:
                guessed_pas += letter

    print(paswd, guessed_pas)
    # return paswd
# pass_guess()



def true_pas(n):
    possible_chracters = "abcdefghijklmnopqrstuwvxyzABCDEFGHIJKLMNOPQRSTUWVXYZ"
    length = random.randint(1, n)
    pas = ""

    for _ in range(length):
        pas += random.choice(possible_chracters)

    print(pas)
    return pas

paswd = true_pas(10)



# def generate(real_pass):
#     real_pass = "hivfoVrBG"
#     possible_chracters = "abcdefghijklmnopqrstuwvxyzABCDEFGHIJKLMNOPQRSTUWVXYZ"
#     guessed_pass = ""
#     i = 0

    # while guessed_pas != real_pass:
    #     for char in possible_chracters:
    #         if char == real_pass[i]:
    #             guessed_pas += char

    #     i += 1

    # while guessed_pass != real_pass:
    #     for char in possible_chracters:
    #         guessed_pass = char
    #     guessed_pass += char
    #     print(guessed_pass)

    # print(real_pass, guessed_pass)

# generate(paswd)
