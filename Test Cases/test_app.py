Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import unittest
from flask import Flask
from flask_testing import TestCase
from app import app, db
from models import User, Role, Request

class TestApp(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        return app

    def setUp(self):
        db.create_all()
        self.client = app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_home_page(self):
        response = self.client.get('/')
        self.assert200(response)
        self.assert_template_used('home.html')

    def test_login(self):
        # create a test user
        test_user = User(name='testuser', email='test@example.com', password='testpassword', role_id=2)
        db.session.add(test_user)
        db.session.commit()

        # test successful login
        response = self.client.post('/login', data=dict(email='test@example.com', password='testpassword'), follow_redirects=True)
        self.assert200(response)
        self.assertIn(b'Welcome back, testuser', response.data)

        # test unsuccessful login
        response = self.client.post('/login', data=dict(email='test@example.com', password='wrongpassword'), follow_redirects=True)
        self.assert200(response)
        self.assertIn(b'Invalid email or password', response.data)

    def test_all_doctors(self):
        # create a test doctor
        test_doctor = User(name='testdoctor', email='testdoctor@example.com', password='testpassword', role_id=1)
        db.session.add(test_doctor)
        db.session.commit()

        # test getting all doctors
        response = self.client.get('/all/doctors')
        self.assert200(response)
        self.assertIn(b'testdoctor', response.data)

    def test_create_request(self):
        # create a test patient
        test_patient = User(name='testpatient', email='testpatient@example.com', password='testpassword', role_id=2)
...         db.session.add(test_patient)
...         db.session.commit()
... 
...         # create a test doctor
...         test_doctor = User(name='testdoctor', email='testdoctor@example.com', password='testpassword', role_id=1)
...         db.session.add(test_doctor)
...         db.session.commit()
... 
...         # test creating a request
...         with self.client:
...             self.client.post('/login', data=dict(email='testpatient@example.com', password='testpassword'), follow_redirects=True)
...             response = self.client.post(f'/request/{test_doctor.id}', data=dict(patient_id=test_patient.id, meeting_date='2023-04-06', meeting_time='12:00'), follow_redirects=True)
...             self.assert200(response)
...             self.assertIn(b'Request created successfully', response.data)
... 
...     def test_view_requests(self):
...         # create a test doctor
...         test_doctor = User(name='testdoctor', email='testdoctor@example.com', password='testpassword', role_id=1)
...         db.session.add(test_doctor)
...         db.session.commit()
... 
...         # create a test patient
...         test_patient = User(name='testpatient', email='testpatient@example.com', password='testpassword', role_id=2)
...         db.session.add(test_patient)
...         db.session.commit()
... 
...         # create a test request
...         test_request = Request(doctor_id=test_doctor.id, patient_id=test_patient.id, meeting_date='2023-04-06', meeting_time='12:00')
...         db.session.add(test_request)
...         db.session.commit()
... 
...         #
