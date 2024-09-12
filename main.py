def main():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()
    total_words = count_words(file_contents)
    letter_count = count_letters(file_contents)
    sorted_letters = sort_letters(letter_count)

    generate_report(file_path, total_words, sorted_letters)

def count_words(string):
    words = string.split()
    total_words = len(words)
    return total_words

def count_letters(string):
    letter_count={}
    words = string.lower().split()
    for word in words:
        letters = [i for i in word]
        for letter in letters:
            if letter.isalpha():
                if letter in letter_count:
                    letter_count[letter] += 1
                else:
                    letter_count[letter] = 1

    return letter_count

def sort_on(d):
    return d["count"]

def sort_letters(letter_count):
    sorted_letters = []
    for letter in letter_count:
        sorted_letters.append({"letter": letter, "count":letter_count[letter]})
    sorted_letters.sort(reverse=True, key=sort_on)
    
    return sorted_letters

def generate_report(book_path, total_words, sorted_letters):
    print(f"--- Begin report of {book_path} ---")
    print(f"{total_words} words found in the document")
    print()

    for letter in sorted_letters:
        print(f"The '{letter['letter']}' character was found {letter['count']} times")

    print("--- End report ---")

main()