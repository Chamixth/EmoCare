import React, { useState, useEffect } from "react";

function ConsultationsList() {
  const [consultations, setConsultations] = useState([]);
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    if (!loaded) {
      fetch('/my/consultations', {
        credentials: 'include'
      })
        .then(response => response.json())
        .then(data => {
          setConsultations(data.Consultations);
          setLoaded(true);
        })
        .catch(error => console.error(error));
    }
  }, [loaded]);

  return (
    <div>
      <h1>My Consultations</h1>
      <ul>
        {consultations.map(consult => (
          <li key={consult['Consultation ID']}>
            Request ID: {consult['Request ID ']}<br />
            Doctor ID: {consult['Doctor ID']}<br />
            Patient ID: {consult['Patient ID']}<br />
            Meeting date: {consult['Meeting date']}<br />
            Meeting time: {consult['Meeting time']}<br />
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ConsultationsList;