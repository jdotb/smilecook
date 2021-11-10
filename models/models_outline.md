# The user model

_The user model will be mapped to the user table in the db_

* **id**: The identity of a user.
* **username**: The username of the user. The maximum length allowed is 80 characters.
It can't be null and is a unique field.
* **email**: The user's email. The maximum length allowed is 200. It can't be blank and
is a unique field.
* **password**: The user's password. The maximum length allowed is 200.
* **is_active**: This is to indicate whether the account is activated by email. It is a
Boolean field with a default value of False.
* **recipes**: This doesn't create a field in the database table. This is just to define the
relationship with the recipe model. So, subsequently, we can get all recipes using
user.recipes.
* **created_at**: The creation time of the user.
* **updated_at**: The last update time of the user

### _Methods used in user model:_
* **get_by_username:** Use for searching the user by username.
* **get_by_email:** Used for searching for user by email.
* **save:** This is to persist the data to the db

# The recipe model
_The recipe model will be mapped to the user table in the db._
* **id:** The identity of a recipe.
* **name:** The name of the recipe. The maximum length allowed is 100 characters. It
can't be null.
* **description:** The description of the recipe. The maximum length allowed is 200.
* **num_of_servings:** The number of servings. This needs to be an integer.
Defining Our Models | 69
* **cook_time:** The cooking time in minutes. This field only accepts an integer.
* **directions:** The directions of the recipe. This can have a maximum length of 1,000.
* **is_publish:** This is to indicate whether the recipe has been published. It is set to
False by default.
* **created_at:** The creation time of the recipe.
* **updated_at:** The last update time of the recipe.