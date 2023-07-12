
## Testing APIs with *curl*

**What is cURL?**

cURL stands for “Client URL” and is a data transfer application. It consists of two components, the libcurl client-side library and the curl command-line tool. cURL was originally designed to allow Linux IRC users to automate common tasks. However, it is now available for most operating systems and behaves similarly across platforms.

`curl` uses the `libcurl` library and a simple URL-based syntax to transmit and receive data. It can be used as a stand-alone command line application, or inside scripts or web applications. The `curl` utility is common in embedded applications for vehicles, routers, printers, and audio-visual equipment. It is also used to access REST APIs and to test new APIs.

The cURL application is:

free and open source.
portable across operating systems.
contains APIs or bindings for over 50 programming languages, including C/C++, Java, and Python.
thread safe.
It also supports:

most transfer protocols and web technologies, including HTTP, FTP, SFTP, and SCP.
Ipv6 and dual-stack requests.
APIs or bindings for over 50 programming languages, including C/C++, Java, and Python.

**Installing curl**

As of 2022, the most recent release of curl is version 7.83.0. curl usually comes pre-installed on Ubuntu and other Linux distributions. To see if curl is already installed, run the curl command with the -V flag for “version”. The local installation might not match the latest edition, but any recent release should be adequate.

```shell
curl -V
```

If necessary, `curl` can be installed using `apt-get install`. Ensure the system is updated first.

```shell
sudo apt-get install curl
```

**Command Line Options for curl**

To use curl from the command line, type curl and the URL to access.

```shell
curl example.com
```

By default, curl displays its output in the terminal window. However, the -o option redirects the output to a file.

```shell
curl -o source.html example.com
```

curl includes a wide range of options. To see a list of all options, use the --help option.

```shell
curl --help
```

Some of the most important options/flags are as follows:

* `d`: Data for the HTTP POST or PUT commands.
* `F`: Update a HTTP form request from a file.
* `H`: Pass a custom header to the server.
* `m`: Set a maximum time for the transfer.
* `o`: Write the output to a file.
* `v`: Verbose mode, for more details.
* `X`: Specifies the HTTP command to use.
* `4`: Use Ipv4 addresses.
* `6`: Use Ipv6 addresses.
* `#`: Display a progress bar. This is useful for large transfers.

**cURL Methods**

`curl` uses several HTTP commands to connect to remote REST APIs. These actions correspond to the different REST verbs. The syntax for RESTful requests is simple and straightforward and is similar to other curl requests. For thorough documentation on how to use `curl`, see the official [`curl` documentation](https://curl.se/docs/).

***GET***

The `GET` operation allows `curl` to receive information from a REST API. To use the `GET` RESTful verb, use the `curl` command followed by the name of the resource to access. The `-X` attribute and the name of the operation are not required because `GET` is the default HTTP operation.

The output varies based on the server. It includes a `status`, which is set to `success` if the request is valid, the `data`, and an optional `message`. In this case, the client does not specify a format for the data, so the server responds using JSON. To see more information about the transfer, including the server options, append the `-v` (verbose) option to the command.

```shell
curl 'https://holidays.abstractapi.com/v1/?api_key=1a1b4f735df9469c9fd5a33a1dcf098e&country=US&year=2020&month=12&day=25'
```

```json
[
  {
    "name":"Christmas Day",
    "name_local":"",
    "language":"",
    "description":"",
    "country":"US",
    "location":"United States",
    "type":"National",
    "date":"12/25/2020",
    "date_year":"2020",
    "date_month":"12",
    "date_day":"25",
    "week_day":"Friday"
  }
]
```

***POST***

The `POST` verb allows users to push data to a REST API and add new entries to the remote database. The data is specified as an argument for the `-d` option. The data should be in a format matching the request. In this case, the `-H` option informs the server the data is in `application/json` format. If a format is not specified, `curl` adds `Content-Type: application/x-www-form-urlencoded` to the HTTP header. This might cause problems on some servers.

The server returns the new record, including the id of the new entry. The following command adds a new record to the application server.

for testing we will use next free public API:
* https://httpbin.org/get Returns GET data.
* https://httpbin.org/post Returns POST data.
* https://httpbin.org/put Returns PUT data.
* https://httpbin.org/delete Returns DELETE data

```shell
curl -d '{"test": "Julia test data", "username": "julia"}' -H 'Content-Type: application/json' -X POST https://httpbin.org/post
```

```json
{
  "args": {}, 
  "data": "{\"test\": \"Julia test data\", \"username\": \"julia\"}", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Content-Length": "48", 
    "Content-Type": "application/json", 
    "Host": "httpbin.org", 
    "User-Agent": "curl/7.68.0", 
    "X-Amzn-Trace-Id": "Root=1-64999e9e-5475e4d25656895c06cf9a05"
  }, 
  "json": {
    "test": "Julia test data", 
    "username": "julia"
  }, 
  "origin": "77.20.254.99", 
  "url": "https://httpbin.org/post"
}
```

This approach is fine for small amounts of data. To add multiple records, pass a file containing the information to the server. The filename can be indicated with a `@` symbol followed by the file name, as follows:

```shell
curl -d @data.json -H 'Content-Type: application/json' -X POST https://httpbin.org/post
```
We can also write response in file:

```shell
curl -o response.json -d @data.json -H 'Content-Type: application/json' -X POST https://httpbin.org/post
```

***PUT***

The RESTful verb `PUT` modifies an existing entry. This option works similarly to the `POST` option. The `-d` flag specifies the updated information for the record, and `-H` indicates the data format. 

```shell
curl -d '{"name":"Jamie","age":"23","image":""}' -H 'Content-Type: application/json' -X PUT  https://httpbin.org/put
```

```json
{
  "args": {}, 
  "data": "{\"name\":\"Jamie\",\"age\":\"23\",\"image\":\"\"}", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Content-Length": "38", 
    "Content-Type": "application/json", 
    "Host": "httpbin.org", 
    "User-Agent": "curl/7.68.0", 
    "X-Amzn-Trace-Id": "Root=1-6499a2ca-03a0b2464091075e6e57b7ed"
  }, 
  "json": {
    "age": "23", 
    "image": "", 
    "name": "Jamie"
  }, 
  "origin": "77.20.254.99", 
  "url": "https://httpbin.org/put"
}
```

***DELETE***

The `DELETE` operation removes a record from the database. It is one of the simpler REST verbs to use. As part of the `-X` option, include the `DELETE` verb and append the `id` of the record to delete to the URI. The data and header flags are not required for this operation.

```shell
curl -X DELETE https://httpbin.org/delete?id=3
```

```json
{
  "args": {
    "id": "3"
  }, 
  "data": "", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Host": "httpbin.org", 
    "User-Agent": "curl/7.68.0", 
    "X-Amzn-Trace-Id": "Root=1-6499a3c4-5f3940e7300ddb9509b4eb3e"
  }, 
  "json": null, 
  "origin": "77.20.254.99", 
  "url": "https://httpbin.org/delete?id=3"
}
```


