# Based on this example:  http://www.vtk.org/Wiki/VTK/Examples/Python/Widgets/EmbedPyQt2

def __import_qt_modules():
    """
    Trys to import and then returns the necessary Qt related modules with a preference given to 
    Qt5 over Qt4 and PySide over PyQt.  If no python Qt libraries are found, raises an
    ImportError.
    """
    try:
        from PySide2 import QtWidgets as  qt_gui
        from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor as renderer
        return qt_gui, renderer 
    except ImportError:
        pass
    
    try:
        from PyQt5 import QtWidgets as  qt_gui
        from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor as renderer
        return qt_gui, renderer 
    except ImportError:
        pass

    try:
        from PySide import QtGui as  qt_gui
        from vtk.qt4.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor as renderer
        return qt_gui, renderer 
    except ImportError:
        pass

    try:
        from PyQt4 import QtGui as  qt_gui
        from vtk.qt4.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor as renderer
        return qt_gui, renderer 
    except ImportError:
        pass

    raise ImportError("Could no import necessary modules. The VTK-OpenCASCADE viewer requires VTK and PySide2, PyQt5, PySide or PyQt4.")


import vtk
qt_gui, vtk_renderer = __import_qt_modules()


def get_QApplication(*args):
    try:
        from PySide2.QtWidgets import QApplication as qApp
        return qApp(args)
    except ImportError:
        pass

    try:
        from PyQt5.QtWidgets import QApplication as qApp
        return qApp(args)
    except ImportError:
        pass

    try:
        from PySide.QtGui import QApplication as qApp
        return qApp(args)
    except ImportError:
        pass

    try:
        from PyQt4.QtGui import QApplication as qApp
        return qApp(args)
    except ImportError:
        pass


    raise ImportError("Could not create the QApplication object.")


 
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(603, 553)
        self.centralWidget = qt_gui.QWidget(MainWindow)
        self.gridlayout = qt_gui.QGridLayout(self.centralWidget)
        self.vtkWidget = vtk_renderer(self.centralWidget)
        self.gridlayout.addWidget(self.vtkWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
 

class SimpleVtkViewer(qt_gui.QMainWindow):
    """
    SimpleVtkViewer uses a VTK QVTKRenderWindowInteractor to provide interactive
    rendeirng of VTK props in a QT window.  For keyboard and mouse interaction
    instructions see https://github.com/Kitware/VTK/blob/master/Wrapping/Python/vtk/qt4/QVTKRenderWindowInteractor.py.

    Note, it seems the 'a' key rather than the 'o' key activates object/actor mode 
    to enable interactive moving of rendered shapes.

    """
    
    def __init__(self, parent = None):
        qt_gui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ren = vtk.vtkRenderer()
        self.ui.vtkWidget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.ui.vtkWidget.GetRenderWindow().GetInteractor()

        self.axes = vtk.vtkAxesActor()
        self.add_actor(self.axes)
        self._axes_visible = True
        self.axes.SetConeRadius(0)

        self.show()
        self.iren.Initialize()


    def add_actor(self, actor):
        self.ren.AddActor(actor)
        self.iren.Render()

    def hide_actor(self, actor):
        self.ren.RemoveActor(actor)
        self.iren.Render()

    def clear_view(self):
        self.ren.RemoveAllViewProps()

        if self._axes_visible:
            self.show_axes()

    def show_axes(self):
        self.add_actor(self.axes)
        self._axes_visible = True

    def hide_axes(self):
        self.hide_actor(self.axes)
        self._axes_visible = False

    def refresh_view(self):
        self.iren.Render()
        


def create_test_actor():
    # Create source
    source = vtk.vtkSphereSource()
    source.SetCenter(0, 0, 0)
    source.SetRadius(5.0)

    # Create a mapper
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(source.GetOutputPort())

    # Create an actor
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    return actor