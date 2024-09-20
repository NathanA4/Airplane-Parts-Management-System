import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate, Link } from 'react-router-dom';
import './Register.css'; // Import your CSS file

const Register = () => {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [role, setRole] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const navigate = useNavigate();

    const handleRegister = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:5000/api/register', {
                username,
                email,
                password,
                role,
            });

            console.log('Response from server:', response.data);
            navigate('/login');
        } catch (error) {
            console.error('Error sending data to server:', error.response ? error.response.data : error.message);
            setErrorMessage('Registration failed. Please try again.');
        }
    };

    return (
        <div>
            <header className="header">
                <div className="container">
                    <Link to="/login">
                        <button className="button">Login</button>
                    </Link>
                    <Link to="/">
                        <button className="button primary">Register</button>
                    </Link>
                </div>
            </header>
            <div className="min-h-screen flex items-center justify-center bg-gray-100">
                <div className="form-container">
                    <h2 className="title">Register</h2>
                    <form className="form" onSubmit={handleRegister}>
                        <div className="input-group">
                            <label htmlFor="username" className="sr-only">Username</label>
                            <input
                                type="text"
                                id="username"
                                className="input"
                                placeholder="Nate"
                                value={username}
                                onChange={(e) => setUsername(e.target.value)}
                            />
                        </div>
                        <div className="input-group">
                            <label htmlFor="email" className="sr-only">Email</label>
                            <input
                                type="email"
                                id="email"
                                className="input"
                                placeholder="Ex: nathaniel.Kebere@airplanesystems.ca"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                            />
                        </div>
                        <div className="input-group">
                            <label htmlFor="password" className="sr-only">Password</label>
                            <input
                                type="password"
                                id="password"
                                className="input"
                                placeholder="Password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                            />
                        </div>
                        <div className="input-group">
                            <label htmlFor="role" className="sr-only">Role</label>
                            <select
                                id="role"
                                name="role"
                                className="input"
                                value={role}
                                onChange={(e) => setRole(e.target.value)}
                            >
                                <option value="">Select Role</option>
                                <option value="user">User</option>
                                <option value="manufacturer">Manufacturer</option>
                            </select>
                        </div>
                        <button
                            type="submit"
                            className="submit-button"
                        >
                            Register
                        </button>
                    </form>
                    {errorMessage && <p className="error-message">{errorMessage}</p>}
                </div>
            </div>
        </div>
    );
};

export default Register;
