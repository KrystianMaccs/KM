import './App.css';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import CategoryPage from "./pages/CategoryPage";
import ProjectListPage from "./pages/ProjectListPage";
import ProjectDetailPage  from './pages/ProjectDetailPage';



const App = () => {
	return (
		<>
			<Router>
          <Route path="/categories/" element={<CategoryPage />} />
		      <Route path="/str:slug/" element={<ProjectDetailPage />} />
          <Route path="/project_list/" element={<ProjectListPage />} />
			</Router>
		</>
	);
};

export default App;

