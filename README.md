
# Advanced Digital Clock in Python
---
[In C script](https://github.com/mdriyadkhan585/advanced-digital-clock-C)

![Clock Logo](logo.svg)

---
## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Code Overview](#code-overview)
7. [How It Works](#how-it-works)
8. [Customization](#customization)
9. [Known Issues](#known-issues)
10. [Contributing](#contributing)
11. [License](#license)

## Introduction
The Advanced Digital Clock project is a terminal-based clock application written in Python. It displays the current date and time in a user-friendly format with 12-hour clock and AM/PM notation. This project is designed for learning, demonstration, and integration into larger applications. It features a clean and continuously updating interface and is compatible with various operating systems.

## Features
- **Real-time Date and Time Display**: Continuously shows the current date and time in the format `DD-MM-YYYY | HH:MM:SS AM/PM`.
- **12-Hour Format**: Time is displayed in a 12-hour format with AM/PM indicator.
- **Clean Interface**: The clock clears the screen before each update, ensuring a clear display.
- **Cross-Platform Compatibility**: Works on UNIX-like systems (Linux, macOS) and can be adapted for Windows.

## Prerequisites
To run this project, ensure you have the following:
- Python 3.x installed on your system.
- A terminal or command prompt to execute the script.
- For Windows users, you might need to configure your terminal to handle screen clearing commands.

## Installation
### Step 1: Clone the Repository
Clone the repository to your local machine using `git`:

```bash
git clone https://github.com/mdriyadkhan585/advanced-digital-clock
```

### Step 2: Navigate to the Directory
Change to the directory containing the script:

```bash
cd advanced-digital-clock
```

### Step 3: Run the Program
Execute the Python script using:

```bash
python digital_clock.py
```

## Usage
The script will display the current date and time, updating every second. The display will clear and refresh to maintain a clean interface.

### Exiting the Program
To exit the program, press `Ctrl+C` in the terminal.

### Example Output
```
======================================
      Welcome to the Digital Clock    
======================================

Press Ctrl+C to exit the program.

Current Date and Time:
======================================
  Date: 01-09-2024
  Time: 02:23:15 PM
======================================
```

## Code Overview
### Main Components
1. **`clear_screen()`**: Clears the terminal screen for a clean update.
2. **`print_welcome_message()`**: Displays a welcome message and exit instructions.
3. **`display_clock()`**: Main function that retrieves and formats the current time, then updates the display.
4. **`if __name__ == "__main__":`**: Ensures that `display_clock()` runs only when the script is executed directly.

### How It Works
- The script uses the `time` module to fetch the current local time.
- It converts the time into a 12-hour format with AM/PM notation.
- The terminal screen is cleared before each update to keep the clock in the same position.

## Customization
You can modify the script to suit your needs:
- **Change Date and Time Format**: Adjust the format in the `print()` statements to alter how the date and time are displayed.
- **Add Colors**: Enhance the display by adding ANSI escape codes for colored text.
- **Additional Features**: Implement new features such as alarms or different time zones.

## Known Issues
- **Screen Clearing**: The `clear_screen()` function may not work on all systems, particularly on Windows without special configuration.
- **Time Drift**: Minor inaccuracies may occur over extended periods due to the `time.sleep()` function.

## Contributing
Contributions are welcome! If you have suggestions, improvements, or bug fixes, please submit a pull request or open an issue.

### Steps to Contribute
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/mdriyadkhan585/advanced-digital-clock?tab=MIT-1-ov-file) file for more details.

---
