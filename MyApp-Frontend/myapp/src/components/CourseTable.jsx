// CourseTable.jsx
import React, { useState, useEffect } from 'react';
import Axios from 'axios';
import '../styles/CourseTable.css';
import '../styles/font.css';

const CourseTable = () => {
  // 添加一个状态变量作为触发器，在数据更改时重新获取数据
  const [dataUpdateTrigger, setDataUpdateTrigger] = useState(0);

  const [rows, setRows] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [showActions, setShowActions] = useState(false);
  const [showInputRow, setShowInputRow] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await Axios.get('http://172.25.3.49:5000//api/courses');
        if (response.status === 200) {
          const data = response.data;
          if (Array.isArray(data.courses)) {
            setRows(data.courses); // 提取出数组部分
          } else {
            setError(`从后端获取数据时出现问题：数据不是数组！实际返回数据：${JSON.stringify(data)}`);
          }
          setLoading(false); // 数据加载完成
        } else {
          setError('从后端获取数据时出现问题！');
        }
      } catch (error) {
        setError('连接后端时出现错误：' + error.message);
      }
    };

    fetchData();
  }, [dataUpdateTrigger]); // 将 dataUpdateTrigger 添加为依赖项

  const [newName, setNewName] = useState('');
  const [newTime, setNewTime] = useState('');
  const [newLocation, setNewLocation] = useState('');

  const addRow = async () => {
    if (!showActions) {
      setShowActions(true);
      setShowInputRow(true);
      setNewName(''); // Reset the new values to empty when adding a new row
      setNewTime('');
      setNewLocation('');
      setRows((prevRows) => [...prevRows, { time: '', name: '', location: '' }]);
    } else {
      const newRow = { time: newTime, name: newName, location: newLocation }; // Use the new values here
      try {
        const response = await Axios.post('http://172.25.3.49:5000//api/courses', newRow, {
          headers: {
            'Content-Type': 'application/json',
          },
        });
        if (response.status === 200) {
          const data = response.data;
          console.log('数据已保存到后端！课程ID：', data.course_id);
          const updatedRows = [...rows];
          updatedRows[updatedRows.length - 1].course_id = data.course_id;
          setRows(updatedRows);
        } else {
          setError('保存数据到后端时出现问题！');
        }
      } catch (error) {
        setError('连接后端时出现错误：' + error.message);
      }
      setShowActions(false);
      setShowInputRow(false);
      setDataUpdateTrigger((prevTrigger) => prevTrigger + 1); // 触发数据更新
    }
  };

  const handleNewNameChange = (e) => {
    setNewName(e.target.value);
  };

  const handleNewTimeChange = (e) => {
    setNewTime(e.target.value);
  };

  const handleNewLocationChange = (e) => {
    setNewLocation(e.target.value);
  };

  const deleteRow = async (index) => {
    if (index < 0 || index >= rows.length) {
      console.error('无法删除：行索引无效！');
      return;
    }
  
    const rowToDelete = rows[index];
    const courseId = rowToDelete.id;
  
    if (!courseId) {
      console.error('无法删除：缺少有效的课程ID！');
      return;
    }
  
    try {
      const response = await Axios.delete(`http://172.25.3.49:5000//api/courses/${courseId}`);
      if (response.status === 200) {
        console.log(`数据已从后端删除！课程ID：${courseId}`);
        setDataUpdateTrigger((prevTrigger) => prevTrigger + 1); // 触发数据更新
      } else {
        setError('删除数据时出现问题！');
      }
    } catch (error) {
      setError('连接后端时出现错误：' + error.message);
    }
  };
  
  
  
  // const updateRow = (index, field, value) => {
  //   const updatedRows = [...rows];
  //   updatedRows[index][field] = value;
  //   setRows(updatedRows);
  // };

  if (loading) {
    return <div>Loading...</div>;
  };
  
  if (error) {
    return <div>Error: {error}</div>;
  };
  
  if (!Array.isArray(rows) || rows.length === 0) {
    return <div>No courses found.</div>;
  };

  return (
    <div className="table-container">
      <table className="course-table">
        <thead>
          <tr>
            <th>時間</th>
            <th>授業名</th>
            <th>場所</th>
            {showActions && <th>操作</th>}
          </tr>
        </thead>
        <tbody>
          {rows.map((row, index) => (
            <tr key={index}>
              <td>
                {showInputRow ? (
                  <input
                    type="text"
                    value={index === rows.length - 1 ? newName : row.name} // Use the new value for the last row
                    onChange={handleNewNameChange}
                  />
                ) : (
                  row.name
                )}
              </td>
              <td>
                {showInputRow ? (
                  <input
                    type="text"
                    value={index === rows.length - 1 ? newTime : row.time} // Use the new value for the last row
                    onChange={handleNewTimeChange}
                  />
                ) : (
                  row.time
                )}
              </td>
              <td>
                {showInputRow ? (
                  <input
                    type="text"
                    value={index === rows.length - 1 ? newLocation : row.location} // Use the new value for the last row
                    onChange={handleNewLocationChange}
                  />
                ) : (
                  row.location
                )}
              </td>
              {showActions && (
                <td>
                  <button onClick={() => deleteRow(index)}>削除</button>
                </td>
              )}
            </tr>
          ))}
        </tbody>
      </table>
      <div className="button-area">
        <button onClick={addRow} className="button">
          {showInputRow ? '登録完了' : 'コース登録'}
        </button>
        {!showActions && (
          <button onClick={() => setShowActions(true)} className="button">
            コース削除
          </button>
        )}
        {showActions && (
          <button onClick={() => setShowActions(false)} className="button">
            削除完了
          </button>
        )}
      </div>
    </div>
  );
};

export default CourseTable;
