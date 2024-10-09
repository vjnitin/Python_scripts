initial_str = input("Enter a string: ")
split_str = initial_str.split()
reversed_str = []
for word in split_str:
    if len(word) >= 8:
        reversed_words = word[::-1]
        reversed_str.append(reversed_words)
        if word != word[-1]:
            reversed_str.append(' ')
result_str = ''.join(reversed_str)
print("Reverse of each more than 8 length sequence (excluding space): ", result_str)
cnt = initial_str.count("TTACT")
print("Number of times 'TTACT' has occured in initial string: ", cnt)