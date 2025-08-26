import React, { useEffect, useState } from 'react';
import { getBabySummary } from '../api';

interface Props {
  babyId: number;
}

const SummaryDashboard: React.FC = () => {
    const [summary, setSummary] = useState<any>(null);
    const babyId = parseInt(localStorage.getItem('babyId') || '1');
    const today = new Date().toISOString().split('T')[0];
  
    useEffect(() => {
      getBabySummary(babyId, today).then(res => setSummary(res.data));
    }, [babyId]);
    ...
  };
  

  if (!summary) return <p>Loading summary...</p>;

  const milkGoal = 1000; // 1L default
  const isGoalMet = summary.total_milk_ml >= milkGoal;

  return (
    <div>
      <h2>Today's Summary</h2>
      <p>Milk: {summary.total_milk_ml} ml</p>
      <p>Calories: {summary.total_calories} kcal</p>
      <p>Protein: {summary.total_protein} g</p>

      <h4>By Food Type:</h4>
      <ul>
        {Object.entries(summary.breakdown).map(([name, info]: any) => (
          <li key={name}>
            {name}: {info.amount_ml} ml ({info.calories} kcal)
          </li>
        ))}
      </ul>

      <div style={{ color: isGoalMet ? 'green' : 'red' }}>
        {isGoalMet ? '✅ Milk goal met!' : '⚠️ Not enough milk yet!'}
      </div>
    </div>
  );
};

export default SummaryDashboard;


