"use client";
import React, { useCallback, useMemo, useState, useReducer } from 'react';
import { useDropzone } from 'react-dropzone';
import { postData } from '../utils/utils';
const baseStyle = {

};

const activeStyle = {
  backgroundColor: '#000',
  opacity: "100%"
};

const acceptStyle = {
  // borderColor: '#0f0'
};

const rejectStyle = {
  // borderColor: '#f00'
};

function DropzoneComponent(props) {
  const [, forceUpdate] = useReducer(x => x + 1, 0);
  const [src, setSrc] = useState("");
  const [imgSrc, setImgSrc] = useState("");
  const [loading, setLoading] = useState(false);

  const onDrop = acceptedFiles => {
    setLoading(true);
    // convert file to base64
    const reader = new FileReader();
    let base64 = "";
    reader.readAsDataURL(acceptedFiles[0]);
    setImgSrc(URL.createObjectURL(acceptedFiles[0]));
    reader.onload = () => {
      base64 = reader.result;
      setSrc("")
      let res = postData({ "imgBase64": base64 })
      res.then((res) => {
        if (res.status === "ok") {
          fetch("http://localhost:5000/getSong", {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
              "Accept": "application/json"
            }
          }).then((res) => {
            // return res.json();
            setSrc("http://localhost:5000/getSong");
          setLoading(false);
          }).then((res) => {
            
          })

          
        }

      })
    };
    reader.onerror = function (error) {
      console.log('Error: ', error);
      base64 = null;
    };



  };

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

    <div className='flex flex-col justify-center items-center gap-8'>
      {
        imgSrc && (
          <div className='relative flex flex-col items-center justify-center w-96 h-96  rounded-xl bg-black'>
            <img src={imgSrc} alt="img" className='w-96 h-96 rounded-xl' />
            {
              loading && <div className='absolute flex w-full h-full text-white bg-black opacity-75 items-center justify-center'>Loading...</div>
            }
          </div>
        )
      }
      {
        !imgSrc && <div {...getRootProps({ style })}
          className='flex flex-col items-center justify-center w-96 h-96 border-4 border-gray-200 border-dashed rounded-xl bg-black opacity-25'
        >
          <input {...getInputProps()} />
          <div>Drag and drop your images here.</div>
        </div>
      }

      <audio controls src={src}></audio>

    </div>
  )
}

export default DropzoneComponent;


