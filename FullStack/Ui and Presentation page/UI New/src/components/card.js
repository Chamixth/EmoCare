import React from 'react'
import './caard.css'
import { getType } from './utils'

export default function Card() {

  const type = getType()


  return (
    <div>
      <div className='cardd'>
        <div className='left'>
          <img src='https://i.imgur.com/cMy8V5j.png'
               alt='user' width='100' className='' />
          <h4 className='m-10'>Name</h4>
          <p>DdoctorID</p>
        </div>

        <div class='right'>
          {type !== 'Doctor' ? <div>
              <div class='info'>
                <h3>Information</h3>
                <div class='info_data'>
                  <div class='data'>
                    <h4>Email</h4>
                    <p></p>
                  </div>
                  <div class='data'>
                    <h4>Date Of Birth</h4>
                    <p></p>
                  </div>
                </div>
              </div>

            

              <div class='social_media'>
                <button className='btn-book'>Book Now</button>
              </div>
            </div> :
            <div className='right-containe'>
              <div className='label-date'>
                Date & Time
              </div>
              <div className='d-flex gap-20'>
                <input type={'date'} />
                <input type={'time'} />
              </div>
              <div className='card-btns'>
                <button className='btn btn-success'>
                  Accept
                </button>
                <button className='btn btn-danger'>
                  Decline
                </button>
              </div>

            </div>}
        </div>
      </div>
    </div>
  )
}
