import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const CategoryPage = () => {
  const [myCategory, setMyCategory] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchMyModels = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/v1/portfolio/categories/');
        setMyCategory(response.data);
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
      {myCategory && 
        myCategory.map(category => (
          <li key={category.id}>
            <Link to='/project_list/'>{category.name}</Link>
          </li>
        ))
      }
    </ul>
  );  
};

export default CategoryPage;