![NBA App main menu](https://res.cloudinary.com/arnaldo10cisne/image/upload/v1636860311/nba_app_python/nba_python1_bzdclz.png)

# NBA App - Python edition

This program was intended as the resolution of a technical test provided by Macheight. The program extracts general information about several NBA players from an URL and is capable of creating pairs of players whose heights add up to a number previously given by the user.

![App capture 1](https://res.cloudinary.com/arnaldo10cisne/image/upload/v1636860526/nba_app_python/nba_python2_nxrg37.png)
![App capture 2](https://res.cloudinary.com/arnaldo10cisne/image/upload/v1636860526/nba_app_python/nba_python3_-_copia_r13anf.png)
![App capture 3](https://res.cloudinary.com/arnaldo10cisne/image/upload/v1636860526/nba_app_python/nba_python4_txpa5g.png)

## How to use:
This repository contains the following ".py" files. You'll need all three of them to run this program:

- **main**:  This is the file where you'll find the rendering of the main menu, and each of the options it contains. It will also do the calls to all the functions that will make this program work.
- **nba_module**: Here, you’ll find the most important functions that will help sort the array of players and search for all the matches.
- **support_module**: This module includes all the imports that the program needs to work, and some auxiliary functions to help with aesthetics.

### Running the code:

You can run this application following the next steps:

1.  First, you have to make sure that you have Python installed on your computer. If you are not quite sure if Python is installed on your computer, please go to the command line and type `python3 --version` if you are on Linux or Mac, or `python --version` if you are on Windows. You should be given the current version of Python installed on your computer. If an error message pops up saying that the command was not recognized, most likely you need to install Python. To do so, please follow [this](www.m.com) tutorial.
 2. After Python has been successfully installed, the next step is very simple. You need to download this repository in a ZIP file
	 - ![enter image description here](https://res.cloudinary.com/arnaldo10cisne/image/upload/v1636934741/nba_app_python/instructions1_kg8aqj.png)
 3. Once you have all files, locate them on a single directory, and make sure to run the file **"main .py"**. If you have all files in the same directory, the app should run without any issues.
 4. If the program doesn't start, however, make sure you have the "request" module installed. This module is required for python to fetch the data from the URL. To install this module, inside the command line execute the following command: `pip install requests`

## Inner workings:
The way this program works can be summarized in the following steps:

 1. After the user selects the option to ***Start this App*** in the main menu, the first thing this program is going to do is try to fetch the data from the given URL.
 2. After the information has been gathered by the program, a sorting algorithm is applied to said data. This is to facilitate the search later.
 3. Once the data has been collected and sorted, the user will be asked for a number. Before continuing, the program will carry out all the necessary validations to prevent any failure during the execution of the algorithm
 4. After doing all the necessary validations, the program will perform a binary search for each of the players in the array given. 
 5. After finding one match, the program will validate all the other results that are next to it, to collect all possible solutions. I called this part the “spread” algorithm.
	 - ![Spread algorithm](https://res.cloudinary.com/arnaldo10cisne/image/upload/v1636863263/nba_app_python/nba_graphic1_sr9yh2.png)
 7.  After the "spread" algorithm has collected the indexes of all the players that match, the program evaluates the next player in the array and does the same process.
 8. To avoid repeated matches, the program has the condition that, in a pair, the first player has to have a lower or equal height to the second player.
	   - ![enter image description here](https://res.cloudinary.com/arnaldo10cisne/image/upload/v1636863762/nba_app_python/nba_graphic2_t2ohhi.png)
 9. Finally, when all the pairs have been saved in an array, the program uses that information to show all those pairs with the first name, last name, and height to the user.

## Algorithmic complexity:
One of the requirements of this project was implementing algorithms that had better performance than *O(N^2)*. 

![enter image description here](https://3.bp.blogspot.com/-Frcylha7Spw/XA51cet8wkI/AAAAAAAACpg/RKrCC5gDtOofmPfCrFNM_UF83BY9AlI3QCLcBGAs/s1600/big-o-complexity-chart.png)

This program has two parts where the Algorithmic complexity is worth considering:

 - **Sorting the array**: The algorithm used to sort the array was *The Merge sort*. Created by John von Neumann in 1945, this is one of the most efficient sorting algorithms to date. Worst case scenario, this algorithm has a performance of *O(N x log N)*. 1.  It works by dividing the array more and more until we have arrays of just one element. Then, through a series of comparisons, combine said unit arrays in such a way that they are in the desired order. 
	 - ![enter image description here](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Merge-sort-example-300px.gif/220px-Merge-sort-example-300px.gif)
 - **Searching inside the array**: 1.  The algorithm used to search for an element in the array was _The Binary search_. It takes the principle of “Divide and conquer”. Worst case scenario, this algorithm has a performance of _O(log N)_, making it one of the most efficient algorithms to date. It works by dividing the array in half again and again until it finds the desired element. The only downside would be the fact that this algorithm requires the list to be ordered. Hence, it the importance of sorting the list before working on it.
	 - ![enter image description here](https://blog.penjee.com/wp-content/uploads/2015/04/binary-and-linear-search-animations.gif)

The most complex algorithm used in this case was the mixing algorithm, used in the sorting section. Then, a function was used where binary searches were performed iteratively, causing an algorithmic complexity of *O(N x log N)*. ![enter image description here](https://res.cloudinary.com/arnaldo10cisne/image/upload/v1636866062/nba_app_python/nba_graphic3_fu9b0w.png)

### Finally

Any suggestion you have on how to improve this project can be submitted using the  [contact form in my personal website](https://www.arnaldocisneros.com/contact). Finally, to the developers at Macheight, I am very grateful for the opportunity you have given me to test my skills as a developer. I hope this resolution is to your liking. Please note that I have put a lot of heart into its realization. Have a wonderful day!