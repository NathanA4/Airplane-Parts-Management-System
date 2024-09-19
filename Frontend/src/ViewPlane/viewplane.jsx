import React from "react";
import { Canvas } from '@react-three/fiber';
import { useState, Suspense } from "react";
import { Environment, OrbitControls } from '@react-three/drei';
import Model from '../../public/Cirrussr22'
import './viewplane.css'

function plane() {
    const [count, setCount] = useState(0)

    return(
        <>
         <Canvas>
            <ambientLight intensity={0.2}/>
            <OrbitControls />
            <Suspense fallback={null}>
                <Model/>
            </Suspense>
            <Environment preset="sunset"/>
         </Canvas>
        </>
    )
}

export default plane;