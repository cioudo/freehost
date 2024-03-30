import streamlit as st
import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def execute_code(code):
    try:
        exec(code)
    except Exception as e:
        st.error(f"An error occurred: {e}")

def main():
    st.title("Code Executor")

    code = st.text_area("Enter your Python code here:")

    if st.button("Execute"):
        # Install required packages dynamically
        packages = []
        for line in code.split('\n'):
            if line.startswith("import"):
                packages.extend(line.split()[1:])
        for package in packages:
            install_package(package)

        execute_code(code)

if __name__ == "__main__":
    main()
