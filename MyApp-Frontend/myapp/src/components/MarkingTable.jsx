// MarkingTable.jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const MarkingTable = () => {
  // State：用于保存打刻目标的列表
  const [markingTargets, setMarkingTargets] = useState([]);

  // State：用于管理输入字段
  const [newTarget, setNewTarget] = useState('');

  // State：用于控制操作列的显示与隐藏
  const [showActionColumn, setShowActionColumn] = useState(false);

  // 使用 useEffect 发起 GET 请求来获取打刻目标的列表数据
  useEffect(() => {
    axios
      .get('http://172.25.3.49:5000/api/markings')
      .then((response) => {
        // 成功获取数据，更新状态中的打刻目标列表
        setMarkingTargets(response.data);
      })
      .catch((error) => {
        console.error(error);
        // 显示错误消息或其他错误处理逻辑
      });
  }, []); // 注意，这里的空数组作为第二个参数，表示只在组件加载时执行一次

  // 处理添加新的打刻目标
  const handleAddTarget = () => {
    const newTargetData = {
      target: newTarget,
      marking_check: false
    };

    axios
      .post('http://172.25.3.49:5000/api/markings', newTargetData, {
        headers: {
          'Content-Type': 'application/json', // 设置请求头为 JSON 格式
        },
      })
      .then((response) => {
        console.log(response.data); // 可以根据需要进行进一步处理
        setMarkingTargets((prevTargets) => [
          ...prevTargets,
          { id: response.data.marking_id, target: newTarget, marking_check: false },
        ]);
        setNewTarget('');
      })
      .catch((error) => {
        console.error(error);
        // 显示错误消息或其他错误处理逻辑
      });
  };

  // 处理打刻按钮点击事件
  const handleMarking = () => {
    // 构造向后端发送的数据
    const dataToSend = markingTargets.map((target) => ({
      id: target.id,
      target: target.target,
      marking_check: target.marking_check
    }));
  
    // 发送POST请求向后端更新数据
    axios
      .post('http://172.25.3.49:5000/api/markings', dataToSend, {
        headers: {
          'Content-Type': 'application/json', // 设置请求头为 JSON 格式
        },
      })
      .then((response) => {
        console.log(response.data); // 可以根据需要进行进一步处理
      })
      .catch((error) => {
        console.error(error);
        // 显示错误消息或其他错误处理逻辑
      });
  };
  

  // 处理切换打刻目标的选择状态
  const handleToggleCheck = (index) => {
    // 根据索引更新打刻目标的选择状态
    setMarkingTargets((prevTargets) =>
      prevTargets.map((target, i) => (i === index ? { ...target, marking_check: !target.checked } : target))
    );
  };

  // 处理删除打刻目标
  const handleDeleteTarget = (index) => {
    const markingIdToDelete = markingTargets[index].id;

    axios
      .delete(`http://172.25.3.49:5000/api/markings/${markingIdToDelete}`)
      .then((response) => {
        console.log(response.data); // 可以根据需要进行进一步处理
        setMarkingTargets((prevTargets) => prevTargets.filter((target, i) => i !== index));
      })
      .catch((error) => {
        console.error(error);
        // 显示错误消息或其他错误处理逻辑
      });
  };

  // 处理切换操作列的显示与隐藏
  const handleToggleActionColumn = () => {
    setShowActionColumn((prevValue) => !prevValue);
  };

  return (
    <div className='mark-area'>
        <div className="target-input">
          <input
            type="text"
            value={newTarget}
            onChange={(e) => setNewTarget(e.target.value)}
            placeholder="目標を入力してください"
          />
          <button onClick={handleAddTarget}>打刻登録</button>
        </div>
        <div className="management-container">
        <table className="target-table">
            <thead>
              <tr>
                <th>Check</th>
                <th>打刻目标</th>
                {showActionColumn && <th>操作</th>}
              </tr>
            </thead>
            <tbody>
            {markingTargets.map((target, index) => (
                <tr key={index}>
                <td>
                    <input
                    type="checkbox"
                    checked={target.marking_check}
                    onChange={() => handleToggleCheck(index)}
                    />
                </td>
                <td>{target.target}</td>
                {showActionColumn && (
                    <td>
                    <button onClick={() => handleDeleteTarget(index)}>削除</button>
                    </td>
                )}
                </tr>
            ))}
            </tbody>
        </table>
        </div>
        <div className="mark-action-button-container">
            <button className="marking-button" onClick={handleMarking}>打刻</button>
            <button className="action-button" onClick={handleToggleActionColumn}>
                {showActionColumn ? '削除完了' : '打刻削除'}
            </button>
        </div>
    </div>
  );
};

export default MarkingTable;
