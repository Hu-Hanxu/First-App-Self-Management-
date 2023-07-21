from flask import Flask, request, jsonify, redirect, url_for,Blueprint
from database import db
from courseModels import Course

api2 = Blueprint('api2', __name__)


@api2.route('/api/courses', methods=['DELETE'])
def delete_courses():
    # 从请求中获取要删除的课程信息
    course_data = request.json.get('courses', [])
    
    # 将课程ID和勾选状态分开成两个列表
    course_ids = [data['id'] for data in course_data if data['is_selected']]
    
    # 验证是否提供了要删除的课程信息
    if not course_ids:
        return jsonify({'error': '削除する授業登を選択されていないよO.o'})

    try:
        # 根据课程ID删除对应的课程信息
        for course_id in course_ids:
            course = Course.query.get(course_id)
            if course:
                db.session.delete(course)

        db.session.commit()
        return jsonify({'message': '削除できた!!<(￣︶￣)>!'})

    except Exception as e:
        db.session.rollback()
        return redirect(url_for('previous_page'))  # 返回到上一个页面

@api2.route('/previous-page')
def previous_page():
    # 根据前端逻辑返回到上一个页面或重定向到特定页面
    return redirect(url_for('your_previous_page_route'))

