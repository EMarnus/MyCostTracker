# Cost Calculator

My Cost Calculator is a program to project managers to easily keep track of ongoing costs to a porject.

For example, Love Maths is a site that hopes to demonstrate how pure JavaScript works in a real-world context. The site will be targeted toward people who not only love to implement more advanced JavaScript concepts but also maths. Love Maths is a fully responsive JavaScript maths game that will allow users to add, subtract, multiply and divide numbers. 

[Live site Link](https://cost-tracker-ci.herokuapp.com/)
[Workflow design](https://lucid.app/documents/embedded/e756fa59-d122-44f1-85af-31b39b35ce3f?invitationId=inv_7a6ed2b7-b615-4b97-ba5c-a47263def9a8#)

## Features 

The program allows users to Add items to the calculator, from there you can Delete the item, Calculate the VAT and Print, Calculate the margin and Print. When first loading the terminal you will set the Global Vat and Margin rates.

The objects add will be stored and reteived from an external database.

## User Experience
### User Stories
#### Visitor Goals
- As a first time user, I want easily understand the main purpose of the website.
  - Opening text explains function and acttions that can be taken.  

- As a first time user, I want to be able to easily see the options.
  - On loading you are presented with a list of options.  

- As a first time user, I want to be able to select set VAT and Margin rates for each cost.
  - Each item has an associated VAT and Margin rate that is entered with the item.  

- As a returning user, I want to be able retreive previously entered items.
  - There is an option to print all saved items.  


### Existing Features

  - The UI is a very basic terminal window.
  - Add and store "items", stores on a google sheet.
  - Print stored items, uses tabulate for readability.
  - Delete items, Items kept in backend just not printed.


### Features Left to Implement

- Add way to exit out of function.
- Add a date object to database, user input.
- Add a total row when printing.
- Add Excel file inport and export function, impossible with current frontend.

### Validator Testing 

- Python
    - All PEP8 Errors found by CI Python Linter fixed, mainly white space and indentation. [CI Python Linter](https://pep8ci.herokuapp.com/) 


## Testing & fixed bugs

- Manual testing done with each function as they are created to ensure they return expected values.
- Testing of number inputs, first iteration stopped program when non-numbers were entered, changed to provide error feedback and restart.
- Deplyed site failed to work, unused dateutil. Import removed.
- Able to input blank as item name.  
  ![Print Error](./images/printError.PNG)

### Unfixed Bugs

- Storing and retreiving Manually entered Dates for items.

## Deployment

- The site was deployed by Heroku as shown by Code Institute and the repo is on Github. The steps to deploy are as follows: 
  - In the Heroku dashboard, Select "New" then "New App" 
  - Name your app and select appropriate region.
  - Once it's created, go to settings and click the "Reveal Confic Vars" Button, add a pair PORT: 8000 and another CREDS: (the contents of you creds.json file)
  - Add 2 buildpacks, Python and Node.js in that order.
  - Go to the deploy tab, select Github as the Deployment method and link your repo, it should be conntected to your profile if you logged in with Github then you just search for the repo name. When the repo popups click "Connect"
  - Under Manual Deploy, click Manual Deploy
  - Finally, once the app has been built you can click "View" and test the deployed app.

The live link can be found here - https://cost-tracker-ci.herokuapp.com/  
The Repository can be found here - https://github.com/EMarnus/MyCostTracker


## Credits 

### Function

- How to use google cloud APIs take/learnt from Code Institute Love Sandwich porject
- Help in Printing data from workbook, https://www.educba.com/python-print-table/ and https://stackoverflow.com/questions/42235918/python-tabulate-dictionary-containing-two-values-per-key
- Updating single cell on google sheet using a string as ref, https://stackoverflow.com/questions/71029282/update-value-in-google-sheet-with-if-condition-in-another-column-using-python
- Input number function from https://www.101computing.net/number-only/