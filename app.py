@app.route('/download_result/')
def download_result():
    filename = request.args.get('filename')
    if not filename:
        flash("Filename not provided.", "danger")
        return redirect(url_for('index'))  # fallback

    return send_from_directory(RESULT_DIR,
                               secure_filename(filename),
                               as_attachment=True)
  
