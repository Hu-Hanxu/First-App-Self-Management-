from flask import Flask, request, jsonify,Blueprint
from database import db
from courseModels import Course

api1 = Blueprint('api1', __name__)

@api1.route('/api/courses', methods=['POST'])
def add_course():
    course_data = request.get_json()
    course_name = course_data.get('name')
    course_time = course_data.get('time')
    course_location = course_data.get('location')

    if not course_name or not course_time or not course_location:
        return jsonify({'error': '授業名、時間、場所は空欄できないよo.O'})

    # 创建课程对象并保存到数据库
    course = Course(name=course_name, time=course_time, location=course_location)
    db.session.add(course)
    db.session.commit()

    return jsonify({'message': '授業登録成功！', 'course_id': course.id})


