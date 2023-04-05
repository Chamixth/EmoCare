import React from 'react'
import './home.css'
import { NavLink } from 'react-router-dom'

export default function Home() {

  return (
    <div className='body-home'>
      <div class='title'>
        <h1>Excelsior</h1>
      </div>
      <div class='container-home'>
        <NavLink to='/login' onClick={() => localStorage.setItem('type', 'Doctor')}
                 class='switch-button'>Doctor</NavLink>
        <NavLink to='/login' onClick={() => localStorage.setItem('type', 'Patient')}
                 class='switch-button'>Patient</NavLink>
      </div>
    </div>
  )
}
