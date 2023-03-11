package main

import (
	"database/sql"
	"fmt"
	"github.com/joho/godotenv"
	_ "github.com/lib/pq"
	"log"
	"os"
)

const (
	host   = "localhost"
	port   = 5432
	user   = "postgres"
	dbname = "shoppingdb"
)

func goDotEnvVariable(key string) string {

	// load .env file
	err := godotenv.Load(".env")

	if err != nil {
		log.Fatalf("Error loading .env file")
	}

	return os.Getenv(key)
}

func getRecipeIngredients(db *sql.DB, recipe_id int) string {
	sqlStatement := `SELECT name FROM recipes where rec_id=$1`
	var name string
	row := db.QueryRow(sqlStatement, recipe_id)
	err := row.Scan(&name)
	if err != nil{
		panic(err)
	}
	return name
}

func main() {
	postgres_pw := goDotEnvVariable("POSTGRESQL_PW")

	psqlInfo := fmt.Sprintf("host=%s port=%d user=%s "+
		"password=%s dbname=%s sslmode=disable",
		host, port, user, postgres_pw, dbname)

	db, err := sql.Open("postgres", psqlInfo)
	if err != nil {
		panic(err)
	}
	defer db.Close()

	err = db.Ping()
	if err != nil {
		panic(err)
	}

	fmt.Println("Successfully connected!")
	name := getRecipeIngredients(db, 1)
	fmt.Println(name)
}
