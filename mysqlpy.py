def my_db():
    import pymysql
    coon = pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='wq123456',
        port=3306,
        db='test',
        charset='utf8'
    )
    # cur = coon.cursor()  # 建立游标
    # cur.execute("select * from star")  # 查询数据
    # res = cur.fetchall()  # 获取结果
    return coon
