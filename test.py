import unittest
from main import *


class Test(unittest.TestCase):

	def test_input_data(self):
		binary_line, number = input_data('io/test.in')
		self.assertEqual('0110101010101000011010', binary_line)
		self.assertEqual(5, number)

	def test_output_data(self):
		result = 15
		file_path = 'io/test.out'
		output_data(file_path, result)
		with open(file_path, 'r') as file:
			assert_result = int(file.readline())
		self.assertEqual(assert_result, result)

	def test_str_bin(self):
		two = str_bin(2)
		five = str_bin(5)
		ten = str_bin(10)
		hundred_fifty_six = str_bin(156)
		self.assertEqual('10', two)
		self.assertEqual('101', five)
		self.assertEqual('1010', ten)
		self.assertEqual('10011100', hundred_fifty_six)

	def test_create_powers_list(self):
		powers_list = create_powers_list(30, 6)
		self.assertEqual([
							'1', 
							'110', 
							'100100', 
							'11011000', 
							'10100010000', 
							'1111001100000', 
							'1011011001000000', 
							'1000100010110000000', 
							'110011010000100000000', 
							'100110011100011000000000', 
							'11100110101010010000000000', 
							'10101100111111101100000000000'
						], powers_list)

	def test_create_powers_list_one(self):
		powers_list = create_powers_list(30, 1)
		self.assertEqual(['1'], powers_list)

	def test_main(self):
		binary_line = '100111011110100100111110110011100101000111100101110010001100111011110100100111110110011100101000110010110000111100101110010001'
		number = 7
		result = main(binary_line, number)
		self.assertEqual(5, result)

	def test_main_one(self):
		binary_line = '101101101'
		number = 5
		result = main(binary_line, number)
		self.assertEqual(3, result)

	def test_main_two(self):
		binary_line = '1111101'
		number = 5
		result = main(binary_line, number)
		self.assertEqual(1, result)

	def test_main_three(self):
		binary_line = '110011011'
		number = 5
		result = main(binary_line, number)
		self.assertEqual(3, result)

	def test_main_false(self):
		binary_line = '1100110110'
		number = 5
		result = main(binary_line, number)
		self.assertEqual(-1, result)


if __name__ == "__main__":
	unittest.main()