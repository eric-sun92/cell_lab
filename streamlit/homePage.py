import streamlit as st

def home():
    # Page Title
    st.title("Home Page")
    st.markdown(
        """
        <style>
        .main-title {
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .sub-title {
            font-size: 24px;
            font-weight: bold;
            margin-top: 20px;
            margin-bottom: 10px;
        }
        .section-content {
            font-size: 18px;
            margin-bottom: 20px;
        }
        .banner-image {
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            max-width: 100%;
            height: auto;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Page Content
    # st.markdown("<div class='main-title'>Gupta Lab - Yale School of Medicine</div>", unsafe_allow_html=True)

    st.markdown("<div class='sub-title'>Research Focus</div>", unsafe_allow_html=True)
    st.write("""The local membrane environment plays a critical role in regulating all aspects of the biology of membrane proteins (MPs), from their assembly to functional activation, to degradation. 
             Gold standard” detergent based MP solubilization strategies completely disrupt this native bilayer-environment. This leads to a fundamental gap in our understanding of how nanoscale molecular organization around target 
             MPs regulates their ability to conjure a cellular response. Addressing this, combining polymer chemistry with quantitative proteomics, we have developed a quantitative guide for spatially-resolved extraction for more than 
             2100 MPs into native-nanodiscs. These nanodiscs are of tunable diameter between 8-20 nm and allow for direct extraction from the endogenous membrane while maintaining that native membrane environment. Here we present that 
             guide to native extraction  in an easily searchable format with the ability to search for single proteins of interest or networks of proteins. Searching for your protein(s) of interest will yield the preferred condition for 
             optimal native extraction for that  protein of interest serving as a starting point for structural and biochemical studies.
             """)

    st.markdown("<div class='sub-title'>Further Info</div>", unsafe_allow_html=True)
    st.write("For further information, our research paper will be published in the near future.")

    from PIL import Image

    image = Image.open('streamlit/your_banner_image.jpg')
    
    st.markdown("---")
    st.image(image)
    st.write("© 2023 Yale School of Medicine. All rights reserved.")