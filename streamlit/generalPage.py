import streamlit as st

def general():
    st.title("General Methods")

    st.header("MAP extraction")
    st.write(
        """HEK293 cells were grown to 90% confluency and harvested using trypsin. 
        Cells were pelleted and washed 3x with PBS to remove any residual trypsin or media. 
        Nitrogen cavitation at 750 PSI for 10 minutes was used to lyse the cells. A “soft” 
        spin of 4000xg was conducted to pellet debris, and a “hard” spin of 200,000xg was 
        used to collect a membrane fraction. For each solubilization, 25% of a 10cm plate 
        was used, or membrane from approximately 2 million cells. Membranes were directly 
        resuspended in buffer containing the various MAPs in percentages between 1-1.5%, 
        homogenized, and incubated with rotation at 4C for 2 hours. Post-extraction, a 
        200,000xg centrifugation spin was conducted to remove insoluble material. The 
        supernatant, containing MAPs was collected and prepared for proteomic analysis. 
        """
    )

    st.header("Sample Prep for Proteomics")
    st.write(
        """Soluble MAP discs were subjected to MTBE extraction to effectively separate protein
        from lipid and metabolites. A basic wash was conducted on the protein pellet to 
        remove polymer prior to digestion. The pellet was dried, resuspended in 10M urea, 
        and boiled at 65C for 30 minutes. Standard reduction, alkylation, and digestion 
        protocols were used. The peptides were subjected to standard desalting procedures 
        using SepPak C18 cartridges, and the peptides were quantified using a BCA assay.
        """
    )

    st.header("LC-MS")
    st.write(
        """Proteomic analysis was conducted on a Vanquish Neo nLC interfaced with an Orbitrap 
        Eclipse (Thermo Fisher Scientific) using a home-packed C18 column. For each sample, 
        equal amounts of peptide were run over a 75-minute gradient in a water/acetonitrile 
        buffer system using a DDA approach.
        """)

    st.header("Proteomic Analysis")
    st.write(
        """MaxQuant was used to ID peptides and perform label-free quantitation for each 
        sample. Membrane and membrane associated proteins were identified using Uniprot 
        repositories along with extensive hand-curated libraries.
        """
)
    
    # Footer
    from PIL import Image

    image = Image.open('streamlit/your_banner_image.jpg')
    
    st.markdown("---")
    st.image(image)
    st.write("© 2023 Yale School of Medicine. All rights reserved.")