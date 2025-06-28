# Flask React Universal Starter

A turnkey, full-stack starter template for modern web applications. This project is designed to support three deployment strategies (the "evolutionary path") without requiring changes to the core application code:

1. **Local Development:** Run Flask and React separately for fast iteration and debugging.
2. **Containerized Monolith:** Build and run the entire stack in a single Docker container for production simulation or deployment.
3. **Composable Microservices:** Easily split frontend and backend into separate containers/services if needed in the future.

## Features
- **Backend:** Python, Flask, Gunicorn
- **Frontend:** React (Create React App)
- **Containerization:** Docker, Docker Compose, Nginx
- **VS Code:** Pre-configured debugging and tasks for a seamless developer experience
- **Source Control:** Proper `.gitignore` at both root and frontend levels

## Getting Started

### Local Development
1. **Install dependencies:**
   - Python 3.11+
   - Node.js 18+
2. **Backend:**
   ```sh
   cd backend
   pip install -r requirements.txt
   python main.py
   ```
3. **Frontend:**
   ```sh
   cd frontend
   npm install
   npm start
   ```
4. Open [http://localhost:3000](http://localhost:3000) in your browser.

### Docker (Production Simulation)
1. **Build and run with Docker Compose:**
   ```sh
   docker-compose up --build
   ```
2. Open [http://localhost:8080](http://localhost:8080) in your browser.

## Debugging in VS Code
- Use the **🚀 Launch ALL** compound configuration to start both backend and frontend debuggers.
- The `.vscode/tasks.json` ensures the frontend starts before debugging.

## Evolutionary Path
- **Monolith:** The default Dockerfile builds a single image for both frontend and backend.
- **Split Services:** You can later separate the frontend and backend into their own containers/services with minimal changes.

## File Structure
```
/flask-react-universal-starter
├── .gitignore
├── .vscode/
│   ├── launch.json
│   └── tasks.json
├── backend/
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   ├── .gitignore
│   ├── public/
│   │   └── index.html
│   └── src/
│       ├── App.css
│       └── App.js
├── Dockerfile
├── docker-compose.yml
├── nginx.conf
├── start.sh
└── README.md
```

---

**Happy coding!**
