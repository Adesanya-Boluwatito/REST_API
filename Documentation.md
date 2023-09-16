## API Endpoints

- **POST /api**
  - Create a new person.
  - Request Body: JSON
    ```json
    {
      "name": "John Doe",
      "age": 30
      "user_id:****
    }
    ```
- **GET /api/{name}**
  - Retrieve details of a person by name.
    
- **PUT /api/{name}**
  - Update details of an existing person by name.
  - Request Body: JSON
    ```json
    {
      "name": "Updated Name",
      "age": 40
      "user_id: ****
    }
    ```
- **DELETE /api/{name}**
  - Delete a person by name.


