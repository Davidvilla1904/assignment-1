from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.
print(products)


# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.
customer_preferences = []


response = ""
while response != "N":
    print("Input a preference:")
    preference = input("")
    customer_preferences.append(preference)
    
    response = input("Do you want to add another preference? (Y/N): ").upper()


  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_preferences = set(customer_preferences)



# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []

for product in products:
    converted = product.copy()
    converted["tags"] = set(product["tags"])
    converted_products.append(converted)


    



# TODO: Step 5 - Write a function to calculate the number of matching tags
    def count_matches(product_tags, customer_tags):
        '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
        '''
        matches = product_tags.intersection(customer_tags)
        return len(matches)


# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A sorted list of products containing product names and their match counts.
    '''
    recommendations = []

    for product in products:
        product_tags = set(product["tags"])  
        match_count = count_matches(product_tags, customer_tags)

        if match_count > 0:
            recommendations.append({
                "name": product["name"],
                "match_score": match_count
            })

    return recommendations




recommended = recommend_products(products, customer_preferences)

print("Recommended Products:")
for product in recommended:
    print(f"- {product['name']} ({product['match_score']} match(es))")


'''
DESIGN MEMO (write below in a comment):
1. What core operations did you use (e.g., intersections, loops)? Why?
I used loops to go over each product to process each one individually. Because we need to check every product tag against customer preferences to find matches and score.
I changed the lists into sets since sets allow for faster comparison operations.
The intersection operation quickly identifies all tags shared between a product and customer preferences, which directly corresponds to the "match score."
In the last function, I used an if loop to make sure only the products that have more than 1 match get shown, since you will not be interested in the products with 0 matches. And with that, also shortening the output, the user would get


2. How might this code change if you had 1000+ products?
It will become a lot slower since it has to go over each product tag individually each time. 
Also, instead of checking all products, quickly find and compare only those that share tags with the customer’s preferences. This reduces how many products you need to look at.
And the output list with matches will also become a lot bigger, so you might want to set up a threshold of how many matches before it shows you it.  
You can also use special tools/databases made for searching lots of items fast. Instead of using the code I wrote, which would be a bit slower.
'''

