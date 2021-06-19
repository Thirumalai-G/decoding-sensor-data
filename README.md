# Decoding Sensor Data with Python

- [Overview](#overview)
- [Installation](#installation)
  - [Verify Local Environment](#verify-local-environment)
  - [Windows](#windows)
  - [macOS](#macos)
  - [About pip](#about-pip)
- [Viewing the Analysis](#viewing-the-analysis)

## Overview

An Analysis of the Home Sensor Data and to extract insights like Temperature,Humidity,Air Quality Content and Energy Usage of the Building from the recorded observations.

## Installation

### Verify Local Environment

### Windows

Open a command prompt or powershell and run the following commands, replacing 'project-root' with the path to the root
folder of the project.

``` bash
> cd 'project-root'
> python -m venv venv
> venv\Scripts\activate.bat
> pip install -r requirements.txt
```

### macOS

Open a terminal and run the following commands, replacing 'project-root' with the path to the root folder of the
project.

```bash
> cd 'project-root'
> python3 -m venv venv
> source venv/bin/activate
> pip install -r requirements.txt
```

*Note: If you've installed Python 3 using a method other than Homebrew, you might need to type `python` in the second
command instead of `python3`.*

### About pip

`pip` updates frequently, but versions greater than 10.x.x should work with this project.

## Viewing the Analysis

The analysis can be previewed by opening a terminal, changing to the project root, activating the virtual environment, and
executing the below python script, which in turn displays the predefined analysis done in your console.

`python sensor/sensor.py`
