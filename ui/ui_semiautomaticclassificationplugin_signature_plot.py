# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_semiautomaticclassificationplugin_signature_plot.ui'
#
# Created: Sun Oct 16 12:02:58 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SpectralSignaturePlot(object):
    def setupUi(self, SpectralSignaturePlot):
        SpectralSignaturePlot.setObjectName(_fromUtf8("SpectralSignaturePlot"))
        SpectralSignaturePlot.resize(737, 557)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SpectralSignaturePlot.sizePolicy().hasHeightForWidth())
        SpectralSignaturePlot.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/semiautomaticclassificationplugin/semiautomaticclassificationplugin.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SpectralSignaturePlot.setWindowIcon(icon)
        self.gridLayout_21 = QtGui.QGridLayout(SpectralSignaturePlot)
        self.gridLayout_21.setObjectName(_fromUtf8("gridLayout_21"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.gridLayout_16 = QtGui.QGridLayout()
        self.gridLayout_16.setObjectName(_fromUtf8("gridLayout_16"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.signature_list_plot_tableWidget = QtGui.QTableWidget(SpectralSignaturePlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signature_list_plot_tableWidget.sizePolicy().hasHeightForWidth())
        self.signature_list_plot_tableWidget.setSizePolicy(sizePolicy)
        self.signature_list_plot_tableWidget.setMinimumSize(QtCore.QSize(0, 100))
        self.signature_list_plot_tableWidget.setMaximumSize(QtCore.QSize(16777215, 150))
        self.signature_list_plot_tableWidget.setEditTriggers(QtGui.QAbstractItemView.SelectedClicked)
        self.signature_list_plot_tableWidget.setObjectName(_fromUtf8("signature_list_plot_tableWidget"))
        self.signature_list_plot_tableWidget.setColumnCount(6)
        self.signature_list_plot_tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.signature_list_plot_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.signature_list_plot_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.signature_list_plot_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.signature_list_plot_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.signature_list_plot_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.signature_list_plot_tableWidget.setHorizontalHeaderItem(5, item)
        self.signature_list_plot_tableWidget.horizontalHeader().setDefaultSectionSize(50)
        self.signature_list_plot_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.signature_list_plot_tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.gridLayout_2.addWidget(self.signature_list_plot_tableWidget, 0, 0, 1, 1)
        self.gridLayout_16.addLayout(self.gridLayout_2, 1, 0, 1, 2)
        self.frame = QtGui.QFrame(SpectralSignaturePlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_18 = QtGui.QGridLayout(self.frame)
        self.gridLayout_18.setObjectName(_fromUtf8("gridLayout_18"))
        self.gridLayout_140 = QtGui.QGridLayout()
        self.gridLayout_140.setObjectName(_fromUtf8("gridLayout_140"))
        self.gridLayout_17 = QtGui.QGridLayout()
        self.gridLayout_17.setObjectName(_fromUtf8("gridLayout_17"))
        self.LCS_pointerButton_2 = QtGui.QToolButton(self.frame)
        self.LCS_pointerButton_2.setStyleSheet(_fromUtf8("margin: 0px;padding: 0px;"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin_LCS_threshold_set_tool.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LCS_pointerButton_2.setIcon(icon1)
        self.LCS_pointerButton_2.setIconSize(QtCore.QSize(22, 22))
        self.LCS_pointerButton_2.setObjectName(_fromUtf8("LCS_pointerButton_2"))
        self.gridLayout_17.addWidget(self.LCS_pointerButton_2, 0, 2, 1, 1)
        self.label_90 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_90.sizePolicy().hasHeightForWidth())
        self.label_90.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSans"))
        font.setBold(False)
        font.setWeight(50)
        self.label_90.setFont(font)
        self.label_90.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_90.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_90.setObjectName(_fromUtf8("label_90"))
        self.gridLayout_17.addWidget(self.label_90, 0, 1, 1, 1)
        self.gridLayout_144 = QtGui.QGridLayout()
        self.gridLayout_144.setObjectName(_fromUtf8("gridLayout_144"))
        self.LCS_cut_checkBox_2 = QtGui.QCheckBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LCS_cut_checkBox_2.sizePolicy().hasHeightForWidth())
        self.LCS_cut_checkBox_2.setSizePolicy(sizePolicy)
        self.LCS_cut_checkBox_2.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin_minus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LCS_cut_checkBox_2.setIcon(icon2)
        self.LCS_cut_checkBox_2.setObjectName(_fromUtf8("LCS_cut_checkBox_2"))
        self.gridLayout_144.addWidget(self.LCS_cut_checkBox_2, 1, 0, 1, 1)
        self.LCS_include_checkBox_2 = QtGui.QCheckBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LCS_include_checkBox_2.sizePolicy().hasHeightForWidth())
        self.LCS_include_checkBox_2.setSizePolicy(sizePolicy)
        self.LCS_include_checkBox_2.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin_plus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LCS_include_checkBox_2.setIcon(icon3)
        self.LCS_include_checkBox_2.setChecked(True)
        self.LCS_include_checkBox_2.setObjectName(_fromUtf8("LCS_include_checkBox_2"))
        self.gridLayout_144.addWidget(self.LCS_include_checkBox_2, 0, 0, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_144, 0, 3, 1, 1)
        self.gridLayout_19 = QtGui.QGridLayout()
        self.gridLayout_19.setObjectName(_fromUtf8("gridLayout_19"))
        self.label_91 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_91.sizePolicy().hasHeightForWidth())
        self.label_91.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSans"))
        font.setBold(False)
        font.setWeight(50)
        self.label_91.setFont(font)
        self.label_91.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_91.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_91.setObjectName(_fromUtf8("label_91"))
        self.gridLayout_19.addWidget(self.label_91, 0, 0, 1, 1)
        self.LCS_ROI_button_2 = QtGui.QToolButton(self.frame)
        self.LCS_ROI_button_2.setStyleSheet(_fromUtf8("margin: 0px;padding: 0px;"))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin_LCS_threshold_ROI_tool.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LCS_ROI_button_2.setIcon(icon4)
        self.LCS_ROI_button_2.setIconSize(QtCore.QSize(22, 22))
        self.LCS_ROI_button_2.setObjectName(_fromUtf8("LCS_ROI_button_2"))
        self.gridLayout_19.addWidget(self.LCS_ROI_button_2, 0, 1, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_19, 0, 0, 1, 1)
        self.gridLayout_140.addLayout(self.gridLayout_17, 2, 0, 1, 2)
        self.gridLayout_14 = QtGui.QGridLayout()
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.label_26 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSans"))
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet(_fromUtf8("background-color : qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #535353, stop:1 #a6a6a6); color : white"))
        self.label_26.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_26.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_26.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_14.addWidget(self.label_26, 0, 0, 1, 3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.gridLayout_20 = QtGui.QGridLayout()
        self.gridLayout_20.setObjectName(_fromUtf8("gridLayout_20"))
        self.set_min_max_Button = QtGui.QToolButton(self.frame)
        self.set_min_max_Button.setStyleSheet(_fromUtf8("margin: 0px;padding: 0px;"))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin_enter.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.set_min_max_Button.setIcon(icon5)
        self.set_min_max_Button.setIconSize(QtCore.QSize(22, 22))
        self.set_min_max_Button.setObjectName(_fromUtf8("set_min_max_Button"))
        self.gridLayout_20.addWidget(self.set_min_max_Button, 0, 1, 1, 1)
        self.label_102 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_102.sizePolicy().hasHeightForWidth())
        self.label_102.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSans"))
        font.setBold(False)
        font.setWeight(50)
        self.label_102.setFont(font)
        self.label_102.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_102.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_102.setObjectName(_fromUtf8("label_102"))
        self.gridLayout_20.addWidget(self.label_102, 0, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_20)
        self.label_101 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSans"))
        font.setBold(False)
        font.setWeight(50)
        self.label_101.setFont(font)
        self.label_101.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_101.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_101.setObjectName(_fromUtf8("label_101"))
        self.horizontalLayout_2.addWidget(self.label_101)
        self.multiplicative_threshold_doubleSpinBox_2 = QtGui.QDoubleSpinBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.multiplicative_threshold_doubleSpinBox_2.sizePolicy().hasHeightForWidth())
        self.multiplicative_threshold_doubleSpinBox_2.setSizePolicy(sizePolicy)
        self.multiplicative_threshold_doubleSpinBox_2.setDecimals(1)
        self.multiplicative_threshold_doubleSpinBox_2.setMaximum(10000.0)
        self.multiplicative_threshold_doubleSpinBox_2.setProperty("value", 1.0)
        self.multiplicative_threshold_doubleSpinBox_2.setObjectName(_fromUtf8("multiplicative_threshold_doubleSpinBox_2"))
        self.horizontalLayout_2.addWidget(self.multiplicative_threshold_doubleSpinBox_2)
        self.automatic_threshold_pushButton_2 = QtGui.QToolButton(self.frame)
        self.automatic_threshold_pushButton_2.setStyleSheet(_fromUtf8("margin: 0px;padding: 0px;"))
        self.automatic_threshold_pushButton_2.setIcon(icon5)
        self.automatic_threshold_pushButton_2.setIconSize(QtCore.QSize(22, 22))
        self.automatic_threshold_pushButton_2.setObjectName(_fromUtf8("automatic_threshold_pushButton_2"))
        self.horizontalLayout_2.addWidget(self.automatic_threshold_pushButton_2)
        self.undo_threshold_Button = QtGui.QToolButton(self.frame)
        self.undo_threshold_Button.setEnabled(False)
        self.undo_threshold_Button.setStyleSheet(_fromUtf8("margin: 0px;padding: 0px;"))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin_undo_lcs_threshold.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undo_threshold_Button.setIcon(icon6)
        self.undo_threshold_Button.setIconSize(QtCore.QSize(22, 22))
        self.undo_threshold_Button.setObjectName(_fromUtf8("undo_threshold_Button"))
        self.horizontalLayout_2.addWidget(self.undo_threshold_Button)
        self.gridLayout_14.addLayout(self.horizontalLayout_2, 1, 0, 1, 3)
        self.gridLayout_140.addLayout(self.gridLayout_14, 1, 0, 1, 2)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.remove_Signature_Button = QtGui.QToolButton(self.frame)
        self.remove_Signature_Button.setStyleSheet(_fromUtf8("margin: 0px;padding: 0px;"))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin_remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove_Signature_Button.setIcon(icon7)
        self.remove_Signature_Button.setIconSize(QtCore.QSize(22, 22))
        self.remove_Signature_Button.setObjectName(_fromUtf8("remove_Signature_Button"))
        self.gridLayout_4.addWidget(self.remove_Signature_Button, 0, 0, 1, 1)
        self.add_signature_list_pushButton = QtGui.QToolButton(self.frame)
        self.add_signature_list_pushButton.setStyleSheet(_fromUtf8("margin: 0px;padding: 0px;"))
        self.add_signature_list_pushButton.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin_save_plot.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_signature_list_pushButton.setIcon(icon8)
        self.add_signature_list_pushButton.setIconSize(QtCore.QSize(22, 22))
        self.add_signature_list_pushButton.setObjectName(_fromUtf8("add_signature_list_pushButton"))
        self.gridLayout_4.addWidget(self.add_signature_list_pushButton, 0, 1, 1, 1)
        self.calculate_spectral_distance_Button = QtGui.QToolButton(self.frame)
        self.calculate_spectral_distance_Button.setStyleSheet(_fromUtf8("margin: 0px;padding: 0px;"))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin_calculate_spectral_distances.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.calculate_spectral_distance_Button.setIcon(icon9)
        self.calculate_spectral_distance_Button.setIconSize(QtCore.QSize(22, 22))
        self.calculate_spectral_distance_Button.setObjectName(_fromUtf8("calculate_spectral_distance_Button"))
        self.gridLayout_4.addWidget(self.calculate_spectral_distance_Button, 0, 2, 1, 1)
        self.gridLayout_140.addLayout(self.gridLayout_4, 0, 0, 1, 2)
        self.gridLayout_18.addLayout(self.gridLayout_140, 0, 0, 1, 1)
        self.gridLayout_16.addWidget(self.frame, 1, 2, 1, 1)
        self.gridLayout_15 = QtGui.QGridLayout()
        self.gridLayout_15.setObjectName(_fromUtf8("gridLayout_15"))
        self.label_25 = QtGui.QLabel(SpectralSignaturePlot)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSans"))
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet(_fromUtf8("background-color : qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #535353, stop:1 #a6a6a6); color : white"))
        self.label_25.setFrameShape(QtGui.QFrame.Panel)
        self.label_25.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_25.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_15.addWidget(self.label_25, 0, 0, 1, 1)
        self.gridLayout_16.addLayout(self.gridLayout_15, 0, 0, 1, 3)
        self.gridLayout_5.addLayout(self.gridLayout_16, 1, 0, 1, 1)
        self.gridLayout_21.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.toolBox = QtGui.QToolBox(SpectralSignaturePlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setMinimumSize(QtCore.QSize(0, 300))
        self.toolBox.setFrameShape(QtGui.QFrame.StyledPanel)
        self.toolBox.setFrameShadow(QtGui.QFrame.Raised)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 717, 271))
        self.page.setObjectName(_fromUtf8("page"))
        self.gridLayout_8 = QtGui.QGridLayout(self.page)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.Sig_Widget = SigWidget2(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Sig_Widget.sizePolicy().hasHeightForWidth())
        self.Sig_Widget.setSizePolicy(sizePolicy)
        self.Sig_Widget.setObjectName(_fromUtf8("Sig_Widget"))
        self.gridLayout_3.addWidget(self.Sig_Widget, 0, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.band_lines_checkBox = QtGui.QCheckBox(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.band_lines_checkBox.sizePolicy().hasHeightForWidth())
        self.band_lines_checkBox.setSizePolicy(sizePolicy)
        self.band_lines_checkBox.setChecked(True)
        self.band_lines_checkBox.setObjectName(_fromUtf8("band_lines_checkBox"))
        self.gridLayout_7.addWidget(self.band_lines_checkBox, 0, 5, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem, 0, 7, 1, 1)
        self.label_8 = QtGui.QLabel(self.page)
        self.label_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_7.addWidget(self.label_8, 0, 8, 1, 1)
        self.plot_text_spinBox = QtGui.QSpinBox(self.page)
        self.plot_text_spinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.plot_text_spinBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.plot_text_spinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.plot_text_spinBox.setMinimum(1)
        self.plot_text_spinBox.setMaximum(100)
        self.plot_text_spinBox.setProperty("value", 15)
        self.plot_text_spinBox.setObjectName(_fromUtf8("plot_text_spinBox"))
        self.gridLayout_7.addWidget(self.plot_text_spinBox, 0, 9, 1, 1)
        self.gridLayout_13 = QtGui.QGridLayout()
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.value_label = QtGui.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Mono"))
        font.setBold(True)
        font.setWeight(75)
        self.value_label.setFont(font)
        self.value_label.setFrameShape(QtGui.QFrame.StyledPanel)
        self.value_label.setFrameShadow(QtGui.QFrame.Sunken)
        self.value_label.setObjectName(_fromUtf8("value_label"))
        self.gridLayout_13.addWidget(self.value_label, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem1, 0, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_13, 0, 11, 1, 1)
        self.value_range_pushButton = QtGui.QToolButton(self.page)
        self.value_range_pushButton.setStyleSheet(_fromUtf8("margin: 0px;padding: 0px;"))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin_sign_edit_range.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.value_range_pushButton.setIcon(icon10)
        self.value_range_pushButton.setIconSize(QtCore.QSize(22, 22))
        self.value_range_pushButton.setObjectName(_fromUtf8("value_range_pushButton"))
        self.gridLayout_7.addWidget(self.value_range_pushButton, 0, 2, 1, 1)
        self.fitToAxes_pushButton = QtGui.QToolButton(self.page)
        self.fitToAxes_pushButton.setStyleSheet(_fromUtf8("margin: 0px;padding: 0px;"))
        self.fitToAxes_pushButton.setText(_fromUtf8(""))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin_fit_plot.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fitToAxes_pushButton.setIcon(icon11)
        self.fitToAxes_pushButton.setIconSize(QtCore.QSize(22, 22))
        self.fitToAxes_pushButton.setObjectName(_fromUtf8("fitToAxes_pushButton"))
        self.gridLayout_7.addWidget(self.fitToAxes_pushButton, 0, 0, 1, 1)
        self.save_plot_pushButton = QtGui.QToolButton(self.page)
        self.save_plot_pushButton.setStyleSheet(_fromUtf8("margin: 0px;padding: 0px;"))
        self.save_plot_pushButton.setText(_fromUtf8(""))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin_save_plot_image.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_plot_pushButton.setIcon(icon12)
        self.save_plot_pushButton.setIconSize(QtCore.QSize(22, 22))
        self.save_plot_pushButton.setObjectName(_fromUtf8("save_plot_pushButton"))
        self.gridLayout_7.addWidget(self.save_plot_pushButton, 0, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem2, 0, 4, 1, 1)
        self.sigma_checkBox = QtGui.QCheckBox(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sigma_checkBox.sizePolicy().hasHeightForWidth())
        self.sigma_checkBox.setSizePolicy(sizePolicy)
        self.sigma_checkBox.setChecked(True)
        self.sigma_checkBox.setObjectName(_fromUtf8("sigma_checkBox"))
        self.gridLayout_7.addWidget(self.sigma_checkBox, 0, 3, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem3, 0, 10, 1, 1)
        self.grid_checkBox = QtGui.QCheckBox(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_checkBox.sizePolicy().hasHeightForWidth())
        self.grid_checkBox.setSizePolicy(sizePolicy)
        self.grid_checkBox.setChecked(True)
        self.grid_checkBox.setObjectName(_fromUtf8("grid_checkBox"))
        self.gridLayout_7.addWidget(self.grid_checkBox, 0, 6, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 1, 0, 1, 1)
        self.toolBox.addItem(self.page, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 717, 271))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.gridLayout_10 = QtGui.QGridLayout(self.page_2)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.gridLayout_9 = QtGui.QGridLayout()
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.value_textBrowser = QtGui.QTextBrowser(self.page_2)
        self.value_textBrowser.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.value_textBrowser.setObjectName(_fromUtf8("value_textBrowser"))
        self.gridLayout_9.addWidget(self.value_textBrowser, 0, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.toolBox.addItem(self.page_2, _fromUtf8(""))
        self.page_3 = QtGui.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 717, 271))
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.gridLayout_12 = QtGui.QGridLayout(self.page_3)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.gridLayout_11 = QtGui.QGridLayout()
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.distance_textBrowser = QtGui.QTextBrowser(self.page_3)
        self.distance_textBrowser.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.distance_textBrowser.setObjectName(_fromUtf8("distance_textBrowser"))
        self.gridLayout_11.addWidget(self.distance_textBrowser, 0, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_11, 0, 0, 1, 1)
        self.toolBox.addItem(self.page_3, _fromUtf8(""))
        self.gridLayout_6.addWidget(self.toolBox, 0, 0, 1, 1)
        self.gridLayout_21.addLayout(self.gridLayout_6, 1, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_21.addLayout(self.gridLayout, 2, 0, 1, 1)

        self.retranslateUi(SpectralSignaturePlot)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SpectralSignaturePlot)

    def retranslateUi(self, SpectralSignaturePlot):
        SpectralSignaturePlot.setWindowTitle(_translate("SpectralSignaturePlot", "SCP: Spectral Signature Plot", None))
        self.signature_list_plot_tableWidget.setSortingEnabled(True)
        item = self.signature_list_plot_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SpectralSignaturePlot", "S", None))
        item = self.signature_list_plot_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("SpectralSignaturePlot", "MC ID", None))
        item = self.signature_list_plot_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("SpectralSignaturePlot", "MC Info", None))
        item = self.signature_list_plot_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("SpectralSignaturePlot", "C ID", None))
        item = self.signature_list_plot_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("SpectralSignaturePlot", "C Info", None))
        item = self.signature_list_plot_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("SpectralSignaturePlot", "Color", None))
        self.LCS_pointerButton_2.setToolTip(_translate("SpectralSignaturePlot", "<html><head/><body><p>Activate pointer for setting thresholds from pixel</p></body></html>", None))
        self.label_90.setText(_translate("SpectralSignaturePlot", "From pixel", None))
        self.LCS_cut_checkBox_2.setToolTip(_translate("SpectralSignaturePlot", "<html><head/><body><p>If checked, signature threshold is reduced to exclude pixel signature</p></body></html>", None))
        self.LCS_include_checkBox_2.setToolTip(_translate("SpectralSignaturePlot", "<html><head/><body><p>If checked, signature threshold is extended to include pixel signature</p></body></html>", None))
        self.label_91.setText(_translate("SpectralSignaturePlot", "From ROI", None))
        self.LCS_ROI_button_2.setToolTip(_translate("SpectralSignaturePlot", "<html><head/><body><p>Set thresholds from temporary ROI</p></body></html>", None))
        self.label_26.setText(_translate("SpectralSignaturePlot", "Automatic  thresholds", None))
        self.set_min_max_Button.setToolTip(_translate("SpectralSignaturePlot", "<html><head/><body><p>Set automatic threshold Min Max</p></body></html>", None))
        self.label_102.setText(_translate("SpectralSignaturePlot", "Min Max", None))
        self.label_101.setText(_translate("SpectralSignaturePlot", "σ *", None))
        self.multiplicative_threshold_doubleSpinBox_2.setToolTip(_translate("SpectralSignaturePlot", "<html><head/><body><p>Set a value that will be multiplied by standard deviation</p></body></html>", None))
        self.automatic_threshold_pushButton_2.setToolTip(_translate("SpectralSignaturePlot", "<html><head/><body><p>Set automatic threshold σ</p></body></html>", None))
        self.undo_threshold_Button.setToolTip(_translate("SpectralSignaturePlot", "<html><head/><body><p>Undo thresholds</p></body></html>", None))
        self.undo_threshold_Button.setText(_translate("SpectralSignaturePlot", "Import library", None))
        self.remove_Signature_Button.setToolTip(_translate("SpectralSignaturePlot", "<html><head/><body><p >Delete row</p></body></html>", None))
        self.remove_Signature_Button.setText(_translate("SpectralSignaturePlot", "Plot", None))
        self.add_signature_list_pushButton.setToolTip(_translate("SpectralSignaturePlot", "<html><head/><body><p>Add highlighted spectral signatures to signature list</p></body></html>", None))
        self.calculate_spectral_distance_Button.setToolTip(_translate("SpectralSignaturePlot", "<html><head/><body><p>Calculate spectral distances</p></body></html>", None))
        self.calculate_spectral_distance_Button.setText(_translate("SpectralSignaturePlot", "Plot", None))
        self.label_25.setText(_translate("SpectralSignaturePlot", " Signature list", None))
        self.band_lines_checkBox.setToolTip(_translate("SpectralSignaturePlot", "<html><head/><body><p>Plot the value range (standard deviation or defined minimum and maximum) for each signature</p></body></html>", None))
        self.band_lines_checkBox.setText(_translate("SpectralSignaturePlot", "Band lines", None))
        self.label_8.setText(_translate("SpectralSignaturePlot", "Max characters", None))
        self.plot_text_spinBox.setToolTip(_translate("SpectralSignaturePlot", "<html><head/><body><p align=\"justify\">Text lenght of names in the spectral plot legend</p></body></html>", None))
        self.value_label.setText(_translate("SpectralSignaturePlot", "x=0.000000 y=0.000000", None))
        self.value_range_pushButton.setToolTip(_translate("SpectralSignaturePlot", "<html><head/><body><p>Change value range interactively in the plot</p></body></html>", None))
        self.fitToAxes_pushButton.setToolTip(_translate("SpectralSignaturePlot", "<html><head/><body><p>Automatically fit the plot to data</p></body></html>", None))
        self.save_plot_pushButton.setToolTip(_translate("SpectralSignaturePlot", "<html><head/><body><p>Save the plot to file (jpg, png, pdf)</p></body></html>", None))
        self.sigma_checkBox.setToolTip(_translate("SpectralSignaturePlot", "<html><head/><body><p>Plot the value range (standard deviation or defined minimum and maximum) for each signature</p></body></html>", None))
        self.sigma_checkBox.setText(_translate("SpectralSignaturePlot", "Plot value range", None))
        self.grid_checkBox.setToolTip(_translate("SpectralSignaturePlot", "<html><head/><body><p>Plot the value range (standard deviation or defined minimum and maximum) for each signature</p></body></html>", None))
        self.grid_checkBox.setText(_translate("SpectralSignaturePlot", "Grid", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("SpectralSignaturePlot", "Plot", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("SpectralSignaturePlot", "Signature details", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("SpectralSignaturePlot", "Spectral distances", None))

from sigwidget2 import SigWidget2
import resources_rc
