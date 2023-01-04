from select import select
import sqlite3

class Bdd:

  conn = sqlite3.connect('yams.db')
  cursor = conn.cursor()

  def createTable(self):
    
    self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS party(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        one INTEGER,
        two INTEGER,
        three INTEGER,
        four INTEGER,
        five INTEGER,
        six INTEGER,
        brelan INTEGER,
        square INTEGER,
        full INTEGER,
        small_suite INTEGER,
        big_suite INTEGER,
        yams INTEGER,
        chance INTEGER
    )
    """)
    self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS game(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        score INTEGER,
        party_end BOOL,
        party_id INTEGER,
        CONSTRAINT fk_party
          FOREIGN KEY (party_id)
          REFERENCES party(id)
    )
    """)
    self.conn.commit()

  def deleteTable(self):
    self.cursor.execute("DROP TABLE game")
    self.cursor.execute("DROP TABLE party")

  def newGame(self):
    
    self.cursor.execute("INSERT INTO party (one,two,three,four,five,six,brelan,square,full,small_suite,big_suite,yams,chance) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", (None,None,None,None,None,None,None,None,None,None,None,None,None))
    self.cursor.execute("INSERT INTO game (score,party_end,party_id) VALUES (?,?,?)", (False,False,self.cursor.lastrowid,))
    self.conn.commit()

  def getGames(self):
    self.cursor.execute("SELECT * FROM game")
    return self.cursor.fetchall()

  def getOnGameWithParty(self,game_id):
    self.cursor.execute("SELECT * FROM game INNER JOIN party ON party.id = game.party_id WHERE game.id = ? ", (game_id,))
    return self.cursor.fetchone()

  def setScore(self, key, value):
    self.cursor.execute("UPDATE party SET "+key+"=? WHERE id = (SELECT MAX(id) FROM game) ", (value,))
    self.conn.commit()

  def setTotal(self, value):
    self.cursor.execute("UPDATE game SET score=? , party_end=? WHERE id = (SELECT MAX(id) FROM game) ", (value,True))
    self.conn.commit()

  def getLastParty(self):
    self.cursor.execute("SELECT * FROM party INNER JOIN game ON party.id = game.party_id WHERE party.id = (SELECT party_id FROM game WHERE id = (SELECT max(id) FROM game)) AND game.party_end = 0")
    return self.cursor.fetchone()

  def db_close(self):
    self.conn.close()