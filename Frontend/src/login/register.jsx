import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import './Register.css';

const Register = () => {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [role, setRole] = useState('');
    const [errors, setErrors] = useState({});
    const navigate = useNavigate();

    const handleRegister = async (e) => {
        e.preventDefault();
        setErrors({}); // Reset errors before new request

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
            if (error.response) {
                console.error('Error from server:', error.response.data);
                const serverErrors = error.response.data;

                // Set specific field errors based on response
                if (error.response.status === 400) {
                    setErrors({ general: 'Please fill in all required fields.' });
                } else if (error.response.status === 409) {
                    if (serverErrors.error.includes('username')) {
                        setErrors(prevErrors => ({ ...prevErrors, username: 'Username is already taken.' }));
                    }
                    if (serverErrors.error.includes('email')) {
                        setErrors(prevErrors => ({ ...prevErrors, email: 'Email is already registered.' }));
                    }
                } else {
                    setErrors({ general: 'Registration failed. Please try again.' });
                }
            } else {
                console.error('Error sending data to server:', error.message);
                setErrors({ general: 'Unable to connect to the server. Please try again later.' });
            }
        }
    };

    return (
        <div>
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
                            {errors.username && <p className="error-message">{errors.username}</p>}
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
                            {errors.email && <p className="error-message">{errors.email}</p>}
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
                    {errors.general && <p className="error-message">{errors.general}</p>}
                </div>
            </div>
        </div>
    );
};

export default Register;
