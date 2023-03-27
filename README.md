<h1 style="text-align:center;">STEM Project Repository</h1>
In this repository you can find all of the code and assets used to make all versions of the website.  <br>
<br>

<b>Link:</b> https://mlev29.pythonanywhere.com/ 
<br>
<br>

## How to use this repository?
If you are unfamiliar with Github this guide will go over the areas to go see.

### Viewing the current website code
The current version of the code ran by the website is located in the folder called `STEMWebsiteMain/STEMproject/`. In this folder you will see the following items.
<br>
<br>

## General Info
<b>Host Used:</b> PythonAnywhere

<b>Programming Languages Used:</b>
- Python
- HTML
- CSS
- Javascript

<b>Website Framework:</b> Django


## Project Overview
<details><summary>STEMproject</summary><blockquote>
	<details><summary>📁 home</summary><blockquote>
    	<details><summary>📁 static</summary><blockquote>
			<details><summary>📁 css</summary><blockquote>
    		extra.css<br>
			style.css
  			</blockquote></details>
			<details><summary>📁 img</summary><blockquote>
    		banner_new.png<br>
			basic_django.png<br>
			bootstrapLogo.png<br>
			CSS_logo.png<br>
			djangoLogo.png<br>
			HTML5_logo.png<br>
			javascript_logo.png<br>
			python_logo.png
  			</blockquote></details>
		</blockquote></details>
		<details><summary>📁 template</summary><blockquote>
			<details><summary>📁 home</summary><blockquote>
			home.html
			</blockquote></details>
  		</blockquote></details>
  	</blockquote></details>
	<details><summary>📁 siteConfig</summary><blockquote>
		asgi.py<br>
		index.py<br>
		settings.py<br>
		urls.py<br>
		wsgi.py
  </blockquote></details>
  manage.py
</blockquote></details>
<br>
The file structure shown above (click on the arrow above), represents all the code when optimized used to keep the site running and display the visual aspect (front-end) of the site.

In the main `STEM_Project` folder, there are both a `SiteConfig` folder and a `home` folder
### Home 
This folder is all the front-end code for the website home page, the main html folder is located under `home/template/home/home.html`. Other resources including the CSS files and images can be found under the `home/static` folder.

### SiteConfig
This folder contains all the website settings and is incharge of getting the required site urls, library urls and starting / shuting down the site. 
<br>
![SiteConfig Diagram](https://raw.githubusercontent.com/MLev29/STEM-Project/main/WebsiteAssets/IMG/basic-django.png)
## Change Log 
### Most Recent
23/3/2023 - Optimisation and cleanup

Full changle log can be found in `implemented.gitignore`. This file can be found under `STEM-Project/WebsiteAssets/changelog.gitignore`