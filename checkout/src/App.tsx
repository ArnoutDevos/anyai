import React from 'react';
import './App.sass';
import HomePage from './HomePage';
import Paid from './Paid';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Transactions from './Transactions';

const App: React.FC = () => {
  return (
    <Router>
      <Switch>
        <Route exact path="/">
          <HomePage/>
        </Route>
        <Route path="/paid">
          <Paid />
        </Route>
        <Route path="/transactions">
          <Transactions />
        </Route>
      </Switch>
    </Router>    
  );
}

export default App;
