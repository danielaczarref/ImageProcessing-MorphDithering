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