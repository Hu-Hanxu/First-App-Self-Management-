import React from 'react';
import '../App.css';
import '../styles/main.css';
import Button from '@mui/material/Button';

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
    <div className='container'>
      <h1 style={styles.title}>Name Name</h1>
      <div className="button-container">
        <Button variant='contained' style={styles.Button} onClick={handleStudyManagement}>学習管理</Button>
      </div>
      <div className="button-container">
        <Button variant='contained' style={styles.Button} onClick={handleScheduleManagement}>日程管理</Button>
      </div>
      <div className="button-container">
        <Button variant='contained' style={styles.Button} onClick={handleChoiceHelper}>選択ヘルパー</Button>
      </div>
    </div>
  );
}

const styles = {
  title: {
    fontSize: '50px',
    color: '#64affa',
    textAlign: 'center',
    margin: '50px'
  },
  Button: {
    margin: '20px',
    width: '300px',
    height: '80px',
    fontSize: '20px',
    backgroundColor: '#64affa'
  },
};
export default MainPage;