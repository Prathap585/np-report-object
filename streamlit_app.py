import streamlit as st
from twilio.rest import Client

st.title("Automated Call App")

# Get user input
phone_number = st.text_input("Enter phone number to call (e.g., +1234567890):")
message = st.text_area("Enter the message to be spoken:")

if st.button("Make Call"):
   # Twilio credentials
   account_sid = "AC010dcac2f5e8fb73760141f4c1dc8024"
   auth_token = "932822d20040fde88ee2b68d43ae69f9"

   # Initialize Twilio client
   client = Client(account_sid, auth_token)

   try:
      call = client.calls.create(twiml='<Response><Say voice="alice">' + message + '</Say></Response>',to=phone_number,from_='+1 919 998 6768',record=True)
      st.success("Call initiated successfully!")
   except Exception as e:
      st.error(f"Error making call: {e}")
