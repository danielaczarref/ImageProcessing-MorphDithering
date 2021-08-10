import * as React from "react"
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import { Home, Loading } from '../pages';

const Routes = () => (
  <BrowserRouter>
    <Switch>
      <Route exact path='/loading' component={Loading} />
      <Route exact path='/home' component={Home} />
      <Route path='*' component={Loading} />
    </Switch>
  </BrowserRouter>
)

export default Routes