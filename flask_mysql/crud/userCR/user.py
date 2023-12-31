from mysqlconnection import connectToMySQL
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
        return connectToMySQL('user_schema').query_db( query, data )
    @classmethod
    def display_all(cls):
        query="SELECT * from users"
        results= connectToMySQL('user_schema').query_db(query)
        users=[]
        for row in results:
            user=cls(row)
            users.append(user)
        return users    
