import streamlit as st
from PIL import Image
import ollama
import traceback

# Set up the Streamlit app
st.set_page_config(
    page_title="Passport Data Extraction",
    page_icon="🛂",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and description
st.title("Passport Data Extraction")
st.subheader("Extract all structured data from passport images")

# Add horizontal rule for separation
st.markdown("---")

# Initialize session state
if 'ocr_result' not in st.session_state:
    st.session_state['ocr_result'] = None
if 'passport_type' not in st.session_state:
    st.session_state['passport_type'] = "Romanian"

# Sidebar for uploading files and passport type selection
with st.sidebar:
    st.header("Settings")
    st.markdown("### Choose Passport Type:")
    if st.button("Romanian Passport"):
        st.session_state['passport_type'] = "Romanian"
    if st.button("Pakistani Passport"):
        st.session_state['passport_type'] = "Pakistani"
    
    st.markdown(f"**Current Passport Type:** {st.session_state['passport_type']}")

    st.header("Upload Image")
    st.markdown("Please upload a **passport image**:")
    uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])

    # Display uploaded image in sidebar
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

# Main content
if uploaded_file is not None:
    # Button to extract data
    if st.button("Extract Data"):
        with st.spinner("Processing the image..."):
            try:
                # Define fields based on passport type
                if st.session_state['passport_type'] == "Romanian":
                    fields = [
                        "Seria", "NR", "CNP", "Nume Familie/Last name", "Prenume/First name",
                        "Sex", "Loc nastere", "Domiciliu", "Emis de", "Valabilitate"
                    ]
                else:  # Pakistani Passport
                    fields = [
                        "country code ", "Passport Number", "SurName" "Name", "Date of Birth", "Citizenship Number", "Sex"
                        "Place of Birth", "Father's Name", "Date of Issue", "Date of Expiry", "Issuing Authority", "Tracking Number", "Booklet Number"
                    ]

                # Define prompt
                fields_list = ''.join([f'- **{field}**: [Value]\n' for field in fields])  # Create fields as a formatted string

                prompt = f"""
                    Extract all available text from the provided {st.session_state['passport_type']} passport image.
                    Focus on the following fields but include all readable text exactly as it appears make sure you read all the given fields data accurately because it is a passport data:

                    {', '.join(fields)}

                    Return the results in the following structured Markdown format:

                    ```markdown
                    {fields_list}
                    ```

                    Do not omit or filter any data. If a field is not found, write `Not Found`.
                """



                # Use Ollama to extract data
                response = ollama.chat(
                    model='llama3.2-vision',
                    messages=[{
                        'role': 'user',
                        'content': prompt,
                        'images': [uploaded_file.getvalue()]
                    }]
                )

                # Save the result to session state
                st.session_state['ocr_result'] = response.message.content

            except Exception as e:
                st.error(f"Error processing image: {str(e)}")
                st.text(traceback.format_exc())

    # Display extracted data if available
    if st.session_state['ocr_result']:
        st.markdown(f"### Extracted {st.session_state['passport_type']} Passport Data")
        col1, col2 = st.columns(2)

        # Show uploaded image in the first column
        with col1:
            st.image(image, caption="Uploaded Image", use_container_width=True)

        # Show extracted data in the second column
        with col2:
            st.markdown("#### Extracted Data")
            extracted_lines = st.session_state['ocr_result'].splitlines()
            for line in extracted_lines:
                st.markdown(line)

else:
    st.info("Upload an image to extract passport data.")
