# Home Conditions Inspector

HomeConditionsInspector is a Python project designed to help inspect and monitor various conditions within a home. The project gathers relevant data, processes it, and provides insights into home conditions such as temperature, humidity, and other environmental factors. The tool is primarily aimed at helping homeowners, landlords, and property managers assess and improve the living conditions within their homes.

## Features

- **Real-Time Monitoring**: Collects data from various sensors (e.g., temperature, humidity) and displays real-time statistics.
- **Data Logging**: Automatically logs sensor data into files for long-term tracking and analysis.
- **Condition Analysis**: Provides insights and flags if certain environmental conditions are outside of the ideal range.
- **Reports**: Generates detailed reports based on the data collected, helping users to track changes and trends over time.
- **User-Friendly Interface**: Simple, clear UI to access and visualize home conditions.

## Installation

To get started with HomeConditionsInspector, follow these steps:

### Prerequisites
- Raspberry PI with LCD device and temperature/humidity sensors properly wired
- Python 3.x
- pip (Python package installer)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/MaciejSzczypek/HomeConditionsInspector.git
   ```
2. Navigate to the project directory:
   ```bash
   cd HomeConditionsInspector
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run HomeConditionsInspector, use the following command on your Raspberry PI:
```bash
python show_inside_conditions.py
```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## Contact

For any questions or suggestions, feel free to open an issue or contact the project maintainer:
- Maintainer: Maciej Szczypek