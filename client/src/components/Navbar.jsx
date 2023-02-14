import React, { useState, useEffect } from 'react';
import axios from 'axios';

const NavbarPage = () => {
  const [myNavbar, setMyNavbar] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchMyModels = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/v1/home/navbar/');
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
            {navbar.name}
          </li>
        ))
      }
    </ul>
  );  
};

export default NavbarPage;