from studyapp import studyapp_obj, db

db.create_all()
studyapp_obj.run(debug=True)
