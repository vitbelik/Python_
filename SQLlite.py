import sqlite3 as sql
import random, datetime, time, logging


# Enable Logging
logging.basicConfig(
        filename = 'log.log',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# creating database and tables
logger.info('Starting executing program...')
id_table = sql.connect('prog_1.db')

logger.debug('connecting to db {}'.format(id_table))


logger.info('Creating table....')

def create_tables(id_table):
    for i in range(5):
        print(i)
        try:
            c = id_table.cursor()
            if i == 0:
                logger.info('Creating table user_reg')
                c.execute(
                    '''CREATE TABLE  (username text, name text, data_of_registration text, id int primary key)''')
            elif i == 1:
                logger.info('Creating table user_data')
                c.execute(
                    'create table user_data (id int, user_name text, user_last_name text, user_birth data, foreign key(id) references user_reg(id))')
            elif i == 3:
                logger.info('Creating table checkers')
                c.execute(
                    'Create table checker (id int, is_name int, is_last_name int, is_birth int, is_next int, is_n int, foreign key(id) references user_reg(id))')
            elif i == 4:
                logger.info('Creating table id')
                c.execute('Create table id (id int primary key, comment text)')

            id_table.commit()
            logger.debug('commit made!')
        except sql.OperationalError as err:
            # logger.warning('user_reg or user_data or checker or all tables are exist')
            logger.error(err)


def check_id(u_id):
    logger.info('Checking correctness of id = {}'.format(u_id))
    logger.info('Search for id in id_table')
    o_id_table = id_table.cursor()
    count = 0
    for row in o_id_table.execute("Select * from id where id='{}'".format(u_id)):
        logger.info('Executing sql query: Select * from id where id=\'{}\''.format(u_id))
        count += 1
        print(count, 'hey')
    if count == 0:
        logger.info('good id: {}'.format(u_id))
        return True
    else:
        o_id_table.close()
        logger.warning('This id is alredy in our db')
        return False


def set_k_to_db(k):
    o_id_table = id_table.cursor()
    logger.info('Executing query: Insert into id values (?, ?)'.format(k, 'n'))
    o_id_table.execute("""Insert into id values (?, ?)""", (k, 'n'))
    id_table.commit()
    logger.info('Changes was commited!')
    o_id_table.close()

def exec_query(query, param=None, response=False):

    db = id_table.cursor()
    if param is not None:
        s = db.execute(query, param)
    else:
        s = db.execute(query)

    if response:
        return s.fetchall()

    id_table.commit()

    logger.debug('Changes commited')

def procc(id, what=None):

    if what is not None:

        if what == 0:
            name = str(input("Enter you name, or enter [o] to see options: "))
            if name:
                exec_query('Update user_data set user_name=? where id=?', (name, id))
                exec_query('Update checker set is_name = 1 where id ={}'.format(id))
        elif what == 1:
            l_name = str(input("Enter your last name, or enter [o] to see options: "))
            if l_name:
                exec_query('Update user_data set user_last_name = ? where id = ?', (l_name, id))
                exec_query('Update checker set is_last_name = 1 where id = {}'.format(id))
        elif what == 2:
            birth = str(input("My birthday is, or enter [o] to see options: "))
            if birth_validator(birth):
                exec_query('Update user_data set birth = ? where id = ?', (birth, id))
                exec_query('Update checker set is_birth = 1 where id = {}'.format(id))

        else:
            print("\nError while processing procc() function\n")


    else:

        user_input_name = input("Enter you name, or enter [o] to see options: ")
        user_input_lastname = input("And, enter your last name, or enter [o] to see options:: ")
        user_input_birth = input("My birthday is, or enter [o] to see options: ")
        if birth_validator(user_input_birth):
            exec_query('Insert into user_data (id, user_name, user_last_name, user_birth) values (?, ?, ?, ?)',
                       (id, user_input_name, user_input_lastname, user_input_birth))

        times = time.strftime('%d-%m-%Y:%H-%M-%s')
        exec_query('insert into user_reg (id, username, name, data_of_registration) values (?, ?, ?, ?)',
                   (id, user_input_lastname, user_input_name, times))
        exec_query('Insert into checker (id, is_name, is_last_name, is_birth, is_next, is_n) values (?, ?, ?, ?, 0, 0)',
                   (id, 1 if user_input_name else 0, 1 if user_input_lastname else 0, 1 if user_input_birth else 0))

        return user_input_name, user_input_lastname, user_input_birth


def birth_validator(birth):
    while date_validator(birth) == False:
        birth = procc(2)
        show_options()

def show_options():
    print("Enter [q] to finish, or [c] to continue")

def generate_id():

    k = random.randint(0, 1000)

    if check_id(k):
        set_k_to_db(k)
        return k
    else:
        print('ooops, this value is busy')
        generate_id()


def start(u_id):
    o_id_table = id_table.cursor()


def date_validator(date):
    try:
        datetime.datetime.strptime(date, "%d-%m-%Y")
        return True
    except ValueError:
        print('Incorrect date format, should be DD-MM-YYYY')
        return False

def main():


    while True:
        #show_options()
        try:
            id = generate_id()
            exec_query('Insert into user_data values ({}, "", "", "")'.format(id))

            name, last, birth = procc(id)

            limit = 10
            curr = 0

            while curr < limit:
                check = exec_query('Select is_name, is_last_name, is_birth from checker where id = {}'.format(id), response = True)

                if check[0][0] == 0:
                    logger.info('Name value is empty, request to re-enter it')
                    procc(id, 0)
                elif check[0][1] == 0:
                    logger.info('Last Name value is empty, request to re-enter it')
                    procc(id, 1)
                elif check[0][2] == 0:
                    logger.info('Birth value is empty, request to re-enter it')
                    procc(id, 2)
                else:
                    print('everysing is ok')
                    break

                print(check)

                curr += 1

                print('This is curr:', curr)
                if curr == limit:
                    logger.warning('Limit of entering names and other is existed.')
        except EOFError as err:
            logger.error(err)
            print (err)

        p = exec_query('Select * from checker where id = {}'.format(id), response=True)
        print(p)

        return



main()