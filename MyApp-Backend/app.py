from flask import Flask, request, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from flask_cors import CORS
import psycopg2 as pg
app = Flask(__name__)
CORS(app)
scheduler = BackgroundScheduler()

# 配置信息
_DATABASE = 'mydatabase'  # 自分のデータベース名に変える
_USER = 'postgres'     # 自分のユーザー名に変える
_PASSWORD = '990218'   # 自分のパスワードに変える
_HOST = '127.0.0.1'
_PORT = '5432'

def connect_to_database():
    # 连接数据库
    try:
        con = pg.connect(user=_USER, password=_PASSWORD, host=_HOST, port=_PORT, database=_DATABASE)
        cur = con.cursor()
        return con, cur
    except pg.Error as e:
        print(f"データベース接続失败：{e}")
        return None, None

@app.route('/')
def index():
    return 'Welcome to OurApp!'



@app.route('/api/courses', methods=['GET'])
def get_courses():
    con, cur = connect_to_database()

    if con and cur:
        try:
            cur.execute("SELECT * FROM courses")
            courses = cur.fetchall()

            courses_json = []
            for course in courses:
                course_dict = {
                    'id': course[0],
                    'name': course[1],
                    'time': course[2],
                    'location': course[3]
                }
                courses_json.append(course_dict)

            return jsonify({'courses': courses_json})
        except pg.Error as e:
            print(f"データベースクエリが失敗しました：{e}")
            return jsonify({'error': 'データベースクエリが失敗しました'}), 500
        finally:
            cur.close()
            con.close()
    else:
        return jsonify({'error': 'データベースへアクセスが失敗しました'}), 500
    
@app.route('/api/subjects', methods=['GET'])
def get_subjects():
    con, cur = connect_to_database()

    if con and cur:
        try:
            cur.execute("SELECT * FROM subjects")
            subjects = cur.fetchall()

            subjects_json = []
            for subject in subjects:
                subject_dict = {
                    'id': subject[0],
                    'name': subject[1],
                    'deadline': subject[2]
                }
                subjects_json.append(subject_dict)

            return jsonify({'subjects': subjects_json})
        except pg.Error as e:
            print(f"データベースクエリが失敗しました：{e}")
            return jsonify({'error': 'データベースクエリが失敗しました'}), 500
        finally:
            # 关闭数据库连接
            cur.close()
            con.close()
    else:
        return jsonify({'error': 'データベースへアクセスが失敗しました'}), 500

@app.route('/api/tests', methods=['GET'])
def get_tests():
    con, cur = connect_to_database()

    if con and cur:
        try:
            cur.execute("SELECT * FROM tests")
            tests = cur.fetchall()

            tests_json = []
            for test in tests:
                test_dict = {
                    'id': test[0],
                    'name': test[1],
                    'time': test[2],
                    'location': test[3]
                }
                tests_json.append(test_dict)

            return jsonify({'tests': tests_json})
        except pg.Error as e:
            print(f"データベースクエリが失敗しました：{e}")
            return jsonify({'error': 'データベースクエリが失敗しました'}), 500
        finally:
            cur.close()
            con.close()
    else:
        return jsonify({'error': 'データベースへアクセスが失敗しました'}), 500




@app.route('/api/events', methods=['GET'])
def get_events():
    con, cur = connect_to_database()

    if not con or not cur:
        return jsonify({'error': 'データベース接続に失敗しました。'}), 500

    try:
        cur.execute("SELECT id, name, date FROM events")
        events = cur.fetchall()

        event_list = []
        for event in events:
            event_dict = {
                'id': event[0],
                'name': event[1],
                'date': event[2]  # イベントの日付情報
            }
            event_list.append(event_dict)

        return jsonify(event_list)
    except pg.Error as e:
        print(f"データベースクエリエラー：{e}")
        return jsonify({'error': 'データベースエラー。'}), 500
    finally:
        cur.close()
        con.close()




@app.route('/api/markings', methods=['GET'])
def get_markings():
    con, cur = connect_to_database()

    if not con or not cur:
        return jsonify({'error': 'データベース接続に失敗しました。'}), 500

    try:
        cur.execute("SELECT id, target, marking_check FROM markings")  # 添加 'marking_check' 字段到 SELECT 语句中
        markings = cur.fetchall()

        marking_list = []
        for marking in markings:
            marking_dict = {
                'id': marking[0],
                'target': marking[1],
                'marking_check': marking[2]
            }
            marking_list.append(marking_dict)

        return jsonify(marking_list)
    except pg.Error as e:
        print(f"データベースクエリエラー：{e}")
        return jsonify({'error': 'データベースエラー。'}), 500
    finally:
        cur.close()
        con.close()



@app.route('/api/courses', methods=['POST'])
def add_course():
    course_data = request.get_json()
    if course_data is None:
        return jsonify({'error': '請求対のデータはjsonではない'}), 400

    print('Received course data:', course_data)    
    course_name = course_data.get('name')
    course_time = course_data.get('time')
    course_location = course_data.get('location')

    if not course_name or not course_time or not course_location:
        return jsonify({'error': '授業名、時間、場所は空欄できないよo.O'}), 400

    con, cur = connect_to_database()

    if con and cur:
        try:
            cur.execute("SELECT MAX(id) FROM courses")
            max_id = cur.fetchone()[0]
            if max_id is None:
                max_id = 0

            new_course_id = max_id + 1

            cur.execute("INSERT INTO courses (id, name, time, location) VALUES (%s, %s, %s, %s)", (new_course_id, course_name, course_time, course_location))
            con.commit()
            return jsonify({'message': '授業登録成功！', 'course_id': new_course_id})
        except pg.Error as e:
            print(f"データベース操作失败：{e}")
            con.rollback()
            return jsonify({'error': 'データベースエラーが発生しました。もう一度やり直してください。'}), 500
        finally:
            cur.close()
            con.close()
    else:
        return jsonify({'error': 'データベースに接続できませんでした。'}), 500



@app.route('/api/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    con, cur = connect_to_database()

    if not con or not cur:
        return jsonify({'error': 'データベースに接続できませんでした。'}), 500

    try:
        cur.execute("DELETE FROM courses WHERE id = %s", (course_id,))
        con.commit()
        return jsonify({'message': '授業情報が削除されました。'})
    except pg.Error as e:
        print(f"データベース削除操作失敗：{e}")
        con.rollback()
        return jsonify({'error': 'データベースエラーが発生しました。もう一度やり直してください。'}), 500
    finally:
        cur.close()
        con.close()

@app.route('/api/courses', methods=['DELETE'])
def delete_courses():
    course_data = request.get_json()
    course_ids = course_data.get('courseIds')

    con, cur = connect_to_database()

    if not con or not cur:
        return jsonify({'error': 'データベースに接続できませんでした。'}), 500

    try:
        cur.execute("DELETE FROM courses WHERE id IN %s", (tuple(course_ids),))
        con.commit()
        return jsonify({'message': '授業情報が削除されました。'})
    except pg.Error as e:
        print(f"データベース削除操作失敗：{e}")
        con.rollback()
        return jsonify({'error': 'データベースエラーが発生しました。もう一度やり直してください。'}), 500
    finally:
        # 关闭数据库连接
        cur.close()
        con.close()

@app.route('/api/subjects', methods=['POST'])
def add_subject():
    subject_data = request.get_json()
    subject_name = subject_data.get('name')
    subject_deadline = subject_data.get('deadline')

    if not subject_name or not subject_deadline:
        return jsonify({'error': '科目名と締め切りは必須項目です。'}), 400

    con, cur = connect_to_database()

    if con and cur:
        try:
            cur.execute("SELECT MAX(id) FROM subjects")
            max_id = cur.fetchone()[0]
            if max_id is None:
                max_id = 0

            new_subject_id = max_id + 1

            cur.execute("INSERT INTO subjects (id, name, deadline) VALUES (%s, %s, %s)", (new_subject_id, subject_name, subject_deadline))
            con.commit()
            return jsonify({'message': '科目登録成功！', 'subject_id': new_subject_id})
        except pg.Error as e:
            print(f"データベース操作失败：{e}")
            con.rollback()
            return jsonify({'error': 'データベースエラーが発生しました。もう一度やり直してください。'}), 500
        finally:
            cur.close()
            con.close()
    else:
        return jsonify({'error': 'データベースに接続できませんでした。'}), 500

    
@app.route('/api/subjects/<int:subject_id>', methods=['DELETE'])
def delete_subject(subject_id):
    con, cur = connect_to_database()

    if not con or not cur:
        return jsonify({'error': 'データベースに接続できませんでした。'}), 500

    try:
        cur.execute("DELETE FROM subjects WHERE id = %s", (subject_id,))
        con.commit()
        return jsonify({'message': '科目情報が削除されました。'})
    except pg.Error as e:
        print(f"データベース削除操作失敗：{e}")
        con.rollback()
        return jsonify({'error': 'データベースエラーが発生しました。もう一度やり直してください。'}), 500
    finally:
        cur.close()
        con.close()


@app.route('/api/subjects', methods=['DELETE'])
def delete_subjects():
    subject_data = request.get_json()
    subject_ids = subject_data.get('subjectIds')

    con, cur = connect_to_database()

    if not con or not cur:
        return jsonify({'error': 'データベースに接続できませんでした。'}), 500

    try:
        cur.execute("DELETE FROM subjects WHERE id IN %s", (tuple(subject_ids),))
        con.commit()
        return jsonify({'message': '科目情報が削除されました。'})
    except pg.Error as e:
        print(f"データベース削除操作失敗：{e}")
        con.rollback()
        return jsonify({'error': 'データベースエラーが発生しました。もう一度やり直してください。'}), 500
    finally:
        cur.close()
        con.close()

@app.route('/api/tests', methods=['POST'])
def add_test():
    test_data = request.get_json()
    test_name = test_data.get('name')
    test_time = test_data.get('time')
    test_location = test_data.get('location')

    if not test_name or not test_time or not test_location:
        return jsonify({'error': '授業名、時間、場所は空欄できないよo.O'}), 400

    con, cur = connect_to_database()

    if con and cur:
        try:
            cur.execute("SELECT MAX(id) FROM tests")
            max_id = cur.fetchone()[0]
            if max_id is None:
                max_id = 0

            new_test_id = max_id + 1

            cur.execute("INSERT INTO tests (id, name, time, location) VALUES (%s, %s, %s, %s)", (new_test_id, test_name, test_time, test_location))
            con.commit()
            return jsonify({'message': 'テスト登録成功！', 'test_id': new_test_id})
        except pg.Error as e:
            print(f"データベース操作失败：{e}")
            con.rollback()
            return jsonify({'error': 'データベースエラーが発生しました。もう一度やり直してください。'}), 500
        finally:
            cur.close()
            con.close()
    else:
        return jsonify({'error': 'データベースに接続できませんでした。'}), 500
    
@app.route('/api/tests/<int:test_id>', methods=['DELETE'])
def delete_test(test_id):
    con, cur = connect_to_database()

    if con and cur:
        try:
            cur.execute("SELECT * FROM tests WHERE id = %s", (test_id,))
            test = cur.fetchone()
            if not test:
                return jsonify({'error': 'テストが存在しないO.o。'}), 404

            cur.execute("DELETE FROM tests WHERE id = %s", (test_id,))
            con.commit()
            return jsonify({'message': 'テスト削除成功！'})
        except pg.Error as e:
            print(f"データベース操作失败：{e}")
            con.rollback()
            return jsonify({'error': 'データベースエラー。'}), 500
        finally:
            cur.close()
            con.close()
    else:
        return jsonify({'error': 'データベースへの接続できないよ0.o。'}), 500

@app.route('/api/tests', methods=['DELETE'])
def delete_tests():
    test_ids_data = request.get_json()

    if not test_ids_data or not isinstance(test_ids_data, list):
        return jsonify({'error': 'テストなし。'}), 400

    con, cur = connect_to_database()

    if con and cur:
        try:
            deleted_count = 0
            for test_id in test_ids_data:
                cur.execute("SELECT * FROM tests WHERE id = %s", (test_id,))
                test = cur.fetchone()
                if not test:
                    continue

                cur.execute("DELETE FROM tests WHERE id = %s", (test_id,))
                con.commit()
                deleted_count += 1

            if deleted_count > 0:
                return jsonify({'message': f' {deleted_count} 個テスト削除できた。'})
            else:
                return jsonify({'error': 'このテスト見つからないO.o。'}), 404
        except pg.Error as e:
            print(f"データベース操作失敗。：{e}")
            con.rollback()
            return jsonify({'error': 'データベースエラー。'}), 500
        finally:
            cur.close()
            con.close()
    else:
        return jsonify({'error': 'データベースへの接続できないよ。'}), 500
    
# @app.route('/api/markings', methods=['POST'])
# def add_marking():
#     marking_data = request.get_json()  # 从请求中获取JSON数据，此时接收到的是一个JSON对象
#     con, cur = connect_to_database()  # 连接到数据库

#     if con and cur:
#         try:
#             target = marking_data.get('target')  # 从JSON数据中获取目标（target）
#             check = marking_data.get('marking_check')  # 从JSON数据中获取check值

#             if not target:
#                 return jsonify({'error': 'Targetが提供されていません。'}), 400  # 如果目标为空，返回错误响应

#             cur.execute("SELECT MAX(id) FROM markings")  # 获取数据库中最大的marking ID
#             max_id = cur.fetchone()[0]
#             if max_id is None:
#                 max_id = 0

#             new_marking_id = max_id + 1  # 生成新的marking ID

#             # 执行数据库操作，插入新的marking记录并使用新生成的marking ID和check值
#             cur.execute("INSERT INTO markings (id, target, marking_check) VALUES (%s, %s, %s)", (new_marking_id, target, check))

#             con.commit()  # 提交事务
#             return jsonify({'message': '打刻目標登録成功！', 'marking_id': new_marking_id})  # 返回成功响应
#         except pg.Error as e:
#             print(f"データベース操作失败：{e}")
#             con.rollback()  # 回滚事务
#             return jsonify({'error': 'データベースエラーが発生しました。もう一度やり直してください。'}), 500  # 返回数据库错误响应
#         finally:
#             cur.close()  # 关闭游标
#             con.close()  # 关闭数据库连接
#     else:
#         return jsonify({'error': 'データベースに接続できませんでした。'}), 500  # 返回数据库连接错误响应

def reset_check_value():
    con, cur = connect_to_database()

    if con and cur:
        try:
            # 将所有记录的 marking_check 字段重置为 False
            cur.execute("UPDATE markings SET marking_check = %s", (False,))
            con.commit()
        except pg.Error as e:
            print(f"数据库操作失败：{e}")
            con.rollback()
        finally:
            cur.close()
            con.close()

# 在每天的0点触发重置 check 值的任务
scheduler.add_job(reset_check_value, 'cron', hour=0, minute=0)

# 启动定时任务调度器
scheduler.start()


@app.route('/api/markings', methods=['POST'])
def add_or_update_marking():
    marking_data = request.get_json()

    if not isinstance(marking_data, dict):
        return jsonify({'error': '请求数据必须是一个JSON对象（字典类型）。'}), 400

    target = marking_data.get('target')  # 从JSON数据中获取目标（target）
    check = marking_data.get('marking_check')  # 从JSON数据中获取check值

    if not target:
        return jsonify({'error': 'Targetが提供されていません。'}), 400

    con, cur = connect_to_database()  # 连接到数据库

    if con and cur:
        try:
            # 保持原有的数据库操作代码不变
            cur.execute("SELECT MAX(id) FROM markings")
            max_id = cur.fetchone()[0]
            if max_id is None:
                max_id = 0

            new_marking_id = max_id + 1

            cur.execute("INSERT INTO markings (id, target, marking_check) VALUES (%s, %s, %s)", (new_marking_id, target, check))

            con.commit()
            return jsonify({'message': '打刻目標登録/更新成功！'}), 200
        except pg.Error as e:
            print(f"データベース操作失败：{e}")
            con.rollback()
            return jsonify({'error': 'データベースエラーが発生しました。もう一度やり直してください。'}), 500
        finally:
            cur.close()
            con.close()
    else:
        return jsonify({'error': 'データベースに接続できませんでした。'}), 500



@app.route('/api/markings/<int:marking_id>', methods=['DELETE'])
def delete_marking(marking_id):
    con, cur = connect_to_database()

    if not con or not cur:
        return jsonify({'error': 'データベース接続エラー。'}), 500

    try:
        cur.execute("SELECT target FROM markings WHERE id = %s", (marking_id,))
        existing_marking = cur.fetchone()
        if not existing_marking:
            return jsonify({'error': 'マーキング（打刻）が存在しません。'}), 404

        cur.execute("DELETE FROM markings WHERE id = %s", (marking_id,))
        con.commit()
        return jsonify({'message': 'マーキング（打刻）が削除されました。'})
    except pg.Error as e:
        print(f"データベース削除操作エラー：{e}")
        con.rollback()
        return jsonify({'error': 'データベースエラー。もう一度やり直してください。'}), 500
    finally:
        cur.close()
        con.close()


@app.route('/api/events', methods=['POST'])
def add_event():
    event_data = request.get_json()
    event_name = event_data.get('name')
    event_date = event_data.get('date')  # 日付情報を取得

    if not event_name or not event_date:
        return jsonify({'error': 'イベント名、日付は空欄できません。'}), 400

    con, cur = connect_to_database()

    if con and cur:
        try:
            cur.execute("SELECT MAX(id) FROM events")
            max_id = cur.fetchone()[0]
            if max_id is None:
                max_id = 0

            new_event_id = max_id + 1
            cur.execute("INSERT INTO events (id, name, date) VALUES (%s, %s, %s)", (new_event_id, event_name, event_date))
            con.commit()
            return jsonify({'message': 'イベント登録成功！', 'event_id': new_event_id})
        except pg.Error as e:
            print(f"データベース操作失敗：{e}")
            con.rollback()
            return jsonify({'error': 'データベースエラーが発生しました。もう一度やり直してください。'}), 500
        finally:
            cur.close()
            con.close()
    else:
        return jsonify({'error': 'データベースに接続できませんでした。'}), 500

@app.route('/api/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    con, cur = connect_to_database()

    if con and cur:
        try:
            cur.execute("SELECT * FROM events WHERE id = %s", (event_id,))
            event = cur.fetchone()
            if not event:
                return jsonify({'error': '事项は存在しない。'}), 404

            cur.execute("DELETE FROM events WHERE id = %s", (event_id,))
            con.commit()
            return jsonify({'message': '事项削除成功！'})
        except pg.Error as e:
            print(f"データベース操作失败：{e}")
            con.rollback()
            return jsonify({'error': 'データベースエラー。'}), 500
        finally:
            cur.close()
            con.close()
    else:
        return jsonify({'error': 'データベースに接続できませんでした。'}), 500



if __name__ == '__main__':
    app.run(host='0.0.0.0')
