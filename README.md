# SaveSoil-Research-code

Helps find the desired social media URLs related to a given input text  
It does so by automatically searching Google with the text in a file called input.txt that must be in the same directory as the executable  
Each line in that input file will result in a new output line  
An empty input line will result in an empty output line  
The input file is mainly intended for organizations' names. Sometimes you'll need to add some text after the company name to help disambiguate, to help increase the possibility that Google finds what you intend it to find  

Each output line will contain:  
  1. Instagram URL
  2. Number of Instagram follower
  3. Facebook URL
  4. Twitter URL
  5. Number of Twitter followers
  6. Youtube URL
  7. "Contact Us" URL
  8. Main URL
  
The output file is called output.csv and can be opened as a spreadsheet  
If it stops running at a given moment (check every ~5 min), delete the input lines related to inputs it has correctly found already and run it again. It does happen with some frequency
