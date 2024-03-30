import streamlit as st
import os

def install_package(package):
    os.system(f"pip install -U {package}")

def execute_code(code, requirements):
    try:
        # Install required packages
        for package in requirements.split('\n'):
            if package.strip():
                install_package(package.strip())

        # Execute the code
        exec(code)
    except Exception as e:
        st.error(f"An error occurred: {e}")

def main():
    st.title("Code Executor")

    code = st.text_area("Enter your Python code here:")
    requirements = st.text_area("Enter required packages (one per line):")

    if st.button("Execute"):
        execute_code(code, requirements)

if __name__ == "__main__":
    main()
