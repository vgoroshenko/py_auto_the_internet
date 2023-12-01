## Getting Started Test the internet in chrome

[Example application for writing automated acceptance tests](http://the-internet.herokuapp.com)

[Link to Allure report after run tests](https://vgoroshenko.github.io/py_auto_the_internet/)


Install your dependencies:

    make pull
    python -m venv venv
    venv/Scripts/activate
    pip install -r requirements.txt

Start selenoid server:

    docker-compose up -d

Load the page you want to see in your browser:

    http://localhost:5000/

Start tests:
 
    pytest -v --tb=line --alluredir=reports -n 3


An example application that captures prominent and ugly functionality found on the web. Perfect for writing automated acceptance tests against.

Deployed and available at [http://the-internet.herokuapp.com](http://the-internet.herokuapp.com).