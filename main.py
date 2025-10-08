import streamlit as st

# Use session_state to persist tasks between reruns
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

st.set_page_config(layout="wide")
st.title("!TaskIt")

new_task = st.text_input('Enter your Task')
if st.button('Add'):
    if new_task:
        st.session_state.tasks.append(new_task)
        st.success(f"Task added: {new_task}")

st.write("Tasks:")
for task in st.session_state.tasks:
    st.write("- " + task)

st.sidebar.header('Analyze your tasks!')
st.sidebar.caption('*Early Stage App, Sidebar to be created at a later stage to add more functionalities')
selected_model = st.sidebar.selectbox('To be created', ['Plot your Progress', 'Focus Mode'])
