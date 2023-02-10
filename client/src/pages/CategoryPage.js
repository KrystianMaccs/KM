import React, { useState, useEffect } from 'react';
import axios from 'axios';

const CategoryList = () => {
  const [myCategory, setMyCategory] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchMyModels = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/v1/categories/');
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
      {myCategory.map(myCategory => (
        <li key={myCategory.id}>{myCategory.name}</li>
      ))}
    </ul>
  );
};

export default CategoryList;
