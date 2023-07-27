import React from "react";
import "../styles/CourseManagement.css";
import { useNavigate } from "react-router-dom";
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import EventTable from '../components/EventTable'

const EventManagement = () => { 
    const navigate = useNavigate();

    const handleGoBack = () => {
        navigate(-1);
    };
    return (
        <>
            <div className='area'>
            <div className='back-btn' onClick={handleGoBack}><ArrowBackIcon className='ArrowBackIcon'/></div>
                <h1 className='title'>事項管理</h1>
                <div className='list-area'>
                    <EventTable />
                </div>
                <div className='mb'></div>
            </div>
        </>
    )
};
export default EventManagement;