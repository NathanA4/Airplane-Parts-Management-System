import React, { useState } from "react";
import './manu.css'; 

function Home() {
    const [file, setFile] = useState(null);

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (file) {
            alert(`File ${file.name} uploaded successfully!`);
        } else {
            alert("Please select a file first!");
        }
    };

    const handleRetrieve = () => {
        alert("Retrieving data...");
        // Add your data retrieval logic here
    };

    return (
        <div className="home-container">
            <h1 className="home-title">Retrieving Data</h1>
            
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
                        onChange={handleFileChange}
                    />
                    <label htmlFor="file" className="file-label">
                        {file ? file.name : "Choose File"}
                    </label>
                </div>
                <button type="submit" className="upload-button">
                    Upload
                </button>
            </form>
        </div>
    );
}

export default Home;
