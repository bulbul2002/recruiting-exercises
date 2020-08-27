#function to take inputs
def inventory(items_dict, inventory_list):

  # feed result output in this dictionary
  result = {}
  # feed result dictionary in this list
  result_list = []  

   # iterating through the dictionaries for different warehouses
  for inventory_dict in inventory_list:   

    # iterating through the item name and count for different warehouses
    for key,values in inventory_dict['inventory'].items():

      #name of the item to be looked up
      item_name = key   
      #count of the item per warehouse  
      item_count = values 
      #dictionary of item name and item count to be looked up

      for k,v in items_dict.items(): 

         #needed value 
        item_count_needed = v
        #checking for item name

        if k == item_name: 
          #if there is no item available, return empty dict

          if item_count == 0 or item_count_needed==0: 
            break
           #if item count is equla to item_needed

          if item_count_needed == item_count: 
            #putting the output in a dict  #name of warehouse
            result[inventory_dict['name']]={}   
             #item name and item count
            result[(inventory_dict['name'])][item_name]=item_count_needed  

            #updating the count needed 
            item_count_needed = 0
            items_dict[k] = item_count_needed 

            #return item_name and item_count
            break
            
          #if item-count is more than item_needed
          if item_count_needed < item_count: 
            #putting the output in a dict  #name of warehouse
            result[inventory_dict['name']]={}   
            #item name and item count
            result[(inventory_dict['name'])][item_name]=item_count_needed

            #updating the count needed 
            item_count_needed = 0
            items_dict[k] = item_count_needed 

            #return item_name, item_needed    
            break

             

          #if item_needed> item_count
          if item_count_needed > item_count: 
             #putting the output in a dict  #name of warehouse
            result[inventory_dict['name']]={}  
            #item name and item count
            result[(inventory_dict['name'])][item_name]=item_count   

             #items left = item_needed- item_count from the first warehouse          
            item_count_needed = item_count_needed - item_count   
            #change the amount of item_needed after subtracting item_count from it
            items_dict[k] = item_count_needed 

            
        else:
          continue

  result_list.append(result)
  

  #returning the list     
  return(result_list)  


print(inventory({ 'apple': 1 }, [{ 'name': 'owd', 'inventory': { 'apple': 0 } }]))

print(inventory({ 'apple': 10 }, [{ 'name': 'owd', 'inventory': { 'apple': 5 } }, { 'name': 'dm', 'inventory': { 'apple': 5 }}]))

print(inventory({ 'apple': 1 }, [{ 'name': 'owd', 'inventory': { 'apple': 1 } }]))


print(inventory({ 'apple': 12 }, [{ 'name': 'owd', 'inventory': { 'apple': 10 } }, { 'name': 'dm', 'inventory': { 'apple': 5 }}]))

print(inventory({ 'apple': 7 }, [{ 'name': 'owd', 'inventory': { 'apple': 5 } }, { 'name': 'dm', 'inventory': { 'apple': 5 }}]))


