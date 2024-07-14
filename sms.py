from twilio.rest import Client
import keys

client = Client(keys.account_sid, keys.auth_token)

message = client.messages.create(
    body = "S.A.F.E.G.E.N Alert ! Fire Detected ",
    from_ =keys.twilio_no,
    to=keys.reciever_no 
)
print(message.body)