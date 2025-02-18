import time
import sys
from unitree_sdk2py.core.channel import ChannelSubscriber, ChannelFactoryInitialize
from unitree_sdk2py.g1.audio.g1_audio_client import AudioClient

def set_rgb_light(audio_client, r, g, b, duration=1):
    """
    Controls the G1 RGB light strip.
    
    :param audio_client: Initialized AudioClient instance
    :param r: Red intensity (0-255)
    :param g: Green intensity (0-255)
    :param b: Blue intensity (0-255)
    :param duration: How long the color remains before turning off (in seconds)
    """
    result = audio_client.LedControl(r, g, b)
    if result == 0:
        print(f"✅ RGB Light set to ({r}, {g}, {b}) for {duration} seconds")
    else:
        print(f"❌ Error setting RGB Light: Error Code {result}")
    
    time.sleep(duration)  # Keep light on for the duration
    audio_client.LedControl(0, 0, 0)  # Turn off light

# Initialize AudioClient
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} networkInterface")
        sys.exit(-1)

    ChannelFactoryInitialize(0, sys.argv[1])

    audio_client = AudioClient()
    audio_client.SetTimeout(10.0)
    audio_client.Init()

    # Set RGB light examples
    set_rgb_light(audio_client, 255, 0, 0, 1)   # Red
    set_rgb_light(audio_client, 0, 255, 0, 1)   # Green
    set_rgb_light(audio_client, 0, 0, 255, 1)   # Blue
    set_rgb_light(audio_client, 255, 255, 0, 1) # Yellow
    set_rgb_light(audio_client, 255, 255, 255, 1) # White
