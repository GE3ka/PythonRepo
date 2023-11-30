from user_app.config.mysqlconnection import connectToMySQL,DB

class User:
    def __init__(self,data):
        self.id=data['id']
        self.first_name= data['first_name']
        self.last_name= data['last_name']
        self.email= data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    
    @classmethod
    def create(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );"
        return connectToMySQL(DB).query_db( query, data )
    @classmethod
    def display_all(cls):
        query="SELECT * from users"
        results= connectToMySQL(DB).query_db(query)
        users=[]
        for row in results:
            user=cls(row)
            users.append(user)
        return users    
    
    @classmethod
    def display_one(cls,id):
        data = {'id': id}
        query="SELECT * from users where id = %(id)s "
        results= connectToMySQL(DB).query_db(query,data)
        one_user = None
        if results != []:
            one_user = cls(results[0])
        return one_user
    
    @classmethod
    def update_user(cls,data):
        
        query="Update users set first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s,updated_at=NOW() WHERE id=%(id)s "
        result=connectToMySQL(DB).query_db(query,data)
        print (result)
        return result
    @classmethod
    def delete_user(cls,data):
        query="delete from users where id = %(id)s"
        result=connectToMySQL(DB).query_db(query,data)
        return result