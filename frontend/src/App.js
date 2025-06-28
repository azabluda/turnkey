import React, { useState } from 'react';
import './App.css';

function App() {
  const [message, setMessage] = useState('');
  const apiUrl = `${process.env.REACT_APP_API_URL || ''}/api/message`;

  const fetchMessage = async () => {
    const res = await fetch(apiUrl);
    const data = await res.json();
    setMessage(data.message);
  };

  return (
    <div className="App">
      <h1>Flask React Universal Starter</h1>
      <button onClick={fetchMessage}>Get Message from Flask</button>
      <div>
        <input type="text" value={message} readOnly />
      </div>
    </div>
  );
}

export default App;
