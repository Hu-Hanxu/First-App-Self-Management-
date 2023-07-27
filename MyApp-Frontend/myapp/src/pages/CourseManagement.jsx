import React from "react";
import "../styles/CourseManagement.css";
import { useNavigate } from "react-router-dom";
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import CourseTable from '../components/CourseTable'

const CourseManagement = () => { 
    const navigate = useNavigate();

    const handleGoBack = () => {
        navigate(-1);
    };
    return (
        <>
            <div className='area'>
            <div className='back-btn' onClick={handleGoBack}><ArrowBackIcon className='ArrowBackIcon'/></div>
                <h1 className='title'>コース管理</h1>
                <div className='list-area'>
                    <CourseTable />
                </div>
                <div className='mb'></div>
            </div>
        </>
    )
};
export default CourseManagement;