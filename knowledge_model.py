from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
    __tablename__ = 'articles'
    article_key = Column(Integer, primary_key=True)
    topic = Column(String)
    title = Column(String)
    rating = Column(String)

    def __repr__(self):
       return ("If you want to learn about {},\n"
               "you should look at the wikipedia article called {} \n"
               "we gave this articlea rating of {} out of 10").format(
                    self.topic, self.title, self.rating)

article1 = Knowledge(topic ="Kamari Maxine Clarke", title = "Kamari Maxine Clarke", rating = "7", article_key = 1)

article2 = Knowledge(topic ="classical poetry", title = "Anapaest", rating = "5", article_key = 2)

article3 = Knowledge(topic ="Armored warfare", title = "Armored warfare", rating = "8", article_key = 3)

print(article1)
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.

