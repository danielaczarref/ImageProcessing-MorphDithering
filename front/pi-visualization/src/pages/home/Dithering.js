import React from 'react';
import '../../App.css';
import { webservice } from '../../controller/webservice';
import * as SC from './styles';

export default function Dithering() {

  function getLimiarSimples() {
    webservice('http://127.0.0.1:5000').get('/dithering/testSimpleThreshold')
  }

  function getModulacaoAleatoria() {
    webservice('http://127.0.0.1:5000').get('/dithering/testRandomModulation')
  }

  function getModulacaoAglomerada() {
    webservice('http://127.0.0.1:5000').get('/dithering/testModOrderedAglomeration')
  }

  function getModulacaoDispersa() {
    webservice('http://127.0.0.1:5000').get('/dithering/testModOrderedDispersion')
  }

  function getModulacaoAperiodica() {
    webservice('http://127.0.0.1:5000').get('/dithering/testModOrderedAperiodicDispersed')
  }

  return (
    <SC.HomeContainer>
      <SC.ContainerButtons>
        <SC.Button onClick={() => getLimiarSimples()}  margin={16}>Limiar simples</SC.Button>
      </SC.ContainerButtons>
      <SC.ContainerButtons>
        <SC.Button onClick={() => getModulacaoAleatoria()}  margin={16}>Limiar com modulação aleatória</SC.Button>
      </SC.ContainerButtons>
      <SC.ContainerButtons>
        <SC.Button onClick={() => getModulacaoAglomerada()}  margin={16}>Limiar com modulação ordenada periódico aglomerado</SC.Button>
      </SC.ContainerButtons>
      <SC.ContainerButtons>
        <SC.Button onClick={() => getModulacaoDispersa()}  margin={16}>Limiar com modulação ordenada periódico disperso</SC.Button>
      </SC.ContainerButtons>
      <SC.ContainerButtons>
        <SC.Button onClick={() => getModulacaoAperiodica()}  margin={16}>Limiar com modulação ordenada aperiódico</SC.Button>
      </SC.ContainerButtons>
    </SC.HomeContainer>
  );
}