class User:
    
    def __init__ (self,name, username,email):
        self.name =name
        self.username =username
        self.email =email
        self.shoppinglists =[]

    def add_shoppinglist(self,list_name):
        if list_name not in self.shoppinglists:
            self.shoppinglists.append(list_name)
            return "Shopping list added succesfully"
        return "shoppinglist already exists"

    def edit_shoppinglist(self,newname,oldname):
        if oldname in self.shoppinglists:
            self.shoppinglists =[newname for oldname  in self.shoppinglists]
            return "edited succesfully"
        return "shopping list not found"

    def delete_shoppinglist(self,list_name):
        if list_name in self.shoppinglists:
            self.shoppinglists.remove(list_name)
            return "shopping list deleted"
        return "shopping list not found"

    def view_shoppinglist(self,item):
        for item in self.shoppinglists:
            return self.shoppinglists
        return "shopping list empty"

class Shoppinglist:
    
    def __init__(self,item):
        self.item=item
        self.items =[]

    def add_items(self, name):
        if name not in self.items:
            self.items.append(name)
            return "item added succesfully"
        return "Item already on the list"

    def edit_itemslist(self,olditem,newitem):
        if olditem in self.items:
            self.items= [newitem for olditem in self.items]
            "item added successfully"
        return "no items to edit"
    
    def delete_item(self,name):
        if name in self.items:
            self.items.remove(name)
            return "Item deleted"
        "No item to delete "

    def view_items(self,item):
        for item in self.items:
            return self.items
        return "shopping list empty"

class Item:

    def __init__(self, name):
        self.name = name
    
    def veiw_item(self):
        return self.name

