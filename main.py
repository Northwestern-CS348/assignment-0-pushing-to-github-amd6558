import unittest
import student_code

class SetupTest(unittest.TestCase):

	def test01(self):
		result = student_code.shouldReturnTrue()
		self.assertTrue(result)

	def test02(self):
		result = student_code.shouldReturnTrue()
		self.assertEqual(result, True)

if __name__ == '__main__':
	unittest.main()