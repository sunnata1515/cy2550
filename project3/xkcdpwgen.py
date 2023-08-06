import argparse
import random


def load_wordlist(filename):
    with open(filename, 'words.txt') as file:
        return [line.strip() for line in file]


def generate_password(wordlist, num_words, num_caps, num_numbers, num_symbols):
    words = random.sample(wordlist, num_words)

    for i in range(num_caps):
        random_word = random.choice(words)
        words[words.index(random_word)] = random_word.capitalize()

    password = ''.join(words)

    if num_numbers > 0:
        password += ''.join(random.choice('0123456789') for _ in range(num_numbers))

    if num_symbols > 0:
        password += ''.join(random.choice('~!@#$%^&*.:;') for _ in range(num_symbols))

    return password


def main():
    parser = argparse.ArgumentParser(
        description="Generate a secure, memorable password using the XKCD method")
    parser.add_argument('-w', '--words', type=int, default=4,
                        help="include WORDS words in the password (default=4)")
    parser.add_argument('-c', '--caps', type=int, default=0,
                        help="capitalize the first letter of CAPS random words (default=0)")
    parser.add_argument('-n', '--numbers', type=int, default=0,
                        help="insert NUMBERS random numbers in the password (default=0)")
    parser.add_argument('-s', '--symbols', type=int, default=0,
                        help="insert SYMBOLS random symbols in the password (default=0)")

    args = parser.parse_args()

    wordlist = load_wordlist(
        'words.txt')  # Make sure to have your wordlist file in the same directory

    password = generate_password(wordlist, args.words, args.caps, args.numbers, args.symbols)
    print(password)


