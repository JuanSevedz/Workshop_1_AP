# Vehicle Catalog Management Web Service

This web service provides endpoints to manage a catalog of vehicles and engines. It allows users to view the catalog, add new vehicles, add new engines, and filter vehicles by type.

## Endpoints

### 1. Show Catalog

- **HTTP Method:** GET
- **URL:** `/catalog`
- **Request:** None (GET request)
- **Expected Response:**
  - Content-Type: application/json
  - Format:
    ```json
    {
        "vehicles": [
            {
                // Vehicle data
            },
            // More vehicles...
        ]
    }
    ```

### 2. Add Vehicle

- **HTTP Method:** POST
- **URL:** `/add_vehicle`
- **Request:**
  - Content-Type: application/json
  - Format:
    ```json
    {
        "vehicle_type": "Car",
        "chassis": "A",
        "model": "Hatchback",
        "year": 2023,
        "gas_consumption": 320.0,
        "engine": {
            "engine_type": "Hybrid",
            "potency": 180,
            "weight": 250
        },
        "num_doors": 5
    }
    ```
- **Expected Response:**
  - Content-Type: application/json
  - Format:
    ```json
    {
        "message": "Vehicle added successfully"
    }
    ```

### 3. Add Engine

- **HTTP Method:** POST
- **URL:** `/add_engine`
- **Request:**
  - Content-Type: application/json
  - Format:
    ```json
    {
        "engine_type": "Electric",
        "potency": 150,
        "weight": 200
    }
    ```
- **Expected Response:**
  - Content-Type: application/json
  - Format:
    ```json
    {
        "message": "Engine added successfully"
    }
    ```

### 4. Show Specific Type of Vehicle

- **HTTP Method:** GET
- **URL:** `/specific_type?type=Car` (Replace `Car` with the desired vehicle type)
- **Request:** None (GET request)
- **Expected Response:**
  - Content-Type: application/json
  - Format:
    ```json
    {
        "vehicles": [
            {
                // Vehicle data
            },
            // More vehicles...
        ]
    }
    ```

