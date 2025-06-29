import { render, screen, waitFor, fireEvent } from '@testing-library/react';
import App from './App';

// Mock fetch for /api/message
beforeEach(() => {
  global.fetch = jest.fn(() =>
    Promise.resolve({
      json: () => Promise.resolve({ message: 'Hello from Flask 2025-06-29!' })
    })
  );
});

afterEach(() => {
  jest.resetAllMocks();
});

test('renders message from backend in input after button click', async () => {
  render(<App />);
  const button = screen.getByText(/Get Message from Flask/i);
  fireEvent.click(button);
  await waitFor(() => {
    const input = screen.getByRole('textbox');
    expect(input.value).toMatch(/Hello from Flask/);
  });
});
