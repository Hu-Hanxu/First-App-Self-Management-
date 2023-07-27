import React from "react";
import "../styles/SubjectManagement.css";
import { useNavigate } from "react-router-dom";
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import SubjectTable from '../components/SubjectTable'

const SubjectManagement = () => { 
    const navigate = useNavigate();

    const handleGoBack = () => {
        navigate(-1);
    };
    return (
        <>
            <div className='area'>
            <div className='back-btn' onClick={handleGoBack}><ArrowBackIcon className='ArrowBackIcon'/></div>
                <h1 className='title'>課題管理</h1>
                <div className='list-area'>
                    <SubjectTable />
                </div>
                <div className="mb"/>
            </div>
        </>
    )
};
export default SubjectManagement;