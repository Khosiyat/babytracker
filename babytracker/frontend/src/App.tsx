import { BrowserRouter, Routes, Route } from 'react-router-dom';
import LoginForm from './components/LoginForm';
import SignupForm from './components/SignupForm';
import FeedingForm from './components/FeedingForm';
import FoodForm from './components/FoodForm';
import SummaryDashboard from './components/SummaryDashboard';

const App: React.FC = () => {
  const token = localStorage.getItem('token');
  const babyId = 1;

  if (!token) {
    return (
      <BrowserRouter>
        <Routes>
          <Route path="/signup" element={<SignupForm />} />
          <Route path="/*" element={<LoginForm />} />
        </Routes>
      </BrowserRouter>
    );
  }

  return (
    <div>
      <h1>Baby Tracker</h1>
      <FeedingForm />
      <FoodForm />
      <SummaryDashboard babyId={babyId} />
    </div>
  );
};

export default App;
