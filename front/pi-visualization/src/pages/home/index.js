import React, { useState } from 'react';
import '../../App.css';
import Dropzone from 'react-dropzone';
import { webservice } from '../../controller/webservice';
import * as SC from './styles';

export default function Home() {
  const [fileObj, setFileObj] = useState('');

  const handleUpload = file => {
    setFileObj(file)
    console.log('file: ', file)
    if (file.length > 0) {
      const data = new FormData();
      data.append('file', file)
      
      webservice('http://127.0.0.1:5000')
      .post('/dithering/testRandomModulation', data)
      .then((res) => {
        console.log('porra: ', res)
      })
    }
    // fetch('http://127.0.0.1:5000/dithering/testRandomModulation', {
    //   method: 'POST',
    //   body: data
    // }).then((res) => {
    //   console.log('teste: ', res)
    // })
  }

  const renderDragMessage = (isDragActive, isDragReject) => {
    if (!isDragActive) return <SC.UploadMessage>Por favor, selecione uma imagem</SC.UploadMessage>
    if (isDragReject) return <SC.UploadMessage type='error'>Arquivo não suportado. Envie apenas imagem.</SC.UploadMessage>
    return <SC.UploadMessage type='success'>Solte a imagem aqui</SC.UploadMessage>
  }

  return (
    <SC.HomeContainer>
      <SC.ContainerInfo>
        <SC.Titulo>Engenharia da Computação</SC.Titulo>
        <SC.Subtitulo>Processamento de Imagens - Daniela Carvalho</SC.Subtitulo>
      </SC.ContainerInfo> 
      <SC.ContainerStyle>   
      <Dropzone accept="image/*" onDropAccepted={handleUpload} >
        {({ getRootProps, getInputProps, isDragActive, isDragReject }) => (
          <SC.DropContainer {...getRootProps()} isDragActive={isDragActive} isDragReject={isDragReject}>
            <input {...getInputProps()} />
            {renderDragMessage(isDragActive, isDragReject)}
          </SC.DropContainer>
        )}
      </Dropzone>
      </SC.ContainerStyle>
    </SC.HomeContainer>
  );
}