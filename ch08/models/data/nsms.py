from config.db.gino_db import db

class Login(db.Model): 
    __tablename__ = "login"
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String, unique=False, index=False, nullable=False)
    password = db.Column(db.String, unique=False, index=False, nullable=False)
    user_type = db.Column(db.Integer, unique=False, index=False, nullable=False)
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self._children = set()

    @property
    def children(self):
        return self._children

    @children.setter
    def add_child(self, child):
        self._children.add(child)


class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True, index=True)
    firstname = db.Column(db.String, unique=False, index=False, nullable=False)
    lastname = db.Column(db.String, unique=False, index=False, nullable=False)
    age = db.Column(db.Integer, unique=False, index=False, nullable=False)
    date_started = db.Column(db.Date, unique=False, index=False, nullable=False)
    status = db.Column(db.Integer, unique=False, index=False, nullable=False)
    login_id = db.Column(db.Integer, db.ForeignKey('login.id'), unique=False, index=False, nullable=False)
    birthday = db.Column(db.Date, unique=False, index=False, nullable=False)
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self._children = set()

    @property
    def children(self):
        return self._children

    @children.setter
    def add_child(self, child):
        self._children.add(child)

class Vendor(db.Model): 
    __tablename__ = "vendor"
    id = db.Column(db.Integer, primary_key=True, index=True)
    rep_firstname = db.Column(db.String, unique=False, index=False, nullable=False)
    rep_lastname = db.Column(db.String, unique=False, index=False, nullable=False)
    rep_id = db.Column(db.String, unique=False, index=False, nullable=False)
    rep_date_employed = db.Column(db.Date, unique=False, index=False, nullable=False)
    account_name = db.Column(db.String, unique=False, index=False, nullable=False)
    account_number = db.Column(db.String, unique=False, index=False, nullable=False)
    date_consigned = db.Column(db.Date, unique=False, index=False, nullable=False)
    login_id = db.Column(db.Integer, db.ForeignKey('login.id'), unique=False, index=False, nullable=False) 

    def __init__(self, **kw):
        super().__init__(**kw)
        self._children = set()

    @property
    def children(self):
        return self._children

    @children.setter
    def add_child(self, child):
        self._children.add(child)

class Customer(db.Model): 
    __tablename__ = "customer"
    id = db.Column(db.Integer, primary_key=True, index=True)
    firstname = db.Column(db.String, unique=False, index=False, nullable=False)
    lastname = db.Column(db.String, unique=False, index=False, nullable=False)
    age = db.Column(db.Integer, unique=False, index=False, nullable=False)
    birthday = db.Column(db.Date, unique=False, index=False, nullable=False)
    date_subscribed = db.Column(db.Date, unique=False, index=False, nullable=False)
    status = db.Column(db.Integer, unique=False, index=False, nullable=False)
    subscription_type = db.Column(db.Integer, unique=False, index=False, nullable=False)
    login_id = db.Column(db.Integer, db.ForeignKey('login.id'), unique=False, index=False, nullable=False) 
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self._children = set()

    @property
    def children(self):
        return self._children

    @children.setter
    def add_child(self, child):
        self._children.add(child)
    
class Billing(db.Model):
    __tablename__ = "billing"
    id = db.Column(db.Integer, primary_key=True, index=True)
    payable = db.Column(db.Float, unique=False, index=False, nullable=False)
    approved_by = db.Column(db.String, unique=False, index=False, nullable=False)
    date_approved = db.Column(db.Date, unique=False, index=False, nullable=False)
    date_billed = db.Column(db.Date, unique=False, index=False, nullable=False)
    received_by = db.Column(db.String, unique=False, index=False, nullable=False)
    date_received = db.Column(db.Date, unique=False, index=False, nullable=False)
    total_issues = db.Column(db.Integer, unique=False, index=False, nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'), unique=False, index=False, nullable=False) 
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), unique=False, index=False, nullable=False) 
    
class Messenger(db.Model): 
    __tablename__ = "messenger"
    id = db.Column(db.Integer, primary_key=True, index=True)
    firstname = db.Column(db.String, unique=False, index=False, nullable=False)
    lastname = db.Column(db.String, unique=False, index=False, nullable=False)
    salary = db.Column(db.Float, unique=False, index=False, nullable=False)
    date_employed = db.Column(db.Date, unique=False, index=False, nullable=False)
    status = db.Column(db.Integer, unique=False, index=False, nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'), unique=False, index=False, nullable=False)  
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self._children = set()

    @property
    def children(self):
        return self._children

    @children.setter
    def add_child(self, child):
        self._children.add(child)

class Publication(db.Model):
    __tablename__ = "publication"
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String, unique=False, index=False, nullable=False)
    type = db.Column(db.String, unique=False, index=False, nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'), unique=False, index=False, nullable=False)  
    messenger_id = db.Column(db.Integer, db.ForeignKey('messenger.id'), unique=False, index=False, nullable=False)      

    def __init__(self, **kw):
        super().__init__(**kw)
        self._children = set()

    @property
    def children(self):
        return self._children

    @children.setter
    def add_child(self, child):
        self._children.add(child)


class Content(db.Model):
    __tablename__ = "content"
    id = db.Column(db.Integer,  primary_key=True, index=True)
    publication_id = db.Column(db.Integer, db.ForeignKey('publication.id'), unique=False, index=False, nullable=False)
    headline = db.Column(db.String, unique=False, index=False, nullable=False)
    content = db.Column(db.String, unique=False, index=False, nullable=False)
    content_type = db.Column(db.String, unique=False, index=False, nullable=False)
    date_published = db.Column(db.Date, unique=False, index=False, nullable=False)
    

class Sales(db.Model):
    __tablename__ = "sales"
    id = db.Column(db.Integer,  primary_key=True, index=True)
    publication_id = db.Column(db.Integer, db.ForeignKey('publication.id'), unique=False, index=False, nullable=False)
    copies_issued = db.Column(db.Integer, unique=False, index=False, nullable=False)
    copies_sold = db.Column(db.Integer, unique=False, index=False, nullable=False)
    date_issued = db.Column(db.Date, unique=False, index=False, nullable=False)
    revenue = db.Column(db.Float, unique=False, index=False, nullable=False)
    profit = db.Column(db.Float, unique=False, index=False, nullable=False)

class Subscription(db.Model):
    __tablename__ = "subscription"
    id = db.Column(db.Integer,  primary_key=True, index=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), unique=False, index=False, nullable=False)
    branch = db.Column(db.String, unique=False, index=False, nullable=False)
    price = db.Column(db.Float, unique=False, index=False, nullable=False)
    qty = db.Column(db.Integer, unique=False, index=False, nullable=False)
    date_purchased = db.Column(db.Date, unique=False, index=False, nullable=False)
