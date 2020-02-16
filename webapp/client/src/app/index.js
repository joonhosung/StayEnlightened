import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import { NavBar } from "../components";
import { StudyspacesList, About, Home } from "../pages";
import api from "../api";

import "bootstrap/dist/css/bootstrap.min.css";

let buildings = api.getBuildings();

function App() {
  return (
    <Router>
      <NavBar />
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/about" exact component={About} />
        {/*Object.entries(buildings).map(async function(building) {
          await console.log(`/${buildings}`)
          return (
            <Route
              path={"/".concat(toString(building))}
              render={props => <StudyspacesList {...props} building={toString(building)} />}
            />
          );
        })*/}
        <Route path="/studyspaces/list" exact component={StudyspacesList} />
        <Route
          path="/Myhal_Centre"
          render={props => <StudyspacesList {...props} building={"Myhal_Centre"} />}
        />
        <Route
          path="/Bahen"
          render={props => <StudyspacesList {...props} building={"Bahen"} />}
        />
      </Switch>
    </Router>
  );
}

export default App;
