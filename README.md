# Airplane-Parts-Management-System
Developed an advanced interface using Flask, MySQL, React, and Tailwind CSS, allowing users to design airplanes, save configurations, and optimize parts and measurements for their Physical Model (PSM).

## Table of Contents

1. [Backend Setup](#backend-setup)
2. [Frontend Setup](#frontend-setup)
3. [Project Folder Structure](#project-folder-structure)

## Backend Setup

The backend is built using **Flask** and provides an API to fetch data for various airplane systems.

### Prerequisites
- Python 3.x
- `pip` for installing dependencies

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/airplane-systems-management
   cd airplane-systems-management
   ```
2. Python virtual environment to isolate your dependencies:
  ```bash
    python3 -m venv venv
    source venv/bin/activate
   ```
3. Install the required dependencies:
   ```bash
     pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```bash
   flask run
   ```

## Frontend Setup

The frontend is built using React, with CSS for styling, and uses Chart.js and React Three Fiber for visualizing airplane designs and data.

## Navigate to the frontend directory:
  ```bash  
   cd frontend
```
### Prerequisites
- npm
- 'npm install' for installing dependencies

### Required Imports

In the React components, you need to import the following libraries for data visualizations, API calls, and 3D rendering:

```javascript
import { Bar } from "react-chartjs-2";
import axios from "axios";
import * as XLSX from 'xlsx';
import { Canvas } from '@react-three/fiber';
import { useNavigate } from 'react-router-dom';
import { Environment, OrbitControls } from '@react-three/drei';
```
## Project Folder Structure
│── Backend/                      
│   ├── __pycache__/
│   ├── app.py       
│   ├── models.py 
│── Database/   
│   ├── DB.sql                 
│── Frontend/              
│   ├── public/
│   │ ├── textures/
│   │   │   └── …
│   │ ├── Cirrussr22.jsx
│   │ ├── Lowpoly.jsx
│   │ ├── cirrussr22.bin
│   │ ├── cirrussr22.gltf
│   │ ├── lowpoly.bin
│   │ ├── lowpoly.gltf
│   ├── src/
│   │   ├── Home/
│   │   │   ├── manu.css
│   │   │   └── manu.jsx
│   │   ├── System/
│   │   │   ├── node.jsx
│   │   │   ├── partparameters.js
│   │   │   ├── system.css
│   │   │   └── system.jsx
│   │   ├── ViewPlane/
│   │   │   ├── viewplane.css
│   │   │   └── viewplane.jsx
│   │   ├── Assets/
│   │   │   └── …
│   │   ├── Login/
│   │   │   ├── login.css
│   │   │   ├── login.jsx
│   │   │   ├── register.css
│   │   │   └── register.jsx
│   │   ├──SharedContext.jsx
│   │   ├──index.css
│   │   ├──main.ksx
│   ├── .gitignore
│   ├── .eslint.config.js
│   ├── .index.html
│   ├── package-lock.json
│   ├── package.json
│   ├── tailwind.config.js
│   └──vite.config.js 
├── requirements.txt 
├── .gitignore    
└── README.md   
      
