from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import skfuzzy as fuzz
import skfuzzy.membership as mf
import matplotlib.pyplot as plt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 340)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.btnCalc = QtWidgets.QPushButton(self.centralwidget)
        self.btnCalc.setGeometry(QtCore.QRect(200, 290, 75, 23))
        self.btnCalc.setObjectName("btnCalc")

        # self.btnGraph = QtWidgets.QPushButton(self.centralwidget)
        # self.btnGraph.setGeometry(QtCore.QRect(270, 290, 75, 23))
        # self.btnGraph.setObjectName("btnGraph")

        self.grpInputBox = QtWidgets.QGroupBox(self.centralwidget)
        self.grpInputBox.setGeometry(QtCore.QRect(50, 20, 480, 211))
        self.grpInputBox.setObjectName("grpInputBox")

        self.lblAge = QtWidgets.QLabel(self.grpInputBox)
        self.lblAge.setGeometry(QtCore.QRect(10, 20, 300, 13))
        self.lblAge.setObjectName("lblAge")

        self.lblBloodPressure = QtWidgets.QLabel(self.grpInputBox)
        self.lblBloodPressure.setGeometry(QtCore.QRect(10, 50, 300, 16))
        self.lblBloodPressure.setObjectName("lblBloodPressure")

        self.lblCholesterol = QtWidgets.QLabel(self.grpInputBox)
        self.lblCholesterol.setGeometry(QtCore.QRect(10, 80, 300, 16))
        self.lblCholesterol.setObjectName("lblCholesterol")

        self.lblBloodSugar = QtWidgets.QLabel(self.grpInputBox)
        self.lblBloodSugar.setGeometry(QtCore.QRect(10, 110, 300, 16))
        self.lblBloodSugar.setObjectName("lblBloodSugar")

        self.lblHDL = QtWidgets.QLabel(self.grpInputBox)
        self.lblHDL.setGeometry(QtCore.QRect(10, 140, 300, 16))
        self.lblHDL.setObjectName("lblHDL")

        self.lblLDL = QtWidgets.QLabel(self.grpInputBox)
        self.lblLDL.setGeometry(QtCore.QRect(10, 170, 300, 16))
        self.lblLDL.setObjectName("lblLDL")

        self.iptAge = QtWidgets.QLineEdit(self.grpInputBox)
        self.iptAge.setGeometry(QtCore.QRect(350, 20, 113, 20))
        self.iptAge.setObjectName("iptAge")

        self.iptBP = QtWidgets.QLineEdit(self.grpInputBox)
        self.iptBP.setGeometry(QtCore.QRect(350, 50, 113, 20))
        self.iptBP.setObjectName("iptBP")

        self.iptCholesterol = QtWidgets.QLineEdit(self.grpInputBox)
        self.iptCholesterol.setGeometry(QtCore.QRect(350, 80, 113, 20))
        self.iptCholesterol.setObjectName("iptCholesterol")

        self.iptBloodSugar = QtWidgets.QLineEdit(self.grpInputBox)
        self.iptBloodSugar.setGeometry(QtCore.QRect(350, 110, 113, 20))
        self.iptBloodSugar.setObjectName("iptBloodSugar")

        self.iptHDL = QtWidgets.QLineEdit(self.grpInputBox)
        self.iptHDL.setGeometry(QtCore.QRect(350, 140, 113, 20))
        self.iptHDL.setObjectName("iptHDL")

        self.iptLDL = QtWidgets.QLineEdit(self.grpInputBox)
        self.iptLDL.setGeometry(QtCore.QRect(350, 170, 113, 20))
        self.iptLDL.setObjectName("iptLDL")

        self.lblRisk = QtWidgets.QLabel(self.centralwidget)
        self.lblRisk.setGeometry(QtCore.QRect(140, 250, 47, 13))
        self.lblRisk.setObjectName("lblRisk")

        self.optRisk = QtWidgets.QLineEdit(self.centralwidget)
        self.optRisk.setGeometry(QtCore.QRect(250, 250, 113, 20))
        self.optRisk.setReadOnly(True)
        self.optRisk.setObjectName("optRisk")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # self.btnGraph.clicked.connect(self.showGraph)
        self.btnCalc.clicked.connect(self.showGraph)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # def showRisk(self):
    #     defuzzified = defuzzResult

    def showGraph(self):
        # Set the range for each
        x_age = np.arange(0, 101, 1)
        x_bloodPressure = np.arange(0, 221, 1)
        x_cholesterol = np.arange(100, 251, 1)
        x_bloodSugar = np.arange(0, 121, 1)
        x_hdl = np.arange(0, 71, 1)
        x_ldl = np.arange(0, 191, 1)
        y_risk = np.arange(0, 46, 1)

        # Trapezium and triangle
        age_young = mf.trapmf(x_age, [-40, -5, 30, 40])
        age_mid = mf.trapmf(x_age, [30, 40, 50, 60])
        age_old = mf.trapmf(x_age, [50, 60, 100, 100])

        bloodPressure_low = mf.trapmf(x_bloodPressure, [-40, -5, 100, 120])
        bloodPressure_mid = mf.trapmf(x_bloodPressure, [100, 120, 140, 160])
        bloodPressure_high = mf.trapmf(x_bloodPressure, [140, 160, 180, 200])
        bloodPressure_veryHigh = mf.trapmf(x_bloodPressure, [180, 200, 220, 220])

        cholesterol_low = mf.trapmf(x_cholesterol, [-40, -5, 180, 200])
        cholesterol_mid = mf.trapmf(x_cholesterol, [180, 200, 220, 240])
        cholesterol_high = mf.trapmf(x_cholesterol, [220, 240, 250, 270])

        bloodSugar_veryHigh = mf.trimf(x_bloodSugar, [90, 120, 130])

        hdl_low = mf.trapmf(x_hdl, [0, 0, 30, 40])
        hdl_mid = mf.trapmf(x_hdl, [30, 40, 50, 60])
        hdl_high = mf.trapmf(x_hdl, [50, 60, 80, 80])

        ldl_normal = mf.trimf(x_ldl, [0, 0, 100, ])
        ldl_limit = mf.trimf(x_ldl, [100, 130, 160, ])
        ldl_high = mf.trimf(x_ldl, [130, 160, 190, ])
        ldl_veryHigh = mf.trapmf(x_ldl, [160, 190, 200, 200])

        risk_not = mf.trapmf(y_risk, [0, 0, 5, 10])
        risk_little = mf.trapmf(y_risk, [5, 10, 15, 20])
        risk_mid = mf.trapmf(y_risk, [15, 20, 25, 30])
        risk_high = mf.trapmf(y_risk, [25, 30, 35, 40])
        risk_veryHigh = mf.trapmf(y_risk, [35, 40, 45, 50])

        # Fuzzification
        age_fit_young = fuzz.interp_membership(x_age, age_young, float(self.iptAge.text()))
        age_fit_mid = fuzz.interp_membership(x_age, age_mid, float(self.iptAge.text()))
        age_fit_old = fuzz.interp_membership(x_age, age_old, float(self.iptAge.text()))

        bloodPressure_fit_low = fuzz.interp_membership(x_bloodPressure, bloodPressure_low, float(self.iptBP.text()))
        bloodPressure_fit_mid = fuzz.interp_membership(x_bloodPressure, bloodPressure_mid, float(self.iptBP.text()))
        bloodPressure_fit_high = fuzz.interp_membership(x_bloodPressure, bloodPressure_high, float(self.iptBP.text()))
        bloodPressure_fit_veryHigh = fuzz.interp_membership(x_bloodPressure, bloodPressure_veryHigh, float(self.iptBP.text()))

        cholesterol_fit_low = fuzz.interp_membership(x_cholesterol, cholesterol_low, float(self.iptCholesterol.text()))
        cholesterol_fit_mid = fuzz.interp_membership(x_cholesterol, cholesterol_mid, float(self.iptCholesterol.text()))
        cholesterol_fit_high = fuzz.interp_membership(x_cholesterol, cholesterol_high, float(self.iptCholesterol.text()))

        bloodSugar_fit_veryHigh = fuzz.interp_membership(x_bloodSugar, bloodSugar_veryHigh, float(self.iptBloodSugar.text()))

        ldl_fit_normal = fuzz.interp_membership(x_ldl, ldl_normal, float(self.iptLDL.text()))
        ldl_fit_limit = fuzz.interp_membership(x_ldl, ldl_limit, float(self.iptLDL.text()))
        ldl_fit_high = fuzz.interp_membership(x_ldl, ldl_high, float(self.iptLDL.text()))
        ldl_fit_veryHigh = fuzz.interp_membership(x_ldl, ldl_veryHigh, float(self.iptLDL.text()))

        hdl_fit_low = fuzz.interp_membership(x_hdl, hdl_low, float(self.iptHDL.text()))
        hdl_fit_mid = fuzz.interp_membership(x_hdl, hdl_mid, float(self.iptHDL.text()))
        hdl_fit_high = fuzz.interp_membership(x_hdl, hdl_high, float(self.iptHDL.text()))

        # ***************************************Fuzzy graph visualization**************************************************
        fig, (ax0) = plt.subplots(nrows=1, figsize=(10, 25))
        fig, (ax1) = plt.subplots(nrows=1, figsize=(10, 25))
        fig, (ax2) = plt.subplots(nrows=1, figsize=(10, 25))
        fig, (ax3) = plt.subplots(nrows=1, figsize=(10, 25))
        fig, (ax4) = plt.subplots(nrows=1, figsize=(10, 25))
        fig, (ax5) = plt.subplots(nrows=1, figsize=(10, 25))
        fig, (ax6) = plt.subplots(nrows=1, figsize=(10, 25))
        # fig, (ax5) = plt.subplots(nrows = 1, figsize =(10, 25))

        ax0.set_xlim([0, 100])
        ax0.set_ylim([0, 1.1])
        ax1.set_xlim([0, 220])
        ax1.set_ylim([0, 1.1])
        ax2.set_xlim([100, 250])
        ax2.set_ylim([0, 1.1])
        ax3.set_xlim([0, 120])
        ax3.set_ylim([0, 1.1])
        ax4.set_xlim([0, 70])
        ax4.set_ylim([0, 1.1])
        ax5.set_xlim([0, 190])
        ax5.set_ylim([0, 1.1])
        ax6.set_xlim([0, 45])
        ax6.set_ylim([0, 1.1])

        # -------------------------------------Age Plot-------------------------------------
        ax0.plot(x_age, age_young, 'b', linewidth=2, label='Young')
        ax0.plot(x_age, age_mid, 'g', linewidth=2, label='Middle')
        ax0.plot(x_age, age_old, 'r', linewidth=2, label='Old')

        # ax0.axvline(x=float(self.iptAge.text()), color='black', linewidth=1.0, linestyle='--')
        # ax0.text(float(self.iptAge.text()), -0.1, float(self.iptAge.text()), color='red', ha='center')
        #
        # ax0.axhline(y=age_fit_young, color='black', linewidth=1.0, linestyle='--')
        # ax0.text(4, age_fit_young, round(age_fit_young, 2), ha='left', va='bottom', color='red')
        #
        # ax0.axhline(y=age_fit_mid, color='black', linewidth=1.0, linestyle='--')
        # ax0.text(4, age_fit_mid, round(age_fit_mid, 2), ha='left', va='bottom', color='red')
        #
        # ax0.axhline(y=age_fit_old, color='black', linewidth=1.0, linestyle='--')
        # ax0.text(4, age_fit_old, round(age_fit_old, 2), ha='left', va='bottom', color='red')

        ax0.set_ylabel("Membership values")
        ax0.set_xlabel("Age/ years")
        ax0.set_title('Age')
        ax0.legend()

        # -------------------------------------Blood Pressure Plot-------------------------------------
        ax1.plot(x_bloodPressure, bloodPressure_low, 'b', linewidth=2, label='Low')
        ax1.plot(x_bloodPressure, bloodPressure_mid, 'g', linewidth=2, label='Middle')
        ax1.plot(x_bloodPressure, bloodPressure_high, 'r', linewidth=2, label='High')
        ax1.plot(x_bloodPressure, bloodPressure_veryHigh, 'c', linewidth=2, label='Very High')

        # ax1.axvline(x=float(self.iptBP.text()), color='black', linewidth=1.0, linestyle='--')
        # ax1.text(float(self.iptBP.text()), -0.1, float(self.iptAge.text()), color='red', ha='center')
        #
        # ax1.axhline(y=bloodPressure_fit_low, color='black', linewidth=1.0, linestyle='--')
        # ax1.text(5, bloodPressure_fit_low, round(bloodPressure_fit_low, 2), ha='left', va='bottom', color='red')
        #
        # ax1.axhline(y=bloodPressure_fit_mid, color='black', linewidth=1.0, linestyle='--')
        # ax1.text(5, bloodPressure_fit_mid, round(bloodPressure_fit_mid, 2), ha='left', va='bottom', color='red')
        #
        # ax1.axhline(y=bloodPressure_fit_high, color='black', linewidth=1.0, linestyle='--')
        # ax1.text(5, bloodPressure_fit_high, round(bloodPressure_fit_high, 2), ha='left', va='bottom', color='red')
        #
        # ax1.axhline(y=bloodPressure_fit_veryHigh, color='black', linewidth=1.0, linestyle='--')
        # ax1.text(5, bloodPressure_fit_veryHigh, round(bloodPressure_fit_veryHigh, 2), ha='left', va='bottom', color='red')

        ax1.set_ylabel("Membership values")
        ax1.set_xlabel("BLood Pressure/ mmHg")
        ax1.set_title('Blood Pressure')
        ax1.legend()

        # -------------------------------------Cholesterol Plot-------------------------------------
        ax2.plot(x_cholesterol, cholesterol_low, 'b', linewidth=2, label='Low')
        ax2.plot(x_cholesterol, cholesterol_mid, 'g', linewidth=2, label='Middle')
        ax2.plot(x_cholesterol, cholesterol_high, 'r', linewidth=2, label='High')

        # ax2.axvline(x=float(self.iptCholesterol.text()), color='black', linewidth=1.0, linestyle='--')
        # ax2.text(float(self.iptCholesterol.text()), -0.1, float(self.iptAge.text()), color='red', ha='center')
        #
        # ax2.axhline(y=cholesterol_fit_low, color='black', linewidth=1.0, linestyle='--')
        # ax2.text(103, cholesterol_fit_low, round(cholesterol_fit_low, 2), ha='left', va='bottom', color='red')
        #
        # ax2.axhline(y=cholesterol_fit_mid, color='black', linewidth=1.0, linestyle='--')
        # ax2.text(103, cholesterol_fit_mid, round(cholesterol_fit_mid, 2), ha='left', va='bottom', color='red')
        #
        # ax2.axhline(y=cholesterol_fit_high, color='black', linewidth=1.0, linestyle='--')
        # ax2.text(103, cholesterol_fit_high, round(cholesterol_fit_high, 2), ha='left', va='bottom', color='red')

        ax2.set_ylabel("Membership values")
        ax2.set_xlabel("Cholesterol/ mmol/L")
        ax2.set_title('Cholesterol')
        ax2.legend()

        # -------------------------------------Blood Sugar Plot-------------------------------------
        ax3.plot(x_bloodSugar, bloodSugar_veryHigh, 'b', linewidth=2, label='Very High')

        # ax3.axvline(x=float(self.iptBloodSugar.text()), color='black', linewidth=1.0, linestyle='--')
        # ax3.text(float(self.iptBloodSugar.text()), -0.1, float(self.iptAge.text()), color='red', ha='center')
        #
        # ax3.axhline(y=bloodSugar_fit_veryHigh, color='black', linewidth=1.0, linestyle='--')
        # ax3.text(4, bloodSugar_fit_veryHigh, round(bloodSugar_fit_veryHigh, 2), ha='left', va='bottom', color='red')

        ax3.set_ylabel("Membership values")
        ax3.set_xlabel("Sugar/ mmol/L")
        ax3.set_title('Blood Sugar')
        ax3.legend()

        # -------------------------------------HDL Plot-------------------------------------
        ax4.plot(x_hdl, hdl_low, 'b', linewidth=2, label='Low')
        ax4.plot(x_hdl, hdl_mid, 'g', linewidth=2, label='Middle')
        ax4.plot(x_hdl, hdl_high, 'r', linewidth=2, label='High')

        # ax4.axvline(x=float(self.iptHDL.text()), color='black', linewidth=1.0, linestyle='--')
        # ax4.text(float(self.iptHDL.text()), -0.1, float(self.iptAge.text()), color='red', ha='center')
        #
        # ax4.axhline(y=hdl_fit_low, color='black', linewidth=1.0, linestyle='--')
        # ax4.text(4, hdl_fit_low, round(hdl_fit_low, 2), ha='left', va='bottom', color='red')
        #
        # ax4.axhline(y=hdl_fit_mid, color='black', linewidth=1.0, linestyle='--')
        # ax4.text(4, hdl_fit_mid, round(hdl_fit_mid, 2), ha='left', va='bottom', color='red')
        #
        # ax4.axhline(y=hdl_fit_high, color='black', linewidth=1.0, linestyle='--')
        # ax4.text(4, hdl_fit_high, round(hdl_fit_high, 2), ha='left', va='bottom', color='red')

        ax4.set_ylabel("Membership values")
        ax4.set_xlabel("HDL/ mmol/L")
        ax4.set_title('HDL')
        ax4.legend()

        # -------------------------------------LDL Plot-------------------------------------
        ax5.plot(x_ldl, ldl_normal, 'b', linewidth=2, label='Normal')
        ax5.plot(x_ldl, ldl_limit, 'g', linewidth=2, label='Limit')
        ax5.plot(x_ldl, ldl_high, 'r', linewidth=2, label='High')
        ax5.plot(x_ldl, ldl_veryHigh, 'c', linewidth=2, label='Very High')

        # ax5.axvline(x=float(self.iptLDL.text()), color='black', linewidth=1.0, linestyle='--')
        # ax5.text(float(self.iptLDL.text()), -0.1, float(self.iptAge.text()), color='red', ha='center')
        #
        # ax5.axhline(y=ldl_fit_normal, color='black', linewidth=1.0, linestyle='--')
        # ax5.text(5, ldl_fit_normal, round(ldl_fit_normal, 2), ha='left', va='bottom', color='red')
        #
        # ax5.axhline(y=ldl_fit_limit, color='black', linewidth=1.0, linestyle='--')
        # ax5.text(5, ldl_fit_limit, round(ldl_fit_limit, 2), ha='left', va='bottom', color='red')
        #
        # ax5.axhline(y=ldl_fit_high, color='black', linewidth=1.0, linestyle='--')
        # ax5.text(5, ldl_fit_high, round(ldl_fit_high, 2), ha='left', va='bottom', color='red')
        #
        # ax5.axhline(y=ldl_fit_veryHigh, color='black', linewidth=1.0, linestyle='--')
        # ax5.text(5, ldl_fit_veryHigh, round(ldl_fit_veryHigh, 2), ha='left', va='bottom', color='red')

        ax5.set_ylabel("Membership values")
        ax5.set_xlabel("LDL/ mmol/L")
        ax5.set_title('LDL')
        ax5.legend()

        # -------------------------------------Risk Plot-------------------------------------
        ax6.plot(y_risk, risk_not, 'b', linewidth=2, label='Not')
        ax6.plot(y_risk, risk_little, 'g', linewidth=2, label='Little')
        ax6.plot(y_risk, risk_mid, 'r', linewidth=2, label='Middle')
        ax6.plot(y_risk, risk_high, 'c', linewidth=2, label='High')
        ax6.plot(y_risk, risk_veryHigh, 'm', linewidth=2, label='Very High')

        ax6.set_ylabel("Membership values")
        ax6.set_xlabel("Risk value")
        ax6.set_title('Risk')
        ax6.legend()

        plt.tight_layout()
        # ***************************************Endf of Fuzzy graph visualization**************************************************

        # *******************************************RULES******************************************************************************
        rule1 = np.fmin(np.fmin(np.fmin(np.fmin(bloodPressure_fit_low, cholesterol_fit_low), ldl_fit_normal), hdl_fit_high), risk_not)
        rule2 = np.fmin(np.fmin(np.fmin(np.fmin(bloodPressure_fit_low, cholesterol_fit_low), ldl_fit_limit), hdl_fit_high), risk_little)
        rule3 = np.fmin(np.fmin(np.fmin(np.fmin(bloodPressure_fit_low, cholesterol_fit_low), ldl_fit_high), hdl_fit_high), risk_mid)
        rule4 = np.fmin(np.fmin(np.fmin(np.fmin(bloodPressure_fit_low, cholesterol_fit_low), ldl_fit_veryHigh), hdl_fit_high), risk_high)
        rule5 = np.fmin(np.fmin(np.fmin(bloodPressure_fit_mid, cholesterol_fit_low), hdl_fit_high), risk_not)

        rule6 = np.fmin(np.fmin(np.fmin(age_fit_young, bloodPressure_fit_mid), cholesterol_fit_mid), risk_not)
        rule7 = np.fmin(np.fmin(np.fmin(age_fit_mid, bloodPressure_fit_mid), cholesterol_fit_mid), risk_not)
        rule8 = np.fmin(np.fmin(np.fmin(age_fit_old, bloodPressure_fit_mid), cholesterol_fit_mid), risk_not)
        rule9 = np.fmin(np.fmin(np.fmin(age_fit_young, bloodPressure_fit_high), cholesterol_fit_high), risk_mid)
        rule10 = np.fmin(np.fmin(np.fmin(age_fit_mid, bloodPressure_fit_high), cholesterol_fit_high), risk_high)
        rule11 = np.fmin(np.fmin(np.fmin(age_fit_old, bloodPressure_fit_high), cholesterol_fit_high), risk_veryHigh)

        rule12 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(age_fit_young, bloodPressure_fit_mid), cholesterol_fit_low), ldl_fit_normal), hdl_fit_low), risk_not)
        rule13 = np.fmin(np.fmin(age_fit_young, bloodSugar_fit_veryHigh), risk_little)
        rule14 = np.fmin(np.fmin(age_fit_mid, bloodSugar_fit_veryHigh), risk_high)
        rule15 = np.fmin(np.fmin(age_fit_old, bloodSugar_fit_veryHigh), risk_veryHigh)
        rule16 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(age_fit_young, bloodPressure_fit_low), cholesterol_fit_low), bloodSugar_fit_veryHigh), ldl_fit_normal), hdl_fit_high), risk_little)
        rule17 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(age_fit_mid, bloodPressure_fit_low), cholesterol_fit_low), bloodSugar_fit_veryHigh), ldl_fit_normal), hdl_fit_high), risk_high)
        rule18 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(age_fit_old, bloodPressure_fit_low), cholesterol_fit_low), bloodSugar_fit_veryHigh), ldl_fit_normal), hdl_fit_high), risk_veryHigh)
        rule19 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(age_fit_mid, bloodPressure_fit_low), cholesterol_fit_low), bloodSugar_fit_veryHigh), ldl_fit_veryHigh), hdl_fit_high), risk_veryHigh)

        rule20 = np.fmin(np.fmin(np.fmin(np.fmin(bloodPressure_fit_veryHigh, cholesterol_fit_high), ldl_fit_veryHigh), hdl_fit_high), risk_veryHigh)
        rule21 = np.fmin(np.fmin(np.fmin(np.fmin(bloodPressure_fit_high, cholesterol_fit_high), ldl_fit_high), hdl_fit_mid), risk_veryHigh)
        rule22 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(age_fit_young, bloodPressure_fit_veryHigh), cholesterol_fit_high), ldl_fit_veryHigh), hdl_fit_mid), risk_mid)
        rule23 = np.fmin(np.fmin(age_fit_mid, bloodPressure_fit_veryHigh), risk_veryHigh)
        rule24 = np.fmin(np.fmin(age_fit_old, bloodPressure_fit_veryHigh), risk_veryHigh)
        # ********************************************************END OF RULES***********************************************************************

        # MAMDANI
        out_not = np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(rule1, rule5), rule6), rule7), rule8), rule12)
        out_little = np.fmax(np.fmax(rule2, rule13), rule16)
        out_mid = np.fmax(np.fmax(rule3, rule9), rule22)
        out_high = np.fmax(np.fmax(np.fmax(rule4, rule10), rule14), rule17)
        out_veryHigh = np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(rule11, rule15), rule18), rule19), rule20), rule21), rule23), rule24)

        # Aggregation
        risk0 = np.zeros_like(y_risk)

        fig, ax0 = plt.subplots(figsize=(7, 4))
        ax0.set_xlim([0, 45])
        ax0.set_ylim([0, 1.1])
        ax0.fill_between(y_risk, risk0, out_not, facecolor='b', alpha=0.7, label='Not')
        ax0.plot(y_risk, risk_not, 'b', linestyle='--')
        ax0.fill_between(y_risk, risk0, out_little, facecolor='g', alpha=0.7, label='Little')
        ax0.plot(y_risk, risk_little, 'g', linestyle='--')
        ax0.fill_between(y_risk, risk0, out_mid, facecolor='r', alpha=0.7, label='Mid')
        ax0.plot(y_risk, risk_mid, 'r', linestyle='--')
        ax0.fill_between(y_risk, risk0, out_high, facecolor='c', alpha=0.7, label='High')
        ax0.plot(y_risk, risk_high, 'c', linestyle='--')
        ax0.fill_between(y_risk, risk0, out_veryHigh, facecolor='m', alpha=0.7, label='Very High')
        ax0.plot(y_risk, risk_veryHigh, 'm', linestyle='--')

        ax0.axvline(x=y_risk, color='black', linewidth=1.0, linestyle='--')
        ax0.text(y_risk, -0.1, float(self.iptAge.text()), color='red', ha='center')
        # ax0.axhline(y=ldl_fit_normal, color='black', linewidth=1.0, linestyle='--')
        # ax0.text(5, ldl_fit_normal, round(ldl_fit_normal, 2), ha='left', va='bottom', color='red')

        ax0.set_title('Out of the Risk')
        ax0.legend()

        plt.tight_layout()

        # COG Calculation
        aggregated = np.fmax(np.fmax(np.fmax(np.fmax(out_not, out_little), out_mid), out_high), out_veryHigh)
        defuzzified = fuzz.defuzz(y_risk, aggregated, 'centroid')
        result = fuzz.interp_membership(y_risk, aggregated, defuzzified)
        print("Coroner Heart Diagnosis:", defuzzified)

        # Defuzzification and visualization
        fig, ax0 = plt.subplots(figsize=(7, 4))
        ax0.set_xlim([0, 45])
        ax0.set_ylim([0, 1.1])
        ax0.plot(y_risk, risk_not, 'b', linewidth=0.5, linestyle='--', label='Not')
        ax0.plot(y_risk, risk_little, 'g', linewidth=0.5, linestyle='--', label='Little')
        ax0.plot(y_risk, risk_mid, 'r', linewidth=0.5, linestyle='--', label='Mid')
        ax0.plot(y_risk, risk_high, 'c', linewidth=0.5, linestyle='--', label='High')
        ax0.plot(y_risk, risk_veryHigh, 'm', linewidth=0.5, linestyle='--', label='Very High')
        ax0.fill_between(y_risk, risk0, aggregated, facecolor='Orange', alpha=0.7)

        ax0.axvline(x=defuzzified, color='black', linewidth=1.5)
        ax0.text(defuzzified, -0.1, round(defuzzified,2), color='red', ha='center')
        # ax0.plot([defuzzified, defuzzified], [0, result], 'k', linewidth=1.5, alpha=0.9)
        ax0.set_title('Centroid Deffuzification')
        ax0.legend()

        self.optRisk.setText(str(round(defuzzified, 2)))

        plt.tight_layout()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnCalc.setText(_translate("MainWindow", "Calculate"))
        # self.btnGraph.setText(_translate("MainWindow", "Graph"))
        self.grpInputBox.setTitle(_translate("MainWindow", "Input Box"))
        self.lblAge.setText(_translate("MainWindow", "Age (0-100):"))
        self.lblBloodPressure.setText(_translate("MainWindow", "Blood pressure (0-220); normal<120: "))
        self.lblCholesterol.setText(_translate("MainWindow", "Cholesterol (100-250); normal<200:"))
        self.lblBloodSugar.setText(_translate("MainWindow", "Blood sugar (0-120); normal(90-120):"))
        self.lblHDL.setText(_translate("MainWindow", "HDL (0-70); normal>60/: at risk(41-59)/ dangerous<40:"))
        self.lblLDL.setText(_translate("MainWindow", "LDL (0-190); normal<100:/ at risk(100-159)/ dangerous>160:"))
        self.lblRisk.setText(_translate("MainWindow", "Risk"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
