# MindMapAI ![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![Version](https://img.shields.io/badge/version-1.0.0-blue) ![License](https://img.shields.io/badge/license-MIT-yellowgreen)

## Project Description
MindMapAI is an innovative web application that leverages AI to assist users in creating and organizing their thoughts visually through mind maps. The application allows for real-time collaboration, making it ideal for teams and brainstorming sessions. Users can also integrate their mind maps with task management tools to streamline their workflow.

## Features
- 🤖 **AI-assisted mind mapping**: Users can create mind maps with suggestions from AI based on their input.
- 👥 **Collaborative editing**: Multiple users can work on the same mind map in real-time.
- 📤 **Export options**: Users can export their mind maps in various formats (PDF, image, text).
- 🔗 **Integration with task management tools**: Users can link tasks from their mind maps to popular task management applications.
- 📜 **Version history**: Users can view and revert to previous versions of their mind maps.

## Tech Stack
### Frontend
- 🌐 **Next.js**

### Backend
- ⚡ **FastAPI**
- 🧠 **LangChain**
- 🤖 **OpenAI**

### Database
- 🗄️ **PostgreSQL**

## Installation
To set up MindMapAI locally, follow these steps:

- Clone the repository
bash
git clone https://github.com/arun-kumar-codes/mindmapai
- Navigate to the project directory
bash
cd mindmapai
- Install the backend dependencies
bash
cd backend
pip install -r requirements.txt
- Install the frontend dependencies
bash
cd ../frontend
npm install
- Set up the PostgreSQL database and update the configuration
- Run the backend server
bash
cd ../backend
uvicorn main:app --reload
- Run the frontend development server
bash
cd ../frontend
npm run dev
## Usage
1. Open your browser and navigate to `http://localhost:3000`.
2. Create a new mind map or join an existing one.
3. Start adding your ideas and let the AI assist you in organizing them.
4. Collaborate with others in real-time and export your mind maps as needed.

## API Documentation
For detailed API documentation, please refer to the [API Documentation](https://github.com/arun-kumar-codes/mindmapai/wiki/API-Documentation).

## Testing
To run tests for the backend, follow these steps:

- Navigate to the backend directory
bash
cd backend
- Run the tests
bash
pytest
## Deployment
To deploy MindMapAI, follow these steps:

- Set up a production environment with PostgreSQL.
- Build the frontend for production
bash
cd frontend
npm run build
- Serve the frontend and backend using a production server like Gunicorn or Nginx.

## Contributing
We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.
