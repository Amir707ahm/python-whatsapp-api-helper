import requests

class WhatsAppHelper:
    def __init__(self, api_token: str, phone_number_id: str):
        self.api_token = api_token
        self.phone_number_id = phone_number_id
        self.base_url = f"https://graph.facebook.com/v17.0/{phone_number_id}/messages"

    def send_text_message(self, recipient_phone: str, message_body: str):
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json",
        }
        payload = {
            "messaging_product": "whatsapp",
            "to": recipient_phone,
            "type": "text",
            "text": {"body": message_body},
        }
        
        response = requests.post(self.base_url, json=payload, headers=headers)
        return response.json()
