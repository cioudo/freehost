import streamlit as st
import execnet

def execute_code(code):
    try:
        # Create a gateway to the Python interpreter
        gateway = execnet.makegateway()

        # Execute the Python code dynamically
        channel = gateway.remote_exec(code)
        result = channel.receive()

        st.success(f"Code executed successfully. Result: {result}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def main():
    st.title("Dynamic Code Executor")

    code = st.text_area("Enter your Python code here:")

    if st.button("Execute"):
        execute_code(code)

if __name__ == "__main__":
    main()
