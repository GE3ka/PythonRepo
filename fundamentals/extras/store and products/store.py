from products import Products
class Store:
    def __init__(self):
        self.name= "My Market"
        self.listProducts=[]
    def add_product(self, new_product):
            self.listProducts.append(new_product)
    def sell_product(self, id):        
        print(f"This product will be removed \n{self.listProducts[id].name} Category: {self.listProducts[id].category} ")
        self.listProducts.pop(id)
    def inflation(self, percent_increase):
        for item in self.listProducts:
            item.update_price(percent_increase,True)   
    def set_clearance(self, category, percent_discount):
        for item in self.listProducts:
            if item.category==category:
                item.update_price(percent_discount,False) 
            else:
                continue           
    def print_all_products(self):
        for item in self.listProducts:
            item.print_info()  



myStore=Store()
item_1=Products("Coffe",4,"Alimentary")
myStore.add_product(item_1)
item_2=Products("Sugar",1,"Alimentary")
myStore.add_product(item_2)
item_3=Products("Flour",0.8,"Alimentary")
myStore.add_product(item_3)
item_4=Products("Salt",0.5,"Alimentary")
myStore.add_product(item_4)
item_5=Products("Oil",4.5,"Alimentary")
myStore.add_product(item_5)
item_6=Products("Fairy Gel",2,"Cleaning")
myStore.add_product(item_6)
item_7=Products("Bleach",0.9,"Cleaning")
myStore.add_product(item_7)
myStore.inflation(0.2)
myStore.print_all_products()
myStore.sell_product(1)
myStore.print_all_products()
myStore.set_clearance("Cleaning",0.2)
myStore.print_all_products()