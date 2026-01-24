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

## Build Plan
I will be handwiring the matrix using diodes and flexible jumper wires, connecting them directly to the XIAO controllers. I will fabricate custom battery contacts using component leads during assembly. Will be using gemini for the firmware and code related help and also in queries while building if I encounter some issues...

## Update (some fixes)
So I generated the step files and also mirrored to obtain the right sides... also firmware is in a different file and I'm uloading these files as well as the schematic... here are a few images

<img width="644" height="503" alt="Screenshot 2026-01-07 130930" src="https://github.com/user-attachments/assets/ee24a3c4-1922-480a-bdbf-2b537835e935" />
<img width="1360" height="666" alt="Screenshot 2026-01-11 114709" src="https://github.com/user-attachments/assets/6c6fd789-5dcb-4f4b-b992-7ab5fd1db003" />
<img width="1365" height="702" alt="Screenshot 2026-01-11 114523" src="https://github.com/user-attachments/assets/7b909b23-b0e3-4599-85fd-970cc1067be5" />
<img width="1364" height="665" alt="Screenshot 2026-01-11 114840" src="https://github.com/user-attachments/assets/1bc165d7-99ca-4286-b9aa-34981e378f96" />
<img width="1364" height="662" alt="Screenshot 2026-01-11 114956" src="https://github.com/user-attachments/assets/7f7546ab-bd8e-4d6f-8934-85f5b4dee7bf" />

