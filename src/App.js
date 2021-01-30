import './App.css';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import CreateReddit from './components/pages/CreateReddit';
import CreateTwitter from './components/pages/CreateTwitter';
import CreateWebsite from './components/pages/CreateWebsite';

function App() {
  return (
    <Router>
      <div className="App">
        <Route path="/" exact component={Dashboard}/>
        <Route path="/create/reddit" exact component={CreateReddit}/>
        <Route path="/create/twitter" exact component={CreateTwitter}/>
        <Route path="/create/website" exact component={CreateWebsite}/>
      </div>
    </Router>

  );
}

export default App;
