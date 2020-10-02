from datamining_lab1.proccessing import *

SET_WORD = "word"
SET_TIMES = "times"
OUTPUT_DIRECTORY = 'datamining_lab1/output'
SPAM_OUTPUT_FILE = 'spam.csv'
HAM_OUTPUT_FILE = 'ham.csv'


def csv_dict_reader(file_obj):
    return csv.DictReader(file_obj, delimiter=',')


def create_dictionary(file):
    dictionary = {}
    with open(OUTPUT_DIRECTORY + '/' + file) as csv_file:
        reader = csv_dict_reader(csv_file)
        for line in reader:
            dictionary[line[SET_WORD]] = int(line[SET_TIMES])
    return dictionary


def present_words(words):
    amount = 0
    for word in words:
        amount += int(words[word])
    return amount


def unknown_words(words, message):
    unknowns = 0
    known_words = words.keys()
    for word in message:
        if word not in known_words:
            unknowns += 1
    return unknowns


def calculate_probability(words, message):
    present_words_amount = present_words(words)
    unknown_words_amount = unknown_words(words, message)
    probability = 1
    for word in message:
        word_count = 0
        if word in words:
            word_count = int(words[word])
        probability *= (word_count + 1) / (present_words_amount + unknown_words_amount)
    return probability


def main():
    message = str(input("Enter message: "))

    statistic_spam_dictionary = create_dictionary(SPAM_OUTPUT_FILE)
    statistic_ham_dictionary = create_dictionary(HAM_OUTPUT_FILE)

    spam_probability = calculate_probability(statistic_spam_dictionary, message)
    ham_probability = calculate_probability(statistic_ham_dictionary, message)

    sum_of_probabilities = spam_probability + ham_probability
    spam_normalized_probability = spam_probability / sum_of_probabilities
    ham_normalized_probability = ham_probability / sum_of_probabilities

    print("Spam with {} probability".format(spam_normalized_probability))
    print("Ham with {} probability".format(ham_normalized_probability))


if __name__ == '__main__':
    main()
