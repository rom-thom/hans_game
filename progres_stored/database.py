import sqlite3


class DatabaseProgress:
    def __init__(self):
        self.conn = sqlite3.connect("progress.db")
        self.cur = self.conn.cursor()

        #self.cur.execute("DROP TABLE user_progress")
        self.cur.execute('''CREATE TABLE IF NOT EXISTS user_progress (
            user_name TEXT UNIQUE, 
            password TEXT, 
            max_level REAL,
            caracter INTEGER
        )''')
        

    def add_account(self, info):
        # info = (user_name: str, password: str, max_level: float, caracter: int)
        try:
            self.cur.execute("INSERT INTO user_progress VALUES (?, ?, ?, ?)", info)
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        except sqlite3.ProgrammingError:
            print("Incorrect number of values supplied to account. Must be 4")
            return False


    def access_account(self, user_name, password):
        user_accounts = self.cur.execute("""SELECT * FROM user_progress""").fetchall()
        for account in user_accounts:
            if account[0] == user_name and account[1] == password:
                print("Account accessed")
                return list(account)
        return [None, None, 0, 0]
    

    def check_if_valid_password_and_username_and_signing_in(self, username, password, max_level, caracter):
        return_list = ["Valid", True]
        
        if 10 < len(username) or 10 < len(password):
            return_list[0] = "Username and password must be smaller than 11 things"
            return_list[1] = False
        elif 3 > len(username) or 3 > len(password):
            return_list[0] = "Username and password must be at least 3 things long"
            return_list[1] = False
        elif self.access_account(username, password)[0] != None:
            return_list[0] = "This account allredy exist"
            return_list[1] = False
        else:
            print("Adding account")
            return_list[1] = self.add_account((username, password, max_level, caracter))
        return return_list


    def update_account_info(self):
        self.cur.execute("""UPDATE user_progress 
                            SET
                                max_level = ?,
                                caracter = ?
                            WHERE
                                user_name = ?
                                """, (self.account[2], self.account[3], self.account[0]))
        self.conn.commit()



if __name__ == "__main__":
    data = DatabaseProgress()

    info = ("Thomas", "passord", 7, 2)
    #data.add_account(info)

    account = data.access_account("kolle", "kalle")
    print(account)
