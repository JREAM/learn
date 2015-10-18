#!/usr/bin/env python
# http://www.pygtk.org/pygtk2reference/

import gtk

def press(widget):
    num = entry.get_text() # Default is empty
    pressed = widget.get_label()
    entry.set_text(num + pressed)

def send_press(widget):
    print "Dialing: " + entry.get_text()

def clear_text(widget):
    entry.set_text('')

win = gtk.Window()
win.move(50, 50)
win.resize(200,200)

# Prevent running in the background
win.connect('destroy', lambda w: gtk.main_quit())

box = gtk.VBox()
win.add(box)

entry = gtk.Entry()
box.pack_start(entry)


send = gtk.Button('Send')
send.connect('clicked', send_press)

clear = gtk.Button('Clear')
clear.connect('clicked', clear_text)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, '#', 0, '*']
x = 0
y = 0

table = gtk.Table(2, 3, True) 

for i in nums:
    button = gtk.Button(str(i))
    button.connect('clicked', press)
    table.attach(button, x, x+1, y, y+1)

    x += 1
    if x > 2:
        x = 0
        y += 1


#table = gtk.Table(2, 2, gtk.TRUE)
box.pack_start(table, False) # False stretches the table

send = gtk.Button('Send')
send.connect('clicked', send_press)

clear = gtk.Button('Clear')
clear.connect('clicked', clear_text)

table = gtk.Table(1, 2, True)
table.attach(send, 0, 1, 0, 1)
table.attach(clear, 1, 2, 0, 1)
box.pack_start(table, False)

win.show_all()

gtk.main()
