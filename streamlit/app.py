import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

local_css("style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

label_text = "<div class='custom-label'>What gene name would you like to search for? (Or enter 'done') to finish...</div>"
st.markdown(label_text, unsafe_allow_html=True)

selected = st.text_input("", "Search...")



# selected == gene 
# need to connect these somehow

# then add a done button to signal done

