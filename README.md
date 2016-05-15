# xml_presset_TI
Example files for JSOM Travis-CI tests

1. Download the files 
2. Copy the .travis file on the root of your repository. This file explain to Travis-CI what tests will do when the test run.
3. Copy the test folder to the root of your repository. This folder contains two files, an xsd than specifies how the xml should be and the test source code in python.
4. Edit the file test_unitest.py in the line 7 to put the name of your xml filename.
5. Register to Travis-CI using github and give travis rights to acces to your data (step 1 from [here](https://docs.travis-ci.com/user/getting-started/#To-get-started-with-Travis-CI%3A) )
6. Enable the tests for your repository( step 2 from [here](https://docs.travis-ci.com/user/getting-started/#To-get-started-with-Travis-CI%3A) )
7. You can add a Travis indicating the build status to force the re-build following this instructions
