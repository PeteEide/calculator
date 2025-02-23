import streamlit as st

def total_area():
    st.image("logo1.png", use_container_width=True)
    st.title("Total Area Calculator")
    
    if "current_square" not in st.session_state:
        st.session_state.current_square = 0
    if "squares" not in st.session_state:
        st.session_state.squares = []
    
    num_squares = st.number_input("Enter the number of squares:", min_value=1, step=1, format="%d")
    
    if len(st.session_state.squares) < num_squares:
        st.session_state.squares = [None] * num_squares
    
    current_index = st.session_state.current_square
    
    st.subheader(f"Square {current_index + 1}")
    a = st.number_input("Enter the length (a):", min_value=0.0, step=0.1, format="%.2f", key=f"a_{current_index}")
    b = st.number_input("Enter the width (b):", min_value=0.0, step=0.1, format="%.2f", key=f"b_{current_index}")
    
    if st.button("Next"):
        st.session_state.squares[current_index] = (a, b)
        if current_index < num_squares - 1:
            st.session_state.current_square += 1
        
    if st.button("Back") and current_index > 0:
        st.session_state.current_square -= 1
    
    if current_index == num_squares - 1 and None not in st.session_state.squares:
        total = sum(a * b for a, b in st.session_state.squares)
        st.write(f"### The total area of all squares is: {total:.2f}")

if __name__ == "__main__":
    total_area()