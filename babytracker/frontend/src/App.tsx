import React from 'react';
import FeedingForm from './components/FeedingForm';
import FoodForm from './components/FoodForm';
import SummaryDashboard from './components/SummaryDashboard';

const App: React.FC = () => {
  const babyId = 1; // Hardcoded for now

  return (
    <div>
      <h1>Baby Tracker</h1>
      <FeedingForm babyId={babyId} />
      <FoodForm />
      <SummaryDashboard babyId={babyId} />
    </div>
  );
};

export default App;
