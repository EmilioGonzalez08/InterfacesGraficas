Public Class Form1
   Dim SelectRect As Rectangle = New Rectangle()
   Dim ps As Point = New Point()
   Dim pe As Point = New Point()
   Private Sub Form1_MouseDown(ByVal sender As Object, ByVal e As System.Windows.Forms.MouseEventArgs) Handles Me.MouseDown
       SelectRect.Width = 0
       SelectRect.Height = 0
       SelectRect.X = e.X
       SelectRect.Y = e.Y
       ps.X = e.X
       ps.Y = e.Y
       pe = ps
   End Sub
 
   Private Sub Form1_MouseMove(ByVal sender As Object, ByVal e As System.Windows.Forms.MouseEventArgs) Handles Me.MouseMove
       If (e.Button = Windows.Forms.MouseButtons.Left) Then
           ControlPaint.DrawReversibleFrame(Me.RectangleToScreen(SelectRect), Color.Black, FrameStyle.Dashed)
           SelectRect.Width = e.X - SelectRect.X
           SelectRect.Height = e.Y - SelectRect.Y
           ControlPaint.DrawReversibleFrame(Me.RectangleToScreen(SelectRect), Color.Black, FrameStyle.Dashed)
       End If
   End Sub
 
   Private Sub Form1_MouseUp(ByVal sender As System.Object, ByVal e As System.Windows.Forms.MouseEventArgs) Handles MyBase.MouseUp
       Dim g As Graphics = Me.CreateGraphics()
       Dim p As Pen = New Pen(Color.Blue, 2)
       ControlPaint.DrawReversibleFrame(Me.RectangleToScreen(SelectRect), Color.Black, FrameStyle.Dashed)
       g.DrawRectangle(p, SelectRect)
       g.Dispose()
   End Sub
 
   Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
 
   End Sub
End Class