from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://{}:{}:@localhost/{}'.format("root", "password", "cooler_db"), pool_pre_ping=True)
Base = declarative_base()


class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(106), unique=True, nullable=False)
    age = Column(Integer)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

employees_data = [
    {'name': 'Brain', 'email': 'brain@gmail.com', 'age': 25},
    {'name': 'Sobil', 'email': 'sobil@gmail.com', 'age': 34},
    {'name': 'Bilal', 'email': 'bilaln@gmail.com', 'age': 22},
    {'name': 'Julien', 'email': 'julien@gmail.com', 'age': 67},
]

for emp in employees_data:
    new_employee = Employee(name=emp['name'], email=emp['email'], age=emp['age'])
    session.add(new_employee)

session.commit()

employees = session.query(Employee).all()
for i in employees:
    print(i.id, i.name, i.email, i.age)

session.close()
