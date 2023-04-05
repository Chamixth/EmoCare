import React, { useState } from 'react'
import Layout from '../layout'
import './profile.css'
import { FileUploader } from 'react-drag-drop-files'

export default function EditProfile() {

  const fileTypes = ['JPG', 'PNG', 'GIF']
  const [file, setFile] = useState(null)
  const handleChange = (file) => {
    setFile(file)
  }


  return (
    <Layout>
      <div className='edit-profile'>
        <form action=''>
          <fieldset>
            <legend align='center'>Personal Details</legend>
            <label for='name'>FirstName: </label>
            <input type='text' id='name' />
            <label for='name'>LastName: </label>
            <input type='text' id='name' />
            <label for='dob'>Birthday: </label>
            <input type='date' id='dob' />
            <label for='dob'>Image: </label>
            <FileUploader handleChange={handleChange} name='file' types={fileTypes} />
            <br />
            <br />
            <button className='btn btn-primarys'>Update</button>
          </fieldset>
          <fieldset>
            <legend align='center'>Update Password</legend>
            <label for='oldpassword'>Old password: </label>
            <input type='password' id='oldpassword' />
            <br />
            <label for='newpassword'>New password: </label>
            <input type='password' id='newpassword' />
            <br />
            <button className='btn btn-primarys'>Update</button>
          </fieldset>
        </form>
      </div>
    </Layout>
  )
}
