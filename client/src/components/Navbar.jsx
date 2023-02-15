import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const NavbarPage = () => {
  const [myNavbar, setMyNavbar] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchMyModels = async () => {
      try {
        const response = await axios.get('/api/v1/home/navbar/');
        setMyNavbar(response.data);
        setLoading(false);
      } catch (err) {
        setError(err);
        setLoading(false);
      }
    };

    fetchMyModels();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>An error occurred: {error.message}</div>;
  }

  return (
    <ul>
      {myNavbar && 
        myNavbar.map(navbar => (
          <li key={navbar.id}>
            <Link to='/'>{navbar.name}</Link>
          </li>
        ))
      }
    </ul>
  );  
};

export default NavbarPage;