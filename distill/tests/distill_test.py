from flask import Flask, request

from distill import app as test_app

def test_example ():
	with test_app.test_client () as c:
		rv = c.get ('/?tequila=42')
		assert request.args ['tequila'] == '42'

# import os
# import flaskr
# import unittest
# import tempfile

# class FlaskrTestCase(unittest.TestCase):

#     def setUp(self):
#         self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
#         flaskr.app.config['TESTING'] = True
#         self.app = flaskr.app.test_client()
#         flaskr.init_db()

#     def tearDown(self):
#         os.close(self.db_fd)
#         os.unlink(flaskr.app.config['DATABASE'])

# if __name__ == '__main__':
#     unittest.main()