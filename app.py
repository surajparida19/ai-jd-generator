        padding: 10px 20px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background-color: #E9F1FA;
    }

    .stTextInput>div>input, .stTextArea>div>textarea {
        border-radius: 8px;
        padding: 10px;
        border: 1px solid #ccc;
    }
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# App Title
st.title("\u2708\ufe0f AI Job Description Generator")

# User Inputs
role_title = st.text_input("Enter the role title:")
seniority = st.selectbox("Select seniority level:", ["Junior", "Mid-level", "Senior", "Lead", "Executive"])
location = st.text_input("Enter the job location:")
responsibilities = st.text_area("Enter responsibilities (comma-separated):")

# Generate Formal Job Description Button
if st.button("Generate Formal JD"):
    if role_title and seniority and location:
        st.success("Generating your formal job description...")

        # Generate Formal JD using Gemini
        jd_text = generate_formal_jd(role_title, seniority, location, responsibilities)

        # Display Formal JD in rich text editor
        st.text_area("Your Formal Job Description:", jd_text, height=400)
    else:
        st.error("Please fill in all required details.")

# Generate Funky Job Description Button
if st.button("Generate Funky JD"):
    if role_title and seniority and location:
        st.success("Generating your funky job description...")

        # Generate Funky JD using Gemini
        jd_text = generate_fun_jd(role_title, seniority, location, responsibilities)

        # Display Funky JD in rich text editor
        st.text_area("Your Funky Job Description:", jd_text, height=400)
    else:
        st.error("Please fill in all required details.")