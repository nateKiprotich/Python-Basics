file = open('text.txt', 'r')


# Read the file line by line
def read_text_file_by_line(f):
    for line in f:
        print(line)


def read_file_by_character(f, num_chars):
    # num_chars is the number of characters to be read
    while True:
        f_chars = f.read(num_chars)

        if not f_chars:
            break

        print(f_chars)


def count_lines(f):
    counter = 0
    for line in f:
        counter += 1

    print('The file has %s lines', counter)


def word_counter(f):
    counter = 0

    for line in f:
        word = line.split()
        counter += len(word)

    print('There are %s word in the file', counter)


# read_text_file_by_line(file)

# read_file_by_character(file, 10)

# count_lines(file)

word_counter(file)

file.close()
