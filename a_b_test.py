import codecademylib3
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
#print(ad_clicks.head())
utm_views = ad_clicks.groupby('utm_source').user_id.count().reset_index()
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
#print(clicks_by_source)
clicks_pivot = clicks_by_source.pivot(
  columns = 'is_click',
  index = 'utm_source',
  values = 'user_id'
)
clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])
#print(clicks_pivot['percent_clicked'])

num_ads = ad_clicks.groupby('experimental_group').user_id.count()
#print(num_ads)

which_click = ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index()
#print(which_click)
which_click_pivot = which_click.pivot(
  columns = 'is_click',
  index = 'experimental_group',
  values = 'user_id'
)
#print(which_click_pivot)
#Using this method will create a new dataframe 
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
#print(type(a_clicks))
#Using this method will create a series and not a df
a_clicks_2 = ad_clicks.experimental_group == 'A'
#print(type(a_clicks_2))
b_clicks = ad_clicks[ad_clicks.experimental_group == "B"]
#print(a_clicks)
percent_user_by_day_a = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
percent_user_by_day_b = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
percent_user_a_pivot = percent_user_by_day_a.pivot(columns = 'is_click', index = 'day', values = 'user_id')
percent_user_b_pivot = percent_user_by_day_b.pivot(columns = 'is_click', index = 'day', values = 'user_id')
print(percent_user_a_pivot)
percent_click_a = percent_user_a_pivot[True] / (percent_user_a_pivot[True] + percent_user_a_pivot[False])
print(percent_click_a)
percent_click_b = percent_user_b_pivot[True]/ (percent_user_b_pivot[True] + percent_user_b_pivot[False])
print(percent_click_b)
#Ad A started off stronger and finished stronger than ad B. Ad A caused a larger percentage of people to click on it, so I would reccomend to use ad A and not Ad B
