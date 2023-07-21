
![Logo](resources/MouseBanner.png)

<p align="center">
An A.I.-powered, hand gesture controlled virtual mouse
</p>

<div align="center">

  <a href="">![GitHub last commit](https://img.shields.io/github/last-commit/AndersHaroldson/Virtual-Gesture-Mouse?style=flat-square)</a>
  <a href="">![GitHub Repo stars](https://img.shields.io/github/stars/AndersHaroldson/Virtual-Gesture-Mouse?style=flat-square)</a>
  <a href="">![GitHub contributors](https://img.shields.io/github/contributors/AndersHaroldson/Virtual-Gesture-Mouse?style=flat-square)</a>

</div>


## Introduction
This project was inspired by the original Iron Man movie, hence the Iron Man banner. In his workshop, Tony Stark interacts with his computers using his hands and a pen as a mouse. 

## Features

- Left mouse click
- Right mouse click
- Hold left mouse click

<!--
## Demo

demo video
-->
## How to use
1. Start with your open hand facing the camera.
2. The mouse cursor will follow the tip of your thumb. 
3. Left mouse click: Bring your index finger down towards the tip of your thumb (same x-axis)
4. Right mouse click: Bring your middle finger down towards the tip of your thumb (same x-axis)
5. Hold left mouse click: Bring your ring finger down towards the tip of your thumb (same y-axis)

## Installation
1. Clone this repository
```bash
git clone https://github.com/AndersHaroldson/Virtual-Gesture-Mouse.git
```
2. Change directory into the cloned repo
```bash
cd Virtual-Gesture-Mouse
```
3. Install the dependencies
```bash
pip install -r requirements.txt
```
4. Run the script!
```bash
python3 main.py
```

## Acknowledgements
  - Docs used: [Mediapipe documentation](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker#models)

