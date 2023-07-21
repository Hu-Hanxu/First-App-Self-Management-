from flask import Flask, request, jsonify,Blueprint
from database import db
from subjectModels import Subject

api3 = Blueprint('api3', __name__)


@api3.route('/api/subjects', methods=['POST'])
def add_course():
    subject_data = request.get_json()
    subject_name = subject_data.get('subjectname')
    subject_deadline = subject_data.get('deadline')

    if not subject_name or not subject_deadline:
        return jsonify({'error': '課題名、締め切りは空欄できないよo.O'})

    # 创建课程对象并保存到数据库
    subject = Subject(subjectname=subject_name, deadline=subject_deadline)
    db.session.add(subject)
    db.session.commit()

    return jsonify({'message': '授業登録成功！(๑╹ヮ╹๑)ﾉ', 'subject_id': subject.id})

