import React, {useState,useEffect} from 'react';
import logo from './logo.svg';
import './App.css';
import ReactDOM from 'react-dom';
import 'semantic-ui-css/semantic.min.css';
import { Header} from 'semantic-ui-react';

function App() {
  const [predictedClass, setPredictedClass] = useState('2');
  useEffect(()=>{
    fetch('/index',{
      headers : { 
        'Content-Type': 'application/json',
        'Accept': 'application/json'
       }
    }).then(res => res.json()).then(data => {
      setPredictedClass(data.predictedClass);
    });
  },[]);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <Header as ='h3'> Predicted Class: {predictedClass} </Header>
      </header>
    </div>
  );
}

export default App;
