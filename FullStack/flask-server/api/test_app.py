import unittest
from app import app
from models import db
from models import User,Role
import bcrypt

class TestApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/User/GitHub/EmoCare/FullStack/flask-server/api/memory.db'
        db.create_all()

        role = Role.query.filter_by(id=1).first()
        if not role:
            doctor_role = Role(id=1,name='Doctor')
            db.session.add(doctor_role)
            db.session.commit()
        else:
            doctor_role = role
        role = Role.query.filter_by(id=2).first()
        if not role:
            patient_role = Role(id=2,name='Patient')
            db.session.add(patient_role)
            db.session.commit()
        else:
            patient_role = role
            
    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
    
    def test_about_page(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code,200)

    def test_patient_dashboard(self):
        self.client.post('/signin', data=dict(username="testuser", password="testpassword"), follow_redirects=True)
        response = self.client.get('/patient/dashboard')
        self.assertEqual(response.status_code,302)

    def test_doctor_dashboard(self):
        self.client.post('/signin', data=dict(username="testuser", password="testpassword"), follow_redirects=True)
        response = self.client.get('/doctor/dashboard')
        self.assertEqual(response.status_code,302)

    def test_signup_success(self):
        data = {
            'name': 'Sathmi',
            'email': 'sathmi@gmail.com',
            'username': 'sathmi',
            'password': 'password',
            'options': '1'
        }
        response = self.client.post('/signup',data=data,follow_redirects=True)
        self.assertEqual(response.status_code,200)
        user = User.query.filter_by(username='sathmi').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.name,'Sathmi')
        self.assertEqual(user.email,'sathmi@gmail.com')
        self.assertEqual(user.roles[0].name, 'Doctor')
        self.assertEqual(user.username,'sathmi')

    def test_signup_existing_username(self):
        user = User(name = 'Sathmi', email ='sathmi@gmail.com' , username = 'sathmi')
        db.session.add(user)
        db.session.commit()
    
        data = {
            'name': 'Yasara',
            'email': 'yasara@gmail.com',
            'username': 'yasara',
            'password': 'password123',
            'options': '2'
        }

        user = User(name='Navod', email='navod@gmail.com', username='navod',password='password',active=1)
        db.session.add(user)
        db.session.commit()
        response = self.client.post('/signup', data=data,follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        user_count = User.query.filter_by(username='sathmi').count()
        self.assertEqual(user_count, 1)

if __name__=='__main__':
    unittest.main()