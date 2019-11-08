import xmlrunner
import unittest

suite = unittest.TestLoader().discover('.', pattern='test*')
runner = xmlrunner.XMLTestRunner(output='test-reports')
result = unittest.main(testRunner=runner)
