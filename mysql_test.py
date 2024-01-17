import mysql.connector

try:
    connection = mysql.connector.connect(
        host='your_host',
        user='your_user',
        password='your_password',
        database='mathGenius'
    )
    print("MySQL connection successful.")
    connection.close()
except Exception as e:
    print(f"Error during MySQL connection test: {str(e)}")


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
