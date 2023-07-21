import React from 'react';
import '../App.css';
import '../styles/main.css';
import { Card } from '@mui/material';

const MainPage = () => {
  const handleStudyManagement = () => {
    // 学習管理画面に飛ぶ
  };

  const handleScheduleManagement = () => {
    // 日程管理画面に飛ぶ
  };

  const handleChoiceHelper = () => {
    // 選択ヘルパー画面に飛ぶ
  };

  return (
    <div className='area'>
      <h1 className='title'>自己管理システム</h1>
      <div className='card-area'>
        <Card className='card'>
          <img className='img' src="/MyApp-Frontend/myapp/src/images/lesson.png" alt='学習管理'/>
          <p className='text'>学習管理</p>
          <div className='border-top'/>
        </Card>
        <Card className='card'>
          <img className='img' src="/MyApp-Frontend/myapp/src/images/schedule.png" alt='日程管理'/>
          <p className='text'>日程管理</p>
          <div className='border-top'/>
        </Card>
        <Card className='card'>
          <img className='img' src="/MyApp-Frontend/myapp/src/images/choice.png" alt='選択ヘルパー'/>
          <p className='text'>選択ヘルパー</p>
          <div className='border-top'/>
        </Card>
      </div>
    </div>
  );
}

const styles = {
};
export default MainPage;