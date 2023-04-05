import React from 'react'
import Layout from '../layout'
import img01 from '../../Assets/13.png'
import img02 from '../../Assets/10.png'
import img03 from '../../Assets/09.png'
import img04 from '../../Assets/11.png'
import { useNavigate } from 'react-router-dom'


export default function Doctor() {

  const navigate = useNavigate()


  return (
    <div>
      <Layout type={'dashboard'}>
        <div class='box-container'>

          <div class='box box1'>
            <div class='text'>
              <h2 class='topic-heading'></h2>
              <h2 class='topic'>Doctor Views</h2>
            </div>

            <img src={img04}
                 alt='Views' />
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

          <div class='box box3'>
            <div class='text'>
              <h2 class='topic-heading'></h2>
              <h2 class='topic'>Reviws</h2>
            </div>

            <img src={img02}
                 alt='comments' />
          </div>

          <div class='box box4'>
            <div class='text'>
              <h2 class='topic-heading'></h2>
              <h2 class='topic'>Attendies</h2>
            </div>

            <img src={img03} alt='logo' />
          </div>
        </div>

        <div class='report-container'>
          <div class='report-header'>
            <h1 class='recent-Articles'>Recent Patients</h1>
            <button class='view'>View All</button>
          </div>

          <div class='report-body'>
            <div class='report-topic-heading'>
              <h3 class='t-op'>Name</h3>
              <h3 class='t-op'>Hours</h3>
              <h3 class='t-op'>Report</h3>
              <h3 class='t-op'>Status</h3>
            </div>

          </div>
        </div>
      </Layout>
    </div>
  )
}
