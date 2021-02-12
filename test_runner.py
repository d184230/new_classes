import unittest
from tests.test_user import TestUserClass

testCases = [TestUserClass, ]

testLoad = unittest.TestLoader()

suites = []
for tc in testCases:
    suites.append(testLoad.loadTestsFromTestCase(tc))

res_suite = unittest.TestSuite(suites)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(res_suite)
