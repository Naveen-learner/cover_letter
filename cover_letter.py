import streamlit as st
import random
import datetime

# Define function to generate cover letter
def generate_cover_letter(name, email, mobile, position, company, hr_name, city, state,field):
    # Add date to the cover letter
    today = datetime.date.today().strftime("%d %B %Y")
    # Define cover letter templates
    templates = [

        "\n\n{name:>65}\n{email:>65}\n{mobile:>65}\n"+today+"\n{company}\n{hr_name}\n{city}\n{state}\n\nSubject: Application for the {position} position at {company}\n\nDear {hr_name},\n\nI am excited to apply for the position of {position} at {company} located in {city}, {state}. With a Master's degree in Renewable Energy Systems and experience in data science and automation, I am confident that I possess the necessary skills and qualifications to excel in this role.\n\nThank you for considering my application. I am excited about the opportunity to contribute to {company} and am looking forward to discussing my qualifications in further detail.\n\nYours sincerely,\n\n{name}",
        
        "\n\n{name:>65}\n{email:>65}\n{mobile:>65}\n"+today+"\n{company}\n{hr_name}\n{city}\n{state}\n\nSubject: Application for the {position} position at {company}\n\nDear {hr_name},\n\nI am writing to express my interest in the {position} position at {company} located in {city}, {state}. I am confident that my experience in programming languages such as Python and SQL, as well as my ability to design and develop analytical algorithms and software, would enable me to make valuable contributions to the team at {company}. I also possess strong organizational and communication skills, which would allow me to collaborate effectively with team members and clients.\n\nThank you for considering my application. I am excited about the opportunity to contribute to {company} and am looking forward to discussing my qualifications in further detail.\n\nYours sincerely,\n\n{name}",
        
        "\n\n{name:>65}\n{email:>65}\n{mobile:>65}\n"+today+"\n{company}\n{hr_name}\n{city}\n{state}\n\nSubject: Application for the {position} position at {company}\n\nDear {hr_name},\n\nI am writing to express my interest in the {position} position at {company} located in {city}, {state}. With my extensive experience in {field}, I am confident that I possess the necessary skills and qualifications to excel in this role. I have a proven track record of success in and I am excited about the opportunity to bring my expertise to {company}.\n\nThank you for considering my application. I am excited about the opportunity to contribute to {company} and am looking forward to discussing my qualifications in further detail.\n\nYours sincerely,\n\n{name}"
    ]
    
    # Select a random template
    template = random.choice(templates)

    # Fill in the template with applicant and company details
    cover_letter = template.format(
        name=name,
        email=email,
        mobile=mobile,
        position=position,
        company=company,
        hr_name=hr_name,
        city=city,
        state=state,
        field=field
    )
    
    
    #cover_letter = cover_letter.format(date=today)
    # Add subject to the cover letter
    #cover_letter = f"\n\n{cover_letter}\n\nSubject: Application for the {position} position at {company}"
    
    # Add closing statement to the cover letter
    #closing_statement = "Thank you for considering my application. I am excited about the opportunity to contribute to {company} and am looking forward to discussing my qualifications in further detail."
    #closing_statement = closing_statement.format(company=company)
    
    # Add applicant name to the closing statement
    #closing_statement += f"\n\nYours sincerely,\n\n{name}"
    
    #cover_letter += closing_statement
    
    return cover_letter

# Define Streamlit app
def app():
    st.title("Cover Letter Generator")
    
    # Collect applicant details
    name = st.text_input("Name")
    email = st.text_input("Email")
    mobile = st.text_input("Mobile")
    
    # Collect job details
    position = st.text_input("Position Applying")
    company = st.text_input("Company Name")
    hr_name = st.text_input("HR Name")
    city = st.text_input("City")
    state = st.text_input("State/Country")
    field = st.text_input("field")
    
    # Generate cover letter when the button is clicked
    if st.button("Generate Cover Letter"):
        cover_letter = generate_cover_letter(name, email, mobile, position, company, hr_name, city, state,field)
        st.write(cover_letter)
        st.download_button(
            label="Download Cover Letter",
            data=cover_letter,
            file_name="cover_letter.docx",
            mime="application/docx"
        )

if __name__ == "__main__":
    app()