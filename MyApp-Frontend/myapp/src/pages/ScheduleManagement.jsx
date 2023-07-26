import React from "react";
import "../styles/ScheduleManagement.css";
import { useNavigate } from 'react-router-dom';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';

const ScheduleManagement = () => { 
    const navigate = useNavigate();

    const handleGoBack = () => {
        navigate(-1);
      };

    return (
        <>
            <div className='area'>
            <div className='back-btn' onClick={handleGoBack}><ArrowBackIcon className='ArrowBackIcon'/></div>
                <h1 className='title'>日程管理</h1>
                <div className='list-area'>
                
                </div>
                <div className="button-area">
                    <div className="button">打刻</div>
                    <div className="button">事項</div>
                </div>
                <div className="mb"/>
            </div>
        </>
    )
};
export default ScheduleManagement;