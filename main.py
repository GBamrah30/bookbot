def main():
    book_path = "/home/gagan/workspace/github.com/gbamrah30/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    letters_in_book = number_of_letters(text)
    sort_list = sorted(letters_in_book.items())
    print("--- Begin report of book/Frankenstein ---")
    print(f"'{num_words}' words found in the document.")
    for letter, count in sort_list:
        print(f"The {letter} character was found {count} times.")
    print("---End Report---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    
    return len(words)

def number_of_letters(text):

    letters = {}
    
    for char in text.lower():
        if char.isalpha():
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
                
    return letters

main()