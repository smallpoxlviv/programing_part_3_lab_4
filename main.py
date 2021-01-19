import re


def input_data(file_name):
    try:
        with open(file_name, 'r') as file:
            binary_line, number = file.readline().split()
        return binary_line, int(number)
        
    except (FileNotFoundError):
        sys.exit(f'file "{file_name}" not found')
    except:
        sys.exit(f'check data in "{file_name}"')


def output_data(file_name, output):
    with open(file_name,'w') as file:
        file.write(str(output))
        

def str_bin(number: int):
	return bin(number)[2:]


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


def min_num_of_substrings(binary_line: str, powers_list: list):

	if len(binary_line) == 0:
		return 0
	counter = 0

	for power in powers_list:
		if len(power) > len(binary_line):
			continue
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


def main(binary_line: str, number: int):
	powers_list = create_powers_list(len(binary_line), number)
	powers_list.reverse()
	return min_num_of_substrings(binary_line, powers_list)


if (__name__ == "__main__"):
	binary_line, number = input_data('io/lab_4.in')
	result = main(binary_line, number)
	output_data('io/lab_4.out', result)
	print(result)
