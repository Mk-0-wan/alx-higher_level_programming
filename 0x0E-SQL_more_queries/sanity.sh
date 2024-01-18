#!/bin/bash

read -p 'Enter DB name: ' db_name

read -p 'Do you want to create a DB? y/n? ' response
if [[ $response == "y" || $response == "Y" ]]; then
    create_db="CREATE DATABASE IF NOT EXISTS "
    echo "$create_db $db_name;" | mysql -uroot -p
fi

response=""
read -p 'Do you want to import data from a website? y/n? ' response
if [[ $response == "y" || $response == "Y" ]]; then
    read -p 'Please Enter DB link: ' db_link
    curl "$db_link" -s | mysql -uroot -p "$db_name"
fi

read -p 'Enter table name: ' tb_name

show_db="SELECT * FROM "
echo "$show_db $tb_name;" | mysql -uroot -p "$db_name" | head

