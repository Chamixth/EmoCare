import './App.css'

import Doctor from './components/doctor/doctor'
import Patient from './components/patient/patient'
import { Route, Routes } from 'react-router-dom'
import Video from './components/doctor/video'
import PatientDashboard from './components/patient-dashboard/patient-dashboard'
import Login from './components/login/login'
import Home from './components/home/home'
import EditProfile from './components/edit-profile/edit-profile'


function App() {
  return (
    <div>
      <Routes>
        <Route path='/patient-dashboard' element={<PatientDashboard />} />
        <Route path='/doctor-dashboard' element={<Doctor />} />
        <Route path='/patient' element={<Patient />} />
        <Route path='/video' element={<Video />} />
        <Route path='/login' element={<Login />} />
        <Route path='/edit-profile' element={<EditProfile />} />
        <Route path='/' element={<Home />} />
        <Route path='/doctor' element={<Doctor />} />


      </Routes>
    </div>
  )
}

export default App
