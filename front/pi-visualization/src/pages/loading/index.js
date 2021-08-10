import '../../App.css';
import Lottie from 'react-lottie'
import loadingData from '../../resources/loading.json'
import { useHistory } from 'react-router-dom'

 export const Loading = () => {
  const history = useHistory()

  const defaultOptions = {
    loop: true,
    autoplay: true,
    animationData: loadingData,
    rendererSettings: {
      preserveAspectRatio: 'xMidYMid slice'
    }
  }

  setTimeout(() => {
    history.push('home')
  }, 5000)

  return (
    <div className="App">
      <header className="App-header">
        <Lottie 
          options={defaultOptions}
          height={'60%'}
          width={'60%'}
        />
      </header>
    </div>
  );
}