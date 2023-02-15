import React from 'react';
import { Route } from 'react-router-dom';
import { BrowserRouter as Router, Routes } from 'react-router-dom';
import HomePage from './components/Home';
import CategoryPage from "./pages/CategoryPage";
import ProjectListPage from "./pages/ProjectListPage";
import ProjectDetailPage  from './pages/ProjectDetailPage';
import './App.css';

const App = () => {
    return (
        <>
          <Router>
            <Routes>
              <Route path="*" element={<HomePage/>} />
              <Route path="/portfolio/" element={<CategoryPage />} />
              <Route path="/category-project/:slug/" element={<ProjectListPage />} />
              <Route path="/project_list/:slug/" element={<ProjectDetailPage />} />
            </Routes>
          </Router>
        </>
    );
};

export default App;
