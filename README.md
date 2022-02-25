# SaveSoil-Research-code

Helps find the desired social media URLs related to a given input text.  
It does so by automatically searching Google with the text in a file called input.txt that must be in the same directory as the executable.  
Each line in that input file will result in a new output line.  
An empty input line will result in an empty output line.  
The input file is mainly intended for organizations' names. Sometimes you'll need to add some text after the organization's name to help disambiguate, to help increase the possibility that Google finds what you intend it to find. For example, instead of just leaving "Isha" as input text, you may write "Isha USA" to directly find what you want. There's still a chance that Google doesn't find exactly what you wanted, and maybe what you want doesn't exist, but overall this still helps.  

Each output line will contain:  
  1. Instagram URL
  2. Number of Instagram follower (divided by 1000)
  3. Facebook URL
  4. Twitter URL
  5. Number of Twitter followers (divided by 1000)
  6. LinkedIn URL
  7. Youtube URL
  8. "Contact Us" URL
  9. Main URL
  
The output file is called output.csv and can be opened as a spreadsheet.  
If it stops running at a given moment (check every 5 to 10 min), delete the input lines related to inputs it has correctly found already and run it again. It does happen with some frequency.  
The executable open a command prompt window and promts you for your instagram username and password, in order to be able to grab the instagram followers as desired.

Example single output line:  
Agro Banacaribe,,,,,https://www.instagram.com/agrocaribe19/,0.109,https://www.facebook.com/pages/category/Local-Business/AGROBANACARIBE-509239295831261/,,https://twitter.com/Agro7ca/status/884957666174533632,0.015,https://co.linkedin.com/in/jiovany-p%C3%A9rez-valencia-64b890130,,https://www.youtube.com/watch?v=eNDke7xyBKw,,https://www.bancaribe.com.ve/zona-de-informacion-para-cada-mercado/corporaciones/soluciones-financieras/creditos-soluciones-financieras/linea-agropecuaria,,https://www.bancaribe.com.ve/zona-de-informacion-para-cada-mercado/corporaciones/soluciones-financieras/creditos-soluciones-financieras/linea-agropecuaria,,

USAGE in Windows
1. Go to the dist folder
2. Put what you want to look for in each line of the input file
3. Clear the output.txt file if needed
4. Run social_media_analyzer_with_input_file.exe by double clicking it
5. Enter your instagram credentials
6. Enjoy your time back!
