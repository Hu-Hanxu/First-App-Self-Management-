from flask import Flask, request, jsonify, redirect, url_for,Blueprint
from database import db
from subjectModels import Subject

api4 = Blueprint('api4', __name__)

@api4.route('/api4/subjects', methods=['DELETE'])
def delete_courses():
    # 从请求中获取要删除的课程信息
    subject_data = request.json.get('subjects', [])
    
    # 将课程ID和勾选状态分开成两个列表
    subject_ids = [data['id'] for data in subject_data if data['is_selected']]
    
    # 验证是否提供了要删除的课程信息
    if not subject_ids:
        return jsonify({'error': '削除する課題を選択されていないよO.o'})

    try:
        # 根据课程ID删除对应的课程信息
        for subject_id in subject_ids:
            subject = Subject.query.get(subject_id)
            if subject:
                db.session.delete(subject)

        db.session.commit()
        return jsonify({'message': '削除できた!!<(￣︶￣)>!'})

    except Exception as e:
        db.session.rollback()
        return redirect(url_for('previous_page'))  # 返回到上一个页面

@api4.route('/previous-page')
def previous_page():
    # 根据前端逻辑返回到上一个页面或重定向到特定页面
    return redirect(url_for('your_previous_page_route'))



