def remove_every_third(numbers):
    counter = 0
    index = 0

    while numbers:
        counter += 1
        index %= len(numbers)

        if counter % 3 == 0:
            removed_number = numbers.pop(index)
            print(f"Removed: {removed_number}")
        else:
            index += 1


# Example usage:
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
remove_every_third(numbers_list)








