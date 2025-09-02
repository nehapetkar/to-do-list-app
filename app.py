import streamlit as st

# Title
st.title("📝 To-Do List App")

# Initialize session state for tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Add a new task
with st.form("add_task", clear_on_submit=True):
    new_task = st.text_input("Add a new task:")
    submitted = st.form_submit_button("Add")
    if submitted and new_task.strip():
        st.session_state.tasks.append({"task": new_task, "done": False})

# Display tasks
st.subheader("Your Tasks")
if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([0.1, 0.9])
        with col1:
            done = st.checkbox("", value=task["done"], key=f"done_{i}")
            st.session_state.tasks[i]["done"] = done
        with col2:
            if task["done"]:
                st.markdown(f"~~{task['task']}~~ ✅")
            else:
                st.write(task["task"])
else:
    st.info("No tasks yet! Add one above.")

# Clear completed tasks
if st.button("🗑️ Clear Completed Tasks"):
    st.session_state.tasks = [t for t in st.session_state.tasks if not t["done"]]
