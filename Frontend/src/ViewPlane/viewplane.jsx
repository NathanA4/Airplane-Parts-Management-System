import React, { useState, Suspense } from "react";
import { Canvas } from '@react-three/fiber';
import { useNavigate } from 'react-router-dom';
import { Environment, OrbitControls } from '@react-three/drei';
import Model from '../../public/Cirrussr22'; 
import Plane from "../../public/Lowpoly";
import './viewplane.css';

function PlaneView() {
    const [selectedModel, setSelectedModel] = useState(null);
    const navigate = useNavigate();

    const  modelSelected = () => {
        alert("Model Desgin Saved")
    };
    const backToSystems = () => {
        navigate('/systems')
    }

    return (
        <div className="canvas-container">
            <div style={{ position: 'relative' }}>
                <Canvas className="plane1" camera={{ position: [15, 6, 15], fov: 60 }}>
                    <ambientLight intensity={0.2} />
                    <OrbitControls minDistance={3} maxDistance={30} />
                    <Suspense fallback={null}>
                        <Model />
                    </Suspense>
                    <Environment preset="forest" />
                </Canvas>
                <button className="choose-main" onClick={backToSystems}>Back</button>
                <button className="choose-button choose-button1" onClick={modelSelected}>Choose Model 1</button>
            </div>

            <div style={{ position: 'relative' }}>
                <Canvas className="plane2" camera={{ position: [15, 6, 15], fov: 65 }}>
                    <ambientLight intensity={0} />
                    <OrbitControls minDistance={150} maxDistance={200} />
                    <Suspense fallback={null}>
                        <Plane />
                    </Suspense>
                    <Environment preset="sunset" />
                </Canvas>
                <button className="choose-button choose-button2" onClick={modelSelected}>Choose Model 2</button>
            </div>
        </div>
    );
}

export default PlaneView;
