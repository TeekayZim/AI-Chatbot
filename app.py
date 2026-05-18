{
  "metadata": {
    "kernelspec": {
      "name": "xpython",
      "display_name": "Python 3.13 (XPython)",
      "language": "python"
    },
    "language_info": {
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "version": "3.13.1"
    }
  },
  "nbformat_minor": 5,
  "nbformat": 4,
  "cells": [
    {
      "id": "047a1928-bc28-4b18-b1c5-355462dcebea",
      "cell_type": "code",
      "source": "import os \nfrom flask import Flask, request, abort\nfrom twilio.twiml.messaging_response import MessagingResponse\nfrom datetime import datetime\n\napp = Flask(__name__)\n\nLOG_FILE = \"whatsapp_message.txt\"\n\ndef log_message(sender, message_body, media_url=None):\n    \"\"\"Append message to a text file with timestamp\"\"\"\n    timestamp = datatime.now().strftime(\"%Y-%m-%d H%:%M:%S\")\n    with open(LOG_FILE, \"a\" , encoding=\"utf-8\") as f:\n        f.write(f\"[{timestamp}] From: {sender}\\n\")\n        f.write(f\"Message: {message_body}\\n\")\n        if media_urls :\n            f.write(f\"Media: {','.join(media_urls)}\\n\")\n        f.write(\"-\" * 50+ \"\\n\")\n\n@app.route(\"/whatsapp\", methods=[\"POST\"])\ndef whatsapp_webhook():\n    \"\"\"Handle incoming Whatsapp Messages\"\"\"\n    # Get message details from Twilio\n    sender = request.form.get(\"From\")\n    body = request.form.get(\"Body\")\n    num_media = int(request.form.get(\"NumMedia\", 0))\n\n    media_urls = []\n    for i in range(num_media):\n        media_url = request.form.get(f\"MediaUrl{i}\")\n        media_type = request.form.get(f\"MediaContentType{i}\")\n        media_url.append(f\"{media_url} (type: {media_type})\")\n        # Optional  : Download the media file\n    log_message(sender, body, media_urls)\n\n    resp = MessagingResponse()\n    resp.message(\"Message Logged Successfully!\")\n    return str(resp)\nif __name__ == \"__main__\":\n    app.run(debug=True)\n                  \n        \n        ",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "ename": "<class 'ModuleNotFoundError'>",
          "evalue": "No module named 'flask'",
          "traceback": [
            "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
            "\u001b[31mModuleNotFoundError\u001b[39m                       Traceback (most recent call last)",
            "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[6]\u001b[39m\u001b[32m, line 2\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mos\u001b[39;00m \n\u001b[32m----> \u001b[39m\u001b[32m2\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mflask\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m Flask, request, abort\n\u001b[32m      3\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mtwilio\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mtwiml\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mmessaging_response\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m MessagingResponse\n\u001b[32m      4\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mdatetime\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m datetime\n",
            "\u001b[31mModuleNotFoundError\u001b[39m: No module named 'flask'"
          ],
          "output_type": "error"
        }
      ],
      "execution_count": 6
    },
    {
      "id": "c8ff7d3e-ba8d-421e-b58c-814523d5ab4e",
      "cell_type": "code",
      "source": "",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    }
  ]
}