import streamlit as st

def execute_code(code):
    try:
        global_vars = {}
        local_vars = {}
        exec(code, global_vars, local_vars)
        # Print out any variables defined in the local namespace
        for var_name, var_value in local_vars.items():
            st.write(f"{var_name}: {var_value}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def main():
    st.title("Code Executor")

    code = st.text_area("Enter your Python code here:")

    if st.button("Execute"):
        execute_code(code)

if __name__ == "__main__":
    main()
