import React, { useState } from 'react';
import '../../App.css';
import Lottie from 'react-lottie'
import coding from '../../resources/coding.json'
import Dithering from './Dithering';
import MorfoBinaria from './MorfoBinaria';
import MorfoMono from './MorfoMono';
import * as SC from './styles';

export default function Home() {
  const [selected, setSelected] = useState(0);
  const defaultOptions = {
    loop: true,
    autoplay: true,
    animationData: coding,
    rendererSettings: {
      preserveAspectRatio: 'xMidYMid slice'
    }
  }

  const tabs = ['Dithering', 'Morfologia binária', 'Morfologia monocromática']
  return (
    <SC.HomeContainer>
      <SC.ContainerInfo>
        <SC.Titulo>Engenharia da Computação</SC.Titulo>
        <SC.Subtitulo>Processamento de Imagens - Daniela Carvalho Ferraz Nolasco Neves</SC.Subtitulo>
      </SC.ContainerInfo> 
      <SC.ContainerStyle>   
      <SC.ContainerDisplay>
        <SC.ContainerOptions>
          <SC.Teste>
          {tabs.map((tab, index) => 
          <SC.Tab 
            key={index}
            active={index === selected}
            onClick={() => setSelected(index)}
          >
            {tab}
          </SC.Tab>
          )}
          </SC.Teste>
        </SC.ContainerOptions>
        <SC.ContainerLottie>
          <Lottie 
            options={defaultOptions}
            height={'50%'}
            width={'80%'}
          />
        </SC.ContainerLottie>
        {selected === 0 && (
          <Dithering />
        )}
        {selected === 1 && (
          <MorfoBinaria />
        )}
        {selected === 2 && (
          <MorfoMono />
        )}
      </SC.ContainerDisplay>
      </SC.ContainerStyle>
    </SC.HomeContainer>
  );
}