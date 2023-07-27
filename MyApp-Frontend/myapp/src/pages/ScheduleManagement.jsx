// ScheduleManagement.jsx
import React, { useState, useEffect } from 'react';
import "../styles/ScheduleManagement.css";
import { useNavigate } from 'react-router-dom';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import Calendar from '../components/Calendar';
import axios from 'axios';

const ScheduleManagement = () => { 
    const navigate = useNavigate();

    const handleGoBack = () => {
        navigate(-1);
    };

    const [events, setEvents] = useState([]);

    useEffect(() => {
        // Fetch event data and set the state
        axios
            .get('http://172.25.3.49:5000/api/events')
            .then((response) => {
                setEvents(response.data);
            })
            .catch((error) => {
                console.error(error);
            });
    }, []);

    return (
        <>
            <div className='area'>
                <div className='back-btn' onClick={handleGoBack}><ArrowBackIcon className='ArrowBackIcon'/></div>
                <h1 className='title'>日程管理</h1>
                <div className='calendar-area'>
                    {/* Pass the 'events' prop to the Calendar component */}
                    <Calendar events={events} />
                </div>
                <div className="mb" />
            </div>
        </>
    )
};

export default ScheduleManagement;