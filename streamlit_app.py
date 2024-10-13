

import streamlit as st
from twilio.rest import Client

st.title("Automated Call App")

# Get user input
phone_number = st.text_input("Enter phone number to call (e.g., +1234567890):")
message = st.text_area("Enter the message to be spoken:")

if st.button("Make Call"):
   # Twilio credentials
   account_sid = "YOUR_TWILIO_ACCOUNT_SID" 
   auth_token = "YOUR_TWILIO_AUTH_TOKEN" 

   # Initialize Twilio client
   client = Client(account_sid, auth_token)

   try:
       call = client.calls.create(
           twiml='<Response><Say>' + message + '</Say></Response>',
           to=phone_number,
           from_="YOUR_TWILIO_PHONE_NUMBER" 
       )
       st.success("Call initiated successfully!")
   except Exception as e:
       st.error(f"Error making call: {e}")
