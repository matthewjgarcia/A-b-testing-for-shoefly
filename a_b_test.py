import codecademylib3
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())
utm_views = ad_clicks.groupby('utm_source').user_id.count().reset_index()
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
print(clicks_by_source)
clicks_pivot = clicks_by_source.pivot(
  columns = 'is_click',
  index = 'utm_source',
  values = 'user_id'
)
clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])
print(clicks_pivot['percent_clicked'])

num_ads = ad_clicks.groupby('experimental_group').user_id.count()
print(num_ads)

which_click = ad_clicks.groupby(['experimental_group','is_click']).user_id.count()
print(which_click)
