for sub_category in sub_category_lst:
  category = category_map[sub_category]
  tmp_dct['Source'] = 'CRM'
  tmp_dct['Description'] = msg
  tmp_dct['Category'] = category
  tmp_dct['Sub_Category'] = sub_category
  if category == 'Kudos':
    tmp_dct['Sentiment'] = 'Positive'
  else:
    tmp_dct['Sentiment'] = sentiment_analysis(msg)
  tmp_dct['Business (Customer) (Company)'] = tmp_dct['Business (Customer) (Company)'].strip()
  dct_lst.append(tmp_dct.copy())    # use copy() here, otherwise you are adding the reference of tmp_dct, which will be the save value in your list
