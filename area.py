import streamlit as st

def total_area():
    st.image("logo1.png", use_container_width=True)
    st.title("Total Area Calculator")
    
    num_squares = st.number_input("Enter the number of squares:", min_value=1, step=1, format="%d")
    total = 0.0
    
    for i in range(int(num_squares)):
        st.subheader(f"Square {i+1}")
        a = st.number_input(f"Enter the length (a) for square {i+1}:", min_value=0.0, step=0.1, format="%.2f")
        b = st.number_input(f"Enter the width (b) for square {i+1}:", min_value=0.0, step=0.1, format="%.2f")
        total += a * b
    
    st.write(f"### The total area of all squares is: {total:.2f}")

if __name__ == "__main__":
    total_area()
