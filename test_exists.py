import unittest


class MyTestCase(unittest.TestCase):
	def test_something(self):
		self.assertEqual(True, False)  # add assertion here


class AndrewTestCase_001(unittest.TestCase):
	def test_database_not_exist(self):
		self.assertEquals(True, False)

if __name__ == '__main__':
	unittest.main()
