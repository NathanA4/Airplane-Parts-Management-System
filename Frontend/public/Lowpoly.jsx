/*
Auto-generated by: https://github.com/pmndrs/gltfjsx
Command: npx gltfjsx@6.5.2 lowpoly.gltf 
Author: MaX3Dd (https://sketchfab.com/MaX3Dd)
License: CC-BY-4.0 (http://creativecommons.org/licenses/by/4.0/)
Source: https://sketchfab.com/3d-models/low-poly-airplane-65cc7c4349174f7bbb20ed70206377b5
Title: Low-poly Airplane
*/

import React from 'react'
import { useGLTF } from '@react-three/drei'

export default function Plane(props) {
  const { nodes, materials } = useGLTF('/lowpoly.gltf')
  return (
    <group {...props} dispose={null}>
      <group position={[-0.007, 16.617, -23.697]} scale={10}>
        <mesh geometry={nodes.awionetka_airplane_0.geometry} material={materials.airplane} position={[0.001, -1.662, 2.37]} />
      </group>
    </group>
  )
}

useGLTF.preload('/lowpoly.gltf')
