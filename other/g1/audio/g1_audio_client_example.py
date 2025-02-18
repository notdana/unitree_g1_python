import time
import sys
from unitree_sdk2py.core.channel import ChannelSubscriber, ChannelFactoryInitialize
from unitree_sdk2py.g1.audio.g1_audio_client import AudioClient
from unitree_sdk2py.g1.loco.g1_loco_client import LocoClient

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} networkInterface")
        sys.exit(-1)

    ChannelFactoryInitialize(0, sys.argv[1])

    audio_client = AudioClient()  
    audio_client.SetTimeout(10.0)
    audio_client.Init()

    sport_client = LocoClient()  
    sport_client.SetTimeout(10.0)
    sport_client.Init()

    ret = audio_client.GetVolume()
    print("debug GetVolume: ",ret)

    audio_client.SetVolume(85)

    ret = audio_client.GetVolume()
    print("debug GetVolume: ",ret)


    audio_client.LedControl(255,0,0)
    time.sleep(1)
    audio_client.LedControl(0,255,0)
    time.sleep(1)
    audio_client.LedControl(0,0,255)

    time.sleep(3)
    audio_client.TtsMaker("My name is Dana",0)
    
