while True:
    print("Enter a string to run the program or enter 'q' to exit")
    usr_input = input("Enter a string: ")
    split_str = usr_input.split()
    vowels = 'aeiouAEIOU'
    result = []
    if usr_input != 'q': 
        for word in split_str:
            if len(word) == 1:
                result.append(word)
                result.append(' ')
            else:
                for char in word:
                    if char not in vowels:
                        result.append(char)
                if word != word[-1]:
                    result.append(' ')
        result_str = ''.join(result)
        print(result_str)
    else:
        print("The program ended by entering 'q'.")
        break              