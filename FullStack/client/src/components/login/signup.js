import React, {useState} from 'react'
import { getType } from '../utils'
import './login.css'
import { useNavigate } from 'react-router-dom'
import Navbar from '../../pages/Navbar'


export default function Login() {

  const type = getType()

  const navigate = useNavigate()
  const [signIn,setSignIn] =useState(null)


  return (
    <>
      < Navbar />


    <div className='body-log'>
      {/*<h1>{type === 'Doctor' ? 'Doctor' : 'Patient'}</h1>*/}
      <div class='container login-boxx'>


        <form>
          <div class='form-content'>
            { <div class='signup-form'>
              <div class='title'>Sign up</div>
              <div class='input-box'>
                  <i class='fas fa-lock'></i>
                  <label className='user-label'>Doctor</label>
                  <input type='radio' value="doctor" name='user' checked onClick={
                    window.onload = ()=>{
                      document.getElementById('doctorId').style.display = 'block'
                    }
                  } required/>
                  <label className='user-label'>Patient</label>
                  <input type='radio' value='patient' name='user' onClick={
                    window.onload = ()=>{
                      document.getElementById('doctorId').style.display = 'none'
                    }
                  } required/>
                </div>
              <div class='input-box'>
                <i class='fas fa-user'></i>
                <input type='text' placeholder='User Name' required/>
              </div>
              <div class='input-boxes'>
                <div id='doctorId' class='input-box'>
                  <i class='fas fa-envelope'></i>
                  <input type='text' placeholder='DoctorID' required/>
                </div>
                <div class='input-box'>
                  <i class='fas fa-lock'></i>
                  <input type='email' placeholder='Email' required/>
                </div>
                <div class='input-box'>
                  <i class='fas fa-lock'></i>
                  <input type='password' placeholder='Password' required/>
                </div>
                <div class='button input-box'>
                  <i class='fas fa-envelope'></i>
                  <input type='submit' value='Signup'/>
                </div>
                <div class='text sign-up-text'>Already have an account? <span for='flip' onClick={() => navigate('/signin')}>Sign
                  now</span></div>
              </div>
            </div>}
          </div>
        </form>
      </div>
    </div>
    </>
  )
}
