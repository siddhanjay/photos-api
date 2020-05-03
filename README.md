# photos-api
Simple API for photo sharing. Supports CRUD operations on posts with authentication(including Jwt), user management and filtering and searching of posts.

Built on Python with Django and rest-framework

Project demo can be accessed here: https://siddhanjay.herokuapp.com/

API endpoints:

* Admin panel -> Create and manage users. Superuser id and password is admin for the demo https://siddhanjay.herokuapp.com/admin/

* View all posts -> https://siddhanjay.herokuapp.com/photos/

* View posts by user -> https://siddhanjay.herokuapp.com/photos/?user=1

* Search posts -> https://siddhanjay.herokuapp.com/photos/?search=hello

* Sort posts by publish date -> https://siddhanjay.herokuapp.com/photos/?ordering=publish_time

* View a particular post and modify/delete -> https://siddhanjay.herokuapp.com/photos/2/

* Register user for jwt token -> https://siddhanjay.herokuapp.com/register/

        { "username":"admin",
        "password":"admin",
        "password2":"admin"}

* Obtain JWT token ->  https://siddhanjay.herokuapp.com/token/

* JWt refresh token ->  https://siddhanjay.herokuapp.com/refresh/
