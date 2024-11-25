import React, { useState } from "react";
import axios from "axios";
import './manu.css';
import { Bar } from "react-chartjs-2";
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend,
} from "chart.js";
import * as XLSX from 'xlsx';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

function Home() {
    const [file, setFile] = useState(null);
    const [previewData, setPreviewData] = useState([]);
    const [columns, setColumns] = useState([]);
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [userID, setUserId] = useState("");
    const [retrievedData, setRetrievedData] = useState(null);
    const [city, setCity] = useState(""); 
    const [weatherData, setWeatherData] = useState(null);
    const [selectedView, setSelectedView] = useState("");
    const [viewChartData, setViewChartData] = useState(null);

    const handleWeatherFetch = () => {
        if (!city.trim()) {
            alert("Please enter a city name.");
            return;
        }

        axios
            .get(`http://localhost:5000/api/weather?city=${city}`)
            .then((response) => {
                setWeatherData(response.data);
                console.log('Weather data:', response.data);
            })
            .catch((error) => {
                console.error('Error fetching weather data:', error.response || error.message);
                alert('Failed to fetch weather data.');
            });
    };

    const handleFileChange = (e) => {
        const selectedFile = e.target.files[0];
        if (selectedFile && selectedFile.type === "text/csv") {
            setFile(selectedFile);
        } else {
            alert("Please upload a valid .csv file!");
            setFile(null);
        }
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (file) {
            uploadFile(file);
        } else {
            alert("Please select a .csv file first!");
        }
    };

    const uploadFile = (file) => {
        const formData = new FormData();
        formData.append('file', file);

        axios
            .post('http://localhost:5000/file_upload', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            })
            .then((response) => {
                console.log('File upload response:', response);
                alert(`File ${file.name} uploaded successfully!`);

                const data = JSON.parse(response.data.preview);
                const headers = Object.keys(data[0]);

                setColumns(headers);
                setPreviewData(data);
            })
            .catch((error) => {
                console.error('Error uploading file:', error.response || error.message);
                alert('File upload failed.');
            });
    };

    const handleRetrieveData = () => {
        if (userID) {
            axios
                .get(`http://localhost:5000/api/retrieve_plane?userID=${userID}`)
                .then((response) => {
                    console.log('Retrieved data:', response.data);
                    
                    const retrievedData = {};
                    const engineData = response.data.Engine;
                    const landData = response.data.LandingGear;
                    const fuelSystemData = response.data.FuelSystem;
                    const cockData = response.data.CockpitControl;
                    const avionicData = response.data.Avionic;
                    const electricalData = response.data.ElectricalSystem;
                    const flightInstrumentData = response.data.FlightInstruments;
                    const brakeData = response.data.Brakes;
                    const exhaustData = response.data.ExhaustSystems;
                    const coolingData = response.data.CoolingSystems;
                    const powerplantData = response.data.Powerplant;

                    if (engineData && engineData.length > 0) {
                        retrievedData.Engine = engineData;
                    }
                    if (landData && landData.length > 0) {
                        retrievedData.LandingGear = landData;
                    }
                    if (fuelSystemData && fuelSystemData.length > 0) {
                        retrievedData.FuelSystem = fuelSystemData;
                    }
                    if (cockData && cockData.length > 0) {
                        retrievedData.CockpitControl = cockData;
                    }
                    if (avionicData && avionicData.length > 0) {
                        retrievedData.Avionic = avionicData;
                    }
                    if (electricalData && electricalData.length > 0) {
                        retrievedData.ElectricalSystem = electricalData;
                    }
                    if (flightInstrumentData && flightInstrumentData.length > 0) {
                        retrievedData.FlightInstruments = flightInstrumentData;
                    }
                    if (brakeData && brakeData.length > 0) {
                        retrievedData.Brakes = brakeData;
                    }
                    if (exhaustData && exhaustData.length > 0) {
                        retrievedData.ExhaustSystems = exhaustData;
                    }
                    if (coolingData && coolingData.length > 0) {
                        retrievedData.CoolingSystems = coolingData;
                    }
                    if (powerplantData && powerplantData.length > 0) {
                        retrievedData.Powerplant = powerplantData;
                    }

                    if (Object.keys(retrievedData).length > 0) {
                        setRetrievedData(retrievedData);
                    }
                    else {
                        alert(`No data found for the provided User ID: ${userID}. Please check the ID or try again later.`);
                    }
                })
                .catch((error) => {
                    console.error('Error retrieving data:', error.response || error.message);
                    alert('Failed to retrieve data. Please check your connection or try again later.');
                });
        } else {
            alert("Please enter a valid User ID.");
        }
        setIsModalOpen(false);
    };
    
    const deleteTable = (category) => {
        setRetrievedData((prevData) => {
            const newData = { ...prevData };
            delete newData[category]; 
            return newData;
        });
    };

    const closeModal = () => {
        setIsModalOpen(false);
        setUserId("");
    };

    const handleReset = () => {
        setCity("");
        setWeatherData(null);
    };
    
    const exportToExcel = (data, category) => {
        const worksheet = XLSX.utils.json_to_sheet(data);
        const workbook = XLSX.utils.book_new();
        XLSX.utils.book_append_sheet(workbook, worksheet, category);
        XLSX.writeFile(workbook, `${category}.xlsx`);
    };

    const handleFetchViewData = async () => {
        if (!selectedView) return;
        try {
            const response = await fetch(`http://localhost:5000/api/${selectedView}`);
            const data = await response.json();

            if (response.ok) {
                const labels = data.map((_, index) => `Record ${index + 1}`);
                const datasets = Object.keys(data[0]).map((key) => ({
                    label: key,
                    data: data.map((item) => item[key]),
                    backgroundColor: `rgba(${Math.floor(Math.random() * 255)}, ${
                        Math.floor(Math.random() * 255)
                    }, ${Math.floor(Math.random() * 255)}, 0.6)`,
                }));
                setViewChartData({ labels, datasets });
            } else {
                alert(`Error fetching data: ${data.error}`);
            }
        } catch (error) {
            console.error(error);
            alert("Failed to fetch data. Please try again.");
        }
    };

    return (
        <div className="home-container">
            <h1 className="home-title">Manufacturing System</h1>
            <p className="home-description">
                Welcome to the Manufacture page! Here, you have the option to upload an item CSV file and conveniently retrieve user data from the system.
            </p>
            <form className="upload-form" onSubmit={handleSubmit}>
                <div className="custom-file-input">
                    <input 
                        type="file" 
                        id="file" 
                        className="file-input"
                        accept=".csv, .xlsx"
                        onChange={handleFileChange}
                    />
                    <label htmlFor="file" className="file-label">
                        {file ? file.name : "Select File"}
                    </label>
                </div>
                <button 
                    type="submit" 
                    className="upload-button" 
                    disabled={!file}
                >
                    Upload
                </button>
            </form>
            <div className="weather-section">
                <h2>Check Weather</h2>
                <input
                    type="text"
                    placeholder="Enter city name"
                    value={city}
                    onChange={(e) => setCity(e.target.value)}
                    className="city-input"
                />
                <button onClick={handleWeatherFetch} className="weather-button">
                    Fetch Weather
                </button>
                {weatherData && (
                    <div className="weather-info">
                        <h3>Weather in {weatherData.city}</h3>
                        <p>Temperature: {weatherData.temperature}°C</p>
                        <p>Description: {weatherData.description}</p>
                    </div>
                )}
            </div>
            <button onClick={handleReset} className="reset-button">
                Reset
            </button>
            <div className="view-selection">
                <label htmlFor="view-select">Select a View:</label>
                <select
                    id="view-select"
                    value={selectedView}
                    onChange={(e) => setSelectedView(e.target.value)}
                >
                    <option value="" disabled>
                        Select an option
                    </option>
                    <option value="coolingsystemefficiency">Cooling System Efficiency</option>
                    <option value="comprehensiveavionics">Comprehensive Avionics</option>
                    <option value="highhorsepowerusers">High Horsepower Users</option>
                    <option value="hightorqueengines">High Torque Engines</option>
                    <option value="useraboveaverageengines">Above Average Engines</option>
                    <option value="userbrakessummary">Brakes Summary</option>
                    <option value="usercockpitavionicsview">Cockpit Avionics View</option>
                    <option value="userpowerplantdetails">Powerplant Details</option>
                    <option value="userenginelandinggearview">Engine & Landing Gear View</option>
                    <option value="userswithcomponents">Users with Components</option>
                </select>
                <button
                    onClick={handleFetchViewData}
                    disabled={!selectedView}
                    className="fetch-data-button"
                >
                    Fetch and Visualize
                </button>
            </div>
            {viewChartData && (
                <div className="chart-container">
                    <h2>Visualization: {selectedView.replace(/([A-Z])/g, " $1")}</h2>
                    <Bar
                        data={viewChartData}
                        options={{
                            responsive: true,
                            plugins: {
                                legend: { position: "top" },
                                title: { display: true, text: "Data Visualization" },
                            },
                        }}
                    />
                </div>
            )}
            {previewData.length > 0 && (
                <div className="preview-box">
                    <h2>Items Preview</h2>
                    <div className="preview-scroll">
                        <table className="preview-table">
                            <thead>
                                <tr>
                                    {columns.map((column, index) => (
                                        <th key={index}>{column}</th>
                                    ))}
                                </tr>
                            </thead>
                            <tbody>
                                {previewData.map((row, rowIndex) => (
                                    <tr key={rowIndex}>
                                        {columns.map((column, colIndex) => (
                                            <td key={colIndex}>{row[column]}</td>
                                        ))}
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                    <button className="button-data" onClick={() => setIsModalOpen(true)}>
                        Retrieve Data
                    </button>
                </div>
            )}

            {isModalOpen && (
                <div className="modal">
                    <div className="modal-content">
                        <span className="close" onClick={closeModal}>&times;</span>
                        <h2>Enter User ID</h2>
                        <input
                            type="text"
                            placeholder="Enter User ID"
                            value={userID}
                            onChange={(e) => setUserId(e.target.value)}
                            className="modal-input"
                        />
                        <button className="retrieve-button" onClick={handleRetrieveData}>
                            Retrieve Data
                        </button>
                    </div>
                </div>
            )}
            {retrievedData && (
                <div className="retrieved-data-container">
                    <h2>Retrieved Airplane Data</h2>
                    {Object.entries(retrievedData).map(([category, data]) => (
                        <div key={category}>
                            <h3>{category}</h3>
                            {data.length > 0 ? (
                                <table className="retrieved-data-table">
                                    <thead>
                                        <tr>
                                            {Object.keys(data[0]).map((key, index) => (
                                                <th key={`${category}-header-${index}`}>{key}</th>
                                            ))}
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {data.map((row, rowIndex) => (
                                            <tr key={`${category}-row-${rowIndex}`}>
                                                {Object.values(row).map((value, colIndex) => (
                                                    <td key={`${category}-cell-${rowIndex}-${colIndex}`}>{value}</td>
                                                ))}
                                            </tr>
                                        ))}
                                    </tbody>
                                </table>
                                
                            ) : (
                                <p>No data available for {category}.</p>
                            )}
                            <div className="delete-button-container">
                            <button
                                    className="export-button"
                                    onClick={() => exportToExcel(data, category)}
                                >
                                    Export to Excel
                                </button>
                                <button className="delete-button" onClick={() => deleteTable(category)}>
                                    Delete Table
                                </button>
                            </div>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
}

export default Home;
