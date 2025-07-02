import streamlit as st
import requests
import pandas as pd



BASE_URL = "http://127.0.0.1:8000"

st.title("FastAPI Task Dashboard")

# Refresh Logic
if "refresh_trigger" not in st.session_state:
    st.session_state.refresh_trigger = False

def refresh_tasks():
    st.session_state.refresh_trigger = not st.session_state.refresh_trigger

#Task List Section

st.subheader("Current Task")

if st.button("Refresh"):
    refresh_tasks()

#Fetch and Display task

response = requests.get(f"{BASE_URL}/tasks/")
if response.status_code == 200:
    tasks = response.json()
    if tasks:
        df =pd.DataFrame(tasks)[["id","title","description","completed"]]
        st.dataframe(df,use_container_width=True)
    else:
        st.info("No tasks Avaialable")
else: 
    st.error("Failed to fetch task")


#  Create a new task
st.subheader("Create New Task")
title = st.text_input("Title")
description = st.text_area("Description")

if st.button("Create Task"):
    if title.strip() == "":
        st.warning("Title cannot be empty.")
    else:
        data = {"title": title, "description": description}
        response = requests.post(f"{BASE_URL}/tasks/", json=data)
        if response.status_code == 201:
            st.rerun()
            st.success("Task created successfully. Please refresh to see the update.")
        else:
            st.error(f"Error: {response.text}")

#  Update an existing task
st.subheader("Update Task")
task_id = st.number_input("Task ID to Update", min_value=0, step=1)
new_title = st.text_input("New Title", key="update_title")
new_description = st.text_area("New Description", key="update_desc")
completed = st.checkbox("Completed")

if st.button("Update Task"):
    update_data = {
        "title": new_title,
        "description": new_description,
        "completed": completed
    }
    response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=update_data)
    if response.status_code == 200:
        st.rerun()
        st.success("Task updated successfully. Please refresh to see the update.")
    else:
        st.error(f"Error: {response.text}")

#  Delete a task
st.subheader("Delete Task")
delete_id = st.number_input("Task ID to Delete", min_value=0, step=1, key="delete")

if st.button("Delete Task"):
    response = requests.delete(f"{BASE_URL}/tasks/{delete_id}")
    
    if response.status_code == 200:
        st.rerun()

        st.success("Task deleted successfully. Please refresh to see the update.")
    else:
        st.error(f"Error: {response.text}")