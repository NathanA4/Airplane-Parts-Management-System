import React, { useState } from "react";
import axios from "axios";
import './manu.css';

function Home() {
    const [file, setFile] = useState(null);
    const [imageUrls, setImageUrls] = useState({});

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
            uploadFile(file, "Manufacter Tool", "location");
        } else {
            alert("Please select a .csv file first!");
        }
    };

    const handleRetrieve = () => {
        alert("Retrieving data...");
    };

    const uploadFile = (file, tool, location) => {
        const formData = new FormData();
        formData.append('file', file);
        formData.append('location', location);
    
        axios
            .post('http://localhost:5000/file_upload', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            })
            .then((response) => {
                console.log('File upload response:', response);
                alert(`File ${file.name} uploaded successfully!`);
            })
            .catch((error) => {
                console.error('Error uploading file:', error.response || error.message);
                alert('File upload failed.');
            });
    };

    return (
        <div className="home-container">
            <h1 className="home-title">Manufacter System</h1>
            <p className="home-description">
                Under this section, you can upload a file or retrieve data.
            </p>
            <button type="button" className="retrieve-button" onClick={handleRetrieve}>
                Retrieve Data
            </button>
            <form className="upload-form" onSubmit={handleSubmit}>
                <div className="custom-file-input">
                    <input 
                        type="file" 
                        id="file" 
                        className="file-input"
                        accept=".csv"
                        onChange={handleFileChange}
                    />
                    <label htmlFor="file" className="file-label">
                        {file ? file.name : "Choose .csv File"}
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
        </div>
    );
}

export default Home;
