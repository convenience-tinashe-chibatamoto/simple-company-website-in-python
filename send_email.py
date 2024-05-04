import smtplib, ssl
import os
import streamlit as st
import pandas

df = pandas.read_csv("topics.csv")

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "conveniencechibatamoto@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "conveniencechibatamoto@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address")
    option = st.selectbox(
        'What topic do you want to discuss today?',
        df["topic"]
    )
    raw_message = st.text_area("Text")
    message = f"""
Subject: New email from {user_email}
From: {user_email}
Topic: {option}
{raw_message}
"""
    button = st.form_submit_button("Submit")

    if button:
        send_email(message)
        st.info("Your email was sent successfully!")
