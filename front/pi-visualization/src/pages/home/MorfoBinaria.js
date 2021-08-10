import React from 'react';
import '../../App.css';
import { webservice } from '../../controller/webservice';
import * as SC from './styles';

export default function MorfoBinaria() {

  function getErosao() {
    webservice('http://127.0.0.1:5000').get('/morf-bi/testMorfBiErode')
  }

  function getDilatacao() {
    webservice('http://127.0.0.1:5000').get('/morf-bi/testMorfBiDilate')
  }

  function getAbertura() {
    webservice('http://127.0.0.1:5000').get('/morf-bi/testMorfBiOpening')
  }

  function getFechamento() {
    webservice('http://127.0.0.1:5000').get('/morf-bi/testMorfBiClosing')
  }

  function getBordaInterna() {
    webservice('http://127.0.0.1:5000').get('/morf-bi/testMorfBiInternalBorder')
  }

  function getBordaExterna() {
    webservice('http://127.0.0.1:5000').get('/morf-bi/testMorfBiExternalBorder')
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
        <SC.Button onClick={() => getBordaInterna()} margin={16}>Borda interna</SC.Button>
      </SC.ContainerButtons>
      <SC.ContainerButtons>
        <SC.Button onClick={() => getBordaExterna()} margin={16}>Borda externa</SC.Button>
      </SC.ContainerButtons>
    </SC.HomeContainer>
  );
}