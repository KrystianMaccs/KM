import './App.css';
import CategoryPage from "./pages/CategoryPage";
import ProjectListPage from "./pages/ProjectListPage";
import ProjectDetailPage  from './pages/ProjectDetailPage';

export default function App() {
  return (
    <div>
      <CategoryPage />
      <ProjectListPage />
      <ProjectDetailPage />
    </div>
  );
}
