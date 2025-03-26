import mysql.connector

def save_patient_data(name, age, gender, disease, symptoms):
    try:
        # Connect to MySQL database
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Bharath",
        database="medical"
        )
        cursor = db.cursor()

        # Check if table exists
        cursor.execute("SHOW TABLES LIKE 'patient_data';")
        result = cursor.fetchone()
        if not result:
            print("❌ Table 'patient_data' does not exist!")
            return

        # Insert data
        query = "INSERT INTO patient_data (name, age, gender, disease, symptoms) VALUES (%s, %s, %s, %s, %s)"
        values = (name, age, gender, disease, symptoms)

        cursor.execute(query, values)
        db.commit()

        print("✅ Data inserted successfully!")

    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")

    finally:
        cursor.close()
        db.close()

# Test
save_patient_data("Alice", 28, "Female", "Cold", "Sneezing, Runny Nose")