# Django Robot Controller

## Overview
This web-based application provides a user-friendly interface for controlling your PicarX, making it easy to remotely maneuver and perform various actions 
with your robot. The project aims to simplify the control process, allowing users to focus on more complex tasks while still having full control over their 
robot.

## Features

* **Customizable Interface**: Adapt the control interface to suit your robot's specifications, ensuring seamless integration.
	+ Easily modify layout, add custom widgets, and adjust design to match your preferences.
	+ Support for multiple language translations and dynamic updates.
* **Real-time Feedback**: Receive instant updates on your robot's status and sensor data, allowing you to respond quickly and effectively.
	+ Monitor vital signs, such as battery level, temperature, and motor speed.
	+ Analyze sensor readings from various sensors, including GPS, camera, and more.
* **Responsive Design**: Access the controller interface from various devices, providing a consistent and adaptable experience.
	+ Optimized for desktop, tablet, and mobile devices, ensuring seamless interaction across platforms.
	+ Automatically adjusts layout to accommodate different screen sizes and orientations.

## Setup

### 1. Clone the Repository
Clone this project using Git:
```bash
git clone https://github.com/Uglypr1nces/robot-controller-django.git
cd robot-controller-django
```

### 2. Install Dependencies
Install required packages to ensure smooth execution:
```bash
pip install -r requirements.txt
```
If you encounter any issues, please refer to the project documentation for guidance on installing missing packages.

* **Important Note:** Make sure to install all dependencies specified in `requirements.txt` to avoid errors during setup.
* **Troubleshooting Tips:**
	+ Check Python version and update if necessary (Python 3.8 or later recommended).
	+ Verify package versions and compatibility with the project requirements.
	+ Consult the Django documentation for any specific installation steps.

### 3. Start the Project
Launch the application using Python:
```bash
python3 manage.py runserver
```

### 4. Run the Server on Your Robot
Follow these steps to set up and run the server on your PicarX:

<a href="https://github.com/Uglypr1nces/piserver">Instructions</a>
* **Server Setup:** Configure the server to communicate with your robot's hardware, ensuring proper data transmission and control.
* **Client Setup:** Install and configure the client application on your device to connect to the server and access the controller interface.

## Configuration
Configure the project settings as per your requirements. You can modify the following files:
* `settings.py`: Update database connections, logging configurations, and other project-wide settings.
* `urls.py`: Adjust URL mappings for your custom views and routes.

## Screenshots

![alt text](/static/a.jpg)

## Contributing

* **Issue Tracking:** Report any bugs or feature requests through the issue tracker.
* **Pull Requests:** Share your code contributions by submitting pull requests with clear explanations and documentation.
* **Documentation:** Contribute to the project documentation by adding user guides, API references, and other valuable content.
