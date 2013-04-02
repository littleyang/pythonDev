import MySQLdb

class DBconfig:
  def create_conn():
    conn = MySQLdb.connect(host="localhost",user="mysql",password="")
    return conn

def main():
  myt = DBconfig()
  print myt.create_conn


if __name__== "__main__":
  main()




