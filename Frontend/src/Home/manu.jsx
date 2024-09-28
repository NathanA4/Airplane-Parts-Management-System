import React, { useState } from "react";
import axios from "axios";
import './manu.css';
import placeholder from '../assets/placeholder.jpg';

function Home() {
    const [file, setFile] = useState(null);
    const [previewData, setPreviewData] = useState([]); 
    const [columns, setColumns] = useState([]);
    const [isModalOpen, setIsModalOpen] = useState(false); 

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
        setIsModalOpen(true); 
    };

    const closeModal = () => {
        setIsModalOpen(false);
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
                        accept=".csv"
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
                    <button className="button-data" onClick={handleRetrieveData}>
                        Retrieve Data
                    </button>
                </div>
            )}

            {/* Modal for image */}
            {isModalOpen && (
                <div className="modal">
                    <div className="modal-content">
                        <span className="close" onClick={closeModal}>&times;</span>
                        <img src={placeholder} alt="Item Preview" className="modal-image" />
                        <p>Preview of the selected item.</p>
                    </div>
                </div>
            )}
        </div>
    );
}

export default Home;
