import React, { useState } from 'react';
import { addCustomFoodItem } from '../api';

const FoodForm: React.FC = () => {
    const [name, setName] = useState('');
    const [calories, setCalories] = useState('');
    const [protein, setProtein] = useState('');
  
    const userId = parseInt(localStorage.getItem('userId') || '1');
  
    const handleSubmit = async (e: React.FormEvent) => {
      e.preventDefault();
      await addCustomFoodItem({
        name,
        calories_per_100ml: parseFloat(calories),
        protein_per_100ml: parseFloat(protein),
        is_custom: true,
        created_by: userId,
      });
      alert('Custom food added!');
      setName('');
      setCalories('');
      setProtein('');
    };
  
    ...
  };
  
  return (
    <form onSubmit={handleSubmit}>
      <input placeholder="Food Name" value={name} onChange={e => setName(e.target.value)} required />
      <input
        type="number"
        placeholder="Calories per 100ml"
        value={calories}
        onChange={e => setCalories(e.target.value)}
        required
      />
      <input
        type="number"
        placeholder="Protein per 100ml"
        value={protein}
        onChange={e => setProtein(e.target.value)}
        required
      />
      <button type="submit">Add Custom Food</button>
    </form>
  );
};

export default FoodForm;
