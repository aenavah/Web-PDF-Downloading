#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 14:47:00 2021

@author: alexandranava
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import wget
chrome_options = Options()

#use script only for sites where clicking the link takes to pdf, saves in same directory as script
###user inputs###-------------------------------------------------------
driver = webdriver.Chrome(executable_path = "/Users/alexandranava/Desktop/CODE/World Banking Project/Chrome Driver/chromedriver91", options = chrome_options )
site, bank = "",""
type_, class_ = "",""
#example variable are below
#site, bank = "http://eng......................................lish.cmbchina.com/cmbir/intro.aspx?type=report", "chinamerchantsbank"
#site, bank = "https://www.cib.com.cn/en/aboutCIB/investor/reports/", "industrialbank"
#site, bank = "https://www.cncbinternational.com/about-us/investor-relations/interim-and-annual-reports/en/index.jsp", "chinaciticbank"
#site, bank = "https://webb-site.com/dbpub/docs.asp?p=9318&s=spdup", "chinaminshengbank"
#site, bank = "https://webb-site.com/dbpub/docs.asp?p=13488", "chinaeverbrightbank"
#site, bank = "https://ebank.pingan.com.cn/ir#/pc/index.html/home/index/performance", "pinganbank"
#site, bank = "https://www.hxb.com.cn/en/abouthuaxiabank/investorrelationship/informationdisclosureannualreport/index.shtml", "hauxiabank"
#site, bank = "http://www.cgbchina.com.cn/Channel/12565477", "chinaguangfabank"
#site, bank = "https://webb-site.com/dbpub/docs.asp?p=46012","chinazheshangbank"
#site, bank = "http://www.bank-of-tianjin.com.cn/tzzgxEN/Inford/FinR/index_2.shtml", "bankoftianjin"
##site, bank = "https://www.xib.com.cn/english/AboutXIB/InvestorRelationship/AnnualReport/index.htm", "xiameninternationalbank"
#site, bank = "https://webb-site.com/dbpub/docs.asp?p=2286631&s=repup", "shengjingbank"
#site, bank = "https://webb-site.com/dbpub/docs.asp?p=2209730", "harbin bank"
#site, bank = "https://webb-site.com/dbpub/docs.asp?p=2537294", "bank of jilin"
#site, bank = "http://en.srcb.com/annualreport/index.shtml", "shanghairuralcommercialbank"
#site, bank = "http://www.cqrcb.com/en/investor/report/annual/index.html", "chongqingruralcommercialbank"
#--------------
#type_, class__ = "table","ReportTable"
#type_, class_ = "div", "middle"
#type_, class_ = "div", "cs22 cs22Ext01"
#type_, class_ = "table", "numtable"
#type_, class_ = "table", "numtable"
#type_, class_ ="ul", "list_all"
#type_, class_ = "div", "en_erji_right_box"
#type_, class_ = "div", "rightCon"
#type_, class_ = "table","numtable"
#type_, class_ = "div", "info_r"
##type_, class_ = "div", "baogao clearfix"
#type_, class_ = "table", "numtable"
#type_, class_ = "table", "numtable"
#type_, class_ = "table", "numtable"
#type_, class_ = "div", "invest_title01"
#type_, class_ = "ul", "list clear"
#--------------
last_pdf = "" #if breaks, put link_text of last pdf downloaded, else leave null


def download_pdfs(pdf_path, download_file):
  wget.download(pdf_path, download_file)

driver.get(site)
soup = BeautifulSoup(driver.page_source,"html.parser")  #beautiful soup object of second page html

print("starting...")
if last_pdf == "":
    anchor_list = soup(type_,{"class": class_})[0]("a")
    pdf_ = []
    href_ = []
    counter = 0
    for anchor in anchor_list:
        counter += 1
        link_text = anchor.getText().strip()
        pdf_.append(link_text)
        href = anchor.get('href')
        if bank == "chinaciticbank":
            href = href.strip("../../../../")
            href = "https://www.cncbinternational.com/" + href
        if bank == "hauxiabank":
            href = "https://www.hxb.com.cn" + href
        if bank == "bankoftianjin":
            href = href.strip("../../..")
            href = "http://www.bank-of-tianjin.com.cn/" + href
            if "Annual" not in link_text:
                continue
        if bank == "xiameninternationalbank":
            href = "https://www.xib.com.cn" + href
        if bank == "shanghairuralcommercialbank":
            if ".pdf" not in href:
                continue
            elif "Annual" not in link_text:
                continue
        if bank == "chongqingruralcommercialbank":
            if ".pdf" not in href:
                continue
            href = "http://www.cqrcb.com/" + href
        href_.append(href)
        print("-----")
        print(link_text, "\n" + href)
        ext = href.split(".")
        ext = ext[-1]
        if "Report" not in link_text:
            continue

        print("downloading...")
        download_pdf_name = bank + "_" + link_text +"." + ext
        download_pdfs(href, download_pdf_name)

#use if want to continue from where code stopped previously
# =============================================================================
# if last_pdf != "":
#     counter_ = 0
#     binary = 0
#     pdf_counter = 0
#     for pdf in pdf_:
#         if binary == 1:
#             print(pdf)
#             #print("Downloading: " + pdf_[counter] + "..." + pdf_counter + "/" + len(pdf_))
#             download_pdf_name = bank + "_" + pdf #+ ".pdf"
#             download_pdfs(href_[counter_], download_pdf_name)
#         if pdf == last_pdf:
#             binary = 1
#         counter_ += 1
#        # driver.wait("5")
# =============================================================================
