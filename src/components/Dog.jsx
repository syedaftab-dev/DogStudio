import React from 'react'
import { Canvas } from '@react-three/fiber' // this will contain the 3js file renderer created
export const Dog = () => {
  return (
    <Canvas>
        <mesh>
            <meshBasicMaterial color={0x00FF00}/>
            <boxGeometry args={[1,1,1]}/>
        </mesh>
        {/* ithne se code se humne camera,light aur ek cube baneye with the help of rect-three/fiber */}
    </Canvas>
  )
}
