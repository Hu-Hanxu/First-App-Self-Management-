import React from 'react';
import '../styles/main.css';
import { useNavigate } from 'react-router-dom';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';


const StudyManagement = () => {
  const navigate = useNavigate();

  const handleCourseManagement = () => {
    navigate('/course');
  };

  const handleSubjectManagement= () => {
    navigate('/subject');
  };

  const handleTestManagement = () => {
    navigate('/test');
  };

  const handleGoBack = () => {
    navigate(-1);
  };

  return (
    <div className='area'>
      <div className='back-btn' onClick={handleGoBack}><ArrowBackIcon className='ArrowBackIcon'/></div>
      <h1 className='title'>学習管理</h1>
      <div className='card-area'>
        <div className='card' onClick={handleCourseManagement}>
          <img className='img' src="/images/online-lesson.png" alt='コース管理'/>
          <p className='text'>コース管理</p>
          <div className='border-top'/>
        </div>
        <div className='card' onClick={handleSubjectManagement}>
          <img className='img' src="/images/homework.png" alt='課題管理'/>
          <p className='text'>課題管理</p>
          <div className='border-top'/>
        </div>
        <div className='card' onClick={handleTestManagement}>
          <img className='img' src="/images/test.png" alt='テスト管理'/>
          <p className='text'>テスト管理</p>
          <div className='border-top'/>
        </div>
      </div>
    </div>
  );
};
export default StudyManagement;