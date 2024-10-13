import streamlit as st
from twilio.rest import Client

st.title("Automated Call App")

# Get user input
phone_number = st.text_input("Enter phone number to call (e.g., +1234567890):")
message = st.text_area("Enter the message to be spoken:")

if st.button("Make Call"):
   # Twilio credentials
   account_sid = "ACc2d71daa7ea067cb0d03eaab6d6886bf"
   auth_token = "41124fc7f7addb4c495de1e14d259ff9"

   # Initialize Twilio client
   client = Client(account_sid, auth_token)

   try:
      call = client.calls.create(twiml='<Response><Say voice="alice">' + message + '</Say></Response>',to=phone_number,from_="+17082737116",record=True)
      st.success("Call initiated successfully!")
   except Exception as e:
      st.error(f"Error making call: {e}")
