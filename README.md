# Cost Calculator

My Cost Calculator is a program to project managers to easily keep track of ongoing costs to a porject.

For example, Love Maths is a site that hopes to demonstrate how pure JavaScript works in a real-world context. The site will be targeted toward people who not only love to implement more advanced JavaScript concepts but also maths. Love Maths is a fully responsive JavaScript maths game that will allow users to add, subtract, multiply and divide numbers. 

[Live site Link]()
![Workflow design](https://lucid.app/documents/embedded/e756fa59-d122-44f1-85af-31b39b35ce3f?invitationId=inv_7a6ed2b7-b615-4b97-ba5c-a47263def9a8#)

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

![Logo](media/love_maths_logo.png)

### Features Left to Implement

- Add a date object to database.
- Add a total row when printing.

### Validator Testing 

- HTML
    - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcode-institute-org.github.io%2Flove-maths%2F)
- CSS
    - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvalidator.w3.org%2Fnu%2F%3Fdoc%3Dhttps%253A%252F%252Fcode-institute-org.github.io%252Flove-maths%252F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
- JavaScript
    - No errors were found when passing through the official [Jshint validator](https://jshint.com/)
      - The following metrics were returned: 
      - There are 11 functions in this file.
      - Function with the largest signature takes 2 arguments, while the median is 0.
      - Largest function has 10 statements in it, while the median is 3.
      - The most complex function has a cyclomatic complexity value of 4 while the median is 2.

## Testing & fixed bugs

- Manual testing done with each function as they are created to ensure they return expected values.
- Testing of number inputs, first iteration stopped program when non-numbers were entered, changed to provide error feedback and restart.

### Unfixed Bugs

- Storing and retreiving Dates for items.

## Deployment

- The site was deployed by Heroku as shown by Code Institute and the repo is on Github. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://code-institute-org.github.io/love-maths/


## Credits 

### Function

- How to use google cloud APIs take/learnt from Code Institute Love Sandwich porject
- Help in Printing data from workbook, https://www.educba.com/python-print-table/ and https://stackoverflow.com/questions/42235918/python-tabulate-dictionary-containing-two-values-per-key
- Updating single cell on google sheet using a string as ref, https://stackoverflow.com/questions/71029282/update-value-in-google-sheet-with-if-condition-in-another-column-using-python
- Input number function from https://www.101computing.net/number-only/