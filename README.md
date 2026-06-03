# 💪 AI Gym & Fitness Assistant

**A comprehensive AI-powered fitness platform with MediaPipe pose detection, Gemini AI, real-time IoT monitoring, and advanced analytics.**

## 🎯 Quick Start (5 minutes)

### Prerequisites
- Node.js 18+
- Python 3.10+
- MongoDB (local or Docker)
- Firebase Project
- Gemini API Key

### 1️⃣ Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your credentials
uvicorn app.main:app --reload
```
✅ Backend runs on http://localhost:8000

### 2️⃣ Frontend Setup
```bash
cd frontend
npm install
cp .env.example .env
# Edit .env with Firebase credentials
npm run dev
```
✅ Frontend runs on http://localhost:5173

### 3️⃣ Database & IoT (Docker)
```bash
docker-compose up -d
```
✅ MongoDB: localhost:27017 | MQTT: localhost:1883

## 🧪 Verify Everything Works

```bash
# 1. Health check
curl http://localhost:8000/health

# 2. Calculate diet
curl -X POST http://localhost:8000/api/diet/calculate \
  -H "Content-Type: application/json" \
  -d '{
    "uid": "test-user",
    "age": 25,
    "gender": "male",
    "height": 175,
    "weight": 75,
    "activity_level": "moderate",
    "goal": "maintenance"
  }'
```

## 📋 Features (PHASE 1 ✅)

✅ AI Dietician - BMI, calorie, macro calculation
✅ Virtual Gym Buddy - Gemini AI chatbot
✅ Habit Tracker - Logistic Regression ML
✅ Gym Recommender - Location & budget filtering
✅ Analytics Dashboard - Performance scores
✅ Smart Gym IoT - MQTT sensors (simulated)
✅ AI Gym Trainer - Camera + MediaPipe skeleton
✅ Firebase Auth - Google login
✅ MongoDB persistence - All data stored
✅ AWS S3 ready - With local fallback

## 🏗️ Architecture

```
React Frontend (Vite) ←→ FastAPI Backend (Async)
                             ↓
                    MongoDB + Firebase Auth
                             ↓
                    ML Pipeline (TensorFlow, MediaPipe, Scikit-learn)
                             ↓
                    Gemini API + MQTT + AWS S3
```

## 🔌 API Endpoints (30+ endpoints)

See full endpoint list in PROJECT_ROADMAP.md

## 🧬 12 Technologies Used

- ✅ React.js
- ✅ FastAPI
- ✅ MongoDB
- ✅ Firebase Auth
- ✅ TensorFlow
- ✅ MediaPipe
- ✅ Scikit-learn
- ✅ MQTT
- ✅ Gemini API
- ✅ AWS S3
- ✅ Plotly.js
- ✅ D3.js

## 📁 Project Structure

```
ai-gym-fitness-assistant/
├── backend/
│   ├── app/
│   │   ├── api/ (8 modules)
│   │   ├── ml/ (4 ML files)
│   │   ├── mqtt/ (2 files)
│   │   ├── schemas/
│   │   ├── utils/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── database.py
│   │   └── firebase_config.py
│   ├── requirements.txt
│   ├── .env.example
│
├── frontend/
│   ├── src/
│   │   ├── pages/ (10 React pages)
│   │   ├── components/ (5 reusable components)
│   │   ├── utils/ (Firebase, API, WebSocket)
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   ├── .env.example
│
├── docker-compose.yml
├── PROJECT_ROADMAP.md
└── .gitignore
```

---

**Status**: ✅ PHASE 1 Complete | Ready for PHASE 2 (Core AI Modules)