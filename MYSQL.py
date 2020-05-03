import mysql.connector

class Connector():
    def __init__(self):
        pass

    def post(self, title, companyname, location, salary, summary, description):
        # Connect to DB
        conn = mysql.connector.connect(user= 'root', password= 'Ng@timan9925910h', host= 'localhost',
                                       database= 'indeedapp', port= 3306)

        # Create Cursor
        c = conn.cursor()

        # Query
        query = (f"INSERT INTO `indeedapp`.`indeedjobs` (`title`, `companyname`, `location`, `salary`, `summary`, `description`) VALUES ('{title}', '{companyname}', '{location}', '{salary}', '{summary}', '{description}')")

        # Execute
        c.execute(query)

        # Commit
        conn.commit()

        c.close()
        conn.close()

        print('Sent To DB!\n')


