Me As a XML
Similar to the last exercise, in this exercise you'll have to transcribe yourself as a XML file!

You'll have to create a XML file from scratch. You can either use your prefered text editor, or just use an Online XML Editor like this one here.

Hint: If you don't feel comfortable putting your real data on the exercise, feel free to do it with fake data. The important thing here is the learning experience.

The YOU object
The YOU object can be represented with the Me tag. So, all in all, your solution should start like:

<?xml version="1.0" encoding="utf-8"?>
<Me>
...
</Me>
And in between the Me tag you can start populating with the following values about yourself:

FirstName - Your first name
LastName - Your last name
BirthDate - Your birth date. Use the dd.MM.yyyy format.
Age - Your age
Gender - Your gender. For this exercise, assume you can provider either M for male, F for female or O for other.
Nationality - Your nationality, either as a string (single nationality) or an array of strings (double+ nationalities). In the case of more than one nationality, wrap the Nationality entries inside a Nationalities entry.
IsMarried - If you are married or not, as a boolean value
HasChildren - If you have children or not, as a boolean value
Hobbies: Hobby[] - Your hobbies, as an array of Hobby
Address: Address - Your address, as an address object (more on that below)
Car: Car - Your car, as a car object (more on that below. If you don't have one, it's fine to just put fake values - or your bicycle's data, why not!?)
FavoriteTVShows: TVShow[] - Your favorite TV shows, as an array of TVShow
Pets: Pet[] - Your pets, as an array of the pet object (more on that below. You should write at least two entries here - if you don't have at least two pets, then it's fine to put fake entry)
Data Types
Here, a few things change. In general, most values are just strings.

Special cases:

Nationality: In the case of double+ nationalities, you can wrap the values with a Nationalities entry.
Ex:

<Nationalities>
    <Nationality>Nationality1</Nationality>
    <Nationality>Nationality2</Nationality>
</Nationalities>
Hobbies: Hobby[]: Specify each hobby with the Hobby tag, and wrap them using the Hobbies tag.
FavoriteTVShows: TVShow[]: Same here, but wrapping multiple TVShow inside FavoriteTVShows.
Custom Types
The custom types here should use the attributes from the XML tags. An example of a tag using attributes is the following:

<MyTag myAttribute1="myValue1" myAttribute2="myValue2" />
Address
The Address object model represents your address.

It contains the following attributes:

street - Your street's name
houseNumber - Your house's number
zipCode - Your ZIP code
districtName - The name of your district (neighborhood)
city - The city's name
country - The country's name
Car
The Car object model represents your car.

It contains the following attributes:

modelName - The car's model
brandName - The car's brand
year - The car's year, in a yyyy format
Pet
The Pet object model represents your pet.

It contains the following attributes:

name - The pet's name
type - The type of your pet. Correct values would be Dog, Cat, Fish etc.
breed - Your pet's breed
age Your pet's age
Since we have an array of Pet, wrap them inside the Pets tag.