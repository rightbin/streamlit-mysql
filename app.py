import streamlit as st
import mysql.connector
from mysql.connector import Error
from datetime import datetime ,date,time


def main():

    # title = st.text_input("책 이름을 입력하세요.")
    # author_fname = st.text_input("작가의 이름을 입력하세요")
    # author_lname = st.text_input("작가의 성을 입력하세요")
    # released_year = st.number_input("출판연도를 입력하세요",0,2999)
    # stock_quantity = st.number_input("재고를 입력하세요",0,10000)
    # pages = st.number_input("총 페이지 수를 입력하세요" , 0,99999)
    # name = st.text_input("이름을 입력하세요.")
    # birthdate = st.date_input("생일을 입력하세요.")
    # birthtime = st.time_input("태어난 시간을 입력하세요.")
    

    if st.button("입력하기") :

        try : 
            # 1. 커넥터로부터 커넥션을  받는다.
            connection = mysql.connector.connect(
                host = 'database-3.c9ovrlne0js8.ap-northeast-2.rds.amazonaws.com',
                database = 'yhdb',
                user = 'streamlit',
                password = 'yh1234'
            )
            if connection.is_connected() :
                db_info = connection.get_server_info()
                print('MySQL version: ', db_info)

                # 2. 커서를 가져온다.
                cursor = connection.cursor()

                # 3. 우리가 원하는거 실행 가능.
                # cursor.execute('select database();')

                table = """insert into cats4(name,age)
                        values ('냐옹이지금22',10);"""
                


                # record = [   ('냐옹이',1),('나비',3)     ,('단비',5)     ]

                cursor.execute (table)

                # cursor.executemany(query,record)
                connection.commit()
                print("{}개 적용됨".format(cursor.rowcount))
                st.write("입력이 완료되었습니다.")
                #st.write("{} {} 의 {} 등록 완료!".format(author_fname,author_lname,title))
                # record = cursor.fetchone()

                # print('Connected to db : ', record)
        


        except Error as e:
            print('디비 관련 에러 발생', e)
        
        finally : 
            # 5. 모든 데이터베이스 실행 명령을 전부 끝냈으면,
            #    커서와 커넥션을 모두 닫아준다.
            cursor.close()
            connection.close()
            print('MYSQL 커넥션 종료')


if __name__ == '__main__':
    main()


    #pip install mysql-connector-python 