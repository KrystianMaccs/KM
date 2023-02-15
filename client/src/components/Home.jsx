import React from 'react';
import { Route } from 'react-router-dom';
import { BrowserRouter as Router, Routes } from 'react-router-dom';
import Navbar from './Navbar';

const HomePage = () => {
  return (
    <div>
        <Routes>
            <Route path="*" element={<Navbar />} />
        </Routes>
    </div>
  );
};

export default HomePage;
