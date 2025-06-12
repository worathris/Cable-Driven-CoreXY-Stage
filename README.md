# Cable-Driven CoreXY Stage driven by RP2040 and Micropython

<img src="hardware/coreXY_image_render.png"/>

This repository provides MicroPython firmware for controlling a CoreXY motion system using the Maker Pi Pico and two 20BYG101-02 stepper motors (NEMA 8, P = 4.4 W). The stepper motors are driven by the ET-MINI MicroStep Driver, ensuring precise and smooth motion control. The firmware includes stepper motor control logic for X and Y axis movement, optimized for 2D printing or CNC applications. It also supports adjustable microstepping and timing control for enhanced performance. The system is ideal for DIY 3D printers, robotic arms, or other applications requiring accurate motion control in embedded environments.

The main features of this stage are:

- RP2040 + MicroPython Control
The system is powered by the Raspberry Pi RP2040 microcontroller running MicroPython, offering flexible scripting, real-time control, and rapid prototyping. All firmware is fully open-source and maintained on GitHub for easy customization and collaboration.

- Fully Open Source and Developer-Friendly
Designed for makers, researchers, and educators, the entire project—firmware, mechanical design, and wiring—is open source. Comprehensive documentation and GitHub support enable easy replication, extension, and community contributions.

- Cable-Driven and Fully Backdrivable
Unlike traditional belt or screw-driven systems, this XY stage uses a lightweight cable mechanism that ensures smooth motion with minimal friction. The stage is fully backdrivable, allowing for passive compliance and natural response to external forces.

- No Mechanical End-Stops Required
The design eliminates the need for mechanical end-stop switches. The system can detect contact or obstruction through motion feedback, enhancing safety and reducing component count.

- Compact and Lightweight
Optimized for portability and integration, the entire mechanism is compact and lightweight, making it suitable for desktop environments, mobile platforms, and constrained spaces.

- Economical Design with Readily Available Components
All components—including stepper drivers, cables, pulleys, and fasteners—are chosen for affordability and global availability. The mechanical parts are designed in CAD for easy 3D printing or laser cutting, supporting low-cost fabrication and rapid assembly.

# Wiring diagram
<img src="hardware/coreXY_Wiring_Diagram.jpg" alt="wiring_diagram"/>

## 📸 Demonstration Media
[![Watch the video](https://img.youtube.com/vi/tBpJW4bJub8/hqdefault.jpg)](https://www.youtube.com/watch?v=tBpJW4bJub8)

## 🧠 Applications
- Plotting and drawing robots
- Interactive CNC demonstrations
- Low-cost educational motion platforms
- Vision-guided automation prototypes

The code for this example can be found [here](example/CoreXYDrive.py).

## 🛠️ Hardware
- **Controller:** RP2040
- **Motors:** Stepper motors NEMA8 with ET-MINI MicroStep Driver
- **Drive:** Cable and pulley mechanism
- **Guides:** Linear rails E-GMLG9-200 from Mitsumi

# Hardware details
* [CAD](hardware/coreXY.step)
* [ET-MINI MicroStep Driver](https://www.ett.co.th/prod2019/ET-MINI_MICRO_STEP/th-man-ET-Mini%20MicroStep%20Driver.pdf)
* [Maker Pi Pico](https://docs.google.com/document/d/1JoHsZk5IipQPCLXWbZYpDKjGlnkyACOJ1taUrKVsRg8/edit?tab=t.0)
* [Raspberry Pi Pico Datasheet](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf)
* [RP2040 Datasheet](https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf) 
