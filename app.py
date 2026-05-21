import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("Persona Multiplier")

st.caption("AI-powered recruiter outreach persona generator")

story = st.text_area("Paste the original story here:")

target = st.text_input("Target person or company:")

career_context = st.text_area(
    "Paste recipient LinkedIn About section or recent activity:"
)

if st.button("Generate 3 versions"):

    with st.spinner("Generating persona versions..."):

        # Direct Headhunter
        direct_prompt = f"""
Rewrite this LinkedIn-style story in the voice of a direct headhunter.

Keep it sharp, commercial and concise.
Keep the response under 120 words.
Write in a LinkedIn-friendly format.
Avoid sounding overly AI-generated.

Target:
{target}

Story:
{story}

Recipient career context:
{career_context}

Use this context to stitch one personalised sentence naturally into the middle of the story.
Do not invent career details.

Include one personalized sentence that references the target naturally.
"""

        direct_response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": direct_prompt}
            ]
        )

        # Empathetic Coach
        empathetic_prompt = f"""
Rewrite this LinkedIn-style story in the voice of an empathetic career coach.

Make it supportive and human.
Keep the response under 120 words.
Write in a LinkedIn-friendly format.
Avoid sounding overly AI-generated.

Target:
{target}

Story:
{story}

Recipient career context:
{career_context}

Use this context to stitch one personalised sentence naturally into the middle of the story.
Do not invent career details.
Include one personalized sentence that references the target naturally.
"""

        empathetic_response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": empathetic_prompt}
            ]
        )

        # Trusted Advisor
        advisor_prompt = f"""
Rewrite this LinkedIn-style story in the voice of a trusted advisor.

Make it insightful and thoughtful.
Keep the response under 120 words.
Write in a LinkedIn-friendly format.
Avoid sounding overly AI-generated.

Target:
{target}

Story:
{story}

Recipient career context:
{career_context}

Use this context to stitch one personalised sentence naturally into the middle of the story.
Do not invent career details.
Include one personalized sentence that references the target naturally.
"""

        advisor_response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": advisor_prompt}
            ]
        )

    # Display outputs
    st.subheader("Direct Headhunter")
    st.text_area(
        "Direct Output",
        direct_response.choices[0].message.content,
        height=200
    )

    st.subheader("Empathetic Coach")
    st.text_area(
        "Coach Output",
        empathetic_response.choices[0].message.content,
        height=200
    )

    st.subheader("Trusted Advisor")
    st.text_area(
        "Advisor Output",
        advisor_response.choices[0].message.content,
        height=200
    )