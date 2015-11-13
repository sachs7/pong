write a Python program somewhat similar to http://www.pythonlearn.com/code/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:

Sample data: http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.json (Sum=2553)
Actual data: http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_171038.json (Sum ends with 52)

Data Format
The data consists of a number of names and comment counts in JSON as follows:

{
  comments: [
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }
    ...
  ]
}

Sample Execution

$ python solution.py 
Enter location: 
Retrieving http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.json
Retrieved 2739 characters
Count: 50
Sum: 2553
