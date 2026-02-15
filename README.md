# Mars Hackpad 🚀
<img width="1724" height="897" alt="mars_hackpad" src="https://github.com/mars0x1/hackpad/blob/main/imgs/mars_hackpad.png" />



Mars Hackpad is a 12-input productivity tool designed for seamless media control and custom shortcuts. It features an 11-key matrix and a rotary encoder, providing a tactical way to manage your workspace. It is powered by the **Seeed XIAO RP2040** and runs on **KMK firmware**.

## Features
* **128x64 OLED Display**: Provides real-time status updates via I2C (SDA: D4, SCL: D5).
* **EC11 Rotary Encoder**: Mapped to system volume control. Press the encoder to toggle **System Mute**.
* **11 Mechanical Keys**: Currently configured with macros for **Undo**, **Copy**, **Paste**, and a dedicated **Mic Mute** shortcut (FN + F5).
* **3D Printed Case**: A two-piece snap-fit design that holds the PCB and display at an ergonomic angle.

## CAD Model

* The case was designed in Fusion360 . 
* It consists of two printed parts: a **Top Case** with cutouts for the keys and screen, and a **Bottom Case** to protect the electronics.
* Everything is held together by M3 bolts.

## PCB
My PCB was designed in KiCad. It features a 4x3 matrix layout and custom silkscreen labeling.
* **Schematic**:
*  <img width="796" height="655" alt="image" src="https://github.com/mars0x1/hackpad/blob/main/imgs/Schematic.png" />

* **PCB Layout**:
* <img width="410" height="578" alt="image" src="https://github.com/mars0x1/hackpad/blob/main/imgs/PCB_layout.png" />



* I used standard MX-style footprints for the keys and ensured the XIAO RP2040 sits centrally for easy USB-C access.
<img width="722" height="863" alt="image" src="https://github.com/mars0x1/hackpad/blob/main/imgs/3D_PCB.png" />

## Firmware Overview
This hackpad uses **KMK Firmware** (CircuitPython).
* **Matrix Setup**: Rows use pins **D0, D1, D2, D3** and Columns use **D6, D7, D9**.
* **Rotary Encoder**: Mapped to pins **D11** and **D10**.
* **Shortcuts**: The firmware is set up to handle common productivity commands without needing to touch the main keyboard.

## BOM (Bill of Materials)
Here is everything you need to build the Mars Hackpad:

| Item | Quantity | Description |
| :--- | :--- | :--- |
| **Seeed XIAO RP2040** | 1 | Main Microcontroller |
| **0.91 inch OLED display** | 1 | I2C Display |
| **EC11 Encoder** | 1 | Rotary Encoder with push-button |
| **MX Switches** | 11 | Your choice of mechanical switches |
| **1N4148 Diodes** | 12 | Switching Diodes for the matrix |
| **Case** | 2 parts | 3D Printed Top and Bottom shells |
| **M3 Bolts** | 4 | To secure the case halves |
