from sqlalchemy import Time, Boolean, Column, ForeignKey, Integer, String, Float, Date, Text
from sqlalchemy.orm import relationship
from db_config.sqlalchemy_connect import Base


class Signup(Base):
    __tablename__ = "signup"

    id = Column(Integer, primary_key=True, index=True)
    username = Column('username', String, unique=False, index=False)
    password = Column('password',String, unique=False, index=False)
    
class Login(Base): 
    __tablename__ = "login"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=False, index=False)
    password = Column(String, unique=False, index=False)
    passphrase = Column(String, unique=False, index=False)
    approved_date = Column(Date, unique=False, index=False)
       
    profiles = relationship('Profile', back_populates="login", uselist=False)
    permission_sets = relationship('PermissionSet', back_populates="login")

class Permission(Base):
    __tablename__ = "permission"
    id = Column(Integer, primary_key=True, index=True, )
    name = Column(String, unique=False, index=False)
    description = Column(String, unique=False, index=False)
        
    permission_sets = relationship('PermissionSet', back_populates="permission")
    
class PermissionSet(Base): 
    __tablename__ = "permission_set"
    id = Column(Integer,  primary_key=True, index=True)
    login_id = Column(Integer, ForeignKey('login.id'), unique=False, index=False)
    permission_id = Column(Integer, ForeignKey('permission.id'), unique=False, index=False)
        
    login = relationship('Login', back_populates="permission_sets")
    permission = relationship('Permission', back_populates="permission_sets")

class Profile(Base):
    __tablename__ = "profile"
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, unique=False, index=False)
    lastname = Column(String, unique=False, index=False)
    age = Column(Integer, unique=False, index=False)
    membership_date = Column(Date, unique=False, index=False)
    member_type = Column(String, unique=False, index=False)
    login_id = Column(Integer, ForeignKey('login.id'), unique=False, index=False)
    status = Column(Integer, unique=False, index=False)
    
    login = relationship('Login', back_populates="profiles")
    bids = relationship('Bids', back_populates="profiles")
    sold = relationship('Sold', back_populates="profiles")
    auctions = relationship('Auctions', back_populates="profiles")

class ProductType(Base):
    __tablename__ = "product_type"
    id = Column(Integer, primary_key=True, index=True )
    name = Column(String, unique=False, index=False)
    description = Column(String, unique=False, index=False)
        
    auctions = relationship('Auctions', back_populates="prodtypes")
        
class Auctions(Base): 
    __tablename__ = "auctions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=False, index=False)
    details = Column(Text, unique=False, index=False)
    type_id = Column(Integer, ForeignKey('product_type.id'), unique=False, index=False)
    max_price = Column(Float, unique=False, index=False)
    min_price = Column(Float, unique=False, index=False)
    buyout_price = Column(Float, unique=False, index=False)
    created_date = Column(Date, unique=False, index=False)
    updated_date = Column(Date, unique=False, index=False)
    condition = Column(Text, unique=False, index=False)
    profile_id  = Column(Integer, ForeignKey('profile.id'), unique=False, index=False)
    
    profiles = relationship('Profile', back_populates="auctions")
    prodtypes = relationship('ProductType', back_populates="auctions")
    bids = relationship('Bids', back_populates="auctions")
      
class Bids(Base): 
    __tablename__ = "bids"
    id = Column(Integer, primary_key=True, index=True)
    auction_id  = Column(Integer, ForeignKey('auctions.id'), unique=False, index=False)
    profile_id  = Column(Integer, ForeignKey('profile.id'), unique=False, index=False)
    created_date = Column(Date, unique=False, index=False)
    updated_date = Column(Date, unique=False, index=False)
    price = Column(Float, unique=False, index=False)
    
    auctions = relationship('Auctions', back_populates="bids")
    profiles = relationship('Profile', back_populates="bids")
    sold = relationship('Sold', back_populates="bids")
    
class Sold(Base): 
    __tablename__ = "sold"
    id = Column(Integer, primary_key=True, index=True)
    bid_id  = Column(Integer, ForeignKey('bids.id'), unique=False, index=False)
    sold_date = Column(Date, unique=False, index=False)
    buyer = Column(Integer, ForeignKey('profile.id'), unique=False, index=False)
    
    profiles = relationship('Profile', back_populates="sold")
    bids = relationship('Bids', back_populates="sold")
    