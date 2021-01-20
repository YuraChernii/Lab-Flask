## PythonLab

## How to start:
#### 1) Git clone or download zip
```
$ git clone https://github.com/YuraChernii/Lab-Flask.git
```
### Download, create and activate virtualenv:
```
#### 2)write:
```
$ pip install virtualenv
```
####   3)Open poject and write: virtualenv env -p <path to version of python(example: c:\Python27\python.exe)>
#### 4)Then: pip install -r requirements.txt
#### 5)Then: env\scripts\activate.bat

```

To run project:
1)../PythonLab: set FLASK_APP=PythonLab.py
2)../PythonLab: flask run 
>>>>>>> origin


## General info:
Hi)) This is an online store that provides easy access to the database. The administrator can receive, edit, add and delete data after authorization. And all this he performs on raw sql queries. In the event of an error, the system responds with a fairly clear explanation of the error.

## Let's try to run it:

#### 1)git clone or download zip
#### 2)Double click on Tymchak_shop.csproj file
#### 3)Open dbsettings.json and change ConnectionStrings:DefaultConnection
#### 4)Open Package Manager Console:
```
  $ Add-Migration MyMigration -Context AppDBContent
  $ Update-DataBase
```
#### The program generates data automatically
#### 5)Now you can run. Started!!Huuh))
#### 6)You can see the "For administration" tab. Click on it
#### 7)Then you have to log in. Two fields have a password: 1234ddfSD
#### 8)Finally you can enter sql query
## More:
##### Implementation of "SQLEditor" you can see in HomeController-EditDB
##### Tests in Tests(SQLEditor).docx
