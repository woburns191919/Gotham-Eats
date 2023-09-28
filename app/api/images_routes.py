# from flask import Blueprint, render_template, redirect
# from models import db, Post  # Ensure you have this file and class
# from flask_login import login_required
# from app.s3 import get_unique_filename, upload_file_to_s3, remove_file_from_s3, ALLOWED_EXTENSIONS, upload_file
# from app.forms import ImageForm


# image_routes = Blueprint("images", __name__)

# @image_routes.route("", methods=["POST"])
# @login_required
# def upload_image():
#     form = ImageForm()

#     if form.validate_on_submit():
#         image = form.data["image"]
#         image.filename = get_unique_filename(image.filename)
#         upload = upload_file_to_s3(image)
#         print(upload)
#         if "url" not in upload:
#             return render_template("post_form.html", form=form, errors=[upload])
#         url = upload["url"]
#         new_image = Post(image=url)
#         db.session.add(new_image)
#         db.session.commit()
#         return redirect("/posts/all")

#     if form.errors:
#         print(form.errors)
#         return render_template("post_form.html", form=form, errors=form.errors)

#     return render_template("post_form.html", form=form, errors=None)
