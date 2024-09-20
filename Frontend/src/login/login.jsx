import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate, Link } from 'react-router-dom';
import './Login.css'; // Import the CSS file

const Login = () => {
    const [username, setUsernameOrEmail] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    const navigate = useNavigate();

    const handleUsernameOrEmailChange = (e) => {
        setUsernameOrEmail(e.target.value);
    };

    const handlePasswordChange = (e) => {
        setPassword(e.target.value);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:5000/api/login', {
                username,
                password
            });

            console.log('Login successful:', response.data);
            localStorage.setItem('userId', response.data.userID);
            navigate('/systems');
        } catch (error) {
            console.error('Login error:', error.response ? error.response.data : error.message);
            setErrorMessage('Invalid username or password');
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
            <div className="min-h-screen">
                <div className="form-container">
                    <h2 className="title">Login</h2>
                    <form className="form" onSubmit={handleSubmit}>
                        <div className="input-group">
                            <label htmlFor="username" className="sr-only">Username</label>
                            <input
                                type="text"
                                id="username"
                                className="input"
                                value={username}
                                onChange={handleUsernameOrEmailChange}
                                placeholder="Username"
                                required
                            />
                        </div>
                        <div className="input-group">
                            <label htmlFor="password" className="sr-only">Password</label>
                            <input
                                type="password"
                                id="password"
                                className="input"
                                value={password}
                                onChange={handlePasswordChange}
                                placeholder="Password"
                                required
                            />
                        </div>
                        <button type="submit" className="submit-button">
                            Login
                        </button>
                    </form>
                    {errorMessage && <p className="error-message">{errorMessage}</p>}
                </div>
            </div>
        </div>
    );
};

export default Login;
