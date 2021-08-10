import styled, { css } from 'styled-components';

export const HomeContainer = styled.div`
  flex: 1;
  margin: 16px;
  max-width: 95%;
`;

export const ContainerInfo = styled.div`
  display: flex;
  flex-direction: column;
  margin-bottom: 8px;
`;

export const Titulo = styled.span`
  color: #202029
  font-weight: 600;
  font-size: 28px;
`;

export const Subtitulo = styled.span`
  color: #202029
  font-weight: 400;
  font-size: 20px;
`

const dragActive = css`
  border-color: #6debfc;
`;

const dragReject = css`
  border-color: #fc876d;
`;

export const ContainerStyle = styled.div`
  margin-top: 80px;
  margin: 40px;
`;

export const DropContainer = styled.div.attrs({
  className: "dropzone"
})`
display: flex;
justify-content: center;
align-items: center;
border: 3px dashed #DDDDDD;
border-radius: 20px;
min-height: 100px;
cursor: pointer;

transition: height 0.2s ease;

${props => props.isDragActive && dragActive}
${props => props.isDragReject && dragReject}
`;

const messageColors = {
  default: '#adb7b9',
  error: '#fc876d',
  success:  '#6debfc',
};

export const UploadMessage = styled.div`
  display: flex;
  color: ${props => messageColors[props.type || 'default']};
  justify-content: center;
  align-items: center;
  padding: 15px 0px;
`;

export const ContainerDisplay = styled.div`
  flex: 1;
`;

export const ContainerOptions = styled.div`
  display: flex;
  flex-direction: row;
  margin-bottom: 8px;
  justify-content: space-between;
`;

export const ContainerLottie = styled.div`
  width: 50%;
  position: absolute;
  right: 0;
  bottom: 20px;
`;

export const Tab = styled.div`
background-color: transparent;
padding: 8px;
border: none;
cursor: pointer;
margin: 0px 8px;
font-size: 22px;
color: ${props => props.active ? '#60435F' : '#737385'};
font-weight: ${props => props.active ? 600 : 400};
border-bottom: ${props => props.active ? 'solid #D67AB1' : 'solid transparent'};

&:hover {
  border-bottom: 'solid #D67AB1';
}
`;

export const Button = styled.button`
  height: ${props => props.height ? `${props.height}px` : '48px'};
  min-height: ${props => props.minHeight ? `${props.minHeight}px` : null};
  width: ${props => props.width ? `${props.width}px` : null};
  background-color: ${props => props.backgroundColor || '#D67AB1'};
  border-style: none;
  border-radius: var(--radius);
  color: white;
  padding-left: 16px;
  padding-right: 16px;
  font-size: 14pt;
  cursor: pointer;
  margin: ${props => props.margin ? `${props.margin}` : null};
  outline: 0;
  text-transform: uppercase;

  &:hover {
      opacity: 0.9
  }
`;

export const Teste = styled.div`
  flex-direction: row;
  display: flex;
  flex: 1;
`;

export const ContainerButtons = styled.div`
  flex: 1;
  flex-direction: column;
  margin: 24px;
`;