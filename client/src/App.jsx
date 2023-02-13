import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import CategoryPage from "./pages/CategoryPage";
import ProjectListPage from "./pages/ProjectListPage";
import ProjectDetailPage  from './pages/ProjectDetailPage';
import './App.css';

const App = () => {
    return (
        <>
          <Router>
            <Routes>
              <Route path="/categories/" element={<CategoryPage />} />
              <Route path="/project_list/" element={<ProjectListPage />} />
              <Route path="/str:slug/" element={<ProjectDetailPage />} />
            </Routes>
          </Router>
        </>
    );
};

export default App;
