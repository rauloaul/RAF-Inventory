> [Click Here](https://raf-inventory.adaptable.app/main/) to access RAF's Inventory App

## Assignment 2

<details>
<summary>How do I implement the tasks form the checklist in Assignment 2?</summary>

#### 1. Create a new Django project.
- When creating Django project, I started it with cloning the repository, so I don't have to connect local repository to the Github repository. So, I use this command:
    ```
    git clone [URL]
    ```
- Then I started by creating a virtual environment with:
    ```
    python -m venv env
    ```
- Then I need to activate the virtual environment with the following command:
    ```
    env\Scripts\activate.bat
    ```
- After that I have to set up dependencies, which are components required by the software to function, including libraries, frameworks, or packages. So, we create a .txt file named `requirements.txt`, and add some dependencies.
    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
- Install those dependencies with pip install:
    ```
    pip install -r requirements.txt
    ```
- Finally, I created the Django project with name `assignment2`, and note I don't know how to change this name to a new name because, at first I accidentally create the Django project with this name, and I want to change it with rafinventory, *please help*. I use this following command:
    ```
    django-admin startproject assignment2 .
    ```
- Then, I successfully create the Django project.
- In `settings.py`, I add `"*"` to `ALLOWED_HOSTS` for deployment purposes
- Finally, I create a `.gitignore` file.
#### 2. Create an app with the name main on that project:
- First, I did  it with this following command to create a new application `main`:
    ```
    python manage.py startapp main
    ```
- Then, I have to register `main` application to the project by adding `'main'` in the `INSTALLED_APPS` inside the `settings.py`.
- After that, I created new directory `templates` within the `main` application, and inside it we create `main.html`. Then we successfully create app main with HTML templates.

#### 3. Create URL routing configuration to access the `main` app.
- I add URL routing in `urls.py` to connect it to the `main` view. So, in the `urls.py` inside the `assignment2` directory, I import `include` funtion from module `django.urls`

- I add the URL pattern to direct it to the `main` view inside the `urlpatterns` variable.
    ```py
    path('main/', include('main.urls'))
    ```
- Finally, I successfully create URL routing configuration to the `main` app.

#### 4. Create a model on the main app with the name Item and some mandatory attributes:
- In the `models.py` I create a class named `Item` with this attributes:
    - `name` as the name of the item, with type `CharField`.
    - `amount` as the amount/count of the item, with type `IntegerField`.
    - `description` as the description of the item, with type `TextField`.
    - `category` as the category of the item, with type `TextField`.
    - `power` as the amount of power of the item, with type `IntegerField`.
- Then, I create model migrations with:
    ```
    python manage.py makemigrations
    ```
- After that, I apply the migrations with the local database:
    ```
    python manage.py migrate
    ```

#### 5. Create a funtion in `views.py` that returns an HTML template containing my application name, my name, and my class.
- First, I open `views.py` in the `main` application. Then on the file I add the following import statements, and add function `show_main`:
    ```py
    from django.shortcuts import render

    def show_main(request):
    context = {
        'application_name': 'RAF Inventory',
        'name': 'Rafif Firmansyah Aulia',
        'class': 'PBP KKI'
    }

    return render(request, 'main.html', context)
    ```
- After that, I replace created application name, name, and class in the `main.html` file in `templates`.

#### 6. Create a routing in `urls.py` to map the function `views.py` to an URL.
- I create a file `urls.py` inside `main` application directory, and fill it with this following code:
    ```py
    from django.urls import path
    from main.views import show_main
    
    app_name = 'main'

    urlpatterns = [
       path('', show_main, name='show_main'),
    ]
    ```
#### 7. Deploy the app to adaptable.
- First, perform add, commit, push to the github repository.
- Then, create new app in adaptable, and connect the repository to adaptable.
- After that, I use Python App template and PostgreSQL, then I chose python 3.10 as the version and in the start command I use:
    ```
    python manage.py migrate && gunicorn assignment2.wsgi
    ```
- Then enter the domain name, also check the HTTP Listener on PORT.
- Finally, deploy the app to adaptable.

</details>

<details>
<summary>Diagram explaining the flow of client requests to a Django web app and its response.</summary> 
![Alt text](image-1.png)

</details>

<details>
<summary>What is the purpose of a virtual environment? Can we create a Django web app without a virtual environment?</summary>

Virtual environment is a fundamental tool in Python development. It serves as an isolated workspace, ensuring that each project remains independent of others and the global Python environment. This isolation is critical for managing distinct Python and package versions required for different projects. Analogously, it's akin to maintaining an organized workspace. Just as you wouldn't want your tools intermingled in disarray, virtual environments keep project directories neat and tidy. Additionally, they simplify project sharing and enhance portability. In the context of Django web applications, virtual environments are imperative. They help manage dependencies, ensuring a clean and isolated environment conducive to project development. In conclusion, virtual environments are indispensable for maintaining order, preventing conflicts, and facilitating structured Python project development, particularly for Django web applications.

</details>

<details>
<summary>What is MVC, MVT, and MVVM? Explain the differences between the three.</summary>

- MVC, which stands for Model-View-Controller, is a software architecture. In this pattern, the Model takes care of storing data and managing application logic, the View presents data from the Model to users, and the Controller acts as a middleman between the Model and View.

- MVT, or Model-View-Template, is another software design pattern. Similar to MVC, the Model is responsible for data and application logic, the View displays data from the Model, and it connects this data to a Template. The Template defines how the user interface should look.

- MVVM, short for Model-View-ViewModel, is yet another architectural pattern. Here, the Model still stores data and logic, the View shows this data, and the ViewModel transforms data from the Model into a format that's easily presented and interacted with by the View.

MVC and MVT are quite alike, differing mainly in the terminology they use and how they implement their specific frameworks. On the other hand, MVVM emphasizes a clear separation between the View and ViewModel, focusing on data binding and two-way communication between them.

</details>

## Assignment 3

<details>
<summary>What is the difference between POST form and GET form in Django?</summary>

#### GET Form:
- Data is appended to the URL as query parameters.
- Data is visible in the URL.
- Used for read-only operations and sharing URLs.
- Limited data size due to URL length restrictions.

#### POST Form:
- Data is sent in the HTTP request body.
- Data is not visible in the URL.
- Used for operations that modify server-side data.
- No inherent data size limitations.

In Django, you can access form data via both POST and GET requests using the request object in your views. The choice depends on data sensitivity, the type of operation, and data size considerations.

</details>

<details>
<summary>What are the main differences between XML, JSON, and HTML in the context of data delivery?</summary>

#### Purpose:
- XML: Primarily for structured data exchange.
- JSON: Lightweight data exchange format.
- HTML: For creating web content.

#### Syntax:
- XML: Verbose with explicit tags.
- JSON: Simple key-value pairs and arrays.
- HTML: Uses specific tags for web content.

#### Data Types:
- XML: No built-in data types.
- JSON: Supports basic data types.
- HTML: Focuses on text, links, and media.

#### Readability:
- XML: Less human-readable.
- JSON: Highly readable.
- HTML: Designed for human consumption.

#### Usage:
- XML: Configuration files, data exchange.
- JSON: Web APIs, data exchange.
- HTML: Web content presentation.

</details>

<details>
<summary>Why is JSON often used in data exchange between modern web applications?</summary>

JSON is popular in web applications because it's lightweight, human-readable, works with any programming language, and is secure. Its efficiency, native JavaScript support, and compatibility with cross-domain requests make it a preferred format for data exchange, especially in web APIs.

</details>

<details>
<summary>How I implemented the task above step-by-step</summary>

 - Before creating form input, I have to implement a skeleton as a  view structure.

 - First I create a folder named `templates` in the root directory. Inside that I create a file named `based.html`. Inside of it I insert:

    ```html
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta
                name="viewport"
                content="width=device-width, initial-scale=1.0"
            />
            {% block meta %}
            {% endblock meta %}
        </head>

        <body>
            {% block content %}
            {% endblock content %}
        </body>
    </html>
    ```
- In the `settings.py` on the `assignment2` folder, I enable the detection of `base.html` as a template file

- In `templates` inside `main` folder, I change `main.html` with:
    ```html
    {% extends 'base.html' %}

    {% block content %}
        <h1>RAF Inventory</h1>

        <h5>Application name:</h5>
        <p>{{ application_name }}</p>

        <h5>Name:</h5>
        <p>{{ name }}</p>

        <h5>Class:</h5>
        <p>{{ class }}</p>
    {% endblock content %}
    ```

- Then, I start to create a Data input Form

- I create a new file inside `main` named `forms.py`, which is used to create a form structure that accepts data. Fill it with:
    ```py
    from django.forms import ModelForm
    from main.models import Item

    class ItemForm(ModelForm):
        class Meta:
            model = Item
            fields = ["name", "amount", "description", "category", "power"]
    ```
- In `views.py` in the `main` I add some of the code with import and a new function called `create_item`.
    ```py
    from django.http import HttpResponseRedirect
    from django.urls import reverse
    from main.forms import ItemForm
    from main.models import Item

    def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
    ```

- Then I change the `show_main` function inside this file with:
    ```py
    def show_main(request):
    items = Item.objects.all()

    context = {
        'application_name': 'RAF Inventory',
        'name': 'Rafif Firmansyah Aulia',
        'class': 'PBP KKI',
        'items': items,
    }

    return render(request, 'main.html', context)
    ```

- On `urls.py` inside `main` folder, I import previously created funtion, which is `create_item`.

- And I add new url path inside the `urlpatterns` to access the new importedd function.

- In `templates` directory inside `main`, I created new HTML file `create_item.html`. And fill it with this:
    ```py
    {% extends 'base.html' %} 

    {% block content %}
    <h1>Add New Item</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Add Item"/>
                </td>
            </tr>
        </table>
    </form>

    {% endblock %}
    ```

- In `main.html` I modified new code between `{% block content %}` and `{% endblock content %}`.
    ```html
    <table>
        <tr>
            <th>Name</th>
            <th>Amount</th>
            <th>Description</th>
            <th>Category</th>
            <th>Power</th>
            <th>Date Added</th>
        </tr>

        {% comment %} Below is how to show the item data {% endcomment %}

        {% for item in items %}
            <tr>
                <td>{{item.name}}</td>
                <td>{{item.price}}</td>
                <td>{{item.description}}</td>
                <td>{{item.category}}</td>
                <td>{{item.power}}</td>
                <td>{{item.date_added}}</td>
            </tr>
        {% endfor %}
    </table>

    <br />

    <a href="{% url 'main:create_item' %}">
        <button>
            Add New Item
        </button>
    </a>

    {% endblock content %}
    ```

- After that I run migrate because I tried running with `py manage.py runserver` and it didn't work. So i run `py manage.py makemigrations` and after that `py manage.py makemigrations`.

- in `views.py` in the `main` folder I add import `HttpResponse` and `serializers` and add a new function called `show_xml` . This what I add:
    ```py
    from django.http import HttpResponse
    from django.core import serializers

    def show_xml(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```
- In `urls.py` inside `main`. I import the created function `show_xml`.
- Then route the urls path in the `urlpatterns`:
    ```py
    path('xml/', show_xml, name='show_xml'),
    ```
    add this code.

- Do the same thing with the **JSON**.

- I want to get the xml and json by ID. Firstly, I created new function `show_xml_by_id` with this code:
    ```py
    def show_xml_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```
    After that I import the code to `urls.py` and add path to `urlpatterns`.

- To implement the ** JSON by ID** I just do the same thing like the xml.

</details>

<details>
<summary>Access the five URLs in point 2 using Postman, take screenshots of the results in Postman, and add them to README.md.</summary>

- **HTML**
![Alt text](image-2.png)

- **XML**
![Alt text](image-3.png)

- **JSON**
![Alt text](image-4.png)

- **XML by ID**
![Alt text](image-5.png)

- **JSON by ID**
![Alt text](image-6.png)

</details>

## Assignment 4

<details>
<summary>What is `UserCreationForm`` in Django? Explain its advantages and disadvantages.</summary>

In Django, UserCreationForm is a built-in form class for creating user registration forms. It simplifies the process by providing fields for common registration data like username and password, along with validation. This form integrates seamlessly with Django's authentication system, making it easy to manage user accounts in Django applications. Developers can also customize it to fit their project's specific needs.

### Advantages of using the UserCreationForm, in Django:

1. `Ease of Use`: The UserCreationForm simplifies the process of creating user registration forms making it user friendly and straightforward.

2. `Integration`: It seamlessly integrates with Djangos authentication system ensuring an cohesive experience for users.

3. `Validation`: The UserCreationForm provides built in validation for fields ensuring data integrity and accuracy.

4. `Customization`: You have the flexibility to extend and customize the UserCreationForm according to your projects needs allowing for adaptability.

5. `Security`: The UserCreationForm takes care of security aspects such as password hashing ensuring that user credentials are stored securely.

6. `Consistency`: By utilizing the UserCreationForm you can maintain an user registration experience throughout your project promoting familiarity and ease of use.

### Disadvantages of using the UserCreationForm:

1. `Limited Fields`: The predefined set of fields offered by the UserCreationForm may not cover all requirements to your project. Additional customization might be necessary in cases.

2. `Flexibility`: Depending on your projects needs there could be instances where the default functionality provided by the UserCreationForm might not fully meet your requirements or necessitate additional modifications.

3. `Localization Effort`: If you require support in your application integrating it with the UserCreationForm might require some effort to ensure proper localization.

</details>

<details>
<summary>What is the difference between authentication and authorization in Django application? Why are both important?</summary>

Authentication verifies a user's identity, while authorization determines what actions or resources they can access. Both are vital for the security and functionality of a Django application, ensuring that users have the right level of access and protection of sensitive data.

</details>

<details>
<summary>What are `cookies` in website? How does Django use `cookies` to manage user session data?</summary>

Cookies are small data files sent from a web server to a user's browser and stored on their device. They're used for various purposes, including session management, remembering user preferences, tracking user behavior, etc. Django uses cookies for session management. When a user visits a Django site, it generates a unique session ID stored in a cookie. Django then stores user-specific data associated with that ID on the server. This allows Django to remember user sessions, authentication, and preferences across requests, making it easier to build interactive web applications.

</details>

<details>
<summary>Are `cookies` secure to use? Is there potential risk to be aware of?</summary>

Cookies themselves are not inherently secure. Their security depends on how they are used and the precautions taken by developers. Security risks include data exposure, session hijacking, and potential for cross-site scripting (XSS) or cross-site request forgery (CSRF) attacks. Properly configured and managed cookies can be secure, but developers must implement best practices to mitigate risks.

</details>

<details>
<summary>Explain how you implemented the checklist above step-by-step</summary>
- Firstly, I created Registration form

- Start with creating function `register` inside views.py with parameter `request`.

- Add imports for `redirects`, `UserCreationForm`, and `messages`.

- The funtion for `register` are:
    ```py
    def register(request):
        form = UserCreationForm()

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')
        context = {'form':form}
        return render(request, 'register.html', context)
    ```

- followed by creating `register.hmtl` inside `main/templates` directory, and create the HTML file for the Register new account page.

- Then we add path to the `urlpatterns`.

- After that I moved on to creating the login function. Start by importinng `authenticate` and `login` into the `views.py`.

- Then I add the `login_user` function to authenticate user.
    ```py
    def login_user(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:show_main')
            else:
                messages.info(request, 'Sorry, incorrect username or password. Please try again.')
        context = {}
        return render(request, 'login.html', context)
    ```

- Next I create new HTML file for login in the same directory as the `register.hmtl`.

- After that I create path for login_user in the `urlpatterns`

- Lastly, I have to create the Logout function into the website. The steps are the same like both of the function. In the function I add:
    ```py
    def logout_user(request):
        logout(request)
        return redirect('main:login')
    ```

- Then I add button for logout in the `main.html` and create path in the `urls.py`

- To restricts access for the User has to login/register into the main page, I import `login_required` into the `views.py`.

- The important part, I add the `@login_required(login_url='/login')` above the `show_main` function to restricts access to the main page only to the authenticated users.

- To use data from cookies I have to add last login feature.

- First, start with importing `datetime` into the `views.py`, then inside the `login_user` funtion modify the code inside `if user is not None` like this:
    ```py
    if user is not None:
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main")) 
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    ```

- In the `show_main` funtion, I modified the `context = {}` inside `show_main` with this:

    ```py
    context = {
        'application_name': 'RAF Inventory',
        'name': request.user.username,
        'class': 'PBP KKI',
        'items': items,
        'data_count': data_count,
        'last_login': request.COOKIES['last_login']
        if 'last_login' in request.COOKIES.keys()
        else "",
    }
    ```
    the `if 'last_login' in request.COOKIES.keys()` i get it from pak Daya in the class session, it is to avoid the bug inside my code, because before adding this code I manage to encounter error while opening the localhost with the `last_login` error, and have to delete all the cookies in the browser.

- Then modify the `logout_user` with:
    ```py
    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
    ```

- To connect the Item model to User model, I have to import `User` into the `models.py`.

- On the class Item i add this following code:
    ```py
    class Item(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
   ```

- Then in the `create_item` on `views.py` modify the code as this:
    ```py
    def create_item(request):
        form = ItemForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return HttpResponseRedirect(reverse('main:show_main'))
    ```

- Then modify the `show_main` function with:
    ```py
    def show_main(request):
        items = Item.objects.filter(user=request.user)

        context = {
            'name': request.user.username,
    ```

- Then run `migrations` after changing the models.

</details>

## Assignment 5

<details>
<summary>Explain the purpose of some CSS element selector and when to use it.</summary>

1. `Universal Selector (*)`: Targets all elements on a page, sparingly used for common styles or resets.

2. `Type or Tag Selector`: Targets elements by their HTML tag name `(e.g., <h1>, <p>)`, used for styling all instances of a specific tag.

3. `Class Selector (.classname)`: Targets elements with a specific class attribute value, versatile for styling multiple elements with the same class.

4. `ID Selector (#idname)`: Targets a unique element with a specific id attribute value, suitable for styling a single, unique element.

5. `Attribute Selector ([attribute=value])`: Targets elements with a specific attribute and value, used for styling elements with a particular attribute value.

6. `Pseudo-class Selector (:pseudo-class)`: Targets elements in specific states or conditions, used for adding interactivity or styling based on user actions or element states.

</details>

<details>
<summary>Explain some of the HTML5 tags that you know.</summary>

1. `<nav>`: Defines a navigation menu or links to other pages. It's used for grouping navigation-related content, such as menus and links.

2. `<section>`: Represents a thematic grouping of content, such as chapters, articles, or subsections. It helps in organizing content and providing structural clarity.

3. `<details>` and `<summary>`: `<details>` is used to create a disclosure widget for additional information, and `<summary>` provides a label or summary for the details that can be expanded or collapsed.

</details>

<details>
<summary>What are the differences between margin and padding?</summary>

- Margin affects the space outside the element, influencing its position relative to other elements on the page.

- Padding affects the space inside the element, influencing the space between the content and the element's border.

</details>

<details>
<summary>What are the differences between the CSS framework Tailwind and Bootstrap? When should we use Bootstrap rather than Tailwind, and vice versa?</summary>

**Tailwind CSS and Bootstrap differ in their:**

1. Approach:

    - Tailwind: Utility-first, fine-grained control.
    - Bootstrap: Component-based, pre-designed components.

2. Customization:

    - Tailwind: Highly customizable.
    - Bootstrap: Limited customization.

3. File Size:

    - Tailwind: Smaller due to selective CSS.
    - Bootstrap: Larger, includes all component styles.

3. Learning Curve:

    - Tailwind: Steeper.
    - Bootstrap: Easier, beginner-friendly.

**Tailwind CSS:**
- Need fine-grained styling control.
- Prioritize customization.
- Comfortable with utility-first approach.

**Bootstrap:**
- Rapid prototyping.
- Prefer ready-made components.
- Simplicity and ease of use are key.

</details>

<details>
<summary>Explain how you implemented the checklist above step-by-step (not just following the tutorial).</summary>

- First I Add Bootstrap to the Django project by adding `<meta name="viewport">` inside `templates/base.html` file.

- Then I add Bootstrap and JavaScript by inserting both links into `templates/base.html`:
    ```html
    <head>
        {% block meta %}
            ...
        {% endblock meta %}
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
    </head>
    ```
- Then I start by adding navbar into the application, I create it's own `navbar.html` in `main/templates` then I add this code:
    ```html
    {% block content %}
    <style>
        ul {
            list-style-type: none;
            margin: 0;
            padding: 0;
            overflow: hidden;
            background-color: #0000ff;
        }
        li {
            float: left;
        }
        li a {
            display: block;
            color: white;
            text-align: center;
            padding: 14px 16px;
            text-decoration: none;
        }
        li a:hover {
            background-color: #27a1ff;
        }
        .navbar-text {
            color: white;
            padding: 14px 16px;
        }
    </style>

    <ul>
        <li><a href="/">Home</a></li>
        <li class="navbar-text">Welcome to RAF Inventory</li>
        <li style="float:right"><a class="active" href="{% url 'main:logout' %}">Logout</a></li>
    </ul>
    {% endblock content %}
    ```

- Then if I want to show navbar in certain pages I just use `{% include 'navbar.html' %}` at the very top of the html file after block content.

- Then I create Edit Function into the application. Inside `views.py` add this following code:
    ```py
    def edit_item(request, id):
        item = Item.objects.get(pk = id)
        form = ItemForm(request.POST or None, instance=item)
        if form.is_valid() and request.method == "POST":
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))
        context = {'form': form}
        return render(request, "edit_product.html", context)
    ```

- Later on the html file of `edit_item.html` we modify the layout using bootstrap.

- Add import `edit_item` into `urls.py` and add path into `urlpatterns`

- After that, add buttons into `main.html` for `edit_item` pages.

### Modifying templates using bootstrap

- for `main.html`:

    ```html
    {% extends 'base.html' %}

    {% block content %}
    {% include 'navbar.html' %}

    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@700&display=swap');
        html * {
            font-family: 'Poppins', sans-serif;
        }
        table {
        border-collapse: collapse;
        width: 80%;
        margin: 20px auto; 
        }

        td, th {
        border: 2px solid black;
        padding: 10px;
        text-align: center;
        background-color: rgb(206, 221, 255);
        }

        th {
        background-color: rgb(75, 132, 255);
        }

        body {
        background-color: rgb(255, 255, 255);
        margin: 0;
        padding: 0;
        text-align: center;
        }

        h1, h5, p {
        padding-left: 20px;
        margin: 10px 0; /* Berikan margin atas dan bawah yang lebih besar pada elemen-elemen ini */
        text-align: left;
        }
        </style>
        <h1 style="color: rgb(0, 81, 255);">RAF Inventory</h1> <hr>

        <h5>Account:</h5>
        <p>{{ name }}</p>

        <h5 style="text-align: center;">Inventory</h5>

    <table>
        <tr style="border: 2px solid black;">
            <th style="border: none;">Name</th>
            <th style="border: none;">Amount</th>
            <th style="border: none;">Description</th>
            <th style="border: none;">Category</th>
            <th style="border: none;">Power</th>
            <th style="border: none;"></th>
            <th style="border: none;"></th>
        </tr>

        {% comment %} Below is how to show the item data {% endcomment %}

        {% for item in items %}
            <tr>
                <td>{{item.name}}</td>
                <td>
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <a style="text-decoration: none; color: black;" href="decrement/{{item.id}}">-</a>
                                {{ item.amount }}
                        <a style="text-decoration: none; color: black;" href="increment/{{item.id}}">+</a>
                    </div>
                    </td>
                <td>{{item.description}}</td>
                <td>{{item.category}}</td>
                <td>{{item.power}}</td>
                <td>
                    <a href="delete/{{item.id}}">
                        <button style="background-color: rgb(126, 167, 255);">
                            Remove
                        </button>
                    </a>
                </td>
                <td>
                    <a href="{% url 'main:edit' item.pk %}">
                        <button style="background-color: rgb(126, 167, 255);">
                            Edit
                        </button>
                    </a>
                </td>
            </tr>
        {% endfor %}
    </table>


    <br />
    <p style="text-align: center;">You have inserted {{ data_count }} items in this app</p>

    <a href="{% url 'main:create_item' %}">
        <button style="background-color: rgb(126, 167, 255);">
            Create Item
        </button>
    </a>

    <p>Last login session: {{ last_login }}</p>
    {% endblock content %}
    ```

- for `login.html`:

    ```html
    {% extends 'base.html' %}

    {% block meta %}
        <title>Login</title>
    {% endblock meta %}

    {% block content %}
    <style>
    .gradient-custom-2 {
        /* fallback for old browsers */
        background: #5f5dff;
        
        /* Chrome 10-25, Safari 5.1-6 */
        background: -webkit-linear-gradient(to right, #0000ff, #ff0000);
        
        /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
        background: linear-gradient(to right, #0000ff, #ff0000);
        }
        
        @media (min-width: 768px) {
        .gradient-form {
        height: 100vh !important;
        }
        }
        @media (min-width: 769px) {
        .gradient-custom-2 {
        border-top-right-radius: .3rem;
        border-bottom-right-radius: .3rem;
        }
        }
    </style>

    <section class="h-100 gradient-form" style="background-color: #eee;">
        <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col-xl-10">
            <div class="card rounded-3 text-black">
                <div class="row g-0">
                <div class="col-lg-6">
                    <div class="card-body p-md-5 mx-md-4">
    
                    <div class="text-center">
                        <h4 class="mt-1 mb-5 pb-1">RAF Item Storage</h4>
                    </div>
    
                    <form method="POST" action="">
                        {% csrf_token %}
    
                        <div class="form-outline mb-4">
                            <input type="text" name="username" placeholder="Username" class="form-control">
                        <label class="form-label" for="form2Example11">Username</label>
                        </div>
    
                        <div class="form-outline mb-4">
                            <input type="password" name="password" placeholder="Password" class="form-control"></td>
                        <label class="form-label" for="form2Example22">Password</label>
                        </div>
    
                        <div class="text-center pt-1 mb-5 pb-1">
                        <button class="btn btn-primary btn-block fa-lg gradient-custom-2 mb-3" type="submit" value="Login">Log
                            in</button>
                        </div>
    
                        <div class="d-flex align-items-center justify-content-center pb-4">
                        <p class="mb-0 me-2">Don't have an account?</p>
                        <a class="btn btn-outline-danger" href="{% url 'main:register' %}">Register</a>
                        </div>
    
                    </form>
    
                    </div>
                </div>
                <div class="col-lg-6 d-flex align-items-center gradient-custom-2">
                    <div class="text-white px-3 py-4 p-md-5 mx-md-4">
                    <h4 class="mb-3">Welcome to RAF Item Storage</h4>
                    </div>
                </div>
                </div>
            </div>
            </div>
        </div>
        </div>
    </section>

    {% endblock content %}
    ```

- for `register.html`:

    ```html
    {% extends 'base.html' %}

    {% block meta %}
        <title>Register</title>
    {% endblock meta %}

    {% block content %}  
    <style>
    .gradient-custom-2 {
        /* fallback for old browsers */
        background: #5f5dff;
        
        /* Chrome 10-25, Safari 5.1-6 */
        background: -webkit-linear-gradient(to right, #0000ff, #ff0000);
        
        /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
        background: linear-gradient(to right, #0000ff, #ff0000);
        }
        
        @media (min-width: 768px) {
        .gradient-form {
        height: 100vh !important;
        }
        }
        @media (min-width: 769px) {
        .gradient-custom-2 {
        border-top-right-radius: .3rem;
        border-bottom-right-radius: .3rem;
        }
        }
    </style>

    <section class="h-100 gradient-form" style="background-color: #eee;">
        <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col-xl-10">
            <div class="card rounded-3 text-black">
                <div class="row g-0">
                <div class="col-lg-6">
                    <div class="card-body p-md-5 mx-md-4">
    
                    <div class="text-center">
                        <h4 class="mt-1 mb-5 pb-1">Register Account</h4>
                    </div>
    
                    <form method="POST" action="">
                        {% csrf_token %}
    
                        <div class="form-outline mb-4">
                            <input type="text" name="username" maxlength="150" class="form-control" autocapitalize="none" autocomplete="username" autofocus required id="id_username">
                        <label class="form-label" for="id_username">Username</label>
                        </div>
    
                        <div class="form-outline mb-4">
                            <input type="password" name="password1" class="form-control" autocomplete="new-password" required id="id_password1" aria-autocomplete="list"></td>
                        <label class="form-label" for="id_password1">Password</label>
                        </div>

                        <div class="form-outline mb-4">
                            <input type="password" name="password2" class="form-control" autocomplete="new-password" required id="id_password2"></td>
                        <label class="form-label" for="id_password2">Password Confirmation</label>
                        </div>
    
    
                        <div class="text-center pt-1 mb-5 pb-1">
                        <button class="btn btn-primary btn-block fa-lg gradient-custom-2 mb-3" type="submit" value="Register">Register</button>
                        </div>
    
    
                    </form>
    
                    </div>
                </div>
                <div class="col-lg-6 d-flex align-items-center gradient-custom-2">
                    <div class="text-white px-3 py-4 p-md-5 mx-md-4">
                    <h4 class="mb-3">RAF Inventory</h4>
                    </div>
                </div>
                </div>
            </div>
            </div>
        </div>
        </div>
    </section>

    {% endblock content %}
    ```

- for `create_item`:

    ```html
    {% extends 'base.html' %} 

    {% block content %}
    {% include 'navbar.html' %}

    <style>
    .gradient-custom {
        /* fallback for old browsers */
        background: #14bdff;
        
        /* Chrome 10-25, Safari 5.1-6 */
        background: -webkit-linear-gradient(to right, rgb(255, 0, 0), rgb(0, 0, 255));
        
        /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
        background: linear-gradient(to right, rgb(255, 0, 0), rgb(0, 0, 255))
        }
    </style>

    <section class="vh-120 gradient-custom">
        <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col-12 col-md-8 col-lg-6 col-xl-5">
            <div class="card bg-dark text-white" style="border-radius: 1rem;">
                <div class="card-body p-5 text-center">
                <div class="mb-md-5 mt-md-4 pb-5">
                    
                    <h2 class="fw-bold mb-2">Create Item</h2>
                    <p class="text-white-50 mb-5">Please enter specific item that you want to store!</p>
                    
                    <form method="POST" action="#">
                        {% csrf_token %}
                            <div class="form-outline form-white mb-4">
                                <input type="text" name="name" class="form-control form-control-lg" maxlength="255" required id="id_name"/>
                                <label class="form-label" for="id_name">Name</label>
                                </div>
            
                            <div class="form-outline form-white mb-4">
                                <input type="number" name="amount" id="id_amount" class="form-control form-control-lg" required/>
                                <label class="form-label" for="id_amount">Amount</label>
                                </div>
                            
                            <div class="form-outline form-white mb-4">
                                <textarea name="description" cols="20" rows="10" required="" id="id_description" data-gramm="false" wt-ignore-input="true" class="form-control form-control-lg"></textarea>
                                <label class="form-label" for="id_description">Description</label>
                                </div>
                            
                            <div class="form-outline form-white mb-4">
                                <textarea name="category" cols="40" rows="10" required="" id="id_category" data-gramm="false" wt-ignore-input="true" class="form-control form-control-lg"></textarea>
                                <label class="form-label" for="id_category">Category</label>
                                </div>
                            
                            <div class="form-outline form-white mb-4">
                                <input type="number" name="power" id="id_power" class="form-control form-control-lg" required/>
                                <label class="form-label" for="id_power">Power</label>
                                </div>
            
                            <input class="btn btn-outline-light btn-lg px-5" type="submit" value="Add Item"/>
                        </form>
                </div>
                </div>
            </div>
            </div>
        </div>
        </div>
    </section>
    {% endblock %}
    ```

- for `edit_item,htmnl`:

    ```html
    {% extends 'base.html' %}

    {% load static %}

    {% block content %}

    {% include 'navbar.html' %}

    <style>
    .gradient-custom {
        /* fallback for old browsers */
        background: #14bdff;
        
        /* Chrome 10-25, Safari 5.1-6 */
        background: -webkit-linear-gradient(to right, rgb(255, 0, 0), rgb(0, 0, 255));
        
        /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
        background: linear-gradient(to right, rgb(255, 0, 0), rgb(0, 0, 255))
        }
    </style>

    <section class="vh-120 gradient-custom">
        <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col-12 col-md-8 col-lg-6 col-xl-5">
            <div class="card bg-dark text-white" style="border-radius: 1rem;">
                <div class="card-body p-5 text-center">
                <div class="mb-md-5 mt-md-4 pb-5">
                    
                    <h2 class="fw-bold mb-2">Edit Item</h2>
                    <p class="text-white-50 mb-5">You can freely edit item in this inventory!</p>
                    
                    <form method="POST" action="#">
                        {% csrf_token %}
                            <div class="form-outline form-white mb-4">
                                <input type="text" name="name" class="form-control form-control-lg" maxlength="255" required id="id_name" value="{{form.instance.name}}"/>
                                <label class="form-label" for="id_name">Name</label>
                                </div>
            
                            <div class="form-outline form-white mb-4">
                                <input type="number" name="amount" id="id_amount" class="form-control form-control-lg" required value="{{form.instance.amount}}"/>
                                <label class="form-label" for="id_amount">Amount</label>
                                </div>
                            
                            <div class="form-outline form-white mb-4">
                                <textarea name="description" cols="20" rows="10" required="" id="id_description" data-gramm="false" wt-ignore-input="true" class="form-control form-control-lg">{{form.instance.description}}</textarea>
                                <label class="form-label" for="id_description">Description</label>
                                </div>
                            
                            <div class="form-outline form-white mb-4">
                                <textarea name="category" cols="40" rows="10" required="" id="id_category" data-gramm="false" wt-ignore-input="true" class="form-control form-control-lg">{{form.instance.category}}</textarea>
                                <label class="form-label" for="id_category">Category</label>
                                </div>
                            
                            <div class="form-outline form-white mb-4">
                                <input type="number" name="power" id="id_power" class="form-control form-control-lg" required value="{{form.instance.power}}"/>
                                <label class="form-label" for="id_power">Power</label>
                                </div>
            
                            <input class="btn btn-outline-light btn-lg px-5" type="submit" value="Edit Item"/>
                        </form>
                </div>
                </div>
            </div>
            </div>
        </div>
        </div>
    </section>
    {% endblock %}
    ```
</details>

## Assignment 6

<details>
<summary>Explain the difference between asynchronous programming and synchronous programming.</summary>


- Synchronous programming executes tasks in a predictable, sequential order, one after the other, potentially causing delays and blocking the program. Asynchronous programming, on the other hand, enables tasks to run concurrently and independently, using mechanisms like callbacks or promises to coordinate their execution. It is ideal for non-blocking, parallel tasks, making it suitable for operations such as I/O and network requests, ensuring program responsiveness.
</details>

<details>
<summary>In the implementation of JavaScript and AJAX, there is an implemented paradigm called the event-driven programming paradigm. Explain what this paradigm means and give one example of its implementation in this assignment.</summary>

- Event-driven programming is a paradigm where a program's flow is determined by events, such as user interactions. In JavaScript and AJAX, it's used extensively for creating interactive web applications. For example, when a user clicks a button on a webpage, an event handler function is executed in response to that specific event, making the application dynamic and responsive.
</details>

<details>
<summary>Explain the implementation of asynchronous programming in AJAX.
</summary>

- In AJAX, asynchronous programming allows web applications to send and receive data without blocking the user interface. It's implemented by making asynchronous requests using techniques like the fetch API. These requests run in the background, and when a response is ready, callbacks or promises handle the data. This ensures that the application remains responsive, and error handling is also a part of the process.
</details>

<details>
<summary>In this semester, the implementation of AJAX is done using the Fetch API rather than the jQuery library. Compare the two technologies and write down your opinion which technology is better to use.
</summary>

- In my opinion, for modern web development, the Fetch API is typically the better choice due to its lightweight nature, native browser support, and the use of promises. This approach promotes cleaner, more modern coding practices. However, if I need to support older browsers or require the extensive community and plugin support that jQuery offers, it can still be a relevant choice, especially for legacy systems or projects with a heavy reliance on jQuery-dependent plugins. My decision should be based on my project's specific requirements and my team's expertise.
</details>

<details>
<summary>Explain how you implemented the checklist above step-by-step (not just following the tutorial).
</summary>

- First, create new `get_product_json` function in `views.py`.
    ```py
    def get_product_json(request):
        product_item = Product.objects.all()
        return HttpResponse(serializers.serialize('json', product_item))
    ```

- After that, create a new `add_product_ajax`, before that we import `csrf_exempt` in `views.py`, then add this code:
    ```py
    @csrf_exempt
    def add_product_ajax(request):
        if request.method == 'POST':
            name = request.POST.get("name")
            price = request.POST.get("price")
            description = request.POST.get("description")
            user = request.user

            new_product = Product(name=name, price=price, description=description, user=user)
            new_product.save()

            return HttpResponse(b"CREATED", status=201)

        return HttpResponseNotFound()
    ```

- then add both path in `urls.py` into `urlpatterns` list.

- then replace this table in the `main.html`:
    ```html
    <table id="product_table"></table>
    ```

- add `<script>` tag block and add this for every feature:
    ```html
    <script>
        async function getProducts() {
            return fetch("{% url 'main:get_product_json' %}").then((res) => res.json())
        }

        async function refreshProducts() {
            const productTable = document.getElementById("product_table");
            productTable.innerHTML = "";

            const products = await getProducts();
            let htmlString = "<div class='row'>";  // Start a new row

            products.forEach((item, index) => {
                if (index % 3 === 0 && index !== 0) {
                    htmlString += "</div><div class='row'>";  // Close previous row and start a new row for every 3 cards
                }

                htmlString += `
                    <div class="col-md-4">
                        <div class="card-item">
                            <div class="card mx-auto p-3" style="width: 18rem;">
                                <div class="card-body">
                                    <h2 class="card-title">${item.fields.name}</h2>
                                    <p class="card-text">Amount: ${item.fields.amount}</p>
                                    <p class="card-text">${item.fields.description}</p>
                                    <p class="card-text">Category: ${item.fields.category}</p>
                                    <p class="card-text">Price: ${item.fields.power}</p>
                                    <a style="justify-content: baseline;" href='edit/${item.pk}' class="btn btn-outline-warning" onclick="editItem(${item.pk})">Edit</a>
                                    <button style="justify-content: baseline;" class="btn btn-outline-danger" onclick="deleteProduct(${item.pk})">Delete</button>
                                </div>
                            </div>
                        </div>
                    </div>`;
            });

            htmlString += "</div>";  // Close the last row
            productTable.innerHTML = htmlString;
            document.getElementById("item_count").innerHTML = `Items in Inventory: ${ items.length }`
        }

        function addProduct() {
            fetch("{% url 'main:add_product_ajax' %}", {
                method: "POST",
                body: new FormData(document.querySelector('#form'))
            }).then(refreshProducts)

            document.getElementById("form").reset()
            return false
        }

        function editProduct(productId) {
            fetch(`{% url 'main:edit' 0 %}${productId}/`, {
            method: "POST",
            body: new FormData(document.querySelector('#form'))
        }).then(refreshProducts)

        document.getElementById("form").reset()
        return false
        }

        function deleteProduct(productId) {
            fetch(`{% url 'main:delete' 0 %}`.replace("0", productId), {
                method: "POST",
                body: new FormData(document.querySelector('#form'))
            }).then(refreshProducts)

            document.getElementById("form").reset()
            return false
        }

        refreshProducts()
        document.getElementById("button_add").onclick = addProduct
    </script>
    ```

- add a form modal to the code in `main.html`:
    ```html
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Product</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form id="form" onsubmit="return false;">
                        {% csrf_token %}
                        <div class="mb-3">
                            <label for="name" class="col-form-label">Name:</label>
                            <input type="text" class="form-control" id="name" name="name"></input>
                        </div>
                        <div class="mb-3">
                            <label for="price" class="col-form-label">Price:</label>
                            <input type="number" class="form-control" id="price" name="price"></input>
                        </div>
                        <div class="mb-3">
                            <label for="description" class="col-form-label">Description:</label>
                            <textarea class="form-control" id="description" name="description"></textarea>
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Product</button>
                </div>
            </div>
        </div>
    </div>

    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">Add Product by AJAX</button>
    ```

- then deploy the app to PaaS.
</details>