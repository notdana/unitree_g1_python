
# Unitree SDK2 in Python Modified for G1 23 DOF

![Unitree Robotics Support Page for G1](https://support.unitree.com/home/en/G1_developer/about_G1)

This repository is a modified version of **Unitree SDK2 Python**, specifically adapted for **Unitree G1 with 23 Degrees of Freedom (DOF)**.

It provides Python-based communication and control functionalities, allowing users to interface with Unitree G1 seamlessly.


# Pre-requisites of working with examples included in this repo


## Working with the Depth Camera

```bash
sudo apt install librealsense2-utils librealsense2-dev
pip install pyrealsense2 opencv-python ultralytics
```


## Working with Ollama (Local LLM)

Ollama allows you to run local large language models like `llama3` on your machine.

1. Install Ollama from [https://ollama.com](https://ollama.com)
2. Pull a model such as `llama3`:
```bash
ollama pull llama3
```
3. Install the Python client:
```bash
pip install ollama
```

## Working with Speaker

The Speaker on board of G1 is not connected to the secondary development board, which means that you will have to connect a speaker through a USB-c port.



#Common Issues & Fixes

## WiFi Connection (Manual Configuration)

### 1. Connect to a Network Using `wpa_cli`

```bash
sudo wpa_cli

add_network

set_network 0 ssid "your_ssid"

set_network 0 psk "your_password"

enable_network 0

status
```

> You'll need to repeat this after every reboot unless automated.

### 2. Assign an IP Address (if not automatically assigned)

Check current routes:
```bash
ip route
```

If no IP is assigned:
```bash
sudo dhclient wlan0
```

Then confirm again:
```bash
ip route
```

---

## GUI Setup for NoMachine Access

You may encounter an issue while connecting noMachine to your G1, showing a black screen while connected.
Below are steps to fixing that issue.

### Install XFCE Desktop Environment

```bash
sudo apt update
sudo apt install xfce4
```

### Set NoMachine to Use XFCE

```bash
sudo nano /usr/NX/etc/node.cfg
```

Add or update the following line:
```bash
DefaultDesktopCommand "/usr/bin/startxfce4"
```

Restart NoMachine:
```bash
sudo /etc/NX/nxserver --restart
```

### Auto-Launch XFCE on Boot

```bash
echo "startxfce4" > ~/.xsession
sudo reboot
```

---

## Virtual Display for Headless Mode (Fix NoMachine Zoom Issue)

If you're running G1 without a physical monitor, set up a virtual screen:

### 1. Install Dummy Video Driver

```bash
sudo apt install xserver-xorg-video-dummy
```

### 2. Create a Dummy X11 Configuration

```bash
sudo nano /etc/X11/xorg.conf
```

Paste the following config:

```
Section "Monitor"
    Identifier "Monitor0"
    HorizSync   28.0-80.0
    VertRefresh 48.0-75.0
    Option      "DPMS"
EndSection

Section "Device"
    Identifier  "Card0"
    Driver      "dummy"
    VideoRam    256000
EndSection

Section "Screen"
    Identifier "Screen0"
    Device     "Card0"
    Monitor    "Monitor0"
    DefaultDepth     24
    SubSection "Display"
        Depth     24
        Modes     "1280x720"
    EndSubSection
EndSection

Section "ServerLayout"
    Identifier     "Layout0"
    Screen      0  "Screen0"
EndSection
```

### 3. Reboot and Confirm Resolution

```bash
sudo reboot
DISPLAY=:0 xrandr
```

You should see:
```
Screen 0: minimum 8 x 8, current 1280 x 720, maximum ...
```

---
