# movie_filter

A virtual env is recommended. Install dependencies using requirements.txt for backend. Run python manage.py runserver in
the root folder (djangoProject) to start the backend.

After installing relevant libraries and running the django project, first navigate
to [http://127.0.0.1:8000/fetch-and-save-movies/](url) to load your database (I used Postgresql version 13) with movies
data then navigate to [http://127.0.0.1:8000/movies-list/](url)  to access the filter and search functionality.

PS: I did not work enough on the CSS at all, even though it takes a little work to make a huge difference. My main focus
was functionality. I have also used some JS code to render the data in a pretty way, but I am certain I can convert them
using only backend logic.

Tasks left to be done:

-> Integrate Better JWT authorization

-> Add comments

-> Add login/register and permission based classes

-> Improve css of the table

-> Delete redundant code (non-operational attempts and console logs)

-> Bundle the project better

-> Much, Much more !!
