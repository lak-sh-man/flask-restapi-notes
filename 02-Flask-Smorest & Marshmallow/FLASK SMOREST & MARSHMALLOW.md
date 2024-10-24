## ⚠️ FLASK SMOREST & MARSHMALLOW
- If we're using Flask-Smorest, it's highly recommended and almost essential to use Marshmallow because Flask-Smorest is designed to work closely with Marshmallow for serialization, deserialization, and validation of request and response data

    - ### SERIALIZATION and DESERIALIZATION
        - **Flask-Smorest** uses Marshmallow schemas to convert data (like database objects) into JSON for API responses (serialization) and to convert incoming JSON data into Python objects (deserialization)

    - ### VALIDATION
        - **Marshmallow** provides powerful data validation tools, ensuring that the incoming request data matches the required format before your Flask application processes it
        - Flask-Smorest depends on Marshmallow for request validation

    - ### AUTOMATIC API DOCUMENTAION
        - **Flask-Smorest** integrates with APISpec, and when you define routes with Marshmallow schemas, it automatically generates OpenAPI (**Swagger**) documentation for your endpoints
        - Without Marshmallow, you’d lose this feature