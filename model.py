from peewee import *
import datetime

db = SqliteDatabase('diary.db')

class Entry(Model):
	entryDate = DateField(unique=True)
	content = TextField()

	class Meta:
		database = db

	@classmethod
	def deleteEntry(cls, entryDate):
	"""
	Deletes the an entry based on entryDate
	"""
		try:
			entry = cls.select().where(cls.entryDate == entryDate).get()
			entry.delete_instance()
		except cls.DoesNotExist:
			print("Error deleting")


	@classmethod
	def updateEntry(cls, entryDate, content):
	"""
	Updates or adds a new entry based on whether an entry already exists for the specified entryDate
	"""
		# check if there is already an entry for entryDate
		try:
			entry = cls.select().where(cls.entryDate==entryDate).get()
			entry.content = content
			entry.save()
		except cls.DoesNotExist:
			if content.strip() != "":
				cls.create(entryDate=entryDate, content=content)

	@classmethod
	def getEntry(cls, entryDate):
	"""
	Returns the content of an entry based on entry date
	"""
		try:
			entry = cls.select().where(cls.entryDate==entryDate).get()
			return entry.content
		except cls.DoesNotExist:
			return None 

def initialize():
	"""
	Connects to database and creates tables
	"""
	db.connect()
	db.create_tables([Entry], safe=True)
