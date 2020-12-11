# programing_part_3_lab_4 - "fantz"

Фантазери
Бобри Антін та Орі придумали гру - вигадувати випадкові двійкові числа, і перевіряти, чи ці числа можна розбити на шматки, кожен з яких є степенем числа X у десятковій системі.

Наприклад, якщо X == 5, то двійкове число число 101110011 можна розбити на 101, 11001 та 1, кожне з яких є 5 у якомусь степені (101 у десятковій == 5 == 5^1, 11001 == 25 == 5^2 та 1 == 1 - це 5^0).

Продемонструйте, що люди розумніші за бобрів, і для заданого двійкового числа N знайдіть найменшу кількість шматків, на які його треба розбивати.

Вхідні дані:\
	Перший рядок містить X - послідовність нуликів та одиничок та N.

Вихідні дані:\
	Найменша кількість шматків, на які можемо розбити вхідне число, або -1 якщо це не можливо.

Обмеження:\
	0 < len(X) < 100\
    0 < N < 100

Приклади:\
In:\
101101101 5\
Out:\
	3
	(Можна розбити на 101, 101, 101)

In:\
1111101 5\
Out:\
	1
	(1111101 - це 5^3)

In:\
110011011 5\
Out:\
	3
	(11001, 101, 1)

In:
10011101111010010011111011001110010100011110010111001000\1100111011110100100111110110011100101000110010110000111100101110010001 7\
Out:
	5

### main.py

Ініціалізуємо змінні:
```python
binary_line, number = input_data('io/lab_4.in')
```
```python
def main(binary_line: str, number: int):
	powers_list = create_powers_list(len(binary_line), number)
```
Обраховуємо список можливих підстрічок:
```python
def create_powers_list(length: int, number: int):
	counted_powers = ['1']
	if (number == 1):
		return counted_powers
	power = 1
	while True:
		current_bin = str_bin(number**power)
		if (len(current_bin) > length):
			break
		counted_powers.append(current_bin)
		power += 1
	return counted_powers
```
Обертаємо список, щоб в подальшому пошук збігів починався з найдовшої підстрічки:
```python
def main(binary_line: str, number: int):
	powers_list = create_powers_list(len(binary_line), number)
	powers_list.reverse()
	return min_num_of_substrings(binary_line, powers_list)
```
Знаходимо збіг та рекурсивно запускаємо функцію для пошуку збігів у новій стрічці, яка починається end_index (індекс, перед яким закінчився попередній збіг):
```python
def min_num_of_substrings(binary_line: str, powers_list: list):
```
```python
    counter = 0
	for power in powers_list:
```
```python
		matched = re.match(power, binary_line)
		if (matched):
			end_index = matched.end()
			stack_counter = min_num_of_substrings(binary_line[end_index:], powers_list)
			if stack_counter != -1:
				if counter == 0:
					counter = stack_counter	+ 1
				else:
					counter = min(counter - 1, stack_counter) + 1

	if counter == 0:
		return -1	
	return counter
```
В найнижчому рівні виклику функції min_num_of_substrings при успішному завершенні  повертаємо 0:
```python
def min_num_of_substrings(binary_line: str, powers_list: list):
	if len(binary_line) == 0:
		return 0
```
Якщо збігів не має, counter залишиться рівним нулю, отже повертаємо -1. В свою чергу функція, на рівень вища, викличе себе, але вже для наступної підстрічки.
```python
def min_num_of_substrings(binary_line: str, powers_list: list):
```
```python
	counter = 0
	for power in powers_list:
        ... ... ...
	
	if counter == 0:
		return -1
```
Якщо можливих варіантів комбінації підстрічок є декілька, перевіряємо який з них оптимальніший та запам'ятовуємо його:
```python
def min_num_of_substrings(binary_line: str, powers_list: list):
```
```python
			stack_counter = min_num_of_substrings(binary_line[end_index:], powers_list)
			if stack_counter != -1:
				if counter == 0:
					counter = stack_counter	+ 1
				else:
					counter = min(counter - 1, stack_counter) + 1
```
Повертаємо та виводимо результат:
```python
def main(binary_line: str, number: int):
	powers_list = create_powers_list(len(binary_line), number)
	powers_list.reverse()
	return min_num_of_substrings(binary_line, powers_list)
```
```python
result = main(binary_line, number)
output_data('io/lab_4.out', result)
print(result)
```
