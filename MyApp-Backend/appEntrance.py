from flask import Flask
from database import db
from api.api1 import api1
# from api.api2 import api2
# from api.api3 import api3
# from api.api4 import api4

#, api5, api6, api7, api8, api9, api10, api11, api12

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:990218@localhost:5432/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# 注册每个 API 蓝图
# 课程登录
app.register_blueprint(api1)
# # 课程消除
# app.register_blueprint(api2)
# # 课题登录
# app.register_blueprint(api3)
# # 课题消除
# app.register_blueprint(api4)
# 考试登录
# app.register_blueprint(api5)
# # 考试消除
# app.register_blueprint(api6)
# # 事项登录
# app.register_blueprint(api7)
# # 事项消除
# app.register_blueprint(api8)
# # 打刻登录
# app.register_blueprint(api9)
# # 打刻消除/打刻
# app.register_blueprint(api10)
# # 课题登录
# app.register_blueprint(api11)
# # 選択ヘルパー
# app.register_blueprint(api12)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
