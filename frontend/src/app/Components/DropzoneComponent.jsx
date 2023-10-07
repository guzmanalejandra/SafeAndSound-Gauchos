"use client";
import React, { useCallback, useMemo } from 'react';
import { useDropzone } from 'react-dropzone';
import { postData } from '../utils/utils';
const baseStyle = {
  
};

const activeStyle = {
  backgroundColor:'#000',
  opacity:"100%"
};

const acceptStyle = {
  // borderColor: '#0f0'
};

const rejectStyle = {
  // borderColor: '#f00'
};

function DropzoneComponent(props) {
  const onDrop = useCallback(acceptedFiles => {
    // convert file to base64
    const reader = new FileReader();
    let base64="";
    reader.readAsDataURL(acceptedFiles[0]);
    reader.onload = () => {
      base64 = reader.result;
      postData({"imgBase64":base64})
    };
    reader.onerror = function (error) {
      console.log('Error: ', error);
      base64=null;
    };
    





    


  }, []);

  const {
    getRootProps,
    getInputProps,
    isDragActive,
    isDragAccept,
    isDragReject
  } = useDropzone({
    onDrop,
    accept: 'image/*'
  });

  const style = useMemo(() => ({
    ...baseStyle,
    ...(isDragActive ? activeStyle : {}),
    ...(isDragAccept ? acceptStyle : {}),
    ...(isDragReject ? rejectStyle : {})
  }), [
    isDragActive,
    isDragReject,
    isDragAccept
  ]);

  return (
    <div {...getRootProps({style})}
      className='flex flex-col items-center justify-center w-96 h-96 border-4 border-gray-200 border-dashed rounded-xl bg-black opacity-25'
    >
      <input {...getInputProps()} />
      <div>Drag and drop your images here.</div>
    </div>
  )
}

export default DropzoneComponent;


