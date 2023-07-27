import React from "react";
import "../styles/CourseManagement.css";
import { useNavigate } from "react-router-dom";
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import MarkingTable from '../components/MarkingTable'

const MarkingManagement = () => { 
    const navigate = useNavigate();

    const handleGoBack = () => {
        navigate(-1);
    };
    return (
        <>
            <div className='area'>
            <div className='back-btn' onClick={handleGoBack}><ArrowBackIcon className='ArrowBackIcon'/></div>
                <h1 className='title'>打刻管理</h1>
                <div className='list-area'>
                    <MarkingTable />
                </div>
                <div className='mb'></div>
            </div>
        </>
    )
};
export default MarkingManagement;