# LifeTracker

A comprehensive personal productivity and life tracking application built with Streamlit. Track your daily tasks, learning progress, and reflections to build better habits and achieve your goals.

## Features

### 🏠 Dashboard
- **Today's Overview**: View your daily task completion metrics and productivity score
- **Progress Tracking**: Visual progress bar showing completion percentage
- **Motivational Quotes**: Daily inspirational messages to keep you motivated
- **Perfect Day Recognition**: Celebrate when you complete all tasks for the day

### 📝 Task Manager
- **Add Tasks**: Easily add new tasks for the day
- **Mark Complete**: Check off completed tasks
- **Delete Tasks**: Remove tasks you no longer need
- **Daily Focus**: Tasks are organized by date for better time management

### 📚 Learning Tracker
- **Record Learnings**: Document what you learned each day
- **Knowledge Building**: Build a personal knowledge base over time
- **Date Tracking**: See when you learned specific things

### 📊 Analytics
- **Daily Productivity**: Bar chart showing tasks completed per day
- **Completion Status**: Pie chart visualizing done vs pending tasks
- **Trend Analysis**: Area chart showing productivity trends over time
- **Data-Driven Insights**: Make informed decisions about your habits

### 🧠 Daily Reflection
- **Thought Journaling**: Write daily reflections and thoughts
- **Personal Growth**: Track your mental and emotional progress
- **Date-Stamped Entries**: Keep a chronological record of your reflections

### 🎨 Additional Features
- **Theme Change**: Switch between light and dark themes for comfortable viewing
- **Re-run**: Manually refresh the application to update data and UI
- **Auto Re-run**: Automatic refresh functionality for real-time updates
- **Clear Cache**: Clear application cache to resolve performance issues
- **Print**: Print reports and summaries of your tracked data
- **Record Screen**: Screen recording capability for sharing progress or tutorials

## Screenshots

### Dashboard
![Dashboard Screenshot](src/images/Screenshot%202026-04-06%20at%201.09.24%20AM.png)

### Task Manager
![Task Manager Screenshot](src/images/Screenshot%202026-04-06%20at%201.09.35%20AM.png)

### Learning Tracker
![Learning Tracker Screenshot](src/images/Screenshot%202026-04-06%20at%201.09.43%20AM.png)

### Analytics
![Analytics Screenshot](src/images/Screenshot%202026-04-06%20at%201.09.50%20AM.png)

### Daily Reflection
![Reflection Screenshot](src/images/Screenshot%202026-04-06%20at%201.09.57%20AM.png)

## How to Run

### Prerequisites
- Python 3.7 or higher
- Required packages: streamlit, pandas, matplotlib

### Installation

1. Clone the repository:
```bash
git clone https://github.com/SivaGoogler/LifeTracker.git
cd LifeTracker
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

1. Navigate to the streamlit directory:
```bash
cd src/streamlit
```

2. Run the Streamlit app:
```bash
streamlit run assignment.py
```

3. Open your browser and go to the URL shown in the terminal (usually `http://localhost:8501`)

## Usage

- Use the sidebar to navigate between different sections
- Start by adding tasks in the Task Manager
- Track your learning in the Learning section
- View your progress in Analytics
- Reflect on your day in the Reflection section
- Check your daily overview on the Dashboard

## Data Storage

All data is stored in the browser session and will persist during your current session. Note that data will be lost when you close the browser or restart the app.
