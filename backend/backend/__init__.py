# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.

# 引入MySql连接插件pymSql
import pymysql
pymysql.version_info = (1, 4, 13, "final", 0)
pymysql.install_as_MySQLdb()
