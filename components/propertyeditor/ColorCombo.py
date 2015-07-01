
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class ColorCombo(QComboBox):
  def __init__(self, parent):
    super(ColorCombo, self).__init__(parent)
    colorNames = QColor.colorNames();
    self.m_init = QColor(0, 0, 255)
    index = 0
    for name in  colorNames:
      color = QColor(name);
      self.insertItem(index, name);
      self.setItemData(index, color, Qt.DecorationRole);
      index += 1
    self.addItem("Custom", QVariant.UserType);
    #self.connect(self, QtCore.SIGNAL("currentIndexChanged(int)"), self, SLOT(self.currentChanged));
    self.currentIndexChanged[int].connect(self.IndexChanged)
    
  def color(self):
    print(self.currentIndex())
    return self.itemData(self.currentIndex(), Qt.DecorationRole);


  def setColor(self, color):
    self.m_init = color;
    self.setCurrentIndex(self.findData(color,Qt.DecorationRole));
    if (self.currentIndex() == -1):
      self.addItem(color.name());
      self.setItemData(self.count()-1, color, Qt.DecorationRole);
      self.setCurrentIndex(self.count()-1);


  def IndexChanged(self,  index):
    print(index)
    if (self.itemData(index) == QVariant.UserType):

      color = QColorDialog.getColor(self.m_init, self);		
      if (color.isValid()):
        if (self.findData(color, Qt.DecorationRole) == -1):
          self.addItem(color.name());
          self.setItemData(self.count()-1, color, Qt.DecorationRole);
        self.setColor(color)
      else:
        self.setCurrentIndex(self.findData(self.m_init));

  
