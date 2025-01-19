from Lesson_5_algoritms import boyer_moore_search
from Lesson_5_algoritms import kmp_search
from Lesson_5_algoritms import rabin_karp_search
import chardet
import timeit

with open('Article_1.txt', 'rb') as file:
    raw_data = file.read()
    result = chardet.detect(raw_data)
    encoding = result['encoding']
    # print(encoding)

with open('Article_1.txt', 'r', encoding=encoding) as file:
    content = file.read()
    # print(content)

pattern = "Експоненціальний пошук" # існуючий підрядок тексту
# pattern = "Графи — це математичні об'єкти, що використовуються" # неіснуючий підрядок тексту

# Перевірка роботи алгоритму пошуку.
position = boyer_moore_search(content, pattern)
if position != -1:
        print(f"Substring found at index {position}")
        print(content[position:])
else:
        print("Substring not found")

# Вимірюємо витрати часу на пошук підрядка при використанні різних алгоритмів пошуку
boyer_search_execution_time = timeit.timeit(
    lambda: boyer_moore_search(content, pattern), number=100)
boyer_search_test_result = f"Execution time for boyer_search is {
    boyer_search_execution_time:.5f} sec."
print(boyer_search_test_result) # Execution time for boyer_search is 0.03221 sec.

kmp_search_execution_time = timeit.timeit(
    lambda: kmp_search(content, pattern), number=100)
kmp_search_test_result = f"Execution time for kmp_search is {
    kmp_search_execution_time:.5f} sec."
print(kmp_search_test_result) # Execution time for kmp_search is 0.12712 sec.

rabin_karp_search_execution_time = timeit.timeit(
    lambda: rabin_karp_search(content, pattern), number=100)
rabin_karp_search_test_result = f"Execution time for rabin_karp_search is {
    rabin_karp_search_execution_time:.5f} sec."
print(rabin_karp_search_test_result) # Execution time for rabin_karp_search is 0.27937 sec.



