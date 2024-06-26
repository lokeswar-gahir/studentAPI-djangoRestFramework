
## Student API(DJangoRestFramework)

Check out here: https://studentapi-htla.onrender.com

Endpoints

- __/studnent/__ (['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
    - __GET :__ Returns all the student record.
    - __POST :__ Creates a new student record with required json body with required(__name, age, phone_no__) and optional(alternate_phone_no, email, address, image) parameters such as
    ```
    {
        "name": <string>,
        "age": <int>,
        "phone_no": <string>,
        "alternate_phone_no": <string>,
        "email": <string>,
        "address": <string>,
        "image": <imageFile>
    }
    ```

        Things to be keep in mind while sending a post request or you may face a sweet error:
        
        name: only alphabetic characters and space characters are allowed; special characters and digits are not.
        age : value for age should be ranging from '0' ro '110'
        phone_no : value for phone_no should contain exactly 10 characters
        email: email string should be well formated
    
    - __PUT: (/student/?id=<int>)__ Updates the record with specified ID. While updating the record all the required and optional parameters are mandatory to be passed in the request body as json format.
    - __PATCH: (/student/?id=<int>)__ Updates the record with specified ID. While updating the record at least one parameter to be passed in the request body as json format.
    - __DELETE: (/student/?id=<int>)__ Deletes the record with specified ID.