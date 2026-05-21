# Industrial Monitoring System (Python)

A Python-based industrial monitoring simulator that monitors Temperature, Pressure, and Voltage readings from the terminal.

The program validates sensor input, detects abnormal conditions, tracks alerts, and generates a formatted final report.

---

## Features

- Monitor 3 different sensor types:
  - Temperature
  - Pressure
  - Voltage

- Detects:
  - High alerts
  - Low alerts
  - Normal operating conditions

- Generates final report with:
  - Highest value
  - Lowest value
  - Average value
  - Total alerts
  - Total readings

- Handles invalid input using:
  - `try`
  - `except`

- Uses reusable monitoring architecture instead of separate systems for each sensor.

---

## Concepts Used

This project helped me practice:

- Python functions
- Loops
- Lists
- Dictionaries
- Conditional logic
- Input validation
- Exception handling (`try/except`)
- State tracking
- Reusable system design
- Console report formatting

---

## Sensor Limits

| Sensor | Low Limit | High Limit |
|--------|-----------|------------|
| Temperature | 20 °C | 80 °C |
| Pressure | 30 PSI | 100 PSI |
| Voltage | 210 V | 240 V |

---

## Example Output

```text
Choose sensor from menu (1-3): 1

Enter Temperature: 90
High Temperature

Enter Temperature: 15
Low Temperature

Enter Temperature: 50
Normal Temperature

Enter Temperature: done
```

```text
########################################################
#                        REPORT                        #
########################################################
## Highest Value:            90.0 °C                  ##
## Lowest Value:             15.0 °C                  ##
## Average Value:            51.67 °C                 ##
## Total Alerts:             2                        ##
## Total High Alerts:        1                        ##
## Total Low Alerts:         1                        ##
## Total Number of Readings: 3                        ##
########################################################
```

---

## What I Learned

While building this project I learned:

- How to design reusable monitoring systems
- How to separate logic using functions
- How truthy/falsy values work in Python
- How to safely handle invalid input
- How to improve console output formatting
- How to refactor and simplify program structure

---

## Future Improvements

Possible future upgrades:

- Save reports to CSV/Excel
- Add real-time graphs using matplotlib
- Add MQTT sensor communication
- Create a GUI dashboard
- Connect to real IoT devices

---
