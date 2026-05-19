import os
from flask import Flask, request, abort
from twilio.twiml.messaging_response import MessagingResponse
from datetime import datetime

app = Flask(_name_)

LOG_FILE = "whatapp_message.txt"

def log_message(sender, message body, media url=None):
    """Append message to a text file with timestamps"""
    timestamp = datatime.now().strftime("%Y-%m-%d H%:%M:%S")
    with open(LOG_FILE, "a" , encode="utf-8") as f:
      f.write(f"[{timestamp}] From : {sender}\n")
      f.write(f"Message: {message_body}\n")
      if media_urls :
        f.write(f"Media: {','.join(media_urls)}\n")
      f.write("-" * 50+ "\n")

@app.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
  """Handle incoming Whatsapp Messages"""
  sender = request.form.get("From")
  body =  request.from.get("Body")
  num_media = int(request.from.get("NumMedian", 0))

  media_url = []
  for i in range(num_media):
    media_url = request.form.get(f"MediaURL{i}")
    media_type = request.form.get(f"MediaContentType{i}")
    mdeia_url.append(f"{media_url} (type: {media_type})")
  log_message(sender, body , media_urls)

  resp = MessageingResponse()
  resp.message("Report logged Successfully!")
  return str(resp)
if __name__ =="__main__":
  app.run(debug=True)



