#!/usr/bin/env python3
# -*- coding: utf8 -*-


from flask import request, render_template, redirect, url_for #
from app import app
from app.database import create, read, update, delete, scan
from datetime import datetime
from app.forms.product import ProductForm
from app.forms.deactivate import DeleteProduct, ActivateProduct



@app.route("/")
def index():
    serv_time = datetime.now().strftime("%F %H:%M:%S") 
    tout = {}
    tout["ok"] = True
    tout["version"] = "1.0.0"
    tout["server_time"] = serv_time
    return render_template("index.html", out=tout)

@app.route("/product_form", methods=["GET", "POST"])
def product_form():
    if request.method == "POST":
        p_Name = request.form.get("name")
        p_Price = request.form.get("price")
        p_Description = request.form.get("description")
        p_Category = request.form.get("category")
        p_Quantitiy = request.form.get("quantity")
        p_Tag = request.form.get("unique_tag")

        create(p_Name, p_Price, p_Description, p_Category, p_Quantitiy, p_Tag)
        
    form = ProductForm()

    if form.validate_on_submit():
        return redirect(url_for('product_form'))

    return render_template("form_example.html", form=form)

@app.route("/products", methods=["GET", "PUT"])
def get_all_products():
    if request.method == "GET":

        form = DeleteProduct()
        form_A = ActivateProduct()

        if 'deactivate' in request.form:

            pid = request.form.get["id"]
            update(pid, {"active": False})

        
            return redirect(url_for('get_all_products'))

        elif 'activate' in request.form:
            pid = request.form.get["id"]

            update(pid, {"active": True})

      
            return redirect(url_for('get_all_products'))
        else:
            out = scan() 
            out["ok"] = True
            out["message"] = "Success"
         
            return render_template("products.html", products=out["body"], form=form, form_A=form_A)
    
    elif request.method == "PUT":
        if 'deactivate' in request.form:

            pid = request.form.get["id"]
            update(pid, {"active": False})

          
            return redirect(url_for('get_all_products'))

        elif 'activate' in request.form:
            pid = request.form.get["id"]

            update(pid, {"active": True})

            #rerender template
            return redirect(url_for('get_all_products'))
        

@app.route("/aboutme")
def aboutme():
    return render_template("about_me.html")

#our error 404 html page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
