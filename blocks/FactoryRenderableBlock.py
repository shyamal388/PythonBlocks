#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      A21059
#
# Created:     06/03/2015
# Copyright:   (c) A21059 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from PyQt4 import QtGui
from blocks.RenderableBlock import RenderableBlock
from blocks.BlockUtilities import BlockUtilities
from blocks.Block import Block

class FactoryRenderableBlock(RenderableBlock):
    factoryRBs = {}
    
    def __init__(self,workspaceWidget ):
        RenderableBlock.__init__(self, workspaceWidget)
        

    @classmethod
    def from_block(cls, workspaceWidget, block, isLoading=False,back_color=QtGui.QColor(225,225,225,255)):
        obj = super(FactoryRenderableBlock, cls).from_block(workspaceWidget,block,False, back_color)
        obj.setBlockLabelUneditable()
        obj.createdRB = None
        obj.createdRB_dragged = False
        obj.child_list = []

        return  obj
     
    @classmethod     
    def from_blockID(cls, workspaceWidget, blockID, isLoading=False,back_color=QtGui.QColor(225,225,225,255)):
        return FactoryRenderableBlock.from_block(workspaceWidget,Block.getBlock(blockID),False, back_color)
     
     
    def createNewInstance(self):
        rb = BlockUtilities.cloneBlock(Block.getBlock(self.blockID), self.workspace.getActiveCanvas() )
        self.child_list.append(rb)
        rb.factoryRB = self
        return rb


    def mousePressEvent(self, event):

        if(self.workspaceWidget == None): return

        self.workspace.factory.OnPressed(self.workspace.factory.active_button)        
        self.createdRB = self.createNewInstance()
        self.createdRB.setParent(self.createdRB.workspaceWidget.canvas)
        self.createdRB.move(
            self.x()+self.workspace.getActiveCanvas().horizontalScrollBar().value()-5, 
            self.y()+self.workspace.getActiveCanvas().verticalScrollBar().value()+2);
        self.createdRB.onMousePress(event);
        self.mouseDragged(event); # immediately make the RB appear under the mouse cursor

    def mouseReleaseEvent(self, event):
        if(self.createdRB != None):
            if(not self.createdRB_dragged):
                self.createdRB.setParent(None);
            else:
                self.createdRB.mouseReleaseEvent(event);

        self.createdRB_dragged = False;

    def mouseMoveEvent(self, event):
        if(self.createdRB != None):
            self.createdRB.mouseMoveEvent(event);


    def mouseDragged(self, event):
        if(self.createdRB != None):
            self.createdRB.mouseDragged(event);
            self.createdRB_dragged = True;
