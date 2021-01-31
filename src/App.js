import './App.css';
import React from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import CreateReddit from './components/pages/CreateReddit';
import CreateTwitter from './components/pages/CreateTwitter';
import CreateWebsite from './components/pages/CreateWebsite';
import CreatePRAW from './components/pages/CreatePRAW';
import Login from './components/pages/Login';
import Register from './components/pages/Register';
import axios from 'axios';

function App() {

  return (
    <Router>
      <div className="App">
          <Route path="/" exact component={Login}/>
          <Route path="/create/reddit" exact component={CreateReddit}/>
          <Route path="/create/praw" exact component={CreatePRAW}/>
          <Route path="/create/twitter" exact component={CreateTwitter}/>
          <Route path="/create/website" exact component={CreateWebsite}/>
          <Route path="/home" exact component={Dashboard}/>
          <Route path="/register" exact component={Register}/>
        
      </div>
    </Router>

  );
}

export default App;