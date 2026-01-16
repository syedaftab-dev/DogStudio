import React from 'react'
import { Canvas, useThree } from '@react-three/fiber' // this will contain the 3js file renderer created
import { OrbitControls } from '@react-three/drei'


export const Dog = () => {

    useThree(({camera,scene,gl})=>{
      console.log(camera.position)
    })

  return (
    <>
        {/* ithne se code se humne camera,light aur ek cube baneye with the help of rect-three/fiber */}
        <mesh>
            <meshBasicMaterial color={0x00FF00}/>
            <boxGeometry args={[1,1,1]}/>
        </mesh>
        <OrbitControls />  {/* this will allow us to rotate the camera around the object */}
    </>
    )
}

