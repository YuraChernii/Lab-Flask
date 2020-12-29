import unittest
import flask_testing
from flask_testing import TestCase
from flask import Flask
import urllib.request
import json
#from requests.auth import _basic_auth_str
from pybase64 import b64encode
from app import app
from app import func_for_put
from flask import Flask,abort, jsonify
#from app import routes
class TestRating(unittest.TestCase):
    #def create_app(self):
    #    app = Flask(__name__)
    #    app.config['TESTING'] = True
    #    return app


    def test_rating_get_true(self):
        print(1111111111111111)
        tester = app.test_client(self)
        response = tester.get('/rating',headers={"Authorization": "Basic {user}".format(user=b64encode(b"Petro:12345").decode())}, data=dict(subjectName="math"), follow_redirects=True)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(1, data[0])
        self.assertEqual(200, response.status_code)

    def test_rating_get_false(self):
        tester = app.test_client(self)
        response = tester.get('/rating',headers={"Authorization": "Basic {user}".format(user=b64encode(b"Petro:12345").decode())}, data=dict(subjectName="mathhhhhhhhhhhhhhhhhdfgdfgdf"), follow_redirects=True)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual("This student does not have such subject((", data['message'])
        self.assertEqual(404, response.status_code)

    def test_rating_post_true(self):
        tester = app.test_client(self)
        response = tester.post('/rating',headers={"Authorization": "Basic {user}".format(user=b64encode(b"Petro:12345").decode())}, data=dict(studentName='Petro', subjectName="mathhhhhhhhhhhhhhh", mark='3'), follow_redirects=True)
        #if
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual('mathhhhhhhhhhhhhhh', data['subjectName'])

    def test_rating_put_true(self):
        tester = app.test_client(self)
        response = tester.put('/rating', headers={"Authorization": "Basic {user}".format(user=b64encode(b"Petro:12345").decode())},data=dict(studentName='Petro', subjectName="mathhhhhhhhhhhhhhh", mark='4'),follow_redirects=True)
        # if
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual('mathhhhhhhhhhhhhhh', data['subjectName'])
    def test_rating_put_trueeeeee(self):
        tester = app.test_client(self)
        response = tester.get('/rating/bestStudents/15', headers={
            "Authorization": "Basic {user}".format(user=b64encode(b"Petro:12345").decode())},
                               follow_redirects=True)
        # if
        print(3333)
        data = json.loads(response.get_data(as_text=True))
        print(data)
        self.assertEqual(200, response.status_code)


class TestStudent(unittest.TestCase):
    #def create_app(self):
    #    app = Flask(__name__)
    #    app.config['TESTING'] = True
    #    return app


    def test_rating_get_true(self):
        tester = app.test_client(self)
        response = tester.get('/student',headers={"Authorization": "Basic {user}".format(user=b64encode(b"Petro:12345").decode())}, follow_redirects=True)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual('Petro', data['userName'])
        #self.assertEqual(200, response.status_code)


    def test_rating_post(self):
        tester = app.test_client(self)
        response = tester.post('/student',headers={"Authorization": "Basic {user}".format(user=b64encode(b"Petro:12345").decode())}, data=dict(userName="Roman",email="dsndbdd33333ff3333353f3333333333333g3333rg",phone="sdfgdsdgdfd5ffggdg",password="dsfgsgfd5fgdfg"), follow_redirects=True)
        data = json.loads(response.get_data(as_text=True))
        print(data)
        if "message" in data:
            self.assertEqual('We already have such a student)', data['message'])
            response = tester.delete('/student', headers={"Authorization": "Basic {user}".format(user=b64encode(b"Petro:12345").decode())},data=dict(userName="Roman"))
            self.assertEqual(200, response.status_code)
        else:
            response = tester.delete('/student', headers={"Authorization": "Basic {user}".format(user=b64encode(b"Petro:12345").decode())},data=dict(userName="Roman"))
            self.assertEqual(200, response.status_code)

    def test_rating_put_true(self):
        tester = app.test_client(self)
        response = tester.put('/student',
                              headers={"Authorization": "Basic {user}".format(user=b64encode(b"Petro:12345").decode())},
                              data=dict(email="gfbfffffffbgsfg", phone="eabffffffbdf"), follow_redirects=True)
        response = tester.put('/student',
                              headers={"Authorization": "Basic {user}".format(user=b64encode(b"Petro:12345").decode())},
                              data=dict(email="gfbffffbgsfg", phone="eabbdf"), follow_redirects=True)
        # if
        data = json.loads(response.get_data(as_text=True))
        print(111111)
        print(data)
        print(data)
        print(data)
        print(data)
        print(112111)
        self.assertEqual('eabbdf', data['phone'])

#if __name__ == '__main__':
#    unittest.main()
#pytest -v --cov=. --cov-report=html
#python test_app.py
#pytest --cov=PythonLab
#coverage report -m
