import network.client as client

from kapibara_audio import KapibaraAudio
from microphone import Microphone

mic=Microphone(chunk=16000)

model=KapibaraAudio('./best_model')




data = {
    "Motors":
    {
        "speedA":0,
        "directionA":1,
        "speedB":0,
        "directionB":1
    },
    "Servos":
    {
        "pwm1":45,
        "pwm2":135,
    }
}

with client.connect('192.168.50.42:5051') as channels:
    stub=client.get_stub(channels)
    while True:
        print("Send Command!")
        msg=client.process_data(stub,data)
        print(msg)

