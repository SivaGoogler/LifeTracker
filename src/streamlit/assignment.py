import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import random

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Life Tracker", layout="wide")

# ---------------- SESSION STATE ----------------
if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "learning" not in st.session_state:
    st.session_state.learning = []

if "notes" not in st.session_state:
    st.session_state.notes = []

# ---------------- SIDEBAR ----------------
st.sidebar.title("📊 Life Tracker")
page = st.sidebar.radio("Navigate", [
    "🏠 Dashboard",
    "📝 Tasks",
    "📚 Learning",
    "📊 Analytics",
    "🧠 Reflection"
])

# ---------------- DASHBOARD ----------------
if page == "🏠 Dashboard":
    st.title("🏠 Dashboard")

    today = datetime.now().date()

    today_tasks = [t for t in st.session_state.tasks if t["date"] == today]
    completed = sum(t["done"] for t in today_tasks)
    total = len(today_tasks)

    score = int((completed / max(total, 1)) * 100)

    st.subheader("📌 Today Overview")

    col1, col2, col3 = st.columns(3)
    col1.metric("Tasks", total)
    col2.metric("Completed", completed)
    col3.metric("Score", f"{score}%")

    st.progress(completed / max(total, 1))

    if score == 100 and total > 0:
        st.success("🔥 Perfect Day! Keep the streak going!")

    quotes = [
        "Consistency beats motivation 🔥",
        "Small wins matter 💪",
        "Keep going 🚀",
        "You are building your future 🧠"
    ]
    st.info(random.choice(quotes))

# ---------------- TASKS ----------------
elif page == "📝 Tasks":
    st.title("📝 Task Manager")

    task = st.text_input("Add Task")

    if st.button("➕ Add Task"):
        if task:
            st.session_state.tasks.append({
                "task": task,
                "done": False,
                "date": datetime.now().date()
            })

    for i, t in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([0.8, 0.2])

        with col1:
            checked = st.checkbox(t["task"], t["done"], key=i)
            st.session_state.tasks[i]["done"] = checked

        with col2:
            if st.button("❌", key=f"del{i}"):
                st.session_state.tasks.pop(i)
                st.rerun()

# ---------------- LEARNING ----------------
elif page == "📚 Learning":
    st.title("📚 What I Learned Today")

    learn = st.text_input("New Learning")

    if st.button("➕ Add Learning"):
        if learn:
            st.session_state.learning.append({
                "text": learn,
                "date": datetime.now().date()
            })

    if st.session_state.learning:
        for l in st.session_state.learning:
            st.write(f"📌 {l['text']} ({l['date']})")
    else:
        st.info("No learning added yet")

# ---------------- ANALYTICS ----------------
elif page == "📊 Analytics":
    st.title("📊 Productivity Analytics")

    if st.session_state.tasks:
        df = pd.DataFrame(st.session_state.tasks)
        df["date"] = pd.to_datetime(df["date"])

        daily = df.groupby("date")["done"].sum()

        col1, col2, col3 = st.columns(3)

        # ---------- BAR CHART ----------
        with col1:
            st.subheader("📅 Daily")
            fig1, ax1 = plt.subplots(figsize=(4, 3))
            daily.plot(kind="bar", ax=ax1)
            ax1.set_ylabel("Done")
            ax1.set_xlabel("")
            st.pyplot(fig1)

        # ---------- PIE CHART ----------
        with col2:
            st.subheader("📌 Status")
            completed = df["done"].sum()
            pending = len(df) - completed

            fig2, ax2 = plt.subplots(figsize=(4, 3))
            ax2.pie(
                [completed, pending],
                labels=["Done", "Pending"],
                autopct="%1.0f%%"
            )
            st.pyplot(fig2)

        # ---------- AREA CHART ----------
        with col3:
            st.subheader("📈 Trend")
            st.area_chart(daily)

    else:
        st.warning("No data to analyze yet!")

# ---------------- REFLECTION ----------------
elif page == "🧠 Reflection":
    st.title("🧠 Daily Reflection")

    note = st.text_area("Write your thoughts...")

    if st.button("💾 Save Note"):
        if note:
            st.session_state.notes.append({
                "text": note,
                "date": datetime.now().date()
            })

    if st.session_state.notes:
        for n in st.session_state.notes:
            st.write(f"📝 {n['text']} ({n['date']})")
    else:
        st.info("No reflections yet")