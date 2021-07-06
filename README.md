# PizzaNearMe
https://github.com/DracoY-code/PizzaNearMe

## APIs Used
* Places API
* Geocoding API

## Algorithm
The app algorithm displays pizza places as follows:
1. Loads the API key from .env file.
2. A place is to be inputted by the user.
3. The location data of the place is requested using Geocoding API.
4. If the location is not found, the program ends.
5. The pizza shops in the 3 km radius of the location are requested.
6. If the data is not found, the program ends.
7. The Places API data is stored in an array/list.
8. The data is then displayed in a `pandas.DataFrame`.

---

**Note**: The APIs require billing on the Google Cloud Console, so this is mostly theoretical.