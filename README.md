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
#### First Time Visitor Goals
- As a first time user, I want easily understand the main purpose of the website.
- As a first time user, I want to be able to easily see the options.
- As a first time user, I want to be able to select set VAT and Margin rates for each cost. 

#### Returning Visitor Goals
- As a returning user, I want to be able retreive previously entered items.


### Existing Features

- __UI__

  - The UI is a very basic terminal window

![Logo](media/love_maths_logo.png)

### Features Left to Implement

- Add a date object to database.

## Testing 

Manual testing done with each function as they are created to ensure they return expected values.


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

### Unfixed Bugs

You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed. 

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub) 

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://code-institute-org.github.io/love-maths/


## Credits 

### Function

- How to use google cloud APIs take/learnt from Code Institute Love Sandwich porject
- Help in Printing data from workbook, https://www.educba.com/python-print-table/ and https://stackoverflow.com/questions/42235918/python-tabulate-dictionary-containing-two-values-per-key

### Content 

- 
- 
- 


Congratulations on completing your Readme, you have made another big stride in the direction of being a developer! 

## Other General Project Advice

Below you will find a couple of extra tips that may be helpful when completing your project. Remember that each of these projects will become part of your final portfolio so it’s important to allow enough time to showcase your best work! 

- One of the most basic elements of keeping a healthy commit history is with the commit message. When getting started with your project, read through [this article](https://chris.beams.io/posts/git-commit/) by Chris Beams on How to Write  a Git Commit Message 
  - Make sure to keep the messages in the imperative mood 

- When naming the files in your project directory, make sure to consider meaningful naming of files, point to specific names and sections of content.
  - For example, instead of naming an image used ‘image1.png’ consider naming it ‘landing_page_img.png’. This will ensure that there are clear file paths kept. 

- Do some extra research on good and bad coding practices, there are a handful of useful articles to read, consider reviewing the following list when getting started:
  - [Writing Your Best Code](https://learn.shayhowe.com/html-css/writing-your-best-code/)
  - [HTML & CSS Coding Best Practices](https://medium.com/@inceptiondj.info/html-css-coding-best-practice-fadb9870a00f)
  - [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html#General)