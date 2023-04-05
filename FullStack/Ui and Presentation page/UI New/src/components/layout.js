import React, { useState } from 'react'
import search from '../Assets/14.png'
import dp from '../Assets/15.png'
import dashobardIcon from '../Assets/05.png'
import patientIcon from '../Assets/06.png'
import logoutIcon from '../Assets/08.png'

import { NavLink } from 'react-router-dom'
import { getType } from './utils'

export default function Layout({ children }) {
  const type = getType()
  const [see, setSee] = useState(false)



  return (
    <div>
      <header>

        <div className='logosec'>
          <div className='logo'>Exclesior</div>
          <img src='https://media.geeksforgeeks.org/wp-content/uploads/20221210182541/Untitled-design-(30).png'
               className='icn menuicn'
               id='menuicn'
               onClick={() => setSee(!see)}
               alt='menu-icon' />
        </div>

        <div className='searchbar'>
          <input type='text'
                 placeholder='Search' />
          <div className='searchbtn'>
            <img src={search}
                 className='icn srchicn'
                 alt='search-icon' />
          </div>
        </div>

        <div className='message'>
          <div className='dp'>
            <img src={dp}
                 className='dpicn'
                 alt='dp' />
          </div>
          <div className='user-data'>
            <div className='t-op-nextlvl'>

            </div>
            <div className='t-op-nextlvl color-gray'>

            </div>
          </div>

        </div>

      </header>

      <div className='main-container'>
        <div className={'navcontainer' + (see ? 'd-visible' : '')}>
          <nav className='nav'>
            <div className='nav-upper-options'>
              <NavLink
                className={({ isActive }) => !isActive ? 'nav-option' : 'nav-option option1'}
                to={type === 'Doctor' ? '/doctor-dashboard' : '/patient-dashboard'}>
                <img src={dashobardIcon}
                     className='nav-img'
                     alt='dashboard' />
                <h3> Dashboard</h3>
              </NavLink>

              <NavLink
                className={({ isActive }) => !isActive ? 'nav-option' : 'nav-option option1'}
                to={'/edit-profile'}>
                <img src={dashobardIcon}
                     className='nav-img'
                     alt='dashboard' />
                <h3> Edit Profile</h3>
              </NavLink>


              {type === 'Doctor' && <NavLink
                className={({ isActive }) => !isActive ? 'nav-option' : 'nav-option option1'}
                to='/patient'>
                <img src={patientIcon}
                     className='nav-img'
                     alt='report' />
                <h3> Patients Request</h3>
              </NavLink>}



              <NavLink to='/' className={({ isActive }) => !isActive ? 'nav-option' : 'nav-option option1'}>
                <img src={logoutIcon}
                     className='nav-img'
                     alt='logout' />
                <h3>Logout</h3>
              </NavLink>

            </div>
          </nav>
        </div>
        <div className='main'>

         

          <div>
            {children}
          </div>
        </div>
      </div>

    </div>
  )
}
