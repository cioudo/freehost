import streamlit as st
import execjs

def execute_code(code):
    try:
        # Use execjs to execute Python code dynamically
        ctx = execjs.compile(code)
        result = ctx.eval("executed_code()")
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
