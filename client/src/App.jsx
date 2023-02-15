import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
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
              <Route path="/project_list/:slug/" element={<ProjectDetailPage />} />
              <Route path="/" element={<Navbar />} />
            </Routes>
          </Router>
        </>
    );
};

export default App;
