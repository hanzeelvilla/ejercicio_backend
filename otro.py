#CATEGORIES
@app.route("/add-category", methods=["POST"])
def add_category():
    created_at_date = request.form.get("created_at")
    new_created_at_date = datetime.strptime(created_at_date, "%Y-%m-%d")
    
    new_category = Categories(
        name = request.form.get("name"),
        description = request.form.get("description"),
        created_at = new_created_at_date,
        created_by  = request.form.get("created_by")
    )
    db .session.add(new_category)
    db.session.commit()
    return jsonify(response={"success": "Category added successfully"})

#PRODUCTS
@app.route("/add-product", methods=["POST"])
def add_product():
    created_at_date = request.form.get("created_at")
    new_created_at_date = datetime.strptime(created_at_date, "%Y-%m-%d")
    
    new_product = Products(
        name = request.form.get("name"),
        description = request.form.get("description"),
        category_id = request.form.get("category_id"),
        created_at = new_created_at_date,
        created_by  = request.form.get("created_by")
    )
    db .session.add(new_product)
    db.session.commit()
    return jsonify(response={"success": "Product added successfully"})

#PROVIDERS
@app.route("/add-provider", methods=["POST"])
def add_provider():
    created_at_date = request.form.get("created_at")
    new_created_at_date = datetime.strptime(created_at_date, "%Y-%m-%d")
    
    new_provider = Providers(
        name = request.form.get("name"),
        full_address = request.form.get("full_address"),
        created_at = new_created_at_date,
        created_by  = request.form.get("created_by")
    )
    db .session.add(new_provider)
    db.session.commit()
    return jsonify(response={"success": "Provider added successfully"})

#PURCHASE ORDERS
@app.route("/add-purchase-order", methods=["POST"])
def add_purchase_order():
    date = request.form.get("date")
    new_date = datetime.strptime(date, "%Y-%m-%d")
    
    created_at_date = request.form.get("created_at")
    new_created_at_date = datetime.strptime(created_at_date, "%Y-%m-%d")
    
    new_purchase_order = Purchase_orders(
        provider_id = request.form.get("provider_id"),
        date = new_date,
        total = request.form.get("total"),
        created_at = new_created_at_date,
        created_by  = request.form.get("created_by")
    )
    db .session.add(new_purchase_order)
    db.session.commit()
    return jsonify(response={"success": "Purchase order added successfully"})

#PURCHASE ORDERS DETAIL
@app.route("/add-purchase-order-detail", methods=["POST"])
def add_purchase_order_detail():
    
    created_at_date = request.form.get("created_at")
    new_created_at_date = datetime.strptime(created_at_date, "%Y-%m-%d")
    
    new_purchase_order_detail = Purchase_order_detail(
        purchase_order_id = request.form.get("purchase_order_id"),
        product_id = request.form.get("product_id"),
        quantity = request.form.get("quantity"),
        total = request.form.get("total"),
        created_at = new_created_at_date,
        created_by  = request.form.get("created_by")
    )
    db .session.add(new_purchase_order_detail)
    db.session.commit()
    return jsonify(response={"success": "Purchase order detail added successfully"})

# ----------------------------------- READ ----------------------------------- #

#CATEGORIES
@app.route("/get-categories")
def get_categories():
    result = db.session.execute(db.select(Categories).order_by(Categories.id))
    all_results = result.scalars().all()
    return jsonify(categories=[category.to_dict() for category in all_results])

#PRODUCTS
@app.route("/get-products")
def get_products():
    result = db.session.execute(db.select(Products).order_by(Products.id))
    all_results = result.scalars().all()
    return jsonify(products=[product.to_dict() for product in all_results])

#PROVIDERS
@app.route("/get-providers")
def get_providers():
    result = db.session.execute(db.select(Providers).order_by(Providers.id))
    all_results = result.scalars().all()
    return jsonify(providers=[provider.to_dict() for provider in all_results])

#PURCHASE ORDERS
@app.route("/get-purchase-orders")
def get_purchase_orders():
    result = db.session.execute(db.select(Purchase_orders).order_by(Purchase_orders.provider_id))
    all_results = result.scalars().all()
    return jsonify(purchase_orders=[purchase.to_dict() for purchase in all_results])

#PURCHASE ORDER DETAIL
@app.route("/get-purchase-order-detail")
def get_purchase_order_detail():
    result = db.session.execute(db.select(Purchase_order_detail).order_by(Purchase_order_detail.purchase_order_id))
    all_results = result.scalars().all()
    return jsonify(purchase_order_detail=[purchase.to_dict() for purchase in all_results])

# -------------------------------- READ BY ID -------------------------------- #

#CATEGORIES
@app.route("/search-category")
def search_category():
    id = request.args.get("id")
    result = db.session.execute(db.select(Categories).where(Categories.id == id))
    all_results = result.scalars().all()
    if all_results:
        return jsonify(category=[cat.to_dict() for cat in all_results])
    else:
        return jsonify(error={"Not Found": "The id doesn't exist"}), 404

#PRODUCTS
@app.route("/search-product")
def search_product():
    id = request.args.get("id")
    result = db.session.execute(db.select(Products).where(Products.id == id))
    all_results = result.scalars().all()
    if all_results:
        return jsonify(product=[product.to_dict() for product in all_results])
    else:
        return jsonify(error={"Not Found": "The id doesn't exist"}), 404

#PROVIDERS
@app.route("/search-provider")
def search_provider():
    id = request.args.get("id")
    result = db.session.execute(db.select(Providers).where(Providers.id == id))
    all_results = result.scalars().all()
    if all_results:
        return jsonify(provider=[provider.to_dict() for provider in all_results])
    else:
        return jsonify(error={"Not Found": "The id doesn't exist"}), 404

#PURCHASE ORDERS
@app.route("/search-purchase-order")
def search_purchase_order():
    id = request.args.get("id")
    result = db.session.execute(db.select(Purchase_orders).where(Purchase_orders.provider_id == id))
    all_results = result.scalars().all()
    if all_results:
        return jsonify(order=[order.to_dict() for order in all_results])
    else:
        return jsonify(error={"Not Found": "The id doesn't exist"}), 404
    
#PURCHASE ORDER DETAIL
@app.route("/search-purchase-order-detail")
def search_purchase_order_detail():
    id = request.args.get("id")
    result = db.session.execute(db.select(Purchase_order_detail).where(Purchase_order_detail.purchase_order_id == id))
    all_results = result.scalars().all()
    if all_results:
        return jsonify(order=[order.to_dict() for order in all_results])
    else:
        return jsonify(error={"Not Found": "The id doesn't exist"}), 404
    
# -------------------------- UPDATE BY ID | PATCH | -------------------------- #

#CATEGORIES 
@app.route("/change-category/<int:id>/<column>", methods=["PATCH"])
def change_category(id, column):
    new_value= request.args.get("new_value")
    category = db.get_or_404(Categories, id)
    
    if category:
        setattr(category, column, new_value)
        db.session.commit()
        return redirect(url_for("get_categories"))
    else:
        return jsonify(error={"Not Found": "The id doesn't exist"}), 404

#PRODUCTS
@app.route("/change-product/<int:id>/<column>", methods=["PATCH"])
def change_product(id, column):
    new_value= request.args.get("new_value")
    product = db.get_or_404(Products, id)
    
    if product:
        setattr(product, column, new_value)
        db.session.commit()
        return redirect(url_for("get_products"))
    else:
        return jsonify(error={"Not Found": "The id doesn't exist"}), 404

#PROVIDERS
@app.route("/change-provider/<int:id>/<column>", methods=["PATCH"])
def change_provider(id, column):
    new_value= request.args.get("new_value")
    provider = db.get_or_404(Providers, id)
    
    if provider:
        setattr(provider, column, new_value)
        db.session.commit()
        return redirect(url_for("get_providers"))
    else:
        return jsonify(error={"Not Found": "The id doesn't exist"}), 404

#PURCHASE ORDERS
@app.route("/change-purchase-order/<int:id>/<column>", methods=["PATCH"])
def change_purchase_order(id, column):
    new_value= request.args.get("new_value")
    purchase = db.get_or_404(Purchase_orders, id)
    
    if purchase:
        setattr(purchase, column, new_value)
        db.session.commit()
        return redirect(url_for("get_purchase_orders"))
    else:
        return jsonify(error={"Not Found": "The id doesn't exist"}), 404

#PURCHASE ORDER DETAIL
@app.route("/change-purchase-order-detail/<int:id>/<column>", methods=["PATCH"])
def change_purchase_order_detail(id, column):
    new_value= request.args.get("new_value")
    purchase = db.get_or_404(Purchase_order_detail, id)
    
    if purchase:
        setattr(purchase, column, new_value)
        db.session.commit()
        return redirect(url_for("get_purchase_order_detail"))
    else:
        return jsonify(error={"Not Found": "The id doesn't exist"}), 404
    
# ------------------------------- DELETE BY ID ------------------------------- #

#CATEGORIES 
@app.route("/delete-category/<int:id>", methods=["DELETE"])
def delete_category(id):
    category = db.get_or_404(Categories, id)
    
    if category:
        db.session.delete(category)
        db.session.commit()
        return redirect(url_for("get_categories"))
    else:
        return jsonify(error={"Not Found": "The id doesn't exist"}), 404


#PURCHASE ORDER DETAIL
@app.route("/delete-purchase-order-detail/<int:id>", methods=["DELETE"])
def delete_purchase_order_detail(id):
    purchase = db.get_or_404(Purchase_order_detail, id)
    
    if purchase:
        db.session.delete(purchase)
        db.session.commit()
        return redirect(url_for("get_purchase_order_detail"))
    else:
        return jsonify(error={"Not Found": "The id doesn't exist"}), 404

# --------------------------------- HOME PAGE -------------------------------- #
 