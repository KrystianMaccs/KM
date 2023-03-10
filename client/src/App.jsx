import React from 'react';
import HomePage from './home/Home';
import Portfolio from './components/Portfolio';
import Portfolio from './portfolio/Portfolio';
import ContactForm from './contact/ContactMe';
import './App.css';

const App = () => {
    return (
        <>
          <HomePage />
          <Portfolio />
          <ContactForm />
        </>
    );
};

export default App;
