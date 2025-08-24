import React, { useEffect, useState } from 'react';
import { fetchFoodItems, logFeeding } from '../api';

interface Props {
  babyId: number;
}

const FeedingForm: React.FC<Props> = ({ babyId }) => {
  const [foodItems, setFoodItems] = useState([]);
  const [amount, setAmount] = useState('');
  const [foodId, setFoodId] = useState('');

  useEffect(() => {
    fetchFoodItems().then(res => setFoodItems(res.data));
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    await logFeeding({
      baby: babyId,
      caregiver: 1, // Hardcoded; replace with logged-in user's ID
      food_item: foodId,
      amount_ml: parseFloat(amount),
    });
    alert('Feeding logged!');
    setAmount('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <select onChange={e => setFoodId(e.target.value)} value={foodId} required>
        <option value="">Select Food</option>
        {foodItems.map((item: any) => (
          <option key={item.id} value={item.id}>
            {item.name}
          </option>
        ))}
      </select>
      <input
        type="number"
        placeholder="Amount in ml"
        value={amount}
        onChange={e => setAmount(e.target.value)}
        required
      />
      <button type="submit">Log Feeding</button>
    </form>
  );
};

export default FeedingForm;
