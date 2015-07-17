import datetime
import tkinter

from model import Entry, initialize 

class Diary:
	def __init__(self, master):
		self.currDate = datetime.date.today()

		frame_top = tkinter.Frame(master)
		frame_top.pack(side=tkinter.TOP)
		frame_left = tkinter.Frame(master)
		frame_left.pack(side=tkinter.LEFT)
		frame_right = tkinter.Frame(master)
		frame_right.pack(side=tkinter.RIGHT)

		# create date label
		self.dateLabel = tkinter.Label(frame_top,text="Date: " + str(self.currDate))
		self.dateLabel.pack()

		# create entry widget for storing diary entry
		self.entry = tkinter.Text(frame_left)
		
		# get text for currDate if exists
		entryText = Entry.getEntry(self.currDate)
		if entryText:
			self.entry.insert(1.0,entryText)

		self.entry.pack()

		#create next and previous entry buttons
		self.previousEntryButton = tkinter.Button(frame_right, text="prev", command = self.prevEntry)
		self.nextEntryButton = tkinter.Button(frame_right, text="next", command = self.nextEntry)
		self.previousEntryButton.pack()
		self.nextEntryButton.pack()

		# create a save entry button
		self.saveEntryButton = tkinter.Button(frame_right, text="Save", command = self.saveEntry)
		self.saveEntryButton.pack()

		# create a delete entry button
		self.deleteEntryButton = tkinter.Button(frame_right, text="Delete", command = self.deleteEntry)
		self.deleteEntryButton.pack()

	def nextEntry(self):
		if self.currDate == datetime.date.today():
			print("Can't go past todays date")
		else:
			self.currDate = self.currDate + datetime.timedelta(1)
			self.dateLabel.configure(text="Date: " + str(self.currDate))
			
			entryText = self.getEntry(self.currDate)
			if entryText:
				self.entry.delete(1.0, tkinter.END)
				self.entry.insert(1.0, entryText)
			else:
				self.entry.delete(1.0, tkinter.END)

	def prevEntry(self):
		self.currDate = self.currDate - datetime.timedelta(1)
		self.dateLabel.configure(text="Date: " + str(self.currDate))
		entryText = self.getEntry(self.currDate)
		if entryText:
			self.entry.delete(1.0, tkinter.END)
			self.entry.insert(1.0, entryText)
		else:
			self.entry.delete(1.0, tkinter.END)

	def deleteEntry(self):
		Entry.deleteEntry(self.currDate)
		self.entry.delete(1.0, tkinter.END)

	def saveEntry(self):
		contents = self.entry.get(1.0, tkinter.END)
		Entry.updateEntry(self.currDate, contents)

	def getEntry(self, date):
		return Entry.getEntry(date)

if __name__ == '__main__':
	initialize()
	window = tkinter.Tk()
	diary = Diary(window)
	window.mainloop()

