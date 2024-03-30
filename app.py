import streamlit as st

def execute_code(code):
    try:
        exec(code)
    except Exception as e:
        st.error(f"An error occurred: {e}")

def main():
    st.title("Code Executor")

    code = st.text_area("Enter your Python code here:")

    if st.button("Execute"):
        execute_code(code)

if __name__ == "__main__":
    main()
