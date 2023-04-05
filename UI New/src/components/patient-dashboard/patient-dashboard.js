import React from 'react'
import { useNavigate } from 'react-router-dom'
import Layout from '../layout'
import img01 from '../../Assets/13.png'
import img02 from '../../Assets/10.png'
import Card from '../card'


export default function PatientDashboard() {
  const navigate = useNavigate()
  return (
    <Layout>
      <div className='box-container'>
        <div class='box box3'>
          <div class='text'>
            <h5 class='labe-card'>Date & Time</h5>
            <h6 class='labe-value'>2023-03-14 17:00</h6>
          </div>

          <img src={img02}
               alt='comments' />
        </div>
        <div class='box box2' onClick={() => {
          console.log('asd')
          navigate('/video')
        }}>
          <div class='text'>
            <h2 class='topic-heading'></h2>
            <h2 class='topic'>Video Call</h2>
          </div>

          <img src={img01}
               alt='likes' />
        </div>
      </div>

      <div className='d-flex mobile-block'>
        <Card />
      </div>
    </Layout>
  )
}
