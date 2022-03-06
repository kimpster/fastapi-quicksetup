## Models represent the data and table construction in postgresql
# Example:
# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key= True, nullable= False)
#     email = Column(String, nullable= False, unique= True)
#     password = Column(String, nullable=False)
#     created_at = Column(TIMESTAMP(timezone=True), nullable= False, server_default=text('now()'))


from .database import Base
