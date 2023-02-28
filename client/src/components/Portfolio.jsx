import React from 'react';
import { Route } from 'react-router-dom';
import { BrowserRouter as Router, Routes } from 'react-router-dom';
import CategoryPage from '../portfolio/CategoryPage';
import ProjectListPage from '../portfolio/ProjectListPage';
import ProjectDetailPage from '../portfolio/ProjectDetailPage';

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