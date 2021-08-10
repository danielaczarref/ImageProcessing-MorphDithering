import React from 'react';
import '../../App.css';
import { webservice } from '../../controller/webservice';
import * as SC from './styles';

export default function MorfoMono() {

  function getErosao() {
    webservice('http://127.0.0.1:5000').get('/morf-mono/testMorfMonoErode')
  }

  function getDilatacao(){
    webservice('http://127.0.0.1:5000').get('/morf-mono/testMorfMonoDilate')
  }

  function getAbertura(){
    webservice('http://127.0.0.1:5000').get('/morf-mono/testMorfMonoOpening')
  }

  function getFechamento(){
    webservice('http://127.0.0.1:5000').get('/morf-mono/testMorfMonoClosing')
  }

  function getGradiente() {
    webservice('http://127.0.0.1:5000').get('/morf-mono/testMorfMonoGradient')
  }

  return (
    <SC.HomeContainer>
      <SC.ContainerButtons>
        <SC.Button onClick={() => getErosao()} margin={16}>Erosão</SC.Button>
      </SC.ContainerButtons>
      <SC.ContainerButtons>
        <SC.Button onClick={() => getDilatacao()} margin={16}>Dilatação</SC.Button>
      </SC.ContainerButtons>
      <SC.ContainerButtons>
        <SC.Button onClick={() => getAbertura()} margin={16}>Abertura</SC.Button>
      </SC.ContainerButtons>
      <SC.ContainerButtons>
        <SC.Button onClick={() => getFechamento()} margin={16}>Fechamento</SC.Button>
      </SC.ContainerButtons>
      <SC.ContainerButtons>
        <SC.Button onClick={() => getGradiente()} margin={16}>Gradiente</SC.Button>
      </SC.ContainerButtons>
    </SC.HomeContainer>
  );
}