## About
You know #justgirlythings? Yep.

![alt text](https://raw.github.com/dianaliu/justpicklethings/master/static/img/example.png "#justpicklethings")

## TODO
- Move access_token to env variable
- Handle videos
- Save generated image, with canvas?
- Allow users to change hashtag

## Run Locally
1. Install the [App Engine Python SDK](https://developers.google.com/appengine/downloads).
See the README file for directions. You'll need python 2.7 and [pip 1.4 or later](http://www.pip-installer.org/en/latest/installing.html) installed too.

2. Clone this repo with

   ```
   git clone <project URL>
   ```
3. Install dependencies in the project's server/lib directory - App Engine
   can only import libraries from inside your project directory.

   ```
   cd <project_directory>
   pip install -r requirements.txt -t server/lib
   ```
4. Run this project locally from the command line:

   ```
   dev_appserver.py <projectDirectory>
   ```

Visit the application [http://localhost:8080](http://localhost:8080)

See [the development server documentation](https://developers.google.com/appengine/docs/python/tools/devserver)
for options when running dev_appserver.
