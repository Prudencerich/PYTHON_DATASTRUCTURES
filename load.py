

def load_numbers(file_name):
    numbers = []
    with open("unsorted.txt") as f:
        for line in f:
            numbers.append(int(line))
    return numbers