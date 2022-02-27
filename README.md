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
  4. Number of facebook likes (divided by 1000)
  5. Twitter URL
  6. Number of Twitter followers (divided by 1000)
  7. LinkedIn URL
  8. Youtube URL
  9. TikTok URL
  10. Number of TikTok followers (divided by 1000)
  11. "Contact Us" URL
  12. Main URL

The numbers of followers will only appear if the found URL corresponds to what is expected and if it exists.
The output file is called output.csv and can be opened as a spreadsheet.  
If it stops running at a given moment (check every 5 to 10 min), delete the input lines related to inputs it has correctly found already and run it again. It does happen with some frequency.  
The executable open a command prompt window and promts you for your instagram username and password, in order to be able to grab the instagram followers as desired.

Example single output line:  
Lafrancol,,,,,https://www.instagram.com/explore/tags/lafrancol/?hl=en,51.368,https://www.facebook.com/pages/category/Medical-Lab/Laboratorio-Lafrancol-SAS-100900988047210/,0.496,https://twitter.com/lafrancol2,0.056,https://www.linkedin.com/company/abbott-laboratories---lafrancol-s.a.s,,https://www.youtube.com/playlist?list=PLWKGG5dUqiMGwDsJyzIVZ8Im4Llnv6vOB,,https://www.tiktok.com/@francoescamillaofficial?lang=en,11300.0,https://www.dnb.com/business-directory/company-profiles.laboratorio_franco_colombiano_lafrancol_s_a_s.368cfa7318e90cc5cc8c7012c6eb1cb2.html,,https://www.dnb.com/business-directory/company-profiles.laboratorio_franco_colombiano_lafrancol_s_a_s.368cfa7318e90cc5cc8c7012c6eb1cb2.html,,

USAGE in Windows
1. Download the "dist" folder
2. Go to the downloaded dist folder. Extract it from a zip file if needed
3. Put what you want to look for in each line of the input.txt file
4. Clear the output.csv file if needed
5. Run social_media_analyzer_with_input_file.exe by double clicking it
6. Enter your instagram credentials
7. Enjoy your time back!
