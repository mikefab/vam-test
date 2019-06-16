DB=${MONGODB_DBNAME:-mydb}
	# initializing '${DBENGINE}' database '${DBNAME}'
	if [ $(mongo db:27017  --eval "db.getMongo().getDBNames().indexOf('mydb')" --quiet) -lt 0 ]; then
	    echo "mydb does not exist. Creating now..."
      mongo db:27017 /${DB} --eval 'db.createCollection("forms", {} )'
	else
	    echo "mydb exists"
	fi
