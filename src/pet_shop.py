# WRITE YOUR FUNCTIONS HERE
from itertools import count
from unicodedata import name

from tests import pet_shop_test


def get_pet_shop_name(pet_shop):
    return pet_shop["name"]
    pass

    
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]
    pass
    

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount
    pass


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]
    pass

def increase_pets_sold(pet_shop, sold):
    pet_shop["admin"]["pets_sold"] += sold
    pass

def get_stock_count(pet_shop):
    return len(pet_shop("pets"))
    pass
#could this be count?

def get_pets_by_breed(pet_shop):
    return len(pet_shop("breed")("British shorthair"))
    pass
#could this be count(()())?

def get_pets_by_breed(pet_shop):
    return len(pet_shop("breed")("Dalmation"))
    pass

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if name == pet["name"]:

            return pet


    

   
 
    

    
    
    
        
    
    


        
        
    

