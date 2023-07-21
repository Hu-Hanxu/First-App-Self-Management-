import React from 'react';
import '../styles/main.css';
import { useNavigate } from 'react-router-dom';


const Main = () => {
  const navigate = useNavigate();

  const handleStudyManagement = () => {
    navigate('/study');
  };

  const handleScheduleManagement = () => {
    navigate('/schedule');
  };

  const handleChoiceHelper = () => {
    navigate('/choice');
  };

  return (
    <div className='area'>
      <h1 className='title'>自己管理システム</h1>
      <div className='card-area'>
        <div className='card' onClick={handleStudyManagement}>
          <img className='img' src="/images/lesson.png" alt='学習管理'/>
          <p className='text'>学習管理</p>
          <div className='border-top'/>
        </div>
        <div className='card' onClick={handleScheduleManagement}>
          <img className='img' src="/images/schedule.png" alt='日程管理'/>
          <p className='text'>日程管理</p>
          <div className='border-top'onClick={handleChoiceHelper}/>
        </div>
        <div className='card'>
          <img className='img' src="/images/choice.png" alt='選択ヘルパー'/>
          <p className='text'>選択ヘルパー</p>
          <div className='border-top'/>
        </div>
      </div>
    </div>
  );
};
export default Main;