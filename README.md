# Website-Images-Spider
The repo consists of a source of for scraper made in python for downloading/scraping all public available images from a given website.

How it works 
----------------
Once you specify the website, the scraper will scans through out a given website to find all public available tlinks and dive into all of those to find if there is any downloadable image , If there is , it will automatically download it and save on your local directory.


Getting started
------------------
To get started using this tool, firstly *clone* or *download* the repository to your computer just as shown below;

```bash
$-> git clone https://github.com/Kalebu/Website-Images-Spider
```

Dependancies
---------------
Before you begin playing this project, I recommend you to install the following dependencies first

```bash
$-> pip install bs4, requests, pillow
```

Move into the Project directory
-------------------------------
Navigate into your project repository either by using **cd** commands or by opening a terminal inside a project repository.

```bash
$-> cd Website-Images-Spider
$ Website-Images-Spider-> python app.py
Enter URL with images : 
```

Enjoy downloading the images
-----------------------------
Now once you run the script, it will prompt you to enter a url for a specific website you would like to scrap the images from  and then once done, take a coffe while you wait for the images to be downloaded.


Note
--------
This script doesn't work very well with website with a bunch of JS

Issues 
-----------

Incase you have any difficulties or issues while trying to run the script
you can raise it on the issues. 

Pull Requests
----------------

If you have something to add I welcome pull requests on improvement , you're helpful contribution will be merged as soon as possible 

Give it a Star ✴️
--------------------
If you find this repo useful , give it a star

Credits
-----------
All the credits to [kalebu](github.com/kalebu)
