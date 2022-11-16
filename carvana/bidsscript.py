#reading the files 

import pandas as pd
inv_onsite=pd.read_excel('Inventory_Current_Onsite.xlsx')
inv_his=pd.read_excel('Inventory_Historical.xlsx')
kw_a=pd.read_excel('KW_Attributes.xlsx')
kw_p=pd.read_excel('KW_Performance_L120D.XLSX')
mm_ars=pd.read_excel('Make_Model_ARS.xlsx')

print(inv_onsite)

print(inv_his)

print(kw_a)
# Est First Pos. Bid = Google’s estimate for the bid required to show up in first position (see below)
# Est Top of Page Bid = Google’s estimate for the bid required to show up at the top of the page (i.e., 4th position)
# Mkt = Market = the geography the campaign is targeting

print(kw_p)
# QS = quality score = value google assigns to each KW based (learn more here)
# Impressions = # of times a KW’s ad was seen on in google search results
# Clicks = # of times the KW’s ads were clicked (i.e., # of times people clicked through to carvana.com)
# Conversions = # of car sales generated from the clicks
# CTR = click through rate = clicks / impressions
# CVR = conversion rate = conversions / clicks
# ARS = average revenue per sale = amount of money Carvana makes per car sold

print(mm_ars)

#Merging kw attributes and performances
res=pd.merge(kw_a,kw_p,on='KW ID')

# CVR = conversion rate = conversions / clicks
#Calculating KW CVR
res['CVR']=res['Conversions']/res['Clicks']
temp_ag_cvr=res[['Ad group','CVR']].groupby('Ad group')['CVR'].sum()
ag_cvr=pd.DataFrame({'Ad group':temp_ag_cvr.index,'AG_CVR':temp_ag_cvr.values})
res=pd.merge(res,ag_cvr,on=['Ad group'],how='left')

#calculating KW CVR
temp_kw_cvr=res[['Keyword','CVR']].groupby('Keyword')['CVR'].sum()
kw_cvr=pd.DataFrame({'Keyword':temp_kw_cvr.index,'KW_CVR':temp_kw_cvr.values})
res=pd.merge(res,kw_cvr,on=['Keyword'],how='left')

#calculating Make_Model_Year from AG
mmy=res['Ad group'].str.split('-',n = 3, expand = True)
res['mk_mo_yr']=mmy[3]
mmy

#calculating Mk/Mo/Yr CVR
temp_mmy_cvr=res[['mk_mo_yr','CVR']].groupby('mk_mo_yr')['CVR'].sum()
mmy_cvr=pd.DataFrame({'mk_mo_yr':temp_mmy_cvr.index,'MK_MO_YR_CVR':temp_mmy_cvr.values})
res=pd.merge(res,mmy_cvr,on=['mk_mo_yr'],how='left')

# Make_Model from Make_Model_Year
temp=res['mk_mo_yr'].str.split("-", n = 2, expand = True)
res['mk']=temp[0]
res['mo']=temp[1]
res['mk_mo']=res['mk']+'-'+res['mo']

#calculating Mk/Mo CVR
temp_mm_cvr=res[['mk_mo','CVR']].groupby('mk_mo')['CVR'].sum()
mm_cvr=pd.DataFrame({'mk_mo':temp_mm_cvr.index,'MK_MO_CVR':temp_mm_cvr.values})
res=pd.merge(res,mm_cvr,on=['mk_mo'],how='left')

#Making the columns similar to make the inner join possible Mk/Mo ARS Table and res and joining it
mm_ars['mk']='MK_'+mm_ars['Make']
mm_ars['mo']='MO_'+mm_ars['Model']
mm_ars['mk_mo']=mm_ars['mk']+'-'+mm_ars['mo']
res=pd.merge(res,mm_ars,on=['mk_mo','mo','mk'],how='left')

#Calculating Conversions for KW and Appending them to the result table
temp_kw_conv=res[['Keyword','Conversions']].groupby('Keyword')['Conversions'].sum()
kw_conv=pd.DataFrame({'Keyword':temp_kw_conv.index,'KW_CONV':temp_kw_conv.values})

#Calculating Conversions for AG and Appending them to the result table
temp_ag_conv=res[['Ad group','Conversions']].groupby('Ad group')['Conversions'].sum()
ag_conv=pd.DataFrame({'Ad group':temp_ag_conv.index,'AG_CONV':temp_ag_conv.values})

#Calculating Conversions for  and Appending them to the result table
temp_mmy_conv=res[['mk_mo_yr','Conversions']].groupby('mk_mo_yr')['Conversions'].sum()
mmy_conv=pd.DataFrame({'mk_mo_yr':temp_mmy_conv.index,'MMY_CONV':temp_mmy_conv.values})

#Calculating Conversions for and Appending them to the result table
temp_mm_conv=res[['mk_mo','Conversions']].groupby('mk_mo')['Conversions'].sum()
mm_conv=pd.DataFrame({'mk_mo':temp_mm_conv.index,'MM_CONV':temp_mm_conv.values})

res=pd.merge(res,kw_conv,on=['Keyword'],how='left')
res=pd.merge(res,ag_conv,on=['Ad group'],how='left')
res=pd.merge(res,mmy_conv,on=['mk_mo_yr'],how='left')
res=pd.merge(res,mm_conv,on=['mk_mo'],how='left')

res.columns

# a) If KW has >10 conversions
# ·          

# Calculate KW bid based on KW’s historical performance
# New KW Bid = KW CVR * Mk/Mo ARS
# b)If KW has <11 conversions but ad group has >10 conversions
# Calculate KW bid based on its ad group’s historical performance
# New KW Bid = AG CVR * Mk/Mo ARS
# c) If AG has <11 conversions, but Mk/Mo/Yr has >10 conversions
# Calculate KW bid based on the Mk/Mo’s historical performance
# New KW bid = Mk/Mo/Yr CVR * Mk/Mo ARS
# d) If Mk/Mo/Yr has <11 conversions, but Mk/Mo has >10 conversions
# Calculate KW bid based on the Mk/Mo’s historical performance
# New KW bid = Mk/Mo CVR * Mk/Mo ARS
# e) If Mk/Mo has <11 conversions
# New KW bid = Est First Pos Bid


#step 1
res['new_bid']=0
res.loc[res['KW_CONV']>10,'new_bid']=res['KW_CVR']*res['ARS']

res.loc[(res['KW_CONV']<11) & (res['AG_CONV']>10),'new_bid']=res['AG_CVR']*res['ARS']

res.loc[(res['AG_CONV']<11) & (res['MMY_CONV']>10),'new_bid']=res['MK_MO_YR_CVR']*res['ARS']

res.loc[(res['MMY_CONV']<11) & (res['MM_CONV']>10),'new_bid']=res['MK_MO_CVR']*res['ARS']

res.loc[res['MM_CONV']<11,'new_bid']=res['Est First Pos. Bid']





#Merging both the Historical and Current sites data and appending it to the Result table
inv_combined=pd.merge(inv_his,inv_onsite,on=['Make','Model','Year'],how='inner')
inv_combined['Year']=inv_combined['Year']-2000
inv_combined['mk_mo_yr']='MK_'+inv_combined['Make']+'-'+'MO_'+inv_combined['Model']+'-'+'YR_'+inv_combined['Year'].astype(str)
res=pd.merge(res,inv_combined[['mk_mo_yr','HistAvgInv','CurrentOnsiteInventory']],on=['mk_mo_yr'],how='left')

#2a

	
#If current Mk/Mo/Yr inv < hist Mk/Mo/Yr inv
#Reduce KW bid by % equal to half the % diff between current and historical inv
#E.g., if hist avg is 20 and current inv is 15, reduce bid by 12.5% (i.e., half of 25%)

res.loc[res['HistAvgInv']>res['CurrentOnsiteInventory'],'new_bid']=((1-(res['HistAvgInv']-res['CurrentOnsiteInventory'])/(2*res['HistAvgInv'])))*res['new_bid']

#getting MKT from Ad group column
temp=res['Ad group'].str.split("-", n = 3, expand = True)
res['Mkt']=temp[2]

#calculating MKT CVR and appending it to the result
temp_mkt_cvr=res[['Mkt','CVR']].groupby('Mkt')['CVR'].sum()
mkt_cvr=pd.DataFrame({'Mkt':temp_mkt_cvr.index,'MKT_CVR':temp_mkt_cvr.values})
res=pd.merge(res,mkt_cvr,on=['Mkt'],how='left')

overall_cvr=mkt_cvr['MKT_CVR'].sum()
overall_cvr
mkt_cvr

#2b

#Adjust bid based on Mkt CVR only for KWs whose bids were calculated based on Mk/Mo/Yr or Mk/Mo CVR (i.e., not based on KW or AG CVR) 
#Increase/decrease KW bid by the half the % above or below overall site CVR the market CVR is relative to overall site average
#i.e., if overall CVR for the entire site is 1.0% and DAL overall CVR is 1.07%, increase bids for KWs in DAL by 3.5%

#(Mkt_CVR-Overall_CVR)*50/Overall_CVR (avg of overall site)

#This filter gives the new bids that are affected based on Mkt CVR only for KWs whose bids were calculated based on Mk/Mo/Yr or Mk/Mo CVR

res.loc[((res['AG_CONV']<11) & (res['MMY_CONV']>10)) | ((res['MMY_CONV']<11) & (res['MM_CONV']>10)),'new_bid']=(100-(((res['MKT_CVR']-overall_cvr)*50)/overall_cvr))*res['new_bid']

#2c
#  Cap bids at reasonable levels, based on their quality score
# KWs with QS>7 cannot be higher than Est First Pos Bid
# KWs with QS<8 and QS>5 cannot be higher than average of Est Top of Page Bid and Est First Pos Bid
# KWs with QS<6 cannot be higher than (Est Top of Page Bid *0.9) + (Est First Pos Bid *0.1)
# No bids can be higher than $12
res.loc[res['Quality score']>7 ,'new_bid']=res[['new_bid','Est First Pos. Bid']].min(axis=1)

avg_est_top_of_page_bid=res['Est Top of Page Bid'].mean()
res['avg_est_top_of_page_bid']=avg_est_top_of_page_bid
res.loc[(res['Quality score']>5) & (res['Quality score']<8),'new_bid']=res[['new_bid','avg_est_top_of_page_bid']].min(axis=1)

res['calculated']=(0.1*res['Est First Pos. Bid'])+(0.9*res['Est Top of Page Bid'])
res.loc[res['Quality score']<6,'new_bid']=res[['new_bid','calculated']].min(axis=1)

res.loc[res['new_bid']>12,'new_bid']=12

#2d
#Cap bids of broad match KWs 
#Ensure that no bid for a broad match KW is greater than any bid for an exact match KW within the same ad group
#E.g., if bids for exact match KWs within the same ad group are $1.50, $1.75 and $1.60, then if a broad match KW with a calculated of bid of $2.00 should have its bid reduced to $1.50

exact_match_kws=res.loc[res['Match type']=='Exact',['Ad group','new_bid','Match type']]
temp_mt_compare=exact_match_kws[['Ad group','new_bid']].groupby('Ad group')['new_bid'].min()
exact_type_min=pd.DataFrame({'Ad group':temp_mt_compare.index,'EXACT_TYPE_MIN_VALUE':temp_mt_compare.values})
res=pd.merge(res,exact_type_min,on=['Ad group'],how='left')

res.loc[res['Match type']=='Broad','new_bid']=res[['EXACT_TYPE_MIN_VALUE','new_bid']].min(axis=1)

import os
res1= res[['KW ID','new_bid']]
res1.to_csv("newbids.csv")
os. getcwd()

