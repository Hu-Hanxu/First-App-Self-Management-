from flask import Flask
from .api1 import *
# from .api2 import *
# from .api3 import *
# from .api4 import *
#from .api5 import *
#from .api6 import *
#from .api7 import *
#from .api8 import *
#from .api9 import *
#from .api10 import *
#from .api11 import *
#from .api12 import *
from flask_sqlalchemy import SQLAlchemy
from courseModels import db as course_db
from testModels import db as test_db
from subjectModels import db as subject_db

app = Flask(__name__)

# 初始化数据库连接
course_db.init_app(app)
test_db.init_app(app)
subject_db.init_app(app)

# 导入各个 API 文件
app.register_blueprint(api1)
# app.register_blueprint(api2)
# app.register_blueprint(api3)
# app.register_blueprint(api4)
#app.register_blueprint(api5)
#app.register_blueprint(api6)
#app.register_blueprint(api7)
#app.register_blueprint(api8)
#app.register_blueprint(api9)
#app.register_blueprint(api10)
#app.register_blueprint(api11)
#app.register_blueprint(api12)

# ...


