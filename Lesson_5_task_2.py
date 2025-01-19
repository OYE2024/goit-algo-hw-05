def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iteration = 0
    upper_bound = arr[-1]

    while low <= high:
        iteration = iteration + 1
        mid = (high + low) // 2

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            upper_bound = arr[mid]
            high = mid - 1

        # інакше x присутній на позиції і повертаємо його
        else:
            return arr[mid]

    # якщо елемент не знайдений
    return (iteration, upper_bound)


arr = [2.3, 3.1, 4.7, 10.2, 40.6]
print(type(binary_search(arr, 3.5)))
print(binary_search(arr, 3.5))
print(binary_search(arr, 10))
