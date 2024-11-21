import React, { useState } from "react";
import axios from "axios";
import './manu.css';
import placeholder from '../assets/placeholder.jpg';

function Home() {
    const [file, setFile] = useState(null);
    const [previewData, setPreviewData] = useState([]);
    const [columns, setColumns] = useState([]);
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [userID, setUserId] = useState("");
    const [retrievedData, setRetrievedData] = useState(null);

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
                                <button className="delete-button" onClick={() => handleDeleteTable(category)}>
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
