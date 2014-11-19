# The PDF Project 

*For Software Construction Fall 2014*

Catherine Moresco, Jonathan Jin, Megan Barnes, Michael Zhao, Alberto Rios, and Cristian Saucedo

## Update 11/19/14: Iteration 2 Plans
Features to be included:

##### UI:
- Highlights!
- Annotations!
- Deleting highlights and annotations!
- Some fine-looking front-end desgin!

##### Server:
- Modified PDF document download!
	+ Getting highlight data from frontend
	+ Merging highlights and SVG edits
- Streamlined file handling!

##### Image processing:
- Refined image processing algorithms!
	 + Better skew detection accuracy
	 + Modification of skew algorithm to distinguish images from text
	 + Enhanced handling of noise and blacked-out margins


##### Overall: 
- Opportunities for user correction of algorithmic failings!

Ultimately, there are elements of our original design that we will realistically not have time to implement---element-wise OCRing for highlighting, for example. However, we plan to achieve functionality for the most basic and most common use cases.

## Who's doing what:
The teams will remain largely the same. 

Alberto and Christian will being doing front-end work (and Catherine will work with them on the fine-looking front-end design).

Megan and Catherine will be working on image processing. 

Alberto will also be working on server-side operations. 

Jonathan will be working on test coverage and helping to migrate front-end tests towards a more robust, automated system.

## Features

Features successfully implemented in this iteration include:
- File uploading
- Exporting PDF pages to JPG images
- Image processing
	+ Skew detection and correction
	+ Extraction of text line coordinates
- Image display

## Example Usage and Recommended Acceptance Tests
It's pretty simple to use: upload your own document with the "upload" button, and watch it appear---processed and straightened!

The best images are ones that are well formed, and have only one page of text per PDF page. Images imbedded in the text are OK!


## Dependencies
Install python packages with `pip install -r <path/to/requirements.txt>`.

Third party packages (see respective websites for installation instructions):

- [OpenCV2](http://opencv.org/)
- [ImageMagick](http://www.imagemagick.org/) and [PythonMagick](http://www.imagemagick.org/download/python/)

## How to Run
After installing dependencies, you can run the app locally with `python runserver.py`.

For automatic server-crash recovery, install supervisord and start the server using `run.sh`.

## How to Run Unit Tests
#####Image Processing Tests:
From within tests/cvtests, run the command `python -m unittest -v cv_unit_tests`.

*- Megan and Catherine*

##### UI Tests:
 The unit tests that we initially submitted will not run given the changes in our UI desgin.We are researching automated processes for testing UI that will be incorporated into Iteration 2.

 *- Alberto and Cristian*

## Who did What
##### Alberto & Cristian: 
We were in charge of User Interface design. We created the HTML displayed, worked on uploading files to server, passing files to CV modules, and displaying the resulting files.

##### Catherine & Megan: 
We were in charge of the Computer Vision aspect of the project.  We worked on processing image files in order to determine whether or not they should be rotated and to determine where lines were in text documents.

##### Michael Zhao
Set up the server.

##### Jonathan Jin
Taking on QA and test coverage responsibilities. Designed the preliminary front-end testing framework that, as of 11/19/14, comprises the primary front-end test suite.

## Evolution
While our first iteration of the software construction process did not meet all the grand visions we have for it, it was a good first step. We implemented the basic functions of file uploading, and impage processing and displaying, and laid the groundwork for user interaction with the document. 

One of the major ways in which our current implementation differs from our initial design is the architecture and design portion of the backend. We designed a somewhat elaborate class diagram to structure our document data. Once we started writing code, however, we realized that the PDF data would best be handled by a pipe-and-filter architecture, and so our approach became more functional, implementing no Python classes at all.

The frontend will likely implement more objects as development continues, although it is unlikely to develop into the complextiy of our original plan. And this isn't necessarily a bad thing! After all, Simplicity is one of the twelve principles behind the Agile Manifesto.

## Additional Information

Some limitations are worthy of note. Our image processing algorithms can use improvement. In this iteration, they only support documents that are fairly well-formed: rotated no more than 90 degrees in either direction, with fairly straight text lines, and good contrast. In the future, we intend to implement more sophisticated and efficient algorithms, as well as providing opportunities for the user to correct errors in processing.

