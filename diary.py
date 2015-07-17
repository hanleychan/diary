import datetime
import tkinter

from model import Entry, initialize 

class Diary:
	def __init__(self, master):
		self.currDate = datetime.date.today()

		self.createMenu(master)
		self.createStatusBar(master)

		frame_top = tkinter.Frame(master)
		frame_top.pack(side=tkinter.TOP)
		frame_left = tkinter.Frame(master)
		frame_left.pack(side=tkinter.LEFT)
		frame_right = tkinter.Frame(master, width= 500)
		frame_right.pack()

		# create date label
		self.dateLabel = tkinter.Label(frame_top,text="Date: " + str(self.currDate))
		self.dateLabel.pack()

		# create entry widget for storing diary entry
		self.entry = tkinter.Text(frame_left, wrap = tkinter.WORD)
		
		# get text for currDate if exists
		entryText = Entry.getEntry(self.currDate)
		if entryText:
			self.entry.insert(1.0,entryText)

		self.entry.pack(padx=10, pady=10)

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

	def createStatusBar(self, master):
		"""
		Creates the status bar
		"""
		self.statusBar = tkinter.Label(bd=1, relief=tkinter.SUNKEN, anchor=tkinter.W)
		self.statusBar.pack(side=tkinter.BOTTOM, fill=tkinter.X)
		
	def createMenu(self, master):
		"""
		Creates the menu bar
		"""
		menu = tkinter.Menu(master)
		master.config(menu=menu)
		subMenu = tkinter.Menu(menu, tearoff=False)
		menu.add_cascade(label="File", menu=subMenu)
		subMenu.add_command(label="Exit", command=lambda window=master:quit(window))
	
	def updateStatusBar(self, text):
		"""
		Updates the text on the status bar
		"""
		self.statusBar.configure(text=text)

	def quit(self, master):
		"""
		Close the window
		"""
		master.quit()

	def nextEntry(self):
		"""
		Go to the next day and fetch the entry for it
		"""
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
		"""
		Go to the previous day and fetch the entry for it 
		"""
		self.currDate = self.currDate - datetime.timedelta(1)
		self.dateLabel.configure(text="Date: " + str(self.currDate))
		entryText = self.getEntry(self.currDate)
		if entryText:
			self.entry.delete(1.0, tkinter.END)
			self.entry.insert(1.0, entryText)
		else:
			self.entry.delete(1.0, tkinter.END)

	def deleteEntry(self):
		"""
		Deletes an entry
		"""
		Entry.deleteEntry(self.currDate)
		self.entry.delete(1.0, tkinter.END)
		self.updateStatusBar("Last action: " + str(self.currDate) + " - Entry deleted")

	def saveEntry(self):
		"""
		Updates an entry
		"""
		contents = self.entry.get(1.0, tkinter.END)
		Entry.updateEntry(self.currDate, contents)
		self.updateStatusBar("Last action: " + str(self.currDate) + " - Entry updated")

	def getEntry(self, date):
		"""
		Gets the contents of an entry of a specified date
		"""
		return Entry.getEntry(date)

if __name__ == '__main__':
	initialize()
	window = tkinter.Tk()
	diary = Diary(window)
	window.mainloop()

