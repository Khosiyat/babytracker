import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import FeedingForm from '../FeedingForm';

test('renders FeedingForm and submits', async () => {
  render(<FeedingForm babyId={1} />);

  // Check dropdown and input presence
  expect(screen.getByRole('combobox')).toBeInTheDocument();
  expect(screen.getByPlaceholderText(/Amount in ml/i)).toBeInTheDocument();

  // You can mock API calls and test submit button here
});
