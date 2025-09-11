import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Bar } from 'react-chartjs-2';

interface NutrientData {
  calories: number;
  protein: number;
  fat: number;
  carbs: number;
  vitamin_a: number;
  vitamin_c: number;
  calories_pct: number;
  protein_pct: number;
  fat_pct: number;
  carbs_pct: number;
  vitamin_a_pct: number;
  vitamin_c_pct: number;
}

interface Props {
  babyId: number;
  date: string; // format YYYY-MM-DD
}

const NutrientDashboard: React.FC<Props> = ({ babyId, date }) => {
  const [data, setData] = useState<NutrientData | null>(null);

  useEffect(() => {
    axios.get(`/api/baby/${babyId}/daily-summary?date=${date}`)
      .then(res => setData(res.data))
      .catch(console.error);
  }, [babyId, date]);

  if (!data) return <div>Loading...</div>;

  const nutrients = ['calories', 'protein', 'fat', 'carbs', 'vitamin_a', 'vitamin_c'] as const;

  const chartData = {
    labels: nutrients.map(n => n.toUpperCase()),
    datasets: [
      {
        label: '% of Daily Goal',
        data: nutrients.map(n => data[`${n}_pct`]),
        backgroundColor: 'rgba(75,192,192,0.6)',
      },
      {
        label: 'Consumed',
        data: nutrients.map(n => data[n]),
        backgroundColor: 'rgba(153,102,255,0.6)',
        yAxisID: 'y1',
      },
    ],
  };

  const options = {
    scales: {
      y: { beginAtZero: true, position: 'left', title: { display: true, text: 'Amount' }},
      y1: { beginAtZero: true, position: 'right', grid: { drawOnChartArea: false }, title: { display: true, text: '%' }},
    }
  };

  return (
    <div>
      <h2>Nutrient Intake Summary ({date})</h2>
      <Bar data={chartData} options={options} />
    </div>
  );
};

export default NutrientDashboard;
