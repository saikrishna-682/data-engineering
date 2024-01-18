from flask import Flask, render_template, request, jsonify
import psycopg2

db_params = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="password",
    database="postgres",
    port=5432
)

db_cursor = db_params.cursor()

sql_query = "INSERT INTO employee (empid, empname, empsal) VALUES (%s,%s,%s)"
get_record_query = "SELECT * FROM employee"
delete_record_query="DELETE FROM employee WHERE empid=%s"
app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/save_record', methods=['POST'])
def saveRecord():
    data = request.form
    empid = data.get('empid')
    empname = data.get('empname')
    empsal = data.get('empsal')

    employee_record = {
        'empid': empid,
        'empname': empname,
        'empsal': empsal
    }

    tuple_employee_record = tuple(employee_record)



    db_cursor.execute(sql_query, (empid, empname, empsal))

    db_params.commit()

    return f'insert successful: {employee_record}'


@app.route('/get_record', methods=['GET'])
def getRecord():
    db_cursor.execute(get_record_query)
    data = db_cursor.fetchall()

    records = []
    for row in data:
        record_dict={
            'empid':row[0],
            'empname':row[1],
            'empsal':row[2]
        }
        records.append(record_dict)
    return jsonify(records)


@app.route('/delete_record/<int:empid>', methods=['DELETE'])
def delete_record(empid):
    db_cursor.execute(delete_record_query, (empid,))
    db_params.commit()

    return f'record delete successfully: {empid}'


if __name__ == "__main__":
    app.run(debug=True, port=5000)