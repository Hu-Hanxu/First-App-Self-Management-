// EventTable.jsx

import React, { useState, useEffect } from 'react';
import axios from 'axios';

const EventTable = () => {
  const [events, setEvents] = useState([]);
  const [newEvent, setNewEvent] = useState('');
  const [newTime, setNewTime] = useState('');
  const [showActionColumn, setShowActionColumn] = useState(false);

  const formatDate = (dateString) => {
    const date = new Date(dateString);
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
  };

  useEffect(() => {
    // 获取事件列表数据
    axios
      .get('http://172.25.3.49:5000/api/events')
      .then((response) => {
        setEvents(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  const handleAddEvent = () => {
    const newEventData = {
      name: newEvent,
      date: newTime,
    };

    axios
      .post('http://172.25.3.49:5000/api/events', newEventData, {
        headers: {
          'Content-Type': 'application/json', // 设置请求头为 JSON 格式
        },
      })
      .then((response) => {
        console.log(response.data);
        setEvents((prevEvents) => [
          ...prevEvents,
          { id: response.data.event_id, name: newEvent, time: newTime },
        ]);
        setNewEvent('');
        setNewTime('');
      })
      .catch((error) => {
        console.error(error);
      });
  };

  const handleDeleteEvent = (id) => {
    axios
      .delete(`http://172.25.3.49:5000/api/events/${id}`)
      .then((response) => {
        console.log(response.data);
        setEvents((prevEvents) => prevEvents.filter((event) => event.id !== id));
      })
      .catch((error) => {
        console.error(error);
      });
  };

  const handleToggleActionColumn = () => {
    setShowActionColumn((prevValue) => !prevValue);
  };

  return (
    <div className='event-area'>
      <div className='event-input'>
        <input
          type='text'
          value={newEvent}
          onChange={(e) => setNewEvent(e.target.value)}
          placeholder='事項'
        />
        <input
          type='date'
          value={newTime}
          onChange={(e) => setNewTime(e.target.value)}
          placeholder='時間'
        />
        <button onClick={handleAddEvent}>事项登録</button>
      </div>
      <div className='management-container'>
        <table className='event-table'>
          <thead>
            <tr>
              <th>事項</th>
              <th>時間</th>
              {showActionColumn && <th>操作</th>}
            </tr>
          </thead>
          <tbody>
            {events.map((event, index) => (
              <tr key={index}>
                <td>{event.name}</td>
                <td>{formatDate(event.date)}</td>
                {showActionColumn && (
                  <td>
                    <button onClick={() => handleDeleteEvent(event.id)}>削除</button>
                  </td>
                )}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <div className='mb'></div>
      <div className='action-button-container-event'>
        <button className='action-button' onClick={handleToggleActionColumn}>
          {showActionColumn ? '削除完了' : '事項削除'}
        </button>
      </div>
    </div>
  );
};

export default EventTable;
