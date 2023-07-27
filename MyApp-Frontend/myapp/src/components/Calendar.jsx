// Calendar.jsx
import React, { useState } from 'react';
import { format, startOfMonth, eachDayOfInterval, isSameMonth, isToday, getDay, isSameDay } from 'date-fns';
import { Link, useNavigate } from 'react-router-dom';
import '../styles/Calendar.css';
import '../styles/font.css';
import IconButton from '@mui/material/IconButton';
import ChevronLeftIcon from '@mui/icons-material/ChevronLeft';
import ChevronRightIcon from '@mui/icons-material/ChevronRight';

const Calendar = ({events}) => {
  const today = new Date();
  const firstDayOfMonth = startOfMonth(today);
  const [currentMonth, setCurrentMonth] = useState(firstDayOfMonth);
  const navigate = useNavigate();

  // 跳转到事件管理
  const handleEventManagement = (date) => {
    const hasEvent = hasOverlappingEvents(date);
    if (hasEvent) {
      navigate('/event');
    }
  };  

  // 获取本月的所有日期
  const getDaysOfMonth = (date) => {
    const start = startOfMonth(date);
    const end = new Date(start.getFullYear(), start.getMonth() + 1, 0);
    return eachDayOfInterval({ start, end });
  };

  // 获取上个月剩余的日期
  const getRemainingDaysOfPrevMonth = () => {
    const prevMonthLastDay = new Date(currentMonth.getFullYear(), currentMonth.getMonth(), 0);
    const start = new Date(prevMonthLastDay.getFullYear(), prevMonthLastDay.getMonth(), prevMonthLastDay.getDate() - getDay(currentMonth) + 1);
    return eachDayOfInterval({ start, end: prevMonthLastDay });
  };

  // 获取下个月剩余的日期
  const getRemainingDaysOfNextMonth = () => {
    const lastDayOfMonth = new Date(currentMonth.getFullYear(), currentMonth.getMonth() + 1, 0);
    const end = new Date(lastDayOfMonth.getFullYear(), lastDayOfMonth.getMonth(), lastDayOfMonth.getDate() + 6 - getDay(lastDayOfMonth));
    const nextMonthFirstDay = new Date(lastDayOfMonth.getFullYear(), lastDayOfMonth.getMonth() + 1, 1);
    return eachDayOfInterval({ start: nextMonthFirstDay, end });
  };

  // 组合本月、上个月和下个月的日期
  const daysOfMonth = [...getRemainingDaysOfPrevMonth(), ...getDaysOfMonth(currentMonth), ...getRemainingDaysOfNextMonth()];

  const weekdays = ['日', '月', '火', '水', '木', '金', '土'];

  // Function to check if a date has overlapping events
  const hasOverlappingEvents = (date) => {
    const overlappingEvents = events.map(event => new Date(event.date));
    return overlappingEvents.some((eventDate) => isSameDay(eventDate, date));
  };
  

  // Function to navigate to the previous month
  const handlePrevMonth = () => {
    const prevMonth = new Date(currentMonth.getFullYear(), currentMonth.getMonth() - 1, 1);
    setCurrentMonth(prevMonth);
  };

  // Function to navigate to the next month
  const handleNextMonth = () => {
    const nextMonth = new Date(currentMonth.getFullYear(), currentMonth.getMonth() + 1, 1);
    setCurrentMonth(nextMonth);
  };

  return (
    <div className="calendar-container">
      <div className="calendar-nav">
        <div style={{ display: 'flex', flexDirection: 'row' }}>
          <IconButton onClick={handlePrevMonth} style={{ margin: 'auto' }}>
            <ChevronLeftIcon />
          </IconButton>
          <h2 className="calendar-title">{format(currentMonth, 'MMMM yyyy')}</h2>
          <IconButton onClick={handleNextMonth} style={{ margin: 'auto' }}>
            <ChevronRightIcon />
          </IconButton>
        </div>
      </div>
      <div className="calendar">
        <div className="calendar-weekdays">
          {weekdays.map((weekday, index) => (
            <div key={index} className="calendar-weekday">
              {weekday}
            </div>
          ))}
        </div>
        <div className="calendar-grid">
          {daysOfMonth.map((date, index) => (
            <div
              key={index}
              className={`calendar-day ${isSameMonth(date, currentMonth) ? '' : 'outside-month'} ${
                isToday(date) ? 'today' : ''
              } ${hasOverlappingEvents(date) ? 'overlap' : ''}`}
              onClick={() => handleEventManagement(date)}
            >
              {format(date, 'dd')}
            </div>
          ))}
        </div>
        <div className="calendar-buttons">
          <Link to="/mark" className="calendar-button">
            打刻管理
          </Link>
          <Link to="/event" className="calendar-button">
            事項管理
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Calendar;
