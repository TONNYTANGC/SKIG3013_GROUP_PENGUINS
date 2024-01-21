from flask import Flask, render_template, request, redirect, session, url_for, flash, jsonify
from mysql.connector import pooling

app = Flask(__name__)
app.secret_key = "flash_message"

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'tonnytang01',
    'database': 'mathgenius',
    'port': 3306,
    'charset': 'utf8mb4',
}

# Create a connection pool
connection_pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=10, **db_config)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        with connection_pool.get_connection() as connection:
            cursor = connection.cursor()

            # Example query execution
            cursor.execute("SELECT * FROM accounts")
            result = cursor.fetchall()

            # Close the cursor
            cursor.close()

        return render_template('index.html')
    except Exception as e:
        print(f"Error connecting to the database: {str(e)}")
        # Handle the error as needed
        return render_template('error.html', error_message=str(e))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email_or_username = request.form.get('email_or_username')
        password = request.form.get('password')

        if not email_or_username or not password:
            flash('Please provide both email/username and password.', 'error')
            return render_template('login.html')

        try:
            with connection_pool.get_connection() as connection:
                cursor = connection.cursor()

                query = "SELECT * FROM accounts WHERE (email = %s OR username = %s) AND password = %s"
                cursor.execute(query, (email_or_username, email_or_username, password))

                user = cursor.fetchone()

                if user:
                    session['user_id'] = user[0]
                    session['username'] = user[1]
                    session['email'] = user[2]
                    session['year'] = user[4]
                    session['phone'] = user[5]
                    session['bio'] = user[6]
                    session['address'] = user[7]
                    session['progress1'] = user[9]
                    session['progress2'] = user[10]
                    session['quiz1'] = user[11]
                    session['quiz2'] = user[12]
                    session['quiz3'] = user[13]
                    session['quiz4'] = user[14]
                    session['quiz5'] = user[15]
                    session['quiz6'] = user[16]
                    if user[8]=='admin':
                        return redirect(url_for('teacher_dashboard'))
                    else:
                        return redirect(url_for('profile'))
                else:
                    flash('Login failed. Please check your credentials.', 'error')

        except Exception as e:
            flash(f"Error during login: {str(e)}", 'error')

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        year = request.form['year']

        # Add form data validation and security measures here

        try:
            with connection_pool.get_connection() as connection:
                cursor = connection.cursor()
                # check if the username is taken
                cursor.execute("SELECT * FROM accounts WHERE username = %s", (username,))
                existing_user = cursor.fetchone()

                if existing_user:
                    flash('Username is already taken. Please choose a different username.', 'error')
                    return render_template('signup.html')

                # Assuming your table is named 'accounts'
                #cursor.execute("INSERT INTO accounts (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
                #connection.commit()

                # Assuming your table is named 'accounts'
                cursor.execute("INSERT INTO accounts (username, email, password,year) VALUES (%s, %s, %s,%s)", (username, email, password,year))
                connection.commit()

                # Optionally, you can set up a session for the newly registered user.
                session['user_id'] = cursor.lastrowid  # Store the user's ID in the session
                # Set session variables for the new user
                session['email'] = email
                session['username'] = username
                session['year']=year
                flash('Registration successful!', 'sinup_danger')
                return redirect(url_for('profile'))
        except Exception as e:
            flash('An error occurred while registering the user.', 'signup_danger')
            print(e)  # Print the error for debugging purposes

    # Handle validation errors and redirect back to the signup page if needed
    return render_template('signup.html')

@app.route('/forget_pass', methods=['GET','POST'])
def forget_pass():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password == confirm_password:
           with connection_pool.get_connection() as connection:
                cursor = connection.cursor()
                # Check if the username exists
                cursor.execute("SELECT * FROM accounts WHERE username = %s", (username,))
                existing_user = cursor.fetchone()

                if existing_user:
                    # Update the password
                    cursor.execute("UPDATE accounts SET password = %s WHERE username = %s", (password, username))
                    connection.commit()

                    # Flash a success message
                    flash('Password changed successfully', 'success')
                    return redirect(url_for('login'))

        # Flash an error message if passwords don't match or if the username is not found
        flash('Error changing password. Please check your username / password and try again.', 'error')

    return render_template('forget_pass.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        # Retrieve the updated values from the form
        phone = request.form.get('phone')
        bio = request.form.get('bio')
        address = request.form.get('address')

        # Update the user's profile in the database
        try:
            with connection_pool.get_connection() as connection:
                cursor = connection.cursor()
                update_query = "UPDATE accounts SET phone = %s, bio = %s, address = %s WHERE id = %s"
                cursor.execute(update_query, (phone, bio, address, session['user_id']))
                connection.commit()

                # Update the session variables
                session['phone'] = phone
                session['bio'] = bio
                session['address'] = address

               
                flash('Profile updated successfully!', 'success')
                return redirect(url_for('profile') + '#profil-content')

        except Exception as e:
            flash(f'Error updating profile: {str(e)}', 'error')
            return redirect(url_for('profile') + '#profil-content')

    return render_template('profile.html')

@app.route('/update-progress', methods=['POST'])
def update_progress():
    if request.method == 'POST':
        try:
            # Retrieve the lesson id and increment value from the request data
            lesson_id = request.json.get('lessonId')
            increment = float(request.json.get('increment'))

            # Determine the progress field dynamically based on lesson_id
            progress_field = f'progress{lesson_id}'

            # Update the progress in the database
            with connection_pool.get_connection() as connection:
                cursor = connection.cursor()

                # Retrieve the current progress
                cursor.execute(f"SELECT {progress_field} FROM accounts WHERE id = %s", (session['user_id'],))
                current_progress = cursor.fetchone()[0]

                # Calculate the new progress
                new_progress = current_progress + increment

                # Update the progress in the database
                update_query = f"UPDATE accounts SET {progress_field} = %s WHERE id = %s"
                cursor.execute(update_query, (new_progress, session['user_id']))
                connection.commit()

                # Update the session variable
                session[progress_field] = new_progress

                # You can customize the response if needed
                return jsonify({'message': 'Progress updated successfully'})
        except Exception as e:
            # Handle any errors
            return jsonify({'error': str(e)}), 500

@app.route('/update-grade', methods=['POST'])
def update_grade():
    if request.method == 'POST':
        try: 
            quiz_id = request.json.get('quizId')
            playerGrade = request.json.get('playerGrade')
            app.logger.debug('Received quiz_id: %s, playerGrade: %s', quiz_id, playerGrade)
            quiz_field = f'quiz{quiz_id}'

            with connection_pool.get_connection() as connection:
                cursor = connection.cursor()

                update_query = f"UPDATE accounts SET {quiz_field} = %s WHERE id = %s"
                cursor.execute(update_query, (playerGrade, session['user_id']))
                connection.commit()

                # Update the session variable
                session[quiz_field] = playerGrade

                # You can customize the response if needed
                return jsonify({'message': 'Grade updated successfully'})
        except Exception as e:
            # Handle any errors
            return jsonify({'error': str(e)}), 500

@app.route('/teacher_dashboard', methods=['GET', 'POST'])
def teacher_dashboard():
    if request.method == 'POST':
        # This block handles the profile update
        phone = request.form.get('phone')
        bio = request.form.get('bio')
        address = request.form.get('address')

        try:
            with connection_pool.get_connection() as connection:
                cursor = connection.cursor()
                update_query = "UPDATE accounts SET phone = %s, bio = %s, address = %s WHERE id = %s"
                cursor.execute(update_query, (phone, bio, address, session['user_id']))
                connection.commit()

                session['phone'] = phone
                session['bio'] = bio
                session['address'] = address

                flash('Profile updated successfully!', 'success')
                return redirect(url_for('teacher_profile'))
        except Exception as e:
            flash(f'Error updating profile: {str(e)}', 'error')
            return redirect(url_for('teacher_profile'))
    else:
        # This block handles displaying the list of users
        try:
            with connection_pool.get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT id, username, email, role, year, phone, bio, address, progress1, progress2, quiz1, quiz2, quiz3, quiz4, quiz5, quiz6 FROM accounts")
                # Assuming cursor.fetchall() returns a list of tuples
                user_tuples = cursor.fetchall()

                # Convert the list of tuples to a list of dictionaries
                users = [{'id': user[0], 'username': user[1], 'email': user[2], 'role': user[3], 'year':user[4], 'phone':user[5], 'bio':user[6],'address':user[7],'progress1':user[8],'progress2':user[9], 'quiz1':user[10], 'quiz2':user[11], 'quiz3':user[12],'quiz4':user[13],'quiz5':user[14],'quiz6':user[15]} for user in user_tuples]
                cursor.close()
            return render_template('teacher_dashboard.html', users=users)
        
        except Exception as e:
            print(f"Error retrieving user data: {str(e)}")
            return render_template('teacher_dashboard.html', exception=str(e))

@app.route('/teacher_profile', methods=['GET', 'POST'])
def teacher_profile():
    try:
        with connection_pool.get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id, username, email, role, year, phone, bio, address, progress1, progress2 FROM accounts")
            
            # Assuming cursor.fetchall() returns a list of tuples
            user_tuples = cursor.fetchall()

            # Convert the list of tuples to a list of dictionaries
            users = [{'id': user[0], 'username': user[1], 'email': user[2], 'role': user[3], 'year': user[4], 'phone': user[5], 'bio': user[6], 'address': user[7], 'progress1': user[8], 'progress2': user[9]} for user in user_tuples]

            cursor.close()

        return render_template('teacher_profile.html', users=users)

    except Exception as e:
        print(f"Error retrieving user data: {str(e)}")
        return render_template('teacher_dashboard.html', exception=str(e))


@app.route('/teacher_progress')
def teacher_progress():
    try:
        with connection_pool.get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id, username, email, role, year, phone, bio, address, progress1, progress2 FROM accounts")
            
            # Assuming cursor.fetchall() returns a list of tuples
            user_tuples = cursor.fetchall()

            # Convert the list of tuples to a list of dictionaries
            users = [{'id': user[0], 'username': user[1], 'email': user[2], 'role': user[3], 'year': user[4], 'phone': user[5], 'bio': user[6], 'address': user[7], 'progress1': user[8], 'progress2': user[9]} for user in user_tuples]

            cursor.close()

        return render_template('teacher_progress.html', users=users)

    except Exception as e:
        print(f"Error retrieving user data: {str(e)}")
        return render_template('teacher_progress.html', exception=str(e))
    

@app.route('/teacher_quiz', methods=['GET', 'POST'])
def teacher_quiz():
    try:
        if request.method == 'POST':
            # Check if the form submission is for updating a question
            if 'update_question' in request.form:
                quiz_id = int(request.form['update_question'])
                updated_question = {
                    'lesson': request.form.get('lesson'),
                    'subtopic': request.form.get('subtopic'),
                    'question': request.form.get('question'),
                    'srcQuestion': request.form.get('srcQuestion'),
                    'optionA': request.form.get('optionA'),
                    'optionB': request.form.get('optionB'),
                    'optionC': request.form.get('optionC'),
                    'optionD': request.form.get('optionD'),
                    'correctOption': request.form.get('correctOption')
                }

                update_quiz_in_database(quiz_id, updated_question)

                flash('Question successfully updated', 'success')
                return redirect(url_for('teacher_quiz'))

        # If it's a GET request or not a question update, display the quiz list
        quizs = get_quiz_list_from_database()
        return render_template('teacher_quiz.html', quizs=quizs)

    except Exception as e:
        print(f"Error retrieving/updating quiz data: {str(e)}")
        flash('An error occurred while processing your request', 'error')
        return render_template('teacher_quiz.html', exception=str(e))

def update_quiz_in_database(quiz_id, updated_question):
    with connection_pool.get_connection() as connection:
        cursor = connection.cursor()

        update_query = """
            UPDATE quiz
            SET question=%(question)s, optionA=%(optionA)s, optionB=%(optionB)s, optionC=%(optionC)s, optionD=%(optionD)s, correctOption=%(correctOption)s
            WHERE id=%(quiz_id)s
        """
        cursor.execute(update_query, {'quiz_id': quiz_id, **updated_question})
        connection.commit()

        cursor.close()

def get_quiz_list_from_database():
    with connection_pool.get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM quiz")

        quiz_tuples = cursor.fetchall()
        quizs = [{'id': quiz[0], 'lesson': quiz[1], 'subtopic': quiz[2], 'question': quiz[3],
                  'srcQuestion': quiz[4], 'optionA': quiz[5], 'optionB': quiz[6],
                  'optionC': quiz[7], 'optionD': quiz[8], 'correctOption': quiz[9]} for quiz in quiz_tuples]

        cursor.close()

    return quizs

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/course-1', methods=['GET', 'POST'])
def course_1():
    return render_template('course-1.html')

@app.route('/lesson-1-1', methods=['GET', 'POST'])
def lesson_1_1():
    return render_template('lesson-1-1.html')

@app.route('/lesson-1-2', methods=['GET', 'POST'])
def lesson_1_2():
    return render_template('lesson-1-2.html')

@app.route('/lesson-1-3', methods=['GET', 'POST'])
def lesson_1_3():
    return render_template('lesson-1-3.html')

@app.route('/course-2', methods=['GET', 'POST'])
def course_2():
    return render_template('course-2.html')

@app.route('/lesson-2-1', methods=['GET', 'POST'])
def lesson_2_1():
    return render_template('lesson-2-1.html')

@app.route('/lesson-2-2', methods=['GET', 'POST'])
def lesson_2_2():
    return render_template('lesson-2-2.html')

@app.route('/lesson-2-3', methods=['GET', 'POST'])
def lesson_2_3():
    return render_template('lesson-2-3.html')

@app.route('/create_class', methods=['GET','POST'])
def create_class():
    if request.method == 'POST':
        class_name = request.form.get('class_name')
        selected_students = request.form.getlist('selected_students')

        try:
            # Establish a connection to the database using connection pool
            with connection_pool.get_connection() as connection:
                cursor = connection.cursor()

                # Insert into 'classes' table
                cursor.execute("INSERT INTO classes (class_name) VALUES (%s)", (class_name,))
                class_id = cursor.lastrowid

                # Insert into 'class_enrollments' table for each selected student
                for student_id in selected_students:
                    cursor.execute("INSERT INTO class_enrollments (class_id, student_id) VALUES (%s, %s)",
                                   (class_id, student_id))

                connection.commit()

                flash('Kelas berjaya dicipta dan pelajar telah disenaraikan.', 'success')
                return redirect(url_for('teacher_profile'))

        except Exception as e:
            flash(f'Error creating class: {str(e)}', 'error')

    return render_template('create_class.html')

@app.route('/quiz-1-1', methods=['GET', 'POST'])
def quiz_1_1():
    return render_template('quiz-1-1.html')
@app.route('/quiz-1-2', methods=['GET', 'POST'])
def quiz_1_2():
    return render_template('quiz-1-2.html')
@app.route('/quiz-1-3', methods=['GET', 'POST'])
def quiz_1_3():
    return render_template('quiz-1-3.html')
@app.route('/quiz-2-1', methods=['GET', 'POST'])
def quiz_2_1():
    return render_template('quiz-2-1.html')
@app.route('/quiz-2-2', methods=['GET', 'POST'])
def quiz_2_2():
    return render_template('quiz-2-2.html')
@app.route('/quiz-2-3', methods=['GET', 'POST'])
def quiz_2_3():
    return render_template('quiz-2-3.html')


@app.route('/get_quiz_questions', methods=['GET', 'POST'])
def get_quiz_questions():
    try:
        lesson = request.args.get('lesson')
        subtopic = request.args.get('subtopic')

        with connection_pool.get_connection() as connection:
            cursor = connection.cursor(dictionary=True)
            
            # Use placeholders in the SQL query and pass values as parameters
            query = "SELECT * FROM quiz WHERE lesson = %s AND subtopic = %s ORDER BY ID ASC"
            cursor.execute(query, (lesson, subtopic))
            
            questions = cursor.fetchall()
            return jsonify({'questions': questions})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
