


#hotel menu project
menu={
    "Beverage":{"lachi":"50",
                "faluda":"80",
                "cold coffee":"60",
                "mango juice":"50",
                "orange juice":"60",
                "apple juice":"70"
    },
    "burger":{"chicken burger":"90",
              "veg burger":"70"
    },
    "biryani":{"chicken biryani":"150",
               "mushroom biryani":"130",
               "egg biryani":"100"
    
    },
    "pizza":{"chicken pizza big":"350",
             "chicken pizza small":"250",
             "mushroom pizza":"230"

    }
}

ftotal=0
count=1
item=[]
# print("Welcome to PYTHON Restaurant")
print("category available here\n1. Beverage\n2. Burger\n3. Biryani\n4. Pizza")
cat=input("Enter the category you are looking for\n")
cat.lower()
if cat=="beverage":
    print("\nThings availble to try in beverage")
    print("lachi : 50rs\nfaluda : 80rs\ncold coffee : 60rs\nmango juice : 50rs\nOrange juice : 60rs\napple juice : 70")
    while count==1:
     item1=input("\nAdd the item to order\n")
     item.append(item1)
     rate=menu["Beverage"][item1]      
     ftotal=ftotal+int(rate)
     ref=input("\nDo you want to order more (yes/no)\n")
     if ref=="no":
        count=0
    print("your cart: ",item)
    # print("Total bill :", ftotal)    
elif cat=="burger":
    print("Things available to try in burgers")
    print("chicken burger : 90rs\nveg burger : 70rs")
    while count==1:
     item1=input("Add the item to order\n")
     item.append(item1)
     rate=menu["burger"][item1]    
     ftotal=ftotal+int(rate)
     ref=input("Do you want to order more (yes/no)\n")
     if ref=="no":
        count=0
    print("your cart: ",item)
    # print("Total bill :", total)    
elif cat=="biryani":
    print("Things to try in BIRYANI")
    print("chicken biryani : 150rs\nmushroom biryani : 130rs\negg biryani : 100rs")
    while count==1:
     item1=input("Add the item to order\n")
     item.append(item1)
     rate=menu["biryani"][item1]      
     ftotal=ftotal+int(rate)
     ref=input("Do you want to order more (yes/no)\n")
     if ref=="no":
        count=0
    print("your cart: ",item)
    # print("Total bill :", total)    
else:
    print("Things to try in pizza")
    print("chicken pizza big : 350rs\nchicken pizza small : 250rs\nmushroom pizza : 230rs")   
    while count==1:
     item1=input("Add the item to order\n")
     item.append(item1)
     rate=menu["pizza"][item1]      
     ftotal=ftotal+int(rate)
     ref=input("Do you want to order more (yes/no)\n")
     if ref=="no":
        count=0 
    print("your cart: ",item)
    # print("Total bill :", total)     





