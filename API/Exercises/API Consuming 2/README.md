# Python-APIs-Consuming-II

## Advanced Postman and requests with curl

Since you have had the chance to create a Postman account, create a basic HTTP request, and understand your way around it, here you will dive deeper into some further functionality of Postman: [Open Notify](http://open-notify.org)

Additionally, you will also learn to make a basic GET request using [curl](https://curl.se). 

### 1. Advanced Postman

In this exercise, you will learn to call advanced APIs with query parameters to call specific data, and see the patterns in such sort of information retrieval. 

In the lectures, you have learnt about query parameters. Here we will look at a more complex set of APIs with larger amount of data, a larger JSON structure, and will use query params to call specific information for this data.

The API you will be calling is called the [Faker API](https://fakerapi.it/en). Faker Faker API is a collection of completely free APIs that helps web developers and web designers generate fake data in a fast and easy way. No registration is required. No tokens, no authentication.

#### Exercise Instructions

0. Go to [Faker API](https://fakerapi.it/en) website and read the short description on how to use the API. **Make sure you understand how the queries work**

Then go to your Postman Client and:

1. Make GET call to get some companies. 
2. Make GET call to get 50 persons with English names who were born after 1994. 
3. Make GET call to get 5 German companies. 
4. Make GET call to retrieve 60 credit cards of Spanish people.
5. Make GET call to retrieve 47 products that cost higher than 50€.  
6. Make GET call to retrieve 10 Custom objects with "pokemon", "website", and "name" fields.


### 2. Using curl

Curl is a Command-Line based HTTP client and more. It is highly embedable.and has an insane number of use cases. Never mind, we will take it one step at a time and replicate what you have been doing so far. 
You will be using curl to communicate with the [Faker API](https://fakerapi.it/en), as you did with Postman in the previous exercise. 
Lastly, you will have to save each response to a JSON format file. 

#### Exercise Instructions

0. Go to  https://curl.se/download.html and download + install the curl source package for your machine. 

1. Go to [Faker API](https://fakerapi.it/en) website and read the short description on how to use the API. **Make sure you understand how the queries work**

Open your Terminal (or whatever CLI your machine provides) and using curl:

2. Make GET call to get some companies. 
3. Make GET call to get 50 persons with English names who were born after 1994. 
4. Make GET call to get 5 German companies. 
5. Make GET call to retrieve 60 credit cards of Spanish people.
6. Make GET call to retrieve 47 products that cost higher than 50€.  
7. Make GET call to retrieve 10 Custom objects with "pokemon", "website", and "name" fields.