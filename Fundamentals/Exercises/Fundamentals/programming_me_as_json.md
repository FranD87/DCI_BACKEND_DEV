Me As a JSON
In this exercise, you'll have to transcribe yourself as a JSON file!

You'll have to create a JSON file from scratch. You can either use your prefered text editor, or just use an Online JSON Editor like this one here.

Hint: If you don't feel comfortable putting your real data on the exercise, feel free to do it with fake data. The important thing here is the learning experience.

The YOU object
It should contain the following properties (with their respective types):

first_name: String - Your first name
last_name: String - Your last name
birth_date: Date - Your birth date
age: Number - your age
gender: String - Your gender. For this exercise, assume you can provider either M for male, F for female or O for other.
nationality: String | String[] - Your nationality, either as a string (single nationality) or an array of strings (double+ nationalities)
is_married: Boolean - If you are married or not, as a boolean value
has_children: Boolean - If you have children or not, as a boolean value
hobbies: String[] - Your hobbies, as an array of strings
address: Address - Your address, as an address object (more on that below)
car: Car - Your car, as a car object (more on that below. If you don't have one, it's fine to just put fake values - or your bicycle's data, why not!?)
favorite_tv_shows: String[] - Your favorite TV shows, as an array of strings
pets: Pet[] - Your pets, as an array of the pet object (more on that below. You should write at least two entries here - if you don't have at least two pets, then it's fine to put fake entry)
Data Types
As you can see, each property (key) that describe you has it's own data (value) type. Let's check what each type represents:

Basic Types
String: A text. All you have to do is type a value between the quotes.
Ex:

"My name"
Date: For the sake of simplicity, we'll represent our date object as a formatted string. the format to be used is dd.MM.yyyy.
Ex:

"09.07.2021"
Number: Any number. No quotes needed.
Ex:

33
Boolean: A boolean represents either true or false. No quotes needed.
Ex:

true
X[]: An array of type X. An array represents a list of its specified type.
Ex of an array of strings

["Hi!", "DCI", "Professional"]
Object: Represents another object as a property. In our exercise, we use custom models to better define which kind of objects we're expecting as a value for each key that uses it.
Ex:

{
"custom_object_property_1": "value1",
"custom_object_property_2": "value2"
}
Custom Types
We're also using custom types in our exercise. They are:

Address
The Address object model represents your address.

It contains the following properties:

street: String - Your street's name
house_number: String - Your house's number
zip_code: Number - Your ZIP code
district_name: String - The name of your district (neighborhood)
city: String - The city's name
country: String - The country's name
Car
The Car object model represents your car.

It contains the following properties:

model_name: String - The car's model
brand_name: String - The car's brand
year: Number - The car's year, in a yyyy format
Pet
The Pet object model represents your pet.

It contains the following properties:

name: String - The pet's name
type: String - The type of your pet. Correct values would be Dog, Cat, Fish etc.
breed: String - Your pet's breed
age: Number Your pet's age
Navigating through the object
Once you have the object done, answer the following questions. Write down the full path to access each of the requested values. Consider that the reference to the object representing the YOU object is simply called me.

How can you access your first name?
How can you access your last name?
How can you access your hobbies?
How can you access your street's name?
How can you access your second pet's name?