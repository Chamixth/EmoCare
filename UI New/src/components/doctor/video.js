import React, { useState } from 'react'
import AgoraUIKit, { layout } from 'agora-react-uikit'
import { useNavigate } from 'react-router-dom'
import { getType } from '../utils'
// import Layout from '../layout'

export default function Video() {

  const [inCall, setInCall] = useState(false)
  const [channelName, setChannelName] = useState('')
  const [videoCall, setVideoCall] = useState(false)

  const [videocall, setVideocall] = useState(false)
  const [isHost, setHost] = useState(true)
  const [isPinned, setPinned] = useState(false)
  const [username, setUsername] = useState('')
  const navigate = useNavigate()
  const type = getType()

  const callbacks = {
    EndCall: () => setVideoCall(false)
  }
  return (
    <div>
      <div style={styles.container}>
        <div style={styles.videoContainer}>
          <h1 style={styles.heading}>Excelsior</h1>
          {videocall ? (
            <>
              <div style={styles.nav}>
                <p style={{ fontSize: 20, width: 200 }}>
                  You're {isHost ? 'a host' : 'an audience'}
                </p>
                <p style={styles.btn} onClick={() => setHost(!isHost)}>
                  Change Role
                </p>
                <p style={styles.btn} onClick={() => setPinned(!isPinned)}>
                  Change Layout
                </p>
              </div>
              <AgoraUIKit
                rtcProps={{
                  appId: '15cb7bee7eae4a78a31dc66d95b1f927',
                  channel: 'test',
                  token: '007eJxTYJiWc33Wod/Kcu1bJr6+wyC3XNKgbeHl151HNrVO3ZwSyd+mwGBompxknpSaap6amGqSaG6RaGyYkmxmlmJpmmSYZmlknimtntIQyMiQaKjCzMgAgSA+C0NJanEJAwMAxO0f4w==', // add your token if using app in secured mode
                  role: isHost ? 'host' : 'audience',
                  layout: isPinned ? layout.pin : layout.grid,
                  enableScreensharing: false
                }}
                rtmProps={{ username: username || 'user', displayUsername: true }}
                callbacks={{
                  EndCall: () => {
                    if (type !== 'Doctor') {
                      navigate('/patient-dashboard')
                    } else {

                      navigate('/doctor-dashboard')
                    }
                  }
                }}
              />
              <div style={{backgroundColor:"rgb(0, 123, 255)",display:"flex",justifyContent:"center",alignItems:"center"}}>
                <button className={"btn-video"}>Button</button>
              </div>
            </>
          ) : (
            <div style={styles.nav}>
              <input
                style={styles.input}
                placeholder='Enter Your name'
                type='text'
                value={username}
                onChange={(e) => {
                  setUsername(e.target.value)
                }}
              />
              <h3 style={styles.btn} onClick={() => setVideocall(true)}>
                Start Call
              </h3>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}

const styles = {
  container: {
    width: '100vw',
    height: '100vh',
    display: 'flex',
    flex: 1,
    backgroundColor: '#007bff22'
  },
  heading: { textAlign: 'center', marginBottom: 0 },
  videoContainer: {
    display: 'flex',
    flexDirection: 'column',
    flex: 1
  },
  nav: { display: 'flex', justifyContent: 'space-around' },
  btn: {
    backgroundColor: '#007bff',
    cursor: 'pointer',
    borderRadius: 5,
    marginBottom: 20,
    padding: '4px 8px',
    color: '#ffffff',
    fontSize: 20
  },
  input: {
    alignSelf: 'center',
    height: '42px',
    paddingLeft: '12px',
    borderRadius: '8px',
    border: 'none'
  }
}