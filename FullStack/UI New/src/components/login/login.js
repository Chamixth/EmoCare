import React from 'react'
import { getType } from '../utils'
import './login.css'
import { useNavigate } from 'react-router-dom'


export default function Login() {

  const type = getType()

  const navigate = useNavigate()


  return (


    <div className='body-log'>
      <h1>{type === 'Doctor' ? 'Doctor' : 'Patient'}</h1>
      <div class='container'>
        <input type='checkbox' id='flip' />
        <div class='cover'>

          <div class='back'>

            <div class='text'>

            </div>
          </div>
        </div>
        <form>
          <div class='form-content'>
            <form>
              <div class='login-form'>
                <div class='title'>Login</div>
                <div class='input-boxes'>
                  <div class='input-box'>
                    <i class='fas fa-envelope'></i>
                    <input type='text' placeholder='Username' required />
                  </div>
                  <div class='input-box'>
                    <i class='fas fa-lock'></i>
                    <input type='password' placeholder='Password' required />
                  </div>
                  <div class='text'><a href='#'>Forgot password?</a></div>
                  <div class='button input-box'>
                    <i class='fas fa-envelope'></i>
                    <input type='submit' value='Login' onClick={() => {
                      if (type !== 'Doctor') {
                        navigate('/patient-dashboard')
                      } else {

                        navigate('/doctor-dashboard')
                      }


                    }} />
                  </div>
                  <div class='text sign-up-text'>Don't have an account? <label for='flip'>Signup now</label></div>
                </div>
              </div>
            </form>
            <div class='signup-form'>
              <div class='title'>Sign up</div>
              <div class='input-box'>
                <i class='fas fa-user'></i>
                <input type='text' placeholder='User Name' required />
              </div>
              <div class='input-boxes'>
                {type === 'Doctor' && <div class='input-box'>
                  <i class='fas fa-envelope'></i>
                  <input type='text' placeholder='DoctorID' required />
                </div>}
                <div class='input-box'>
                  <i class='fas fa-lock'></i>
                  <input type='password' placeholder='Email' required />
                </div>
                <div class='input-box'>
                  <i class='fas fa-lock'></i>
                  <input type='password' placeholder='Password' required />
                </div>
                <div class='button input-box'>
                  <i class='fas fa-envelope'></i>
                  <input type='submit' value='Signup' />
                </div>
                <div class='text sign-up-text'>Already have an account? <label for='flip'>Login now</label></div>
              </div>
            </div>
          </div>
        </form>
      </div>
    </div>
  )
}
