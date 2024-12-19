import os

def read_numbers_from_file(input_file, array1, array2):
    with open(input_file, 'r') as file:
        for line in file:
            numbers = line.split()
            if len(numbers) >= 2:
                array1.append(int(numbers[0]))
                array2.append(int(numbers[1]))
    
    return array1, array2

def sort_array_by_size(array):
    return array.sort()

def calculated_similarity(array1, array2):
    total = 0
    for i in range(len(array1)):
        total += abs(array1[i] - array2[i])
    return total

if __name__ == "__main__":
    array1 = []
    array2 = []
    
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    read_numbers_from_file(input_file, array1, array2)
    print("Array 1:", array1)
    print("Array 2:", array2)
    sort_array_by_size(array1)
    sort_array_by_size(array2)
    print("\nSorted Array 1:", array1)
    print("\nSorted Array 2:", array2)
    print(calculated_similarity(array1, array2))