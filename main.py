def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    letter_counts = count_letters(file_contents)

    print_report(word_count, letter_counts, path_to_file)


def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def count_letters(text: str) -> dict[str, int]:
    letters: dict[str, int] = {}
    for char in text:
        lower_char = char.lower()
        if lower_char.isalpha():
            letters[lower_char] = letters.get(lower_char, 0) + 1
    return letters

def print_report(word_count: int, letter_counts: dict[str, int], path_to_file: str):
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document")
    print("")
    for letter, count in sorted(letter_counts.items(), key=lambda item: item[1], reverse=True):
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")

if __name__ == "__main__":
    main()