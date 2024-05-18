import pymysql


def connect():
    conn = pymysql.connect(host='localhost', user='root', password='system', database='project2024')
    return conn


if __name__ == "__main__":
    connect()
