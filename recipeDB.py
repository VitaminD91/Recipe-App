import sqlite3
from ingredient import Ingredient
sqlite3.register_adapter(bool, int)
sqlite3.register_converter("BOOLEAN", lambda v: bool(int(v)))


dbname = "recipeDB.db"

def initialise():
	conn = sqlite3.connect(dbname)
	c = conn.cursor()
	
	c.execute("PRAGMA foreign_keys = ON")
	c.execute('''
		CREATE TABLE IF NOT EXISTS Recipe (
			Id INTEGER PRIMARY KEY AUTOINCREMENT,
			Name TEXT NOT NULL UNIQUE,
			Time TEXT NOT NULL
		)
	''')
	
	c.execute('''
		CREATE TABLE IF NOT EXISTS Ingredient (
			Id INTEGER PRIMARY KEY AUTOINCREMENT,
			Type TEXT NOT NULL,
			Name TEXT NOT NULL UNIQUE,
			IsMain BOOLEAN NOT NULL DEFAULT 0
		)
	''')
	
	c.execute('''
		CREATE TABLE IF NOT EXISTS RecipeIngredients (
			RecipeId INTEGER REFERENCES Recipe(Id),
			IngredientId INTEGER REFERENCES Ingredient(Id),
			IngredientUnit TEXT,
			IngredientAmount DECIMAL NOT NULL, 
			PRIMARY KEY(RecipeId, IngredientId)
		)
	''')
	
	conn.commit()
	conn.close()

initialise()

###CONDENSED QUERY###
def execute_query(query, props, return_id = False):
	conn = sqlite3.connect(dbname)
	c = conn.cursor()
	c.execute(query, props)
	id = c.lastrowid
	conn.commit()
	conn.close()

	if return_id: return id

###CONDENSED UPDATE###
def update_query(query, props):
	conn = sqlite3.connect(dbname)
	conn.row_factory = sqlite3.Row
	c = conn.cursor()
	c.execute(query, props)
	conn.commit()
	conn.close()

###CONDENSED FETCH ALL###
def fetch_all_query(query, props):
	conn = sqlite3.connect(dbname)
	conn.row_factory = sqlite3.Row
	c = conn.cursor()
	c.execute(query, props)
	result = c.fetchall()
	conn.close()
	return result

###CONDENSED FETCH ONE###
def fetch_one_query(query, props):
	conn = sqlite3.connect(dbname)
	conn.row_factory = sqlite3.Row
	c = conn.cursor()
	c.execute(query, props)
	result = c.fetchone()
	conn.close()
	return result
		

###CREATE AN INDIVIDUAL INGREDIENT###
def create_ingredient(type, name, is_main):
	execute_query('INSERT INTO Ingredient(Type, Name, IsMain) VALUES (?, ?, ?)', [type, name, is_main])

#create_ingredient('Poultry', 'Chicken', True)


###CREATE A RECIPE###
def create_recipe(name, time, ingredients):
	recipe_id = execute_query('INSERT INTO Recipe(Name, [Time]) VALUES (?, ?)', [name, time], True)
	for ingredient in ingredients:
		execute_query('''INSERT INTO RecipeIngredients (RecipeId, IngredientId, IngredientUnit, IngredientAmount) 
						VALUES (?, ?, ?, ?)''', [recipe_id, ingredient.id, ingredient.unit, ingredient.amount])

#ingredients = [Ingredient(2, 'g', 400)]
#create_recipe('Carbonara', 'Quick', ingredients)

###GET ALL INGREDIENTS###
def get_all_ingredients():
	ingredients = fetch_all_query('SELECT * FROM Ingredient', [])
	return ingredients

###GET ALL RECIPES###
def get_all_recipes():
	recipes = fetch_all_query('SELECT * FROM Recipe', [])
	return recipes

###EDIT AN INGREDIENT##
def update_ingredient(ingredient_id, name, type, is_main):
	update_query('UPDATE Ingredient SET Name = ?, Type = ?, IsMain = ? WHERE Id = ?', [name, type, is_main, ingredient_id])


###EDIT A RECIPE NAME###
def update_recipe_name(recipe_id, name):
	update_query('UPDATE Recipe SET Name = ? WHERE Id = ?', [name, recipe_id])


###DELETE AN INGREDIENT###
def delete_ingredient(ingredient_id):
	execute_query('DELETE FROM Ingredient WHERE Id = ?', [ingredient_id])


###DELETE A RECIPE###
def delete_recipe(recipe_id):
	execute_query('DELETE FROM Recipe WHERE Id = ?', [recipe_id])


###SORT RECIPE BY MAIN INGREDIENT###
def get_recipes_by_main(type):
	results = fetch_all_query('''SELECT r.Name FROM Recipe r
				 INNER JOIN RecipeIngredients ri ON r.Id=ri.RecipeId
				 INNER JOIN Ingredient i ON i.Id = ri.IngredientId
				 WHERE Type = ? AND IsMain = 1 ''', [type])
	return results
	
###GET INGREDIENT BY ID###
def get_ingredient_by_id(ingredient_id):
	result = fetch_one_query('SELECT * FROM Ingredient WHERE Id =?', [ingredient_id])
	return result

###GET RECIPE BY ID###
def get_recipe_by_id(recipe_id):
	result = fetch_one_query('SELECT * FROM Recipe WHERE Id =?', [recipe_id])
	return result
	