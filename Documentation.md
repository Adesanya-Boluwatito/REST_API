## API Endpoints

- **POST /api/person**
  - Create a new person.
  - Request Body: JSON
    ```json
    {
      "name": "John Doe",
      "age": 30
    }
    ```
- **GET /api/person/{name}**
  - Retrieve details of a person by name.
- **PUT /api/person/{name}**
  - Update details of an existing person by name.
  - Request Body: JSON
    ```json
    {
      "name": "Updated Name",
      "age": 40
    }
    ```
- **DELETE /api/person/{name}**
  - Delete a person by name.


