import { render, screen } from '@testing-library/react';
import App from './App';

test('renders the message from the backend', async () => {
  // Mock the fetch function
  global.fetch = jest.fn(() =>
    Promise.resolve({
      json: () => Promise.resolve({ message: 'Hello from Mocked Lambda!' }),
    })
  );

  render(<App />);

  // Wait for the message to be displayed
  const messageElement = await screen.findByText(/Hello from Mocked Lambda!/i);
  expect(messageElement).toBeInTheDocument();

  // Clean up the mock
  global.fetch.mockClear();
  delete global.fetch;
});
