import wx
import wx.media
class AudioPlayer(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,"Audio Player",size=(400,200))
        panel=wx.Panel(self)
        self.media=wx.media.MediaCtrl(panel)
        b1=wx.Button(panel,-1,'Load',pos=(30,40),size=(60,30))
        b2=wx.Button(panel,-1,'Play',pos=(110,40),size=(60,30))
        b3=wx.Button(panel,-1,'Pause',pos=(180,40),size=(60,30))
        b4=wx.Button(panel,-1,'Stop',pos=(260,40),size=(60,30))
        self.Bind(wx.EVT_BUTTON,self.load,b1)
        self.Bind(wx.EVT_BUTTON,self.play,b2)
        self.Bind(wx.EVT_BUTTON,self.pause,b3)
        self.Bind(wx.EVT_BUTTON,self.stop,b4)

    def load(self,event):
        stl=wx.FD_OPEN
        filedia=wx.FileDialog(self,'open',style=stl)
        if filedia.ShowModal()==wx.ID_OK:
            path=filedia.GetPath()
            self.media.Load(path)

    def play(self,event):
        self.media.Play()
    def pause(self,event):
        self.media.Pause()
    def stop(self,event):
        self.media.Forward()


app=wx.App()
frame=AudioPlayer(None,-1)
frame.Show()
app.MainLoop()