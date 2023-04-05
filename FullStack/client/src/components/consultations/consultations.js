import React, { useState, useEffect } from "react";

function ConsultationsList() {
  const [consultations, setConsultations] = useState([]);

  useEffect(() => {
    if (consultations.length === 0) {
      fetch('/my/consultations', {
        credentials: 'include'
      })
        .then(response => response.json())
        .then(data => setConsultations(data.Consultations))
        .catch(error => console.error(error));
    }
  }, [consultations]); 
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