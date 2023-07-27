import React , {useState} from 'react';
import '../styles/main.css';
import '../styles/font.css';
import { useNavigate } from 'react-router-dom';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';


const ChoiceHelper = () => {
  const navigate = useNavigate();
  const [choices, setChoices] = useState('');
  const [selectedChoice, setSelectedChoice] = useState('');
  const [showResult, setShowResult] = useState(false);
  const handleGoBack = () => {
    navigate(-1);
  };

  const handleInputChange = (event) => {
    setChoices(event.target.value);
  };

  const handleSelectChoice = () => {
    if (choices.trim() === '') {
      // 如果没有输入选择项，则不执行随机选择
      return;
    }
  
    const choicesArray = choices.split('、').map((choice) => choice.trim());
    const randomIndex = Math.floor(Math.random() * choicesArray.length);
    setSelectedChoice(choicesArray[randomIndex]);
    setShowResult(true);
  };
  
return (
  <div className='area'>
    <div className='back-btn' onClick={handleGoBack}>
      <ArrowBackIcon className='ArrowBackIcon' />
    </div>
    <h1 className='title'>選択ヘルパー</h1>
    <div className='choice-helper-content'>
      <p className='hint'>選択肢を入力するとき「、」で選択肢を分けてください</p>
      <div className='input-container'>
        <input
          type='text'
          placeholder='入力したら、下の「RANDOM」ボタンを押してください'
          value={choices}
          onChange={handleInputChange}
        />
      </div>
      <div className='choice-button' onClick={handleSelectChoice}>RANDOM</div>
      {showResult && (
        <div className='result-container'>
          <h3>結果:</h3>
          <p className='selectedChoice'>{selectedChoice}</p>
        </div>
      )}
    </div>
  </div>
);
};
export default ChoiceHelper;