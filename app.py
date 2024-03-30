import streamlit as st

def execute_code(code):
    namespace = {}
    try:
        exec(code, namespace)
        return namespace
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

def main():
    st.title("Code Executor")

    code = st.text_area("Enter your Python code here:")

    if st.button("Execute"):
        namespace = execute_code(code)
        if namespace:
            for var_name, var_value in namespace.items():
                st.write(f"{var_name}: {var_value}")

if __name__ == "__main__":
    main()
