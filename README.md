# Wireless Split Handwired Keyboard

## Project Overview
This is a custom **wireless, handwired** split mechanical keyboard project. It is to run on **KMK Firmware** with Bluetooth Low Energy.

**Grant Request Note:**
This is a **handwired build** (no PCB). I am requesting a grant for the **components** listed in the BOM.

## Hardware Specs
* **Microcontroller:** 2x Seeed Studio XIAO nRF52840 (Bluetooth LE)
* **Switches:** Gateron Low Profile KS-33 (Red Linear)
* **Battery:** 2x 10440 Li-Ion (3.7V)
* **Keycaps:** Cherry Profile PBT (Pastel Dream)
* **Firmware:** KMK Firmware (CircuitPython)

## 3D Printing Notes
* **File Handling:** The case files are located in the `3d_files` folder.
* **Important:** Only one set of case files is provided. The parts must be **mirrored** before printing to create the opposite half.

## Build Plan
I will be handwiring the matrix using diodes and flexible jumper wires, connecting them directly to the XIAO controllers. I will fabricate custom battery contacts using component leads during assembly. Will be using gemini for the firmware and code related help and also in queries while building if I encounter some issues...
