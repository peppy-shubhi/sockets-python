import wx
import random
import socket
import sys

class welkom(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "Hello V.1.0", size=(900,600))
        self.mainFrame = mainFrame

        top_panel = wx.Panel(self)
        w_tekst = wx.StaticText(top_panel, -1, "yo wassssssup bitches!",(325,50), (100, -1), wx.ALIGN_CENTER)
        w_font = wx.Font(20, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        w_tekst.SetFont(w_font)

        st_nr = wx.StaticText(top_panel, -1, 'Student number' ,(100,150))
        inp_st_nr = wx.TextCtrl(top_panel, -1, '', (300,150), size=(140,-1))
        st_vr= wx.StaticText(top_panel, -1, 'Student name' ,(100,200))
        inp_st_vr = wx.TextCtrl(top_panel, -1, '', (300,200), size=(140,-1))

        close_button = wx.Button(top_panel, label = "Stop", pos=(600, 400), size=(150, 200))
        self.Bind(wx.EVT_BUTTON, self.closebutton, close_button)
        go_button = wx.Button(top_panel, label = "Run", pos=(100, 400), size=(150, 200))
        self.Bind(wx.EVT_BUTTON, self.buttonClick, go_button)

    def closebutton(self, event):
        self.Close(True)

    def buttonClick(self, event):
        self.Hide()
        self.mainFrame(None, id = -1).Show()

class mainFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "bitch V.1.0", size=(900,600))

        top_panel = wx.Panel(self)
        self.vraag = 1
        m_tekst = wx.StaticText(top_panel, -1, "Server" + str(self.vraag),(400,50), (100, -1), wx.ALIGN_CENTER)
        m_font = wx.Font(20, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        m_tekst.SetFont(m_font)

        cijfer = random.randint(1,100)

        ### Make an attribute to access from buttonClick1 method.
        self.st = wx.TextCtrl(top_panel, pos=(15,10),size=(200,250))
        self.st.SetValue("hello")

        self.gt = wx.TextCtrl(top_panel, pos=(600,10),size=(200,250))
        self.gt.SetValue("hello")
        #self.test2 = wx.StaticText(top_panel, -1, str(cijfer), (325,300))
        
        self.connection, self.client_address = sock.accept()
        print ('connection from', self.client_address)
        res_but = wx.Button(top_panel, label = "Close", pos=(650, 400), size=(150, 200))
        ga_naar = wx.Button(top_panel, label = "Send", pos=(100, 400), size=(150, 200))
        ga_button = wx.Button(top_panel, label = "Recieve", pos=(380, 400), size=(150, 200))
        self.Bind(wx.EVT_BUTTON, self.buttonClick1, ga_button)
        self.Bind(wx.EVT_BUTTON, self.buttonClick2, ga_naar)
        self.Bind(wx.EVT_BUTTON, self.closebutton, res_but)

    def buttonClick1(self, event):
        ### Change label of static text.
        data = self.connection.recv(50)
        print ('received "%s"' % data)
        data = data.decode('utf-8')
        ans = self.gt.GetValue();
        self.gt.SetValue(ans+" \n "+data)

    def buttonClick2(self, event):
        ### Change label of static text.
        ans = self.st.GetValue();
        message = str.encode(ans)
        self.connection.sendall(message)


    def closebutton(self, event):
        self.Close(True)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 10000)
print ('starting up on %s port %s' % server_address)
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
app = wx.App()
frame = welkom(None, id = -1).Show()
app.MainLoop()
