# Name:        img_metadata_v0
# Purpose:      To capture, validate and save image metadata from image database
#               into a CSV file. (Rough first version of program)
#
# Author:      Renee Topeto
#
# Created:     20/09/2016

def main():
    pass

if __name__ == '__main__':
    main()

from tkinter import *

import tkinter.messagebox

class Img_Metadata:
    def __init__(self, img_id, filename, title, img_size, owner, license ):
        self.img_id = img_id
        self.filename = filename
        self.title = title
        self.img_size = img_size
        self.owner= owner
        self.license= license

    def get_img_id(self):
        return self.img_id

    def get_filename(self):
        return self.filename

    def get_title(self):
        return self.title

    def get_img_size(self):
        return self.img_size

    def get_owner(self):
        return self.owner

    def get_license(self):
        return self.license

class GUI:
    def __init__(self):

        window = Tk()
        window.title("Image Metadata")
        window.minsize(width=600, height=400)

        heading_label = Label(window, bg="black", fg="blue", text="Image Metadata", font=("Times","24"))
        heading_label.pack()

        self.ready_to_write = False
        self.recordlist = []

        img_id_label = Label(window, text='Enter Image ID:')
        img_id_label.pack(anchor="c")
        self.img_id_field = Entry(window)
        self.img_id_field.pack(anchor="c")

        filename_label = Label(window, text='Enter Filename (including extension):')
        filename_label.pack()
        self.filename_field = Entry(window)
        self.filename_field.pack()

        title_label = Label(window, text='Enter Image Title :')
        title_label.pack()
        self.title_field = Entry(window)
        self.title_field.pack()

        img_size_label = Label(window, text ="Enter Image Size(bytes):")
        img_size_label.pack()
        self.img_size_field= Entry(window)
        self.img_size_field.pack()

        owner_label = Label(window, text='Enter Name of Owner:')
        owner_label.pack()
        self.owner_field = Entry(window)
        self.owner_field.pack()

        license_label = Label(window, text='Enter Image License:')
        license_label.pack()
        self.license_field = StringVar()
        OptionMenu(window, self.license_field, "CC0", "BY", "BY-SA", "BY-NC", "BY-ND", "BY-NC-SA", "BY-NC-ND").pack()

        button_label = Label(window, text='Press to validate:')
        button = Button(window, text='Submit', command=self.doSubmit)

        button_label1 = Label(window, text='Convert Record to csv')
        button1 = Button(window, text='write to csv', command=self.writetocsv)
        button_label.pack()
        button.pack()
        button_label1.pack()
        button1.pack()

        window.mainloop()


    def doSubmit(self):

        noduplicate = True;
        for record in self.recordlist:
            if self.img_id_field.get() == record.get_img_id():
                noduplicate= False
                tkinter.messagebox.showwarning('Warning!','Duplicate Image ID!');
                print('Please enter Image ID again');


        if noduplicate == True:
            if len(self.img_id_field.get()) <1 or len(self.filename_field.get()) <1 or len(self.title_field.get()) <1 or len(self.img_size_field.get()) <1 or len(self.owner_field.get()) <1 or len(self.license_field.get()) <1:
                tkinter.messagebox.showwarning('Warning!','Please enter a value for all fields')
            else:
                try:
                    validated_img_id = int(self.img_id_field.get())
                    validated_img_size = int(self.img_size_field.get())
                    self.recordlist.append(Img_Metadata(self.img_id_field.get(),self.filename_field.get(), self.title_field.get() , self.img_size_field.get(), self.owner_field.get(), self.license_field.get()))
                    self.ready_to_write= True
                    tkinter.messagebox.showinfo('Notice','Submission Sucessful')

                    self.img_id_field.delete(0, END)
                    self.filename_field.delete(0, END)
                    self.title_field.delete(0, END)
                    self.img_size_field.delete(0, END)
                    self.owner_field.delete(0, END)

                except:
                    tkinter.messagebox.showwarning('Warning!','Please enter numeric Image ID and Image Size')
                    print('Please enter numeric Image ID and Image Size')


    def writetocsv(self):
        import csv
        file_name = 'imgmetadata_database.csv'

        if self.ready_to_write:
            ofile = open(file_name, 'a')
            writer = csv.writer(ofile, delimiter=',')
            for record in self.recordlist:
                print(record.get_title())
                writer.writerow([record.get_img_id(),record.get_filename(), record.get_title(), record.get_img_size(), record.get_owner(), record.get_license()])
            ofile.close()
        else:
            tkinter.messagebox.showwarning('Error!', 'You need to Validate your data')

        self.ready_to_write= False
        tkinter.messagebox.showinfo('Notice',file_name+' File Generated Sucessfully')

GUI()

