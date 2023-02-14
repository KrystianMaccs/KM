import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams, Link } from 'react-router-dom'; // import from react-router-dom

const ProjectListPage = (props) => {
  const params = useParams(); // Get the params with this hook
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchProjects = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/api/v1/portfolio/project_list/`);
        const data = response.data;
        setProjects(data);
        setLoading(false);
      } catch (err) {
        setError(err);
        setLoading(false);
      }
    };

    fetchProjects();
  }, [params.categoryId]);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>An error occurred: {error.message}</div>;
  }

  return (
    <ul>
      {projects.map(project => (
        <li key={project.id}>
          <Link to='/project_list/:id/'>{project.title}</Link>
        </li>
      ))}
    </ul>
  );
};

export default ProjectListPage;