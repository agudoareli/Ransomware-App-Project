# Ransomware Awareness App

This project is a small Python-based interactive application built with **Gradio** that helps raise awareness about ransomware. The app allows users to explore ransomware-related search trends, view common warning signs, learn prevention tips, and review basic cybersecurity terminology.

The application uses **Google Trends data** to visualize how ransomware-related keywords trend over time and provides educational content for general users.

---

## Features

-  Visualize Google Trends data for ransomware-related keywords  
-  Select trends by geographic region  
-  View common warning signs of ransomware infections  
-  Learn basic ransomware prevention tips  
-  Access a glossary of common cybersecurity terms  
-  Simple web-based UI powered by Gradio  

---

## Project Structure
- main.py # Entry point to launch the app
- ransomwareApp.py # Core application logic and UI
- trendsAPI.py # Google Trends API wrapper
- glossary.py # Cybersecurity glossary content
- trend_plot.png # Example output image
- README.md



---

## Requirements

- Python 3.8 or later  
- Stable Internet connection (for Google Trends API call)

### Python Packages

- gradio  
- pytrends  
- matplotlib  
- pandas  

---

## How to Run the Project

### 1. Clone the Project

- Clone the repository or download zip file: https://github.com/agudoareli/Ransomware-App-Project  

---

### 2. Navigate to the Project Folder(the readme assumes the code is inside the Downloads folder)

**Windows**
```bash
cd Downloads\Ransomware-App-Project
```
**Linux/MacOS**
```
cd ~/Downloads/Ransomware-App-Project
```

### 3. Install Dependencies 

```
pip install gradio pytrends matplotlib pandas
```

### 4. Run the application      

On the project folder, run the main file main.py
```
python main.py
```
After running the command, a browser window will open with the Gradio interface. A public shareable link may also be generated.
