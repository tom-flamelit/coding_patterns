import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [counter, setCounter] = useState(0);

  const handleAdd = async () => {
    try {
      const response = await axios.get('http://localhost:8000/add1');
      setCounter(response.data.new_value);
    } catch (error) {
      console.error('Error during API call', error);
    }
  };

  const handleSubtract = async () => {
    try {
      const response = await axios.get('http://localhost:8000/subtract1');
      setCounter(response.data.new_value);
    } catch (error) {
      console.error('Error during API call', error);
    }
  };

  const handleReport = async () => {
    try {
      const response = await axios.get('http://localhost:8000/report');
      setCounter(response.data.current_value);
    } catch (error) {
      console.error('Error during API call', error);
    }
  };

  return (
    <div>
      <h1>Counter: {counter}</h1>
      <button onClick={handleAdd}>Add 1</button>
      <button onClick={handleSubtract}>Subtract 1</button>
      <button onClick={handleReport}>Report</button>
    </div>
  );
}

export default App;
