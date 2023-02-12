import React from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import CategoryPage from "./pages/CategoryPage";
import ProjectListPage from "./pages/ProjectListPage";
import ProjectDetailPage  from './pages/ProjectDetailPage';
import './App.css';

const App = () => (
  <Router>
    <Route exact path="/categories/" component={CategoryPage} />
    <Route exact path="/projects_list/" component={ProjectListPage} />
    <Route exact path="/project/:slug" component={ProjectDetailPage} />
  </Router>
);

export default App;
